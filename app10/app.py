from flask import Flask, render_template, request, send_file
import pandas
from geopy.geocoders import Nominatim
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success-table", methods=['POST'])
def success_table():
    global filename
    if request.method == "POST":
        file = request.files['file']
        try:
            df = pandas.read_csv(file)
            gc = Nominatim(user_agent="http")
            df["coordinates"] = df["Address"].apply(gc.geocode)
            df["Latitude"] = df["coordinates"].apply(lambda x: x.latitude if x != None else None)
            df["Longitude"] = df["coordinates"].apply(lambda x: x.latitude if x != None else None)
            df = df.drop(columns="coordinates")
            filename = datetime.datetime.now().strftime("uploads/%Y-%m-%d-%H-%M-%S-%f" + ".csv")
            df.to_csv(filename, index=None)
            return render_template("index.html", text=df.to_html(), btn="download.html")
        except:
            return render_template("index.html", text="Please make sure you have an address column in your CSV file!")


@app.route("/download-file/")
def download():
    return send_file(filename, download_name="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
    app.debug = True
    app.run()
