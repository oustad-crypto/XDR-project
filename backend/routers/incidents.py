from flask import Blueprint, request, jsonify

# Create a Blueprint for incident management
incidents_bp = Blueprint('incidents', __name__)

# Sample in-memory data structure for incidents
incidents = []

@incidents_bp.route('/incidents', methods=['GET'])
def get_incidents():
    return jsonify(incidents), 200

@incidents_bp.route('/incidents', methods=['POST'])
def create_incident():
    data = request.json
    incidents.append(data)
    return jsonify(data), 201

@incidents_bp.route('/incidents/<int:incident_id>', methods=['GET'])
def get_incident(incident_id):
    if 0 <= incident_id < len(incidents):
        return jsonify(incidents[incident_id]), 200
    return jsonify({'error': 'Incident not found'}), 404

@incidents_bp.route('/incidents/<int:incident_id>', methods=['PUT'])
def update_incident(incident_id):
    if 0 <= incident_id < len(incidents):
        data = request.json
        incidents[incident_id] = data
        return jsonify(data), 200
    return jsonify({'error': 'Incident not found'}), 404

@incidents_bp.route('/incidents/<int:incident_id>', methods=['DELETE'])
def delete_incident(incident_id):
    if 0 <= incident_id < len(incidents):
        incidents.pop(incident_id)
        return jsonify({'message': 'Incident deleted'}), 204
    return jsonify({'error': 'Incident not found'}), 404
