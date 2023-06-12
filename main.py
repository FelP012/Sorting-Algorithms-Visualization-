from tkinter import *
import sys
import os

root = Tk()
root.geometry("150x200")
root.resizable(False, False)
root.title("Sorter")
root.iconbitmap("icon.ico")
root.config(bg="white")


def bl_sort():
    os.system('python bbsort.py')


def inse_sort():
    os.system('python inssort.py')


def sele_sort():
    os.system('python selectionsort.py')


label = Label(root, text="Select sort type,\n then press ENTER to sort")
label.pack(pady=5)

bubble_sort = Button(root, text="Bubble Sort", font=("Arial", 10), command=bl_sort)
bubble_sort.pack(pady=10)

ins_sort = Button(root, text="Insertion Sort", font=("Arial", 10), command=inse_sort)
ins_sort.pack(pady=10)

sel_sort = Button(root, text="Insertion Sort", font=("Arial", 10), command=sele_sort)
sel_sort.pack(pady=10)

root.mainloop()
