#bubble(list) -> sorted list
def bubble(ls):
    for i in range(len(ls) - 1):  
        # sorts it faster by checking if already sorted early
        shortCut = True
        for j in range(len(ls) - i - 1):  
            a = ls[j]
            b = ls[j + 1] 
            if a > b:  
                ls[j] = b 
                ls[j + 1] = a
                shortCut = False
        if(shortCut):
            print("saved you ",len(ls)-i-1," recurtions")
            break
    return ls

#selection(list) -> sorted list
def selection(ls):
    for i in range(len(ls)-1):  
        index_smallest = i
        # finds the smallest index
        for j in range(i+1, len(ls)):
            if ls[index_smallest] > ls[j]:
                index_smallest = j
        
        temp = ls[i]
        ls[i] = ls[index_smallest]
        ls[index_smallest] = temp
    return ls

#insertion(list) -> sorted list
def insertion(ls):
    for i in range(1,len(ls)):
        j = i
        while j > 0 and ls[j]<ls[j-1]:
            temp = ls[j]
            ls[j] = ls[j-1]
            ls[j-1] = temp
            j-=1
    return ls

#quicksort(list) -> sorted list
def Partition(numbers, lowIndex, highIndex):
    midpoint = lowIndex + (highIndex - lowIndex) / 2
    pivot = numbers[midpoint]
   
    done = False
    while (not done):
        while numbers[lowIndex] < pivot:
            lowIndex += 1
      
        while pivot < numbers[highIndex]: 
            highIndex -= 1
      
        if (lowIndex >= highIndex):
            done = True
      
        else:
            temp = numbers[lowIndex]
            numbers[lowIndex] = numbers[highIndex]
            numbers[highIndex] = temp
         
            lowIndex += 1
            highIndex -= 1

    return highIndex


def quicksort(numbers, lowIndex, highIndex):
   if lowIndex >= highIndex:
      return
   

   lowEndIndex = Partition(numbers, lowIndex, highIndex)
   
   Quicksort(numbers, lowIndex, lowEndIndex)
   Quicksort(numbers, lowEndIndex + 1, highIndex)

#shell(list) -> sorted list
def insertionSort(ls, start, gap):
    for i in range(start + gap, len(ls), gap):
        x = i
        while ((x - gap) >= start) and (ls[x] < ls[x - gap]):
            temp = ls[x]
            ls[x] = ls[x - gap]
            ls[x - gap] = temp
            x = x - gap

def shell(numbers):
    numSize = len(numbers)
    tempSize = numSize
    temp = 0
    gaps = []
    swaps = []
    while tempSize>0:
        tempSize=tempSize/2
        temp+=1
        gaps.append(2^temp)
    gaps.reverse()
    for i in gaps:
        for x in range(i):
            swaps.append(insertionSort(numbers, x, i))
    
    return swaps
