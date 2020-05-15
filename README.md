# py_TSP

## Usage
1. Open a virtual environment to load packages needed.
2. To open a virtual environment open a terminal and paste `python3 -m venv py-TSP`. If you don't have virtual environment installed you can install it by `pip install virtualenv` or go to link [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) for more information.
3. After activating with  `cd py-TSP` and `source bin/activate`  install the packages in **requirements.txt** file by `pip install requirements.txt`.
4. Before we run our project we need to change some files in **Folium**. For this copy the files **folium.py** and **features.py** into folium folder by using `cp py_TSP/static/folium.py lib64/python3.8/site-packages/folium/` and `cp py_TSP/static/features.py lib64/python3.8/site-packages/folium/`.
5. Run `python3 app.py`.
6. After successfully running, go to `http://127.0.0.1:5000/` on web browser and you should see like this.

![Image](https://github.com/aakash0121/py_TSP/blob/master/static/1.png)

7. Add a few locations for delivery and the first location you enter is the location where the vehicle will start travelling.
8. Enter the desired values of Population Size, Elitism, Mutation Rate and Generations.

![Image](https://github.com/aakash0121/py_TSP/blob/master/static/2.png)

9. Hit **Start**.

## Output

![Image](https://github.com/aakash0121/py_TSP/blob/master/static/3.png)

10. To see the plot of distance and generations(iterations) go to Plot and on hover you would see a plot.

![Image](https://github.com/aakash0121/py_TSP/blob/master/static/plot.png)

This represents
