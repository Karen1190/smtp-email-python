import requests
import datetime as dt

x = dt.datetime.now()
print(x)


MY_LAT = "36.286209"
MY_LONG = "59.599800"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data=response.json()
#print(data)
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
# a=sunrise.split("T")[1]
# b=a.split(":")[0]
r=int(sunrise)
o=r+3
print(o)
# a1=sunset.split("T")[1]
# b1=a1.split(":")[0]
p=int(sunset)
c=p+3
print(c)
# sunset=data["results"]["sunset"]
# print(sunrise)
# print(sunset)
# data=response.json()
print(response.text)
# res_str = response.text
# print(type(res_str))
# res_dict = response.json()
# print(type(res_dict))



