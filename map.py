import folium
import numpy as np
import pandas as pd
from collections import namedtuple


def get_rotation(p1, p2):
    
    # getting difference of longitudes in radians 
    long_diff = np.radians(p2.lon - p1.lon)
    
    # getting latitudes of both points in radians
    lat1 = np.radians(p1.lat)
    lat2 = np.radians(p2.lat)
    
    x = np.sin(long_diff) * np.cos(lat2)
    y = (np.cos(lat1) * np.sin(lat2) 
        - (np.sin(lat1) * np.cos(lat2) 
        * np.cos(long_diff)))
    rotation = np.degrees(np.arctan2(x, y))
    
    # adjusting for compass bearing
    if rotation < 0:
        return rotation + 360
    return rotation

def get_arrows(locations, color='red', size=6, n_arrows=3):
    
    Point = namedtuple('Point', field_names=['lat', 'lon'])
    
    # creating point from our Point named tuple
    p1 = Point(locations[0][0], locations[0][1])
    p2 = Point(locations[1][0], locations[1][1])
    
    rotation = get_rotation(p1, p2) - 90

    arrow_lats = np.linspace(p1.lat, p2.lat, n_arrows + 2)[1:n_arrows+1]
    arrow_lons = np.linspace(p1.lon, p2.lon, n_arrows + 2)[1:n_arrows+1]
    
    arrows = []
    
    #creating each "arrow" and appending them to our arrows list
    for points in zip(arrow_lats, arrow_lons):
        arrows.append(folium.RegularPolygonMarker(location=points, 
                      fill_color=color, number_of_sides=3, 
                      radius=size, rotation=rotation))
    return arrows

def drawMarkers(cordinates):

    m = folium.Map(location=[41.2284, 80.9098], zoom_start=3)

    for i in range(len(cordinates)):

        if i == 0:
            # ic = folium.Icon(color="red", icon="static/truck.png", prefix="fa")
            ic = folium.features.CustomIcon('static/truck.png', icon_size=(50, 50))
            # drawing marker
            folium.Marker(location=[cordinates[i].lat, cordinates[i].lon],popup=f'<strong>{i}</strong>',
                        icon=ic).add_to(m)        
        else:
            ic = folium.features.CustomIcon('static/city.png', icon_size=(32, 32))
            # drawing marker
            folium.Marker(location=[cordinates[i].lat, cordinates[i].lon],popup=f'<strong>{i}</strong>',
                            icon=ic).add_to(m)
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

        folium.PolyLine(locations=[from_city, to_city], color='red').add_to(m)
        arrows = get_arrows(locations=[from_city, to_city], n_arrows=3)
        for arrow in arrows:
            arrow.add_to(m)

    m.save('templates/map.html')
