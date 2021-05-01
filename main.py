import tkinter as tk
import random
import time
#from numpy import random

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
MergeSort = tk.Button(window, text="merge", command=lambda: mergeSort(lines, 0, len(lines) -1))
MergeSort.pack()
RadixSort = tk.Button(window, text="radix", command=lambda: radixSort(lines))
RadixSort.pack()
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
        window.after(1)
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




window.mainloop()
