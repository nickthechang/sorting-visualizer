import tkinter as tk
import random
import time

array = random.sample(range(200), 200)

window = tk.Tk()
canvas = tk.Canvas()
canvas.pack()
canvasids = []
makeArray = tk.Button(window, text="make array", command=lambda: makeline(xaxis))
makeArray.pack()
bubbleSort = tk.Button(window, text="bubbles", command=lambda: bubbleSort())
bubbleSort.pack()



xaxis = 0
yaxis = 0
def makeline(xaxis):
    index = 0;
    for i in array:
        canvasid=canvas.create_line(2+xaxis, 20, 2+ xaxis, 20+i)
        canvasids.append(canvasid)
        xaxis += 1
        print(canvasids[index])
        print(array[index])
        index+=1
        window.after(10)
        window.update()

def bubbleSort():
    n = len(canvasids)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j+1], array[j]
                canvas.delete(canvasids[j])
                canvas.delete(canvasids[j+1])
                canvasids[j] = canvas.create_line(2 + j, 20, 2 + j, 20+ array[j])
                canvasids[j+1] = canvas.create_line(3 + j, 20, 3 + j, 20+ array[j+1])
                #window.after(.001)
                window.update()






#for i in 200
window.mainloop()
