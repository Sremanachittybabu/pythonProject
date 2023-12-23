import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6)
fg=folium.FeatureGroup(name="MyMap")
fg.add_child(folium.Marker(location=[38.2, -99.01], popup="Hi Iam a marker", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map2.html")

