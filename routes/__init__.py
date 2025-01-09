from .trip import trip_bp
from .api import api_bp
from .add import add_bp
from .map import map_bp
from .points import points_bp

# Blueprintをリストとしてまとめる
blueprints = [trip_bp, api_bp, add_bp, points_bp, map_bp]
