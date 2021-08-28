import tkinter as tk
import requests
from apiKey import weather_api_key
import time

def getWEATHER(app):

    try:

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
        sunrise = time.strftime("%I:%M:%S", time.gmtime(jsonData['sys']['sunrise'])) # (-)21600 to fix GMT timezone
        sunset = time.strftime("%I:%M:%S", time.gmtime(jsonData['sys']['sunset']))

        finalInfo = cityName + ", " + countrycd + "\n" + str(temp) + "°C" + "\n" + description
        finalData = "\n" + "Max Temp : " + str(maxTemp) + "°C" + "\n" + "Min Temp : " + str(minTemp) + "°C" + "\n" + "Pressure : " + str(pressure) + "bar" + "\n" + "Humidity : " + str(humidity) + "%" + "\n" + "Wind : " + str(wind) + "m/s" + " (" + str(deg) + "°)" + "\n" + "Sunrise : " + str(sunrise) + "GMT" + "\n" + "Sunset : " + str(sunset) + "GMT"

        label1.config(text=finalInfo)
        label2.config(text=finalData)

    except Exception as e:
        label1.config(text="Zoinks! :'(")
        label2.config(text="Please enter the correct city")


app = tk.Tk()

app.geometry("600x500")
app.title("Weather application")
app.configure(bg="skyblue")

f = ("poppins", 15, "bold")
t = ("poppins", 30, "bold")
x = ("poppins", 10, "italic")

textField = tk.Entry(app, font=t, takefocus="center", justify="center", bg="skyblue")
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWEATHER)

label1 = tk.Label(app, font=t, bg="skyblue")
label2 = tk.Label(app, font=f, bg="skyblue")
label1.pack()
label2.pack()

labelx = tk.Label(app, text="Powered by OpenWeather", font=x, bg="skyblue")
labelx.pack()

app.mainloop()
