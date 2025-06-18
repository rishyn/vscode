
/*
agregar el campo ciudad  a la tabla clientes como tipo alfanumerico de 80
caracteres de cada usuario de apex(cada estudiante), con sus respectivas tablas
*/

ALTER TABLE RAYV_CLIENTES
    ADD CIUDAD_CLIENTE VARCHAR2(80);

--DESCRIBE (nombre_tabla)para ver por comando los atributos de una tabla

/*
realizar 2 acciondes asociadas al trabajo con la restriccion de la clave primaria
de la trabla clientes , primero desabilitandola y luego habilitandola
*/

ALTER TABLE RAYV_CLIENTES
    MODIFY CONSTRAINT PK_RAYV_CLIENTES DISABLE;

ALTER TABLE RAYV_CLIENTES
    MODIFY CONSTRAINT PK_RAYV_CLIENTES ENABLE;

/*
EJEMPLO EN EL CASO DE HABER CREADO LA TABLA CLIENTES SIN CLAVE PRIMARIA
CON UN ALTER TABLE , PUEDE CARGARSE DICHA RESTRICCION DESPUES ,POR LO MISMO
SE BORRARA LA TABLA , LUEGO SE CREARA SIN LA RESTRICCION, Y SE LE AGREGARA
LA RESTRICCION A TRAVES DE UN ALTER TABLE.
*/

create table RAYV_CLIENTES(
    NRO_CLIENTE NUMBER,
    NOMBRE_CLIENTE VARCHAR2(50),
    APELLIDO1_CLIENTE VARCHAR2(30),
    APELLIDO2_CLIENTE VARCHAR2(30),
    DIRECCION_CLIENTE VARCHAR2(80),
    SALDO NUMBER,
    CREDITO NUMBER,
    DESCUENTO NUMBER
);

ALTER TABLE RAYV_CLIENTES
    ADD CONSTRAINT PK_RAYV_CLIENTES PRIMARY KEY (NRO_CLIENTE);

/* IMPORTANTE:para dejar en claro, podemos dejar varias tablas isn restricciones primarias
y crearlas despues con ALTER pero lo recomendable es hacer las tablas con sus restricciones altiro
*/

--Intrucciones DML: Lenguaje de Manipulacion de Datos

--4 instrucciones basicas para trabajar

--OPERACION CRUD

C: Cargar -> insert
R: Leer -> select
U: Actualizar -> update
D: Borrar -> delete
--1 insertar datos en una tabla
--EJERCICIO: insertar datos en la tabla ciente
INSERT INTO RAYV_CLIENTES(NRO_CLIENTE,NOMBRE_CLIENTE,APELLIDO1_CLIENTE,APELLIDO2_CLIENTE,DIRECCION_CLIENTE,SALDO,CREDITO,DESCUENTO)
    VALUES(1,'CARLOS','CASTRO','BUSTAMANTE','TALCA',500,5000,20);

INSERT INTO RAYV_CLIENTES(NRO_CLIENTE,NOMBRE_CLIENTE,APELLIDO1_CLIENTE,APELLIDO2_CLIENTE,DIRECCION_CLIENTE,SALDO,CREDITO,DESCUENTO)
    VALUES(2,'ALICIA','SANHUEZA','BRAVO','VILLA ALEGRE',600,2000,40);

INSERT INTO RAYV_CLIENTES(NRO_CLIENTE,NOMBRE_CLIENTE,APELLIDO1_CLIENTE,APELLIDO2_CLIENTE,DIRECCION_CLIENTE,SALDO,CREDITO,DESCUENTO)
    VALUES(3,'PEDRO','BRAVO','NUÑEZ','LINARES',10000,1000,60);



--IMPORTANTE: antes de poder llenar datos de algo primero ver si no esta ligado a este
--EJEMPLO: no puedo llenar datos de unlibro si no tengo una editorial primero

--2 Updates : modificar datos dentri de las tablas
--TAREA: actualizar  el apellido 2 de "pedro" por "soto"
UPDATE RAYV_CLIENTES SET
    APELLIDO2_CLIENTE = 'BUSTAMANTE'
    WHERE(NOMBRE_CLIENTE = 'CARLOS');

--para evitar q se cambie el 2 apellidode todas las personas q hay en DATA de la TABLA


--3 Delete : borrar datos dentro de la tablas
--TRABAJO: quisiera borrar todos aquellos cleintes q tienen el apellido soto
DELETE FROM RAYV_CLIENTES WHERE(APELLIDO2_CLIENTE = 'SOTO');

--4  select consultar datosdesde la tablas

SELECT QUE ES LO QUIERO MOSTRAR
FROM DE DONDE LO VOY A SACAR

/*en la clausula select , si quiero mostrar todos
los campos , puedo agregaren vez de los indicado un *
*/

SELECT NRO_CLIENTE,NOMBRE_CLIENTE,APELLIDO1_CLIENTE,APELLIDO2_CLIENTE,DIRECCION_CLIENTE,SALDO,CREDITO,DESCUENTO
--NOMBRE DE LA TABLA
FROM RAYV_CLIENTES;


SELECT *
--NOMBRE DE LA TABLA
FROM RAYV_CLIENTES;


/*TRABAJO:quisiera un rep¿orte que muestrelo siguiente referente a los clientes , codigo,
nombre,apllido1,despuento,siempre y cuendo este sea mayor al 20%
*/

SELECT NRO_CLIENTE,NOMBRE_CLIENTE,APELLIDO1_CLIENTE,DESCUENTO
FROM RAYV_CLIENTES
WHERE ( DESCUENTO > 20 );

--luego del ejercicio anterior borrar la trabla clientes

/* TAREA en clases: colocar la bibliotecla normalizada en tablas y
colocarle datos q uno quieraa

*/
