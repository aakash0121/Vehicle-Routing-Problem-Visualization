from flask import Flask, render_template
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

@app.route('/processing', methods = ['GET', 'POST'])
def final():
    execute_genetic()
    return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True)