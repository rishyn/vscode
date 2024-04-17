
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.Data
    men db "Ingrese la hora $ "
    men2 db "Ingrese minutos $ "
    men3 db "Ingrese segundos $"
    salto db 10, 13
    const db 10
    hora db "?" 
    minutos db "?"
    segundos db "?"
    ;para la hora de 1 digito por favor ingrese el cero   
    
    
.Code
    mov ax, @Data
    mov ds, ax
    
    ;intro hora
    lea dx ,men
    mov ah,9h 
    
    int 21h
    
    mov ah, 01   
    int 21h 
    
    sub al, 48
    mul const  
    
    mov hora, al 
    
    mov ah,01
    int 21h 
    
    sub al, 48
    add hora ,al
    
    ;intro minuto  
    
    lea dx ,men2
    mov ah,9h
    int 21h
    
    mov ah,01
    int 21h
    
    sub al,48
    mul const 
    
    mov minutos ,al
    
    mov ah,01
    int 21h
    
    sub al,48
    add minutos ,al
    
    
    
    


ret




