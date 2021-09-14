from flask import Flask, render_template, request, send_file
import pandas
from geopy.geocoders import Nominatim
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success-table", methods=['POST'])
def success_table():
    if request.method == "POST":
        file = request.files['file']
        df = pandas.read_csv(file)
        gc = Nominatim(user_agent="http")
        df["coordinates"] = df["Address"].apply(gc.geocode)
        df["Latitude"] = df["coordinates"].apply(lambda x: x.latitude if x != None else None)
        df["Longitude"] = df["coordinates"].apply(lambda x: x.latitude if x != None else None)
        df = df.drop("coordinates", 1)
        df.to_csv("uploads/geocoded.csv", index=None)
        return render_template("index.html", text=df.to_html())


@app.route("/download-file/")
def download():
    return send_file()


if __name__ == '__main__':
    app.debug = True
    app.run()
