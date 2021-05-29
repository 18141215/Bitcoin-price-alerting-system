
from boltiot import Bolt
import time
api_key = "**************************"
device_id  = "*********"
mybolt = Bolt(api_key, device_id)
sp=10000
while True:
      if(get_bitcoin_price()>sp):
         response = mybolt.digitalWrite('0', 'HIGH')
         delay(5000)
         mybolt.digitalWrite('0', 'LOW)
      else
         response = mybolt.digitalWrite('0', 'LOW)
         print (response)
      time.sleep(30)



def get_bitcoin_price():
   URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,INR" 
   response = requests.request("GET", URL)
   response = json.loads(response.text)
   current_price = response["USD"]
   return current_price
