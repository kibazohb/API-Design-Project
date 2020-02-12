from flask.views import MethodView
from flask import jsonify, request, abort

from app.decorators import app_required
class PlayerAPI(MethodView):

    decorators = [app_required]

    players = [
        { "id": 1, "name": u"Lowry", "links": [ {"rel": "self", "href": "/players/1"} ] },
        { "id": 2, "name": u"Siakam" ,"links": [ {"rel": "self", "href": "/players/2"} ] },
        { "id": 3, "name": u"Gasol" ,"links": [ {"rel": "self", "href": "/players/3"} ] }
    ]

    def get(self, player_id):
        if player_id:
            return jsonify({"player": self.players[player_id - 1]})
        else:
            return jsonify({"players": self.players})

    def post(self):
        if not request.json or not 'name' in request.json:
            abort(400)
        player = {
            "id": len(self.players) + 1,
            "name": request.json["name"],
            "links": [ {"rel": "self", "href": "/players/" + str(len(self.players) + 1) } ]
        }
        self.players.append(player)
        return jsonify({'player': player}), 201

    def put(self, player_id):
        if not request.json or not 'name' in request.json:
            abort(400)
        player = self.players[player_id - 1]
        player["name"] = request.json["name"]
        return jsonify({'player': player}), 200

    def delete(self, player_id):
        del self.players[player_id - 1]
        return jsonify({}), 204    


     