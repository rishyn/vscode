import pandas as pd
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt
import json
import os

# Rutas de archivos
script_dir = os.path.dirname(__file__)
aps_path = os.path.join(script_dir, 'APS_Maule.json')
distancias_path = os.path.join(script_dir, 'distancias_establecimientos_salud.json')
calles_path = os.path.join(script_dir, 'calles_region_maule.json')

# --- 1. Carga de Datos ---
df_aps_geo = gpd.read_file(aps_path)
print(f"APS cargados: {len(df_aps_geo)} establecimientos")

posiciones = {row['nomeste']: (row['longitud'], row['latitud'])
              for _, row in df_aps_geo.iterrows()}

# Carga de distancias
distancias_data = []
with open(distancias_path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            feature = json.loads(line)
            distancias_data.append({
                'origin_id': feature['properties']['InputID'],
                'destination_id': feature['properties']['TargetID'],
                'distance_meters': feature['properties']['Distance']
            })

# Mapeo de IDs
id_to_nomeste = {row['FID']: row['nomeste'] for _, row in df_aps_geo.iterrows()}

# --- 2. Creación del Grafo ---
G = nx.Graph()
for arista in distancias_data:
    origin_name = id_to_nomeste.get(arista['origin_id'])
    destination_name = id_to_nomeste.get(arista['destination_id'])
    if origin_name and destination_name:
        G.add_edge(origin_name, destination_name, weight=arista['distance_meters'])

print(f"Grafo creado: {G.number_of_nodes()} nodos, {G.number_of_edges()} aristas")

# --- 3. MST con Prim ---
largest_cc = max(nx.connected_components(G), key=len)
G_sub = G.subgraph(largest_cc).copy()
mst = nx.minimum_spanning_tree(G_sub, weight='weight', algorithm='prim')
print(f"MST (Prim): {mst.number_of_nodes()} nodos, {mst.number_of_edges()} aristas")

# --- 4. Cálculo de Costo ---
costo_total_km = mst.size(weight='weight') / 1000
print(f"\nCosto total (MST): {costo_total_km:.2f} km")

# --- 5. Nodos Críticos ---
centralidad = nx.betweenness_centrality(mst, weight='weight', normalized=True)
nodos_criticos = sorted(centralidad.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 Nodos Críticos:")
for i, (nodo, valor) in enumerate(nodos_criticos):
    print(f"{i+1}. {nodo}: {valor:.4f}")

# --- 6. Visualización (Modificado para SVG) ---
fig, ax = plt.subplots(figsize=(15, 15))
mapa_maule = gpd.read_file(calles_path)
mapa_maule.plot(ax=ax, color='gray', linewidth=0.5)

# Dibujar MST
for u, v in mst.edges():
    if u in posiciones and v in posiciones:
        x_coords = [posiciones[u][0], posiciones[v][0]]
        y_coords = [posiciones[u][1], posiciones[v][1]]
        ax.plot(x_coords, y_coords, 'c-', linewidth=2)

# Dibujar nodos
df_aps_geo.plot(ax=ax, color='blue', markersize=30)
df_criticos = df_aps_geo[df_aps_geo['nomeste'].isin([n[0] for n in nodos_criticos])]
df_criticos.plot(ax=ax, color='red', markersize=100)

ax.set_title('Red Óptima APS - Maule (Prim)')

# Guardar en SVG (Único cambio)
plt.savefig('red_optima_aps_maule_prim.svg', format='svg', dpi=300)
print("\nVisualización guardada como 'red_optima_aps_maule_prim.svg'")