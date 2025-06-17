import pandas as pd
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt
import json
import os

# Obtener la ruta del directorio donde se encuentra el script
script_dir = os.path.dirname(__file__)

# Construir las rutas completas a los archivos
aps_path = os.path.join(script_dir, 'APS_Maule.json')
distancias_path = os.path.join(script_dir, 'distancias_establecimientos_salud.json')
calles_path = os.path.join(script_dir, 'calles_region_maule.json')

# --- 1. Carga de Datos ---

# Cargar las ubicaciones de los establecimientos APS con GeoPandas
# df_aps_geo será un GeoDataFrame.
# Geopandas es robusto y puede leer tu APS_Maule.json aunque no tenga el array principal.
try:
    df_aps_geo = gpd.read_file(aps_path)
    print(f"APS_Maule.json cargado exitosamente. Se encontraron {len(df_aps_geo)} establecimientos.")

    # Verificar si 'nomeste' está en las columnas del GeoDataFrame.
    # Si GeoPandas ha "aplanado" las propiedades, 'nomeste' será una columna directa.
    # También necesitamos 'FID' para el mapeo con las distancias.
    required_cols_aps = ['nomeste', 'longitud', 'latitud', 'FID']
    for col in required_cols_aps:
        if col not in df_aps_geo.columns:
            raise ValueError(f"Columna '{col}' no encontrada en APS_Maule.json. "
                             f"Asegúrate de que tus datos de APS contengan esta información.")

    # Crear un diccionario para buscar coordenadas por nombre de APS
    # Ahora accedemos directamente a las columnas del GeoDataFrame
    posiciones = {row['nomeste']: (row['longitud'], row['latitud'])
                  for idx, row in df_aps_geo.iterrows()}

except Exception as e:
    print(f"Error al cargar APS_Maule.json: {e}")
    print("Asegúrate de que el archivo APS_Maule.json sea un GeoJSON válido y contenga las columnas 'nomeste', 'longitud', 'latitud' y 'FID'.")
    exit()


