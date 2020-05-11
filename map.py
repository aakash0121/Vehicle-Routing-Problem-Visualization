import folium

def initial_map(m, cordinates):
    for i in range(len(cordinates)):

        # drawing marker
        folium.Marker(location=[cordinates[i][0], cordinates[i][1]],popup=f'<strong>{i}</strong>',
                        icon=folium.Icon(color='red')).add_to(m)

def drawMarkers(cordinates):

    m = folium.Map(location=[41.2284, 80.9098], zoom_start=3)

    for i in range(len(cordinates)):

        # drawing marker
        folium.Marker(location=[cordinates[i].lat, cordinates[i].lon],popup=f'<strong>{i}</strong>',
                        icon=folium.Icon(color='red')).add_to(m)
    return m

# draw lines between two points
def drawLines(route):

    m = drawMarkers(route)

    for i in range(len(route)):
        from_city = route[i]
        if i + 1 < len(route):
            to_city = route[i+1]
        else:
            to_city = route[0]

        lat_from_city = from_city.lat
        lon_from_city = from_city.lon

        lat_to_city = to_city.lat
        lon_to_city = to_city.lon

        from_city = [lat_from_city, lon_from_city]
        to_city = [lat_to_city, lon_to_city]

        folium.PolyLine(locations=[from_city, to_city], color='blue').add_to(m)

    m.save('templates/map.html')
