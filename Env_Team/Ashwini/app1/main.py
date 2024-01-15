import folium
import pandas
import json

#Read from a file
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#color checker
def color_dec(elevation):
    if elevation < 1000 :
        return 'blue'
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"
    
def style_function(feature):
    return{
        'fillColor':'green' if feature['properties']['POP2005'] < 10000000
        else 'orange' if 10000000 <= feature['properties']['POP2005'] < 20000000 else 'red',
        'color' : 'white',
        'weight' : 2,
        'dashArray' : '5, 5',
        'fillOpacity' : 0.7


    }


map = folium.Map(location = [38.58, -99.89] , zoom_start=6)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 5 , 
                                     popup=str(el)+"m" , fill_color = color_dec(el) , 
                                     color = 'grey' , fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

geojson_file = 'world.json'
with open(geojson_file,'r',encoding='utf-8-sig') as f:
    geojson_data = json.load(f)

fgp.add_child(folium.GeoJson(geojson_data , name= 'geojson',style_function=style_function))
map.add_child(fgv)
map.add_child(fgp)
map.save("map1.html")