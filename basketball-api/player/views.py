from flask import Blueprint

from player.api import PlayerAPI

player_app = Blueprint('player_app', __name__)

player_view = PlayerAPI.as_view('player_api')
player_app.add_url_rule('/players/', defaults={'player_id': None},
                 view_func=player_view, methods=['GET',])
player_app.add_url_rule('/players/', view_func=player_view, methods=['POST',])
player_app.add_url_rule('/players/<int:player_id>', view_func=player_view,
                 methods=['GET', 'PUT', 'DELETE',])