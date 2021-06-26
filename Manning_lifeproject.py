

import tkinter as tk
import random as r
import time

window = tk.Tk()
unit = tk.Canvas(window, width=1000, height=1000)
unit.pack()


def main():
    line = 20
    window_size = 20
    rain_rate = 0.1
    drop_increase = 5
    reset_size = 50

    window.geometry('1000x1000')
    lst_oval = [[2 for i in range(line)] for j in range(line)]
    for i in range(line):
        unit.create_line(i*1000/line, 0, i*1000/line, 1000)
    for j in range(line):
        unit.create_line(0, j*1000/line, 1000, j*1000/line)

    while True:
        for k in range(line):
            for l in range(line):
                test = r.random()
                if test <= rain_rate:
                    lst_oval[k][l] += drop_increase
                    if lst_oval[k][l] > reset_size:
                        for i in range(k, line):
                            lst_oval[i][l] = 0
                print(test)
                create_oval(l*1000/line, k*1000/line, lst_oval[k][l])

        unit.update()
        time.sleep(0.1)
        unit.delete("drops")

    # window.mainloop()


def create_oval(x, y, size):
    global unit
    unit.create_oval(x+50-size, y+50-size, x+50+size, y+50+size, fill="blue", tag="drops")


if __name__ == "__main__":
    main()