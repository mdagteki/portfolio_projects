import requests
from datetime import datetime
import smtplib
import time

my_email = "sendersemailadress"
password = "writethepasswordhere"

MY_LAT = 35.748409
MY_LONG = -86.932999

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LONG - 5 >= iss_longitude >= MY_LONG + 5  and MY_LAT -5 >= iss_latitude >= MY_LAT +5:
         return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <=sunrise:
        return True
while True:
    time.sleep(5)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="receiver@gmail.com",
                msg=f"Subject:ISS is overhead !\n\n Tonight do not forget to check the sky for ISS sattellite "
            )
    else:
        print("not today")





