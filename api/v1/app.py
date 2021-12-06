from flask import Flask, Response

app = Flask(__name__)


@app.route('/healthcheck', methods=['GET'])
def health_check_view():
    return Response("Everything ok!", 200)


@app.route('/company/<country_iso_code>/<id>', methods=['PUT'])
def z_score_view(country_iso_code, id):
    return Response(f"Route to company with iso {country_iso_code} and id {id}", 200)
