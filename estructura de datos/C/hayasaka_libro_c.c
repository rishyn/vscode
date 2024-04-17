
#include<stdio.h>
#include<stdlib.h>

/*intentar siempre agregar un system("pause"); */

int hello_world(){

    printf("hola mundo");

    return 0;
}



int lectura_de_numeros(){

    int numero,numero2;

    printf("ingrese un numero entero %d\n");
    scanf("%d %d",&numero,&numero2);


    printf("el numero ingresado es %d %d",numero,numero2);

    return 0;

}


int condicionales_c(){



    int numero1,numero2;

    printf("ingrese un numero separados por espacio\n");
    scanf("%d %d" ,&numero1,&numero2);

    if (numero1>numero2){
        printf("el numero %d es mayor que %d\n",numero1,numero2);
    }

    else{
        if (numero2>numero1){
            printf("numero %d s mayor que numero %d\n",numero2,numero1);
        }
        else{printf("los numero %d y %d son iguales\n",numero1,numero2);
        }


    }

    /* tambien se puede usar else if(condicion){resultado}*/



    return 0;
}


int conectores_logicos(){
    /*  &&  : AND
    ||  : OR 
    !   : NOT
    */
    return 0;
}


int ciclos_en_c(){

    int i;
    int numero;

    printf("ingrese un numero \n");
    scanf("%d",&numero);

    for (i=0;i<numero;i=i+2){
        printf("el numero de interacion es: %d\n",i);
    }

    i=0;
    while (i<numero){
        printf("el numero de interacion es: %d\n",i);
        i=i+2;
    }

    return 0;
}




// las funciones
int miFuncionPrimo(int numero){
    int i;
    int bandera=0;
    int modulo;

    for(i=2;i<numero;i++){
        modulo=numero%i;
        if(modulo==0)return 1;
    }
    return 0;
}

int main(){
    int N, resultado;

    printf("Ingrese un numero\n");
    scanf("%d",&N);
    resultado=miFuncionPrimo(N);
    if(resultado==0)printf("El numero es primo");
    else printf("El numero no es primo");
}



//prosigue



int break_and_continue(){

    int i, j=5;
    for(i=0;i<10;i++){
        if(i==j){
            break;
        }
        printf("%d, %d\n",i,j);
    }
    printf("Valores de salida: %d, %d\n",i,j);

    for(i=0;i<10;i++){
        if(i==j){
            continue;
        }
        printf("%d, %d\n",i,j);
    }
    printf("Valores de salida: %d, %d\n",i,j);

    return 0;
}


int cadena_de_caracteres(){

    char miString[4];
    miString[0]='P';
    miString[1]='a';
    miString[2]='n';
    miString[3]='\0';

    char miString2[]="Este es mi String en C";

    int pos=21;
    printf("%s\n",miString);
    printf("%s\n",miString2);
    printf("El valor de %d es igual a: %c\n",pos, miString2[pos]);

    return 0;
}













// cosas del ayudante



#include <stdio.h>
#include <stdlib.h>

