import requests
from win10toast import ToastNotifier
import datetime
try:
    data = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    print("Check your Internet connection")
    data = None


if data is not None:
    getData = data.json()
    covid_India = getData["Success"]

    title = """ Covid-19 India / {}""".format(datetime.date.today())

    message=""" In India covid-19 total cases is : {} , deaths : {} , recovered : {} , today-case is : {}""".format(covid_India["cases"],
    covid_India["deaths"],covid_India["recovered"],covid_India["todayCases"])

    toaster = ToastNotifier()
    toaster.show_toast(title,message,icon_path="./covid-19.ico",duration=10)


