from flask import Flask, request, Response

from api.v1 import validators, z_score

app = Flask(__name__)


@app.route('/healthcheck', methods=['GET'])
def health_check_view():
    return Response("Everything ok!", 200)


@app.route('/company/<country_iso_code>/<id_company>', methods=['PUT'])
def z_score_view(country_iso_code, id_company):
    request_data = request.get_json()
    if not validators.validate_z_score_view(country_iso_code, id_company, request_data):
        return Response('Incorrect input', 400)

    return z_score.z_scores(request_data['financials'])
