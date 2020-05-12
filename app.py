from flask import Flask, render_template, request
import folium
from read_write_data import loadData
import map
from genetic_algo import execute_genetic

app = Flask(__name__)
# m.save('templates/map.html')

# load the data
data = loadData()

m = folium.Map(location=[41.2284, 80.9098], zoom_start=3)

map.initial_map(m, data)
m.save('templates/map.html')

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('map.html')

@app.route('/progress', methods = ['GET', 'POST'])
def final():
    popSize = int(request.form["popSize"])
    elitism = int(request.form["elitism"])
    mutationRate = float(request.form["mutationRate"])
    generations = int(request.form["generations"])
    execute_genetic(popSize=popSize, eliteSize=elitism, mutationRate=mutationRate, generations=generations)
    return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True)