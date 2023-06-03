from flask import Flask ,jsonify
import shapefile

app = Flask(__name__)

@app.route("/geojson", methods=['GET'])
def home():
    reader = shapefile.Reader("C:\\Users\\T460\\OneDrive\\Bureau\\Chambres.shp")
    fields = reader.fields[1:]
    field_names = [field[0] for field in fields]
    buffer = []
    for sr in reader.shapeRecords():
       atr = dict(zip(field_names, sr.record))
       geom = sr.shape.__geo_interface__
       buffer.append(dict(type="Feature", \
        geometry=geom, properties=atr)) 
   # write the GeoJSON file
    from json import dumps
    geojson = open("pyshp.json", "w")
    geojson.write(dumps({"type": "FeatureCollection",\
    "features": buffer}, indent=2) + "\n")
    return jsonify({"type": "FeatureCollection", "features": buffer})

if __name__ == '__main__':
    app.run(debug=True, host='10.0.2.2', port=5000)