# Cargar las distancias pre-calculadas entre establecimientos
# Este archivo también parece ser una secuencia de objetos JSON, no un array único.
# Lo leeremos línea por línea, asumiendo que cada línea es un objeto JSON válido.
distancias_data = []
try:
    with open(distancias_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip() # Eliminar espacios en blanco y saltos de línea
            if line: # Si la línea no está vacía
                try:
                    feature = json.loads(line)
                    # Acceder a las propiedades InputID, TargetID, Distance directamente desde el diccionario 'properties'
                    if 'properties' in feature and \
                       'InputID' in feature['properties'] and \
                       'TargetID' in feature['properties'] and \
                       'Distance' in feature['properties']:
                        distancias_data.append({
                            'origin_id': feature['properties']['InputID'],
                            'destination_id': feature['properties']['TargetID'],
                            'distance_meters': feature['properties']['Distance']
                        })
                    else:
                        print(f"Advertencia: Objeto JSON en {distancias_path} no tiene las propiedades esperadas (InputID, TargetID, Distance): {line[:100]}...")
                except json.JSONDecodeError as e:
                    print(f"Advertencia: No se pudo parsear la línea de {distancias_path} como JSON: {line[:50]}... Error: {e}")
    print(f"distancias_establecimientos_salud.json cargado exitosamente. Se encontraron {len(distancias_data)} distancias.")
except Exception as e:
    print(f"Error al cargar distancias_establecimientos_salud.json: {e}")
    print("Asegúrate de que el archivo contenga objetos JSON válidos por línea.")
    exit()

# Cargar el mapa de calles de la región con GeoPandas
try:
    mapa_maule = gpd.read_file(calles_path)
    print("calles_region_maule.json (mapa de calles) cargado exitosamente.")
except Exception as e:
    print(f"Error al cargar calles_region_maule.json: {e}")
    print("Asegúrate de que el archivo calles_region_maule.json sea un GeoJSON válido.")
    exit()

# --- Mapeo de IDs de Distancias a Nombres de Establecimientos (CRÍTICO) ---
# Creamos un mapeo de FID a nomeste y también un mapeo de nomeste a FID para referencia si es necesario
id_to_nomeste = {row['FID']: row['nomeste'] for idx, row in df_aps_geo.iterrows() if 'FID' in row and 'nomeste' in row}
nomeste_to_id = {row['nomeste']: row['FID'] for idx, row in df_aps_geo.iterrows() if 'FID' in row and 'nomeste' in row}

# --- 2. Creación del Grafo ---
G = nx.Graph()

# Añadir las aristas con sus pesos (distancias en metros)
# Ahora usamos el mapeo de ID a nombre para los nodos del grafo
for arista in distancias_data:
    origin_name = id_to_nomeste.get(arista['origin_id'])
    destination_name = id_to_nomeste.get(arista['destination_id'])

    # Solo añadir la arista si ambos nombres de establecimiento son válidos, existen en 'posiciones'
    # y el nombre del establecimiento no está vacío (caso de 'Clínica Dental Móvil (Talca)' que tiene nombre largo)
    if origin_name and destination_name and \
       origin_name in posiciones and destination_name in posiciones:
        G.add_edge(origin_name, destination_name, weight=arista['distance_meters'])
    else:
        # Esto te ayuda a depurar si faltan establecimientos en APS_Maule.json o hay IDs incorrectos
        if not origin_name:
            print(f"Advertencia: ID de origen {arista['origin_id']} de 'distancias' no encontrado en APS_Maule.json (columna FID).")
        if not destination_name:
            print(f"Advertencia: ID de destino {arista['destination_id']} de 'distancias' no encontrado en APS_Maule.json (columna FID).")
        if origin_name and origin_name not in posiciones:
            print(f"Advertencia: Posición para '{origin_name}' (ID {arista['origin_id']}) no encontrada en 'posiciones' (¿Problema de longitud/latitud?).")
        if destination_name and destination_name not in posiciones:
            print(f"Advertencia: Posición para '{destination_name}' (ID {arista['destination_id']}) no encontrada en 'posiciones' (¿Problema de longitud/latitud?).")


print(f"Grafo completo creado con {G.number_of_nodes()} nodos y {G.number_of_edges()} aristas.")

# Verificar si el grafo está vacío o no es conexo antes de calcular el MST
if G.number_of_nodes() == 0 or G.number_of_edges() == 0:
    print("Error: El grafo no tiene nodos o aristas después de la carga de datos. No se puede calcular el MST. Revisa tus archivos de entrada y el mapeo de IDs.")
    exit()

# Solo intentar calcular MST si el grafo es conexo, o manejar componentes
if not nx.is_connected(G):
    print("Advertencia: El grafo no es completamente conexo. El MST se calculará para cada componente conexo. "
          "El costo total será la suma de los MST de cada componente.")
    # Si quieres un solo MST para el componente más grande:
    # largest_cc = max(nx.connected_components(G), key=len)
    # G_sub = G.subgraph(largest_cc)
    # mst = nx.minimum_spanning_tree(G_sub, weight='weight')
    # print(f"MST calculado solo para el componente más grande con {mst.number_of_nodes()} nodos.")
    # Si quieres un "bosque" de MST (un MST para cada componente):
    mst = nx.minimum_spanning_tree(G, weight='weight') # nx.minimum_spanning_tree lo maneja bien para grafos no conexos, creando un "bosque"

# --- 3. Cálculo del Árbol de Expansión Mínima (MST) ---
mst = nx.minimum_spanning_tree(G, weight='weight')
print(f"Árbol de Expansión Mínima (MST) calculado con {mst.number_of_nodes()} nodos y {mst.number_of_edges()} aristas.")

# --- 4. Cálculo del Costo Total ---
costo_total_metros = mst.size(weight='weight')
costo_total_km = costo_total_metros / 1000
print(f"\nCosto total de la red óptima (MST): {costo_total_km:.2f} km")

# --- 5. Identificación de Nodos Críticos ---
# Asegúrate de que el MST no esté vacío antes de calcular la centralidad
if mst.number_of_nodes() == 0:
    print("El MST está vacío. No se pueden calcular nodos críticos.")
    nombres_nodos_criticos = []
else:
    centralidad = nx.betweenness_centrality(mst, weight='weight', normalized=True)
    nodos_criticos_sorted = sorted(centralidad.items(), key=lambda item: item[1], reverse=True)

    print("\n--- Top 5 Nodos Más Críticos (Mayor Centralidad de Intermediación) ---")
    for i, (nodo, valor) in enumerate(nodos_criticos_sorted[:5]):
        print(f"{i+1}. {nodo}: {valor:.4f}")

    nombres_nodos_criticos = [nodo for nodo, valor in nodos_criticos_sorted[:5]]

# --- 6. Visualización Geoespacial ---
fig, ax = plt.subplots(figsize=(15, 15))

# Dibujar el mapa de calles como fondo
mapa_maule.plot(ax=ax, color='gray', linewidth=0.5, zorder=1)

# Dibujar las conexiones del MST
for u, v in mst.edges():
    # Asegúrate de que las posiciones existan para ambos nodos
    if u in posiciones and v in posiciones:
        x_coords = [posiciones[u][0], posiciones[v][0]]
        y_coords = [posiciones[u][1], posiciones[v][1]]
        ax.plot(x_coords, y_coords, 'c-', linewidth=2, zorder=2, alpha=0.8) # Líneas cian
    else:
        print(f"Advertencia: No se pudo dibujar la arista entre '{u}' y '{v}'. Faltan coordenadas en 'posiciones'.")


# Dibujar todos los nodos (APS)
# df_aps_geo ya es un GeoDataFrame con la geometría.
# No necesitas crear un nuevo GeoDataFrame aquí.
df_aps_geo.plot(ax=ax, color='blue', markersize=30, zorder=3, label='APS')

# Resaltar los nodos críticos
# Asegúrate de que 'nomeste' sea la columna que contiene los nombres para la comparación
df_criticos = df_aps_geo[df_aps_geo['nomeste'].isin(nombres_nodos_criticos)]
df_criticos.plot(ax=ax, color='red', markersize=100, zorder=4, label='Nodos Críticos')

# Configuración del gráfico
ax.set_title('Red Óptima de Atención Primaria de Salud (APS) en la Región del Maule (MST)', fontsize=16)
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
ax.legend()
ax.set_aspect('equal', adjustable='box')
plt.tight_layout()

# Guardar la imagen
plt.savefig('red_optima_aps_maule.png', dpi=300)

print("\nVisualización guardada como 'red_optima_aps_maule.png'")