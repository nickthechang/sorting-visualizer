import tkinter as tk
import random
import time

array = random.sample(range(248), 248)
#lines = []  # holds line height
canvasids = []  # holds ids of lines made
lines = random.sample(range(1, 251), 250)
#lines = random.sample(range(200), 200)

window = tk.Tk()
window.geometry("500x500")
canvas = tk.Canvas(window, bg="white",height=250, width=250)
canvas.pack()
#lines.pack()



makeArray = tk.Button(window, text="make array", command=lambda: makeline(xaxis))
makeArray.pack()
BubbleSort = tk.Button(window, text="bubbles", command=lambda: bubbleSort())
BubbleSort.pack()
SelectionSort = tk.Button(window, text="selection", command=lambda: selectionSort())
SelectionSort.pack()
InsertionSort = tk.Button(window, text="insertion", command=lambda: insertionSort())
InsertionSort.pack()
MergeSort = tk.Button(window, text="merge", command=lambda: mergeSort(lines))
MergeSort.pack()
QuickSort = tk.Button(window, text="quick", command=lambda: quicksort(lines, 0, len(lines)-1))
QuickSort.pack()
HeapSort = tk.Button(window, text="heap", command=lambda: heapsort(lines))
HeapSort.pack()
delete = tk.Button(window, text= "delete", command=lambda: deleteLines())
delete.pack()


xaxis = 0
yaxis = 0
def makeline(xaxis):
    index = 0;
    for i in lines:
        canvasid=canvas.create_line(xaxis, 250, xaxis, 250-i)
        canvasids.append(canvasid)
        xaxis += 1
        #print("index" + str(canvasids[index]))
        #if lines[index] == 200:
            #print(lines[index])
        index+=1
        window.after(10)
        window.update()

def deleteLines():
    canvas.delete("all")
    global lines, canvasids
    lines *= 0
    canvasids *= 0
    lines = random.sample(range(1, 251), 250)

def make(l):
    l = random.sample(range(1, 251), 250)
    return l

def bubbleSort():
    n = len(canvasids)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if lines[j] > lines[j+1]:
                lines[j], lines[j + 1] = lines[j+1], lines[j]
                canvas.delete(canvasids[j])
                canvas.delete(canvasids[j+1])
                canvasids[j] = canvas.create_line(j, 250, j, 250-lines[j])
                canvasids[j+1] = canvas.create_line(1 + j, 250, 1 + j, 250-lines[j+1])
                #window.after(1)
                window.update()

def selectionSort():
    for i in range(len(canvasids)):
        min_idx = i
        for j in range(i + 1, len(lines)):
            if lines[min_idx] > lines[j]:
                min_idx = j
        lines[i], lines[min_idx] = lines[min_idx], lines[i]
        canvas.delete(canvasids[i])
        canvas.delete(canvasids[min_idx])
        canvasids[i] = canvas.create_line(i, 250, i, 250 - lines[i])
        canvasids[min_idx] = canvas.create_line(min_idx, 250, min_idx, 250 - lines[min_idx])
        window.after(1)
        window.update()


def insertionSort():
    global lines
    for i in range(1, len(lines)):
        key = lines[i]
        j = i - 1
        while j >= 0 and key < lines[j]:
            lines[j + 1] = lines[j]
            canvas.delete(canvasids[j])
            canvas.delete(canvasids[j + 1])
            canvasids[j] = canvas.create_line(j, 250, j, 250 - lines[j])
            canvasids[j + 1] = canvas.create_line(1 + j, 250, 1 + j, 250 - lines[j + 1])
            #window.after(1)
            window.update()
            j -= 1
        lines[j + 1] = key


def mergeSort(arr):
    #global lines
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                #canvas.delete(canvasids[k])
                #canvas.delete(canvasids[i])
                #canvasids[i] = canvas.create_line(i, 250, i, 250 - arr[i])
                #canvasids[k] = canvas.create_line(k, 250, k, 250 - arr[k])
                # window.after(1)
                window.update()
            else:
                arr[k] = R[j]
                j += 1
                #canvas.delete(canvasids[k])
                #canvas.delete(canvasids[j])
                #canvasids[j] = canvas.create_line(j, 250, j, 250 - arr[i])
                #canvasids[k] = canvas.create_line(k, 250, k, 250 - arr[k])
                # window.after(1)
                window.update()
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            #canvas.delete(canvasids[k])
            #canvas.delete(canvasids[i])
            #canvasids[i] = canvas.create_line(i, 250, i, 250 - arr[i])
            #canvasids[k] = canvas.create_line(k, 250, k, 250 - arr[k])
            # window.after(1)
            window.update()


        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            #canvas.delete(canvasids[k])
            #canvas.delete(canvasids[j])
            #canvasids[j] = canvas.create_line(j, 250, j, 250 - arr[i])
            #canvasids[k] = canvas.create_line(k, 250, k, 250 - arr[k])
            # window.after(1)
            window.update()
    print(arr)


def partition(array, start, end):
    global canvasids
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            canvas.delete(canvasids[low])
            canvas.delete(canvasids[high])
            canvasids[low] = canvas.create_line(low, 250, low, 250 - lines[low])
            canvasids[high] = canvas.create_line(high, 250, high, 250 - lines[high])
            window.after(1)
            window.update()
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]
    canvas.delete(canvasids[start])
    canvas.delete(canvasids[high])
    canvasids[start] = canvas.create_line(start, 250, start, 250 - lines[start])
    canvasids[high] = canvas.create_line(high, 250, high, 250 - lines[high])
    window.after(1)
    window.update()
    return high


def quicksort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quicksort(array, start, p-1)
    quicksort(array, p+1, end)


def heapify(arr, n, i):
    global canvasids
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        canvas.delete(canvasids[i])
        canvas.delete(canvasids[largest])
        canvasids[i] = canvas.create_line(i, 250, i, 250 - lines[i])
        canvasids[largest] = canvas.create_line(largest, 250, largest, 250 - lines[largest])
        window.after(1)
        window.update()
        heapify(arr, n, largest)


def heapsort(arr):
    global canvasids
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        canvas.delete(canvasids[i])
        canvas.delete(canvasids[0])
        canvasids[i] = canvas.create_line(i, 250, i, 250 - lines[i])
        canvasids[0] = canvas.create_line(0, 250, 0, 250 - lines[0])
        window.after(1)
        window.update()
        heapify(arr, i, 0)


window.mainloop()
