import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=800, height=600)


def button_clicked():
    my_label['text'] = our_input.get()


# Label

my_label = tk.Label(text='I am a label')
my_label.pack()

button = tk.Button(text='Click Me', command=button_clicked)
button.pack()

our_input = tk.Entry()
our_input.pack()

window.mainloop()
