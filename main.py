import tkinter as tk
#from tkinter import *

import random
#import time

array = random.sample(range(248), 248)
#lines = []  # holds line height
canvasids = []  # holds ids of lines made
lines = random.sample(range(1, 251), 250)
#lines = random.sample(range(200), 200)

window = tk.Tk()
window.geometry("500x250")
canvas = tk.Canvas(window, bg="white",height=250, width=250)
#window.resizable(False, False)
canvas.pack()
#lines.pack()



makeArray = tk.Button(window, text="make array", command=lambda: makeline(xaxis))
makeArray.place( x =30, y = 10, anchor = "nw")
#makeArray.pack()
BubbleSort = tk.Button(window, text="bubbles", command=lambda: bubbleSort())
BubbleSort.place(relx = 1, x =-30, y = 10, anchor = "ne")
#BubbleSort.pack()
SelectionSort = tk.Button(window, text="selection", command=lambda: selectionSort())
SelectionSort.place(relx = 1, x =-30, y = 40, anchor = "ne")
InsertionSort = tk.Button(window, text="insertion", command=lambda: insertionSort())
InsertionSort.place(relx = 1, x =-30, y = 70, anchor = "ne")
MergeSort = tk.Button(window, text="merge", command=lambda: mergeSort(lines, 0, len(lines) -1))
MergeSort.place(relx = 1, x =-30, y = 100, anchor = "ne")
RadixSort = tk.Button(window, text="radix", command=lambda: radixSort(lines))
RadixSort.place(relx = 1, x =-30, y = 130, anchor = "ne")
QuickSort = tk.Button(window, text="quick", command=lambda: quicksort(lines, 0, len(lines)-1))
QuickSort.place(relx = 1, x =-30, y = 160, anchor = "ne")
HeapSort = tk.Button(window, text="heap", command=lambda: heapsort(lines))
HeapSort.place(relx = 1, x =-30, y = 190, anchor = "ne")
CountSort = tk.Button(window, text="count", command=lambda: countsort(lines, 250))
CountSort.place(relx = 1, x =-30, y = 220, anchor = "ne")
delete = tk.Button(window, text= "delete", command=lambda: deleteLines())
delete.place( x =30, y = 40, anchor = "nw")
#delete.pack()


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
                canvas.itemconfig(canvasids[j], fill="red")
                window.update()

                window.update()
                canvasids[j+1] = canvas.create_line(1 + j, 250, 1 + j, 250-lines[j+1])
                canvas.itemconfig(canvasids[j+1], fill="red")
                window.update()

                window.after(1)
                window.update()
                canvas.itemconfig(canvasids[j], fill="black")
                canvas.itemconfig(canvasids[j + 1], fill="black")
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
        canvas.itemconfig(canvasids[i], fill="red")
        window.update()
        canvasids[min_idx] = canvas.create_line(min_idx, 250, min_idx, 250 - lines[min_idx])
        canvas.itemconfig(canvasids[min_idx], fill="red")
        window.update()
        window.after(1)
        window.update()
        canvas.itemconfig(canvasids[i], fill="black")
        canvas.itemconfig(canvasids[min_idx], fill="black")
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
            canvas.itemconfig(canvasids[j], fill="red")
            window.update()
            canvasids[j + 1] = canvas.create_line(1 + j, 250, 1 + j, 250 - lines[j + 1])
            canvas.itemconfig(canvasids[j+1], fill="red")
            window.update()
            window.after(1)
            window.update()
            canvas.itemconfig(canvasids[j], fill="black")
            canvas.itemconfig(canvasids[j+1], fill="black")
            window.update()
            j -= 1
        lines[j + 1] = key


#Radix Sort
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
        canvas.delete(canvasids[i])
        canvasids[i] = canvas.create_line(i, 250, i, 250 - arr[i])
        canvas.itemconfig(canvasids[i], fill="red")
        window.update()
        window.after(1)
        window.update()
        canvas.itemconfig(canvasids[i], fill="black")
        window.update()


# Method to do Radix Sort
def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10

#MergeSort


def merge(array, left_index, right_index, middle):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            canvas.delete(canvasids[sorted_index])
            #canvas.delete(canvasids[left_copy_index])
            canvasids[sorted_index] = canvas.create_line(sorted_index, 250, sorted_index, 250 - lines[sorted_index])
            #canvasids[left_copy_index] = canvas.create_line(left_copy_index, 250, left_copy_index, 250 - lines[left_copy_index])
            window.after(1)
            window.update()
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            canvas.delete(canvasids[sorted_index])
            #canvas.delete(canvasids[left_copy_index])
            canvasids[sorted_index] = canvas.create_line(sorted_index, 250, sorted_index, 250 - lines[sorted_index])
            #canvasids[right_copy_index] = canvas.create_line(right_copy_index, 250, right_copy_index, 250 - lines[right_copy_index])
            window.after(1)
            window.update()
            right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        canvas.delete(canvasids[sorted_index])
        # canvas.delete(canvasids[left_copy_index])
        canvasids[sorted_index] = canvas.create_line(sorted_index, 250, sorted_index, 250 - lines[sorted_index])
        # canvasids[left_copy_index] = canvas.create_line(left_copy_index, 250, left_copy_index, 250 - lines[left_copy_index])
        window.after(1)
        window.update()
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        canvas.delete(canvasids[sorted_index])
        # canvas.delete(canvasids[left_copy_index])
        canvasids[sorted_index] = canvas.create_line(sorted_index, 250, sorted_index, 250 - lines[sorted_index])
        # canvasids[right_copy_index] = canvas.create_line(right_copy_index, 250, right_copy_index, 250 - lines[right_copy_index])
        window.after(1)
        window.update()
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

def mergeSort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    mergeSort(array, left_index, middle)
    mergeSort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)

#mergeSort(lines, 0, len(lines) -1)
#print(lines)
#merge_sort(lines, 0, len(lines)-1)





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


def countsort(arr, max_val):
    m = max_val + 1
    count = [0] * m
    for a in arr:
        count[a] += 1
    i=0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            canvas.delete(canvasids[i])
            canvasids[i] = canvas.create_line(i, 250, i, 250 - a)
            window.after(1)
            window.update()
            i += 1
    return arr

window.mainloop()
