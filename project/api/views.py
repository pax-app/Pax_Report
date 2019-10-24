from flask import request, jsonify, Blueprint
from database_singleton import Singleton

reports_blueprint = Blueprint('report', __name__)
db = Singleton().database_connection()

@reports_blueprint.route('/reports/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
