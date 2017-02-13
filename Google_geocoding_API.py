from urllib.request import urlopen
import json

def Revese_geocode_API(long,lat):
    address = urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng="+lat+","+long+ 
                      "&key=AIzaSyAk6RWNv0e9AEw7K1TNl4UGadYn1DINYGg").read().decode('utf-8')
    return(address)

long = '-118.283834'
lat = '34.095475'
address = Revese_geocode_API(long,lat)
json_handle = json.loads(address)
type(json_handle)
address = (json_handle['results'][0]['formatted_address'])
print (address)
###Artist is elliot smith