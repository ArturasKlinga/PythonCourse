import folium

map = folium.Map(location=[55.73, 24.35])

fg = folium.FeatureGroup(name="My map")

for coordinates in [[55.73, 24.35], [55.73, 24.33]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Marker", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")
