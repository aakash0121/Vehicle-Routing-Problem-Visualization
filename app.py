from flask import Flask, render_template, request, jsonify
import folium
from read_write_data import loadData, writeCsv
import map
import os
from genetic_algo import execute_genetic, plot_distance_with_iterations

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    m = folium.Map(location=[ 23.6856, 77.5643], tiles="OpenStreetMap", zoom_start=5)
    m.add_child(folium.ClickForMarker())
    m.save('templates/map.html')

    return render_template('map.html')

@app.route('/progress', methods = ['GET', 'POST'])
def final():

    distance_list = []
    cordinates = []
    data = request.values.get('arr_data')
    data = data.split(",")
    for i, d in enumerate(data):
        if i < len(data)-1:
            lat = float(d[1:8])
            lon = float(d[9:16])
            cordinates.append([lat, lon])
    
    writeCsv('static/data.csv', cordinates)
             
    popSize = int(request.form["popSize"])
    elitism = int(request.form["elitism"])
    mutationRate = float(request.form["mutationRate"])
    generations = int(request.form["generations"])
    for i in execute_genetic(popSize=popSize, eliteSize=elitism, mutationRate=mutationRate, generations=generations):
        bestRoute = i[0]
        distance = i[1]
        distance_list.append(distance)
        map.drawLines(bestRoute)
    print(distance)
    
    plot_distance_with_iterations(distance_list)
    os.remove("static/data.csv")
    return render_template('map.html', distance=distance)

    return jsonify({'status':'200'})
if __name__ == "__main__":
    app.run(debug=True)