import folium
import pandas

data = pandas.read_csv("../../Desktop/MyPythonProject/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
loc = list(data["LOCATION"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6)

fg = folium.FeatureGroup(name="MyMap")

for lt, ln, lc in zip(lat, lon, loc):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(loc), icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map1.html")