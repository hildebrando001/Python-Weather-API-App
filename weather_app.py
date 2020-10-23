from tkinter import *

def search():
    pass


app = Tk()
app.geometry('700x350')
app.title("Weather App")

city_text  = StringVar() 
city_entry = Entry(app, textvariable = city_text)
city_entry.pack()

search_btn = Button(app, text="Search", width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text="", font=("bold", 20))
location_lbl.pack()

image = Label(app, bitmap="")
image.pack()

temp_lbl = Label(app, text="")
temp_lbl.pack()

weather_lbl = Label(app, text="")
weather_lbl.pack()

app.mainloop()

