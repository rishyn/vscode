//Prototipo
#include<stdio.h>







int main()
{
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
    printf("%d - %d - %d \n", x , y , z);

    return 0;
}



