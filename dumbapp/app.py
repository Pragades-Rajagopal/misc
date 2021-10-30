import tkinter as tk
import requests
from apiKey import weather_api_key

def getDetail(app):

    try:
        value = textField.get()
        val_len = len(value)

        if (val_len == 2 or val_len == 3):
            
            url = "https://restcountries.eu/rest/v2/alpha/"+value
            fetch = requests.get(url).json()

            countryName = fetch['name']
            capital = fetch['capital']
            region = fetch['region']
            callcode = int(fetch['callingCodes'][0])
            lat = float(fetch['latlng'][0])
            lng = float(fetch['latlng'][1])
            nativeName = str(fetch['nativeName'])
            currency = fetch['currencies'][0]['name']
            weather = getWeather(capital)
            code = fetch['alpha2Code']
            code3 = fetch['alpha3Code']

            data1 = countryName + "\n" + capital + "\n" + region + "\n" + str(weather) + "°C"
            data2 = "Native Name : " + nativeName + "\n" + "Currency : " + currency + "\n" + "Coordinate : " + str(lat) + "°, " + str(lng) + "°" + "\n" + "Calling Code : " + str(callcode) + "\n" + "ISO Codes : " + code + ", " + code3

            label1.config(text=data1)
            label2.config(text=data2)
            textField.delete(0,"end")

        elif (val_len > 3):

            url = "https://restcountries.eu/rest/v2/capital/"+value
            fetch = requests.get(url).json()

            countryName = fetch[0]['name']
            capital = fetch[0]['capital']
            region = fetch[0]['region']
            callcode = int(fetch[0]['callingCodes'][0])
            lat = float(fetch[0]['latlng'][0])
            lng = float(fetch[0]['latlng'][1])
            nativeName = str(fetch[0]['nativeName'])
            currency = fetch[0]['currencies'][0]['name']
            weather = getWeather(capital)
            code = fetch[0]['alpha2Code']
            code3 = fetch[0]['alpha3Code']

            data1 = countryName + "\n" + capital + "\n" + region + "\n" + str(weather) + "°C"
            data2 = "Native Name : " + nativeName + "\n" + "Currency : " + currency + "\n" + "Coordinate : " + str(lat) + "°, " + str(lng) + "°" + "\n" + "Calling Code : " + str(callcode) + "\n" + "ISO Codes : " + code + ", " + code3

            label1.config(text=data1)
            label2.config(text=data2)
            textField.delete(0,"end")

        elif (val_len == 0):

            label1.config(text="")
            label2.config(text="Please enter the correct code or capital")
            textField.delete(0,"end")

    
    except Exception as e:
        label1.config(text="Zoinks! :'(")
        label2.config(text="Please enter the correct code or capital")
        textField.delete(0,"end")


def getWeather(city):
    weather_url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&appid="+weather_api_key
    fetch = requests.get(weather_url).json()
    
    return int(fetch['main']['temp'])


app = tk.Tk()

app.geometry("600x500")
app.title("Country Details")
app.config(bg="#FF5733")

t = ('poppins', 30, "bold")
f = ('poppins', 15, "italic")

textField = tk.Entry(app, font=t, justify="center", bg="#DAF7A6")
textField.pack(pady=18, padx=50)
textField.focus()
textField.bind('<Return>', getDetail)

label1 = tk.Label(app, font=t, bg="#FF5733")
label2 = tk.Label(app, font=f, bg="#FF5733")

label1.pack()
label2.pack()

app.mainloop()
