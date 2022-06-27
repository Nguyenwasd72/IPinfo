import ipinfo
import pycountry

token = 'your https://ipinfo.io token'
handler = ipinfo.getHandler(token)
ip_address = input("Target IP Address")
response = handler.getDetails(ip_address)

country_lf = pycountry.countries.get(alpha_2=response.country)

if response.loc != undefined:
  print(f"Country: {} \n City: {} \n Timezone: {} \n Location: {}".format(country_lf, response.city, response.timezone, response.loc))
else:
  print("Give me real IP Address next time")
