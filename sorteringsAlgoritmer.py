from random import shuffle

alist = [3,6,2,5,7,3,3,6]

def selectionSort(list):
    #Kører alle elementer i listen igennem
    for i in range(len(list)):

    # Find den mindste værdi i resten af listen
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j

    # Bytter rundt på de 2 værdier
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

def insertionSort(list):

   #Kører alle elementer i listen igennem fra 1 af
   for index in range(1,len(list)):

     #Vi gemmer hvilken værdi den er nået til
     #sådan at algoritmen kan fortsætte derfra
     #når den er færdig med at sammenligne og bytte
     currentvalue = list[index]
     position = index

     #Sammenligner de 2 værdier
     #Hvis den til højre er mindre end den til venstre
     while position>0 and list[position-1]>currentvalue:
         #Byt rundt på de 2 værdier
         list[position]=list[position-1]
         position = position-1
     list[position]=currentvalue
