#include <stdio.h>
#include <stdlib.h>

// Definición de la estructura de un nodo
struct Node {
    int data;
    struct Node* next;
};

// Función para insertar un nuevo nodo al inicio de la lista
void insertAtBeginning(struct Node** head, int data) {
    // Crear un nuevo nodo
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

    // Asignar los datos al nuevo nodo
    newNode->data = data;

    // Hacer que el nuevo nodo apunte al nodo actual de la cabeza
    newNode->next = *head;

    // Hacer que la cabeza apunte al nuevo nodo
    *head = newNode;
}

// Función para imprimir los elementos de la lista
void printList(struct Node* head) {
    struct Node* current = head;

    printf("Lista enlazada: ");

    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }

    printf("\n");
}

int main() {
    struct Node* head = NULL;

    // Insertar elementos en la lista
    insertAtBeginning(&head, 3);
    insertAtBeginning(&head, 2);
    insertAtBeginning(&head, 1);

    // Imprimir la lista
    printList(head);

    return 0;
}