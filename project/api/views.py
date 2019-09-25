from flask import request, jsonify, Blueprint

reports_blueprint = Blueprint('report', __name__)


@reports_blueprint.route('/reports/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
