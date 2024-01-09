#!/usr/bin/python3
"""running flask"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

if app_views is not None:
<<<<<<< HEAD
    from api.v1.views.amenities import *
    from api.v1.views.cities import *
    from api.v1.views.places import *
    from api.v1.views.states import *
    from api.v1.views.users import *
    from api.v1.views.places_reviews import *
=======
    from api.v1.views.amenities import *
    from api.v1.views.cities import *
    from api.v1.views.places import *
    from api.v1.views.states import *
    from api.v1.views.users import *
    from api.v1.views.places_reviews import *
>>>>>>> 1bae26a8a9e332a83ee5a99b9c3d08fc6ede264b
