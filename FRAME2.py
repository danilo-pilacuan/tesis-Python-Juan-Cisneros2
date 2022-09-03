import tkinter as tk
from tkinter import ttk
import tkinter.font as font


class Frame_2(tk.Frame):

    def __init__(self, container, controller, *args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg="yellow")

        self.entrada_usuario = tk.StringVar()

        L_1 = tk.Label(self, text="MI FIRST FRAME WITH OOP AND TKINTER", font=(
            "Times New Roman", 14, "bold"), bg="yellow", fg="blue")
        L_1.grid(row=0, column=0, columnspan=4, sticky="n")
        L_2 = tk.Label(self, text="Entry name: ", font=(
            "Times New Roman", 12), bg="yellow")
        L_2.grid(row=1, column=0, sticky="w")

        self.E_1 = ttk.Entry(self, textvariable=self.entrada_usuario)
        self.E_1.focus()
        self.E_1.grid(row=1, column=1, columnspan=2, padx=(0, 10))

        B_1 = ttk.Button(self, text="SAY HI", command=self.saludarme)
        B_1.grid(row=1, column=3, sticky="e")

        self.L_3 = tk.Label(self, textvariable="", font=(
            "Times New Roman", 12, "bold"), bg="yellow")
        self.L_3.grid(row=2, column=0, columnspan=4, sticky="nsew")

        B_2 = ttk.Button(self, text="espannol",
                         command=lambda: controller.show_frame(Frame_1))
        B_2.grid(row=3, column=0)

    def saludarme(self, *args):
        self.L_3.configure(text="Good Morning, {}.".format(
            self.entrada_usuario.get()))