typedef struct lista{
	int value;
	int caracter;
	struct lista *sgte;
}lista;
lista *crear_lista(){
	lista *p;
	p = NULL;
	return p;
}
lista *crear_nodo(){
	lista *nodo;
	nodo = (lista *) malloc(sizeof(lista));
	nodo -> sgte = NULL;
	return nodo;
}
lista *eliminar_nodo(lista *nodo){
	free(nodo);
}
lista *recorrer_lista(lista *list){
	while(list != NULL){
			printf("%d %c\n", list -> value, list -> caracter);
		list = list -> sgte;
	}
}
lista *ascii_code(lista *list){
	while(list != NULL){
		printf("Ascii: %d Cantidad: %d\n",list->caracter, list->value );
		list = list -> sgte;
	}
}
int buscar(lista *list, int caracter){
 	lista *nodo_a;
 	nodo_a = list;
 	int encontrado = 0;
 	while(nodo_a != NULL){
 		if(nodo_a -> caracter == caracter){
 			encontrado = 1;
 			break;
 		}
 		nodo_a = nodo_a -> sgte;
 	}
 	if(encontrado ==  1){
 		return 1;
 	}
 	return 0;
}
lista *agregar_inicio(lista *list, int value, int caracter){
	lista *nodo_a;
	nodo_a = crear_nodo();
	nodo_a -> value = value;
	nodo_a -> caracter = caracter;
	if(list == NULL){
		nodo_a -> sgte = NULL;
	}
	else{
		nodo_a -> sgte = list;
	}
	list = nodo_a;
	return list;
}
lista *agregar_final(lista *list, int value, char caracter){
	lista *nodo_a;
	nodo_a = crear_nodo();
	nodo_a -> value = value;
	nodo_a -> caracter = caracter;

	lista *nodo_b;
	nodo_b = list;
	if(list == NULL){
		nodo_a -> sgte = NULL;
		list = nodo_a;
	}
	else{
		while(nodo_b -> sgte != NULL){
			nodo_b = nodo_b -> sgte;
		}
		nodo_b -> sgte = nodo_a;
	}
	return list;
}
lista *agregar_posicion(lista *list, int value, char caracter,int posicion){
	lista *nodo_a;
	nodo_a = crear_nodo();
	nodo_a -> value = value;
	nodo_a -> caracter = caracter;
	if(list == NULL){
		nodo_a -> sgte = NULL;
		list = nodo_a;
	}
	else{
		lista *nodo_anterior;
		nodo_anterior = list;
		int pos = 0;
		while(pos < posicion && nodo_anterior -> sgte){
			nodo_anterior = nodo_anterior -> sgte;
			pos++;
		}
		nodo_a -> sgte = nodo_anterior -> sgte;
		nodo_anterior -> sgte = nodo_a;
	}
	return list;
}
lista *eliminar_inicio(lista *list){
	lista *nodo_a;
	nodo_a = list;
	if(list == NULL){
		/*IS NULL, NOT IS POSSIBLE DELETE A ELEMENT*/
	}
	else{
		list = list -> sgte;
		eliminar_nodo(nodo_a);
	}
	return list;
}
lista *eliminar_final(lista *list){
	if(list == NULL){
		/*IS NULL, NOT IS POSSIBLE DELETE A ELEMENT*/
	}
	else if(list -> sgte == NULL){
		lista *nodo_c;
		nodo_c = list;
		list = list -> sgte;
		eliminar_nodo(nodo_c);
	}
	else{
		lista *nodo_a;
		nodo_a = list;
		while(nodo_a -> sgte -> sgte){
			nodo_a = nodo_a -> sgte;
		}
		lista *nodo_b;
		nodo_b = nodo_a -> sgte;
		nodo_a -> sgte = NULL;
		eliminar_nodo(nodo_b);
	}
	return list;
}
lista *eliminar_posicion(lista *list, int posicion){
	if(list == NULL){
		/*IS NULL, NOT IS POSSIBLE DELETE A ELEMENT*/
	}
	else if(list -> sgte == NULL){
		lista *nodo_a;
		nodo_a = list;
		list = list -> sgte;
		eliminar_nodo(nodo_a);
	}
	else{
		lista *nodo_anterior;
		nodo_anterior = list;
		int pos = 0;
		while(pos < (posicion-1)){
			nodo_anterior = nodo_anterior -> sgte;
			pos++;
		}
		lista * nodo_b;
		nodo_b = nodo_anterior -> sgte;
		nodo_anterior -> sgte = nodo_b -> sgte;
		eliminar_nodo(nodo_b);
	}
	return list;
}
lista *ordenar_lista(lista *list){
	if(list == NULL){

	}
	else{
		int tmp = 0;
		lista *pivote;
		lista *actual;
		actual = NULL;
		pivote = list; // i = 0
		char aux_c;
		while(pivote -> sgte){
			actual = pivote -> sgte; // j = i +1
			while(actual != NULL){
				if(pivote ->value > actual->value){
					aux_c = pivote -> caracter;
					tmp = pivote -> value;
					pivote -> value = actual -> value;
					pivote -> caracter = actual -> caracter;
					actual -> value = tmp;
					actual -> caracter = aux_c;
				}
				actual = actual -> sgte;
			}
			pivote = pivote -> sgte;
		}
	}
	return list;
}
int largo_lista(lista *list){
	int largo = 0;
	while(list != NULL){
		largo++;
		list = list -> sgte;
	}
	return largo;
}
int caracter(lista *list,int pos){
	int i = 0;
	if(list == NULL){

	}
	else{
		while(i < pos){
			list = list -> sgte;
			i++;
		}
	}
	int c = list -> caracter;
	return c;
}
int numero(lista *list,int pos){
	int i = 0;
	if(list == NULL){

	}
	else{
		while(i < pos){
			list = list -> sgte;
			i++;
		}
	}
	int n = list -> value;
	return n;
}