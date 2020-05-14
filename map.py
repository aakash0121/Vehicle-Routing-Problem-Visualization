import folium
import numpy as np
import pandas as pd
from collections import namedtuple

def get_bearing(p1, p2):
    
    '''
    Returns compass bearing from p1 to p2
    
    Parameters
    p1 : namedtuple with lat lon
    p2 : namedtuple with lat lon
    
    Return
    compass bearing of type float
    
    Notes
    Based on https://gist.github.com/jeromer/2005586
    '''
    
    long_diff = np.radians(p2.lon - p1.lon)
    
    lat1 = np.radians(p1.lat)
    lat2 = np.radians(p2.lat)
    
    x = np.sin(long_diff) * np.cos(lat2)
    y = (np.cos(lat1) * np.sin(lat2) 
        - (np.sin(lat1) * np.cos(lat2) 
        * np.cos(long_diff)))
    bearing = np.degrees(np.arctan2(x, y))
    
    # adjusting for compass bearing
    if bearing < 0:
        return bearing + 360
    return bearing

def get_arrows(locations, color='blue', size=6, n_arrows=3):
    
    '''
    Get a list of correctly placed and rotated 
    arrows/markers to be plotted
    
    Parameters
    locations : list of lists of lat lons that represent the 
                start and end of the line. 
                eg [[41.1132, -96.1993],[41.3810, -95.8021]]
    arrow_color : default is 'blue'
    size : default is 6
    n_arrows : number of arrows to create.  default is 3
    Return
    list of arrows/markers
    '''
    
    Point = namedtuple('Point', field_names=['lat', 'lon'])
    
    # creating point from our Point named tuple
    p1 = Point(locations[0][0], locations[0][1])
    p2 = Point(locations[1][0], locations[1][1])
    
    # getting the rotation needed for our marker.  
    # Subtracting 90 to account for the marker's orientation
    # of due East(get_bearing returns North)
    rotation = get_bearing(p1, p2) - 90
    
    # get an evenly space list of lats and lons for our arrows
    # note that I'm discarding the first and last for aesthetics
    # as I'm using markers to denote the start and end
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

        # drawing marker
        folium.Marker(location=[cordinates[i].lat, cordinates[i].lon],popup=f'<strong>{i}</strong>',
                        icon=folium.Icon(color='blue')).add_to(m)
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
        arrows = get_arrows(locations=[from_city, to_city], n_arrows=3)
        for arrow in arrows:
            arrow.add_to(m)

    m.save('templates/map.html')
