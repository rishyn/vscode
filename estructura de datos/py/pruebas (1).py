from os import read
import  matplotlib.pyplot as plt

def lectura(nombre):
   Maule=[]
   ar = open(nombre)
   for i in ar:
      leer = i.rstrip('\n')
      leer = leer.split(',')
      if leer[0]=='Maule':
         Maule =leer

   return Maule

def titu(titu):
   ar_2 =open(titu)
   titt= ar_2.readline()
   titt = titt.split(',')
   return titt

def ordenar(Maule,info):


   ordenado=(info[0],Maule[0],
   info[1],Maule[1],
   info[2],Maule[2],
   info[3],Maule[3],
   info[4],Maule[4],
   info[5],Maule[5],
   info[6],Maule[6],
   info[7],Maule[7],
   info[8],Maule[8],
   info[9],Maule[9],
   info[10],Maule[10],
   info[11],Maule[11],
   info[12],Maule[12],
   info[13],Maule[13])
   return ordenado

if __name__ == '__main__':
   todo =lectura('2021-09-28-CasosConfirmados-totalRegional.csv')
   titulos =titu('2021-09-28-CasosConfirmados-totalRegional.csv')
   total_ordenado = ordenar(todo,titulos)
   print(total_ordenado)











