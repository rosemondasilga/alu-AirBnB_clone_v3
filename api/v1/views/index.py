#!/usr/bin/python3
""" shows the index """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ returns json format """
    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ retrieves the number of each objects by type """
    return jsonify(amenities=storage.count("Amenity"),
                   places=storage.count("Place"),
                   states=storage.count("State"),
                   cities=storage.count("City"),
                   reviews=storage.count("Review"),
                   users=storage.count("User"))
