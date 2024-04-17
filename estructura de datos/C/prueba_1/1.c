#include<stdio.h>
#include<stdlib.h>

void ej4();
void fun1_ej4(int *v1,int v2);
void ej5();
void fun_ej5(double s1 ,double *s2);
void ej6();
void fun2_ej6(int *a , int b);
int fun1_ej6(int *a){}
void ej7(){}
int fun_ej7(int x ,int *p){}
void ej8(){}
void fun_ej8(int x){}
void ej9(){}
void ej10(){}
void ej11(){}
void ej12(){}

int main(){
    printf("hola mundo");
    printf("\n ejercisio 4 \n");
    ej4();

    return 0;
}



/*
1)la complejidad algoritmica de tres algoritmos es o(2^n) ,o(log n) y o(n).cuando n es lo suficientemente grande.
cual de los tres algoritmos es el mas eficiente?. el que tiene la complejidad:

a) o(2^n)   b) o(log n)   c)o (n)  d) todos son eficientes pues n grande
la correcta para mi es la  b)  (mas omenos la sabia)
*/

/*
2) el estado del vector {6,22,11,16,27,3,5}despues de aplicarle tres pasadas de un algritmo de ordenamiento es
{6,11,3,5,16,22,17}. que algoritmo se esta utilizando?:

a)inserccion         b)shell sort       c)bubble sort    d)quick sort
al puro achunte puse la d)  (al achunte)

*/


/*
3) cual de los isguientes algoritmos de busqueda es necesarioque el vector en donde se realiza la busqueda
este ordenado?

a)busqueda binaria  b)tablas de dispercion con diserccionamiento abierto  c)busqueda lineal
d) tablas de dispercion con encadenamiento
para mi la que mejor concordaba era la c)
*/

















void ej4(){

    int v1 =10 ,v2=20;
    fun1_ej4(&v1,v2);
    printf("v1 = %d,v2 = %d",v1,v2);

}

void fun1_ej4(int *v1,int v2){
    *v1 = 30;
    v2 = 50;
}
/// respuesta  v1 = 30 v2 = 20

///5) que imprime el programa, si al ejecutarlo se introducen los valores 3 y 4 para ls variable a y b? :

void ej5(){
    double a = 3 , b = 4;
    fun_ej5(a , &b);
    printf("%.llf , %.llf \n",a , b);

}

void fun_ej5(double s1 ,double *s2){
    double x = s1 - *s2;
    s1 = s1 + *s2;
    *s2 = x;

}
/// respuesta 3 ,-1

///6) indique que valor se escribe cuando se ejecuta el siguiente programa

void ej6(){
    int a = 2 ,b = 2;
    fun2_ej6(&a,b);
    printf("%d, %d",a,b);

}
void fun2_ej6(int *a , int b){
    b = fun1_ej6(a) * fun1_ej6(&b);

}
int fun1_ej6(int *a){
    *a = *a * *a;
    return *a;

}
/// la respuesta es 4 ,2
///7) indique que valor se escribe cuando se ejecuta el siguiente programa

void ej7(){
    int n = 10 ,m = 20;
    printf("%d %d %d",fun_ej7(n , &m),n , m);

}
int fun_ej7(int x ,int *p){
    x= x + 1;
    *p = *p + 1;
    return x;

}
///respuesta 11 10 20
///8) indique q valor se escribe cuando se ejecuta el siguiente programa

void ej8(){
    fun(5);

}
void fun_ej8(int x){
    if (x == 1)
        return 0;
    printf ("%d" ,x);
    x = x - 1;
    fun_ej8(x);
    printf("%d",x);

}
///la respuesta es 5 4 3 2 1 2 3 4

///9) imprima lo q sale en el codigo
void ej9(){
    int a , b ,solu;
    a = 2;
    b = -5;
    solu = -b / a;
    printf("%d ",solu);

}
/// la respuesta es 2

/// 10) imprima lo q sale en el siguiente codigo
void ej10(){
    int n1 , n2 , n3;
    n1 = 3;
    n2 = 1;
    n3 = 5;

    if ((n1 > n2) && (n1 > n3)){
        printf("%d", n1);

    }
    else{
        if((n3 > n1) && (n2 > n3)){
            printf("%d" ,n2);

        }
        else{
            if((n3 > n1) && (n3 > n2)){
                printf("%d", n3);

            }
            else{
                printf("son iguales");
            }
        }
    }
}
///respuesta 5

///11) indique q valor se escribe cuando se ejecuta el siguien progrma

void ej11(){
    int nota1 , nota2 , nota3 , promedio ;
    nota1 = 2;
    nota2 = 3;
    nota3 = 3;
    promedio = nota1 + nota2 + nota3/3;
    if (promedio >= 4.0){
        printf('aprobado');

    }
    else{
        printf("reprobado");
    }

}
///respuesta aprobado
/// 12) indique que imprime el siguiente codigo

void ej12(){
    int x , y , z;
    x = 3;
    y = 7;
    x = x - 1;
    if (x % 2 !=0){
        x = x + 1;

    }
    y = y - 1;
    if(y % 2 !=0){
        y = y + 1;

    }
    z = x + y;
    printf('%d - %d - %d', x , y , z);

}




