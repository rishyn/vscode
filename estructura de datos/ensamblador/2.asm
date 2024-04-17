
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.Data
    cadena db "P""h""i""l""i""p""$"
    largo db $-cadena
    
    
.Code
    mov cl,largo
    lea si , cadena
    
    vuelvo:
    
    cmp cl,0
    je fin
    
    mov al ,'i'
    mov bl,[si] 
    
    cmp al ,bl
     
    
    
    je igual
    jne noigual
    
    
    
    
    
    noigual:
        mov dl,bl
        add bl,48
        mov ah,2
        int 21h
         
         
         
        mov dl,1
        add dl,47
        mov ah,2
        int 21h
        
        inc bl
        
        jmp vuelvo
        
    igual:
        mov dl,0
        add dl,47
        mov ah,2
        int 21h
        
        jmp vuelvo
        
    fin:
    


ret




