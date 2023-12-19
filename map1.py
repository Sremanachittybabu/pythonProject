import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6)
fg=folium.FeatureGroup(name="MyMap")
fg.add_child(folium.Marker(location=[38.2, -99.01], popup="Hi Iam a marker", icon=folium.Icon(color='green')))
map.add_child(fg)
<<<<<<< HEAD
map.save("Map2.html")

=======
map.save("Map1.html")
>>>>>>> 4fe6ca6 (mapchanges)
