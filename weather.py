import tkinter as tk
import time
import requests
from apiKey import weather_api_key #config api key here

def getWeather(app):

    try: 
        city = textField.get()
        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&appid="+weather_api_key
        data = requests.get(url).json()
        name = data['name']
        country = data['sys']['country']
        condition = data['weather'][0]['main']
        temp = int(data['main']['temp'])
        minTemp = int(data['main']['temp_min'])
        maxTemp = int(data['main']['temp_max'])
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        sunrise = time.strftime("%I:%M:%S", time.gmtime(data["sys"]["sunrise"] - 21600))
        sunset = time.strftime("%I:%M:%S", time.gmtime(data["sys"]["sunset"] - 21600))

        final_info = name + ", " + country + "\n" + condition + "\n" + str(temp) + "°C"
        final_data = "\n" + "Max Temperature: " + str(maxTemp) + "°C"  + "\n" + "Min Temperature: " + str(minTemp) + "°C" + "\n" + "Pressure: " + str(pressure) + " bar" + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind: " + str(wind) + " m/s"  + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset) 

        label1.config(text= final_info)
        label2.config(text= final_data)

    except Exception as e:
        label1.config(text= "Zoinks :'(")
        label2.config(text= "City doesn't exist! \n Please enter a different city")

app = tk.Tk()
app.geometry("600x500")
app.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(app, justify='center', font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(app, font=t)
label2 = tk.Label(app, font=f)

label1.pack()
label2.pack()

app.mainloop()
