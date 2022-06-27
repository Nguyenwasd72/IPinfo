const fetch = require("node-fetch")
const i18n = require("i18n-iso-countries")

const ip = prompt("Target IP Address")

const token = process.env["token"]

fetch(`https://ipinfo.io/${ip}?token=${token}`).then(
  (response) => response.json()
).then(
  (jsonResponse) => {
    if (jsonResponse.loc != undefined) console.log(`Country: ${i18n.getName(jsonResponse.country, "en")}\nCity: ${jsonResponse.city}\nTimezone: ${jsonResponse.timezone}\nLocation: ${jsonResponse.loc}`)
    else console.log("Give me a real IP address next time")}
)
