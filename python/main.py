import ipinfo
import pycountry

token = 'your https://ipinfo.io token'
handler = ipinfo.getHandler(token)
ip_address = input("Target IP Address")
response = handler.getDetails(ip_address)

country_lf = pycountry.countries.get(alpha_2=response.country)

print(f"{} \n {}response.city \n {} \n {}".format(country_lf, response.city, response.timezone, response.loc))
