from tkinter import *
from tkinter import messagebox
import requests
from configparser import ConfigParser # To make use of config.ini file

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}" # API call

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config["api_key"]["key"]

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json() # convert a result to a json file
        # (City, Country, temp_celsius, temp_fahrenheit, icon, weather)
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = ((temp_celsius * 9) / 5) + 32
        weather = json['weather'][0]['main']
        final = (city, country, temp_celsius, temp_fahrenheit, weather)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = f'{weather[0]}, {weather[1]}'
        
        temp_lbl['text'] = '{:.2f}c {:.2f}f'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[4]
    else:
        messagebox.showerror('Error', f'Cannot find city: {city}')


app = Tk()
app.geometry('500x250')
app.title("Weather App")

city_text  = StringVar() 
city_entry = Entry(app, textvariable = city_text, justify = "center")
city_entry.pack()

search_btn = Button(app, text="Search", width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text="", font=("bold", 20))
location_lbl.pack()

temp_lbl = Label(app, text="")
temp_lbl.pack()

weather_lbl = Label(app, text="")
weather_lbl.pack()

app.mainloop()

