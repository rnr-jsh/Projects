import pandas as pd
import random
import tkinter as tk
from PIL import Image, ImageTk

# Read Data and Store in Variables
data = pd.read_csv("dataset.csv")
authors = data["Author"]
quotes = data["Quote"]

# Random index number and displaying it
random_number = random.randint(0, len(quotes) - 1)

# For Logo
un_logo = Image.open("Logo.png")

# Main Window
root = tk.Tk()
root.geometry("720x450")
root.title("Luminous Wisdom")
root.configure(bg="#0f0f0f")

# Landing Page
land_page = tk.Frame(root, bg="#0f0f0f")
land_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.85, relheight=0.6)

frame1 = tk.Frame(land_page, bg="#0f0f0f")
frame1.grid(row=0, column=0, sticky="nw")

# Adjust the font sizes
def adjust_for_land_page(event):
    new_size = min(event.width, event.height) // 7
    label1.config(font=("Arial", new_size, "bold"))

    label2.config(wraplength=event.width * 0.7)

    new_size2 = new_size // 3
    label2.config(font=("Arial", new_size2))
    lumos.config(font=("Arial", new_size2, "bold"))
    exit1.config(font=("Arial", new_size2, "bold"))

    if(event.width > 900):
        new_width = event.width // 85
        lumos.config(width=new_width)
        exit1.config(width=new_width // 2)
    else:
        new_width = event.width // 50
        lumos.config(width=new_width)
        exit1.config(width=new_width // 2)

    resized_image = un_logo.resize((event.width // 3, event.height), Image.BILINEAR)
    logo = ImageTk.PhotoImage(resized_image)
    label3.config(image=logo)
    label3.image = logo


# Title Label
label1 = tk.Label(frame1, text="LUMINOUS\nWIDSOM", bg="#0f0f0f", fg="#fff000", bd=0,
                anchor="w", justify="left") 
label1.pack(side="top", expand=True, fill=tk.X)

# Description
description = '''A sleek and simple quote generator that delivers daily inspiration, wisdom, and motivation at the click of a button. Whether you need a boost of creativity, a thoughtful perspective, or just a fun quote to share.'''
label2 = tk.Label(frame1, text=description, bg="#0f0f0f", fg="#f0f0f0", bd=0,
                anchor="w", justify="left", wraplength=350)
label2.pack(side="bottom", expand=True, fill=tk.X, pady=20)

frame2 = tk.Frame(land_page, bg="#0f0f0f")
frame2.grid(row=1, column=0, sticky="w")

# Button: Lumos
def lumos():
    quote_page()

lumos = tk.Button(frame2, text="LUMOS", bg="#fff000", fg="#0f0f0f", bd=0, cursor="hand2",
                  command=lumos)
lumos.pack(side="left", expand=True, fill=tk.X, padx=2)

# Button: Exit
def exit():
    root.destroy()

exit1 = tk.Button(frame2, text="EXIT", bg="#fff000", fg="#0f0f0f", bd=0, cursor="hand2",
                  command=exit)
exit1.pack(side="right", expand=True, fill=tk.X, padx=20)


frame3 = tk.Frame(land_page, bg="#ffffff")
frame3.grid(row=0, column=1, rowspan=2)

# Logo
logo = ImageTk.PhotoImage(un_logo)

label3 = tk.Label(frame3, image=logo, bg="#0f0f0f")
label3.pack(side="left", expand=True, fill=tk.BOTH)

land_page.rowconfigure(0, weight=2)
land_page.rowconfigure(1, weight=1)
land_page.columnconfigure(0, weight=6)
land_page.columnconfigure(1, weight=4)

land_page.bind("<Configure>", adjust_for_land_page)

def quote_page():
    quotation = tk.Frame(root, bg="#0f0f0f")
    quotation.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.95, relheight=0.9)

    frame4 = tk.Frame(quotation, bg="#f0f0f0")
    frame4.grid(row=0, column=0, sticky="e")
    
    label4 = tk.Label(frame4, image=logo, bg="#0f0f0f")
    label4.pack(expand=True, fill=tk.BOTH)

    def adjust_for_quotation(event):
        resized_image = un_logo.resize((event.width // 20, event.height // 10), Image.BILINEAR)
        logo = ImageTk.PhotoImage(resized_image)
        label4.config(image=logo)
        label4.image = logo

        new_size = min(event.width, event.height) // 35
        label5.config(font=("Arial", new_size, "bold"))
        exit2.config(font=("Arial", new_size, "bold"))

        new_width = event.width // 100
        if event.width > 850:
            exit2.config(padx=event.width // 120)
            exit2.config(width=new_width // 2)
            this_quote.config(height = event.height / 130)
            lumos_again.pack(padx=50)
            lumos_again.config(font=("Arial", event.width // 70, "bold"))
        else:
            exit2.config(padx=event.width // 30)
            exit2.config(width=new_width)
            this_quote.config(height = event.height / 70)
            lumos_again.pack(padx=30)
            lumos_again.config(font=("Arial", event.width // 50, "bold"))

        canvas.config(width=event.width // 3, height=event.height // 10) 
        canvas1.config(width=event.width // 7, height=event.height // 10)

        new_padx = event.width // 11
        this_quote.pack(padx = new_padx)

        font_size = event.width // 30
        this_quote.config(font=("Arial", font_size))


    frame5 = tk.Frame(quotation, bg="#0f0f0f")
    frame5.grid(row=0, column=1, sticky="w")

    label5 = tk.Label(frame5, text="Luminous Wisdom", bg="#0f0f0f", fg="#f0f0f0",
                      bd=0, anchor="w", justify="left")
    label5.pack(side="left", expand=True, fill=tk.BOTH)

    frame6 = tk.Frame(quotation, bg="#0f0f0f")
    frame6.grid(row=0, column=2)

    canvas = tk.Canvas(frame6, bg="#0f0f0f", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    frame7 = tk.Frame(quotation, bg="#0f0f0f")
    frame7.grid(row=0, column=3)

    canvas1 = tk.Canvas(frame7, bg="#0f0f0f", highlightthickness=0)
    canvas1.pack(fill="both", expand=True)

    frame8 = tk.Frame(quotation, bg="#0f0f0f")
    frame8.grid(row=0, column=4)

    exit2 = tk.Button(frame8, text="EXIT", bg="#0f0f0f", fg="#f0f0f0", bd=0, cursor="hand2",
                  command=exit)
    exit2.pack(side="right", expand=True, fill=tk.X)

    frame9 = tk.Frame(quotation, bg="#0f0f0f")
    frame9.grid(row=1, column=0, columnspan=5, sticky="nsew")

    new_line = "\n\n"
    this_quote = tk.Text(frame9, bg="#0f0f0f", fg="#f0f0f0", wrap="word", bd=0)
    this_quote.pack(expand=True, fill=tk.BOTH)
    this_quote.tag_configure("center", justify="center")
    this_quote.insert("1.0", new_line, "center")

    quote = quotes[random_number]
    this_quote.insert("2.0", quote, "center")

    this_quote.insert("3.0", new_line, "center")

    author = authors[random_number]
    this_quote.insert("4.0", author, "center")

    frame10 = tk.Frame(quotation, bg="#0f0f0f")
    frame10.grid(row=2, column=3, columnspan=2, sticky='nsew')

    def again():
        random_number = random.randint(0, len(quotes) - 1)
        this_quote.delete("2.0", "4.0")

        quote = quotes[random_number]
        this_quote.insert("2.0", quote, "center")

        this_quote.insert("3.0", new_line, "center")

        author = authors[random_number]
        this_quote.insert("4.0", author, "center")

    lumos_again = tk.Button(frame10, text="LUMOS ITERUM", bg="#fff000", fg="#0f0f0f", bd=0, cursor="hand2",
                  command=again)
    lumos_again.pack(expand=True, fill=tk.X)    

    for i in range(3):
        quotation.rowconfigure(i, weight=1)
        for j in range(5):
            quotation.columnconfigure(j, weight=1)
    
    quotation.bind("<Configure>", adjust_for_quotation)


root.mainloop()