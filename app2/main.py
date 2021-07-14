import folium

map = folium.Map(location=[55.73, 24.35])

fg = folium.FeatureGroup(name="My map")
fg.add_child(folium.Marker(location=[55.73, 24.35], popup="Marker", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")
