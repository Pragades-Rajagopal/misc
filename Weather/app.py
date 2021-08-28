import tkinter as tk
import requests
from apiKey import weather_api_key
import time

def getWEATHER(app):
    city = textField.get()

    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&appid="+weather_api_key
    jsonData = requests.get(url).json()

    cityName = jsonData['name']
    countrycd = jsonData['sys']['country']
    description = str(jsonData['weather'][0]['description']).capitalize()
    temp = int(jsonData['main']['temp'])
    minTemp = int(jsonData['main']['temp_min'])
    maxTemp = int(jsonData['main']['temp_max'])
    pressure = jsonData['main']['pressure']
    humidity = jsonData['main']['humidity']
    wind = jsonData['wind']['speed']
    deg = jsonData['wind']['deg']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(jsonData['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(jsonData['sys']['sunset'] - 21600))

    finalInfo = cityName + ", " + countrycd + "\n" + str(temp) + "°C" + "\n" + description
    finalData = "\n" + "Max Temp : " + str(maxTemp) + "°C" + "\n" + "Min Temp : " + str(minTemp) + "°C" + "\n" + "Pressure : " + str(pressure) + "bar" + "\n" + "Humidity : " + str(humidity) + "%" + "\n" + "Wind : " + str(wind) + "m/s" + " (" + str(deg) + "°)" + "\n" + "Sunrise : " + str(sunrise) + "\n" + "Sunset : " + str(sunset)

    label1.config(text=finalInfo)
    label2.config(text=finalData)


app = tk.Tk()

app.geometry("600x500")
app.title("Weather application")

f = ("poppins", 15, "bold")
t = ("poppins", 30, "bold")

textField = tk.Entry(app, font=t, takefocus="center")
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWEATHER)

label1 = tk.Label(app, font=t)
label2 = tk.Label(app, font=f)
label1.pack()
label2.pack()



app.mainloop()
