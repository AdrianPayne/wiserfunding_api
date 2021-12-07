from flask import Flask, request, Response

from v1 import validators, z_score

app = Flask(__name__)


@app.route('/healthcheck', methods=['GET'])
def health_check_view():
    return Response("Everything ok!", 200)


@app.route('/company/<country_iso_code>/<id_company>', methods=['PUT'])
def z_score_view(country_iso_code, id_company):
    request_data = request.get_json()
    if not validators.validate_z_score_view(country_iso_code, id_company, request_data['financials']):
        return Response('Incorrect input', 400)

    return z_score.process_financials_data(request_data['financials'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

