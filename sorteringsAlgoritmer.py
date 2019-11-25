list = ("a","B","c","A")

def selectionSort(list):

    #Kører alle elementer i listen igennem
    for index in range(len(list)):

    # Find den mindste værdi i resten af listen
        min_idx = index
        for j in range(index+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j

    #Bytter rundt på de 2 værdier
        list[index], list[min_idx] = list[min_idx], list[index]

    #Returnerer listen
    return list

def insertionSort(list):

   #Kører alle elementer i listen igennem fra 1 af
   for index in range(1, len(list)):

    #Vi gemmer hvilken værdi den er nået til
    #sådan at algoritmen kan fortsætte derfra
    #når den er færdig med at sammenligne og bytte
    temp = list[index]
    j = index - 1

    #Sammenligner de 2 værdier
    #Hvis den til højre er mindre end den til venstre
    while (j >= 0 and temp < list[j]):

         #Byt rundt på de 2 værdier
         list[j + 1] = list[j]
         j = j - 1
    list[j + 1] = temp
