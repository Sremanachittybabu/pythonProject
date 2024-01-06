import folium
import pandas as pd
import json

# Create a map centered at a specific location
map_center = [37.7749, -122.4194]  # San Francisco, CA
my_map = folium.Map(location=map_center, zoom_start=12)

# Get latitude and longitude from txt file
data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
ele = list(data["ELEV"])


def color_checker(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# Define a style function
def style_function(feature):
    return {
        'fillColor': 'green' if feature['properties']['POP2005'] < 10000000
        else 'orange' if 10000000 <= feature['properties']['POP2005'] < 20000000 else 'red',
        'color': 'white',
        'weight': 2,
        'dashArray': '5, 5',
        'fillOpacity': 0.7
    }


for i, j, k in zip(lat, lon, ele):
    # Create a marker
    marker = [i, j]
    layer1 = folium.Marker(
        location=marker,
        popup=k,
        icon=folium.Icon(color_checker(k))
    )
    layer1.add_to(my_map)

# Load GeoJSON data from a file
geojson_file = 'world.json'
with open(geojson_file, 'r', encoding='utf-8-sig') as f:
    geojson_data = json.load(f)

# Add GeoJSON data to the map
layer2 = (folium.GeoJson(geojson_data, name='geojson', style_function=style_function))
layer2.add_to(my_map)

folium.LayerControl().add_to(my_map)

# Save the map as an HTML file
html_file_path = 'map.html'
my_map.save(html_file_path)
