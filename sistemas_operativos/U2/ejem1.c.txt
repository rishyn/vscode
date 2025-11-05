#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main(void) {
    int fd[2];
    pipe(fd);  // Crear el pipe

    /*
    	fd[0] → descriptor de lectura
	    fd[1] → descriptor de escritura
    */


    pid_t pid = fork();

    if (pid == 0) {
        close(fd[1]);  // Cerrar el extremo de escritura
        char buffer[100];
        read(fd[0], buffer, sizeof(buffer));
        printf("Hijo recibió: %s\n", buffer);
        close(fd[0]);
    } else {
        close(fd[0]);  // Cerrar el extremo de lectura
        const char *mensaje = "Hola Mundo desde el padre";
        write(fd[1], mensaje, strlen(mensaje) + 1);
        close(fd[1]);
        wait(NULL); 
    }

    return 0;
}