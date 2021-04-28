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
MergeSort = tk.Button(window, text="merge", command=lambda: mergeSort(lines))
MergeSort.pack()
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

window.mainloop()
