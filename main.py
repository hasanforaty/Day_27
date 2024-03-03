import tkinter as tk


def button_clicked():
    my_label['text'] = our_input.get()


window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=800, height=600)
window.config(padx=20, pady=20)

# Label

my_label = tk.Label(text='I am a label')
my_label.grid(column=0, row=0)

button = tk.Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

button = tk.Button(text='new Button', command=button_clicked)
button.grid(column=2, row=0)

our_input = tk.Entry()
our_input.grid(column=3, row=2)

window.mainloop()
