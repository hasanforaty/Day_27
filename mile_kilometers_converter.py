import tkinter as tk


def calculate():
    miles = mile_input.get()
    km = int(miles) * 1.6
    km_text['text'] = km


window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=300)
window.config(padx=20, pady=20)

# Labels
tk.Label(text='Miles').grid(row=0, column=2)
tk.Label(text='is equal to').grid(row=1, column=0)
tk.Label(text='Km').grid(row=1, column=2)

mile_input = tk.Entry(width=50,font=("Arial", 8))
mile_input.grid(column=1, row=0)

km_text = tk.Label(width=50, font=("Arial", 8))
km_text.grid(column=1, row=1)

calculate_button = tk.Button(text="Calculate", command=calculate, )
calculate_button.grid(column=1, row=2)

window.mainloop()
