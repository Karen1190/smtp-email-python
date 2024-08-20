import requests

response = requests.get("https://api.genderize.io?name=peter&apikey=YOUR_API_KEY")
print(response.text)
# res_str = response.text
# print(type(res_str))
#
# res_dict = response.json()
# print(type(res_dict))
import requests