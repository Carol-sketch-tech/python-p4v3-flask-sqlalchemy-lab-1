# server/app.py
#!/usr/bin/env python3

from models import db, Earthquake
from flask import make_response, jsonify
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthqaukes/<int:id>')
def get_earthquake(id):
    earthquake = Earthquake.query.get(id)

    if earthquake is None:
        return jsonify({'message':'Earthquake 9999 not found'}), 404
    
    response = {
        'Id': earthquake.id,
        'location': earthquake.location,
        'magnitude': earthquake.maginitude,  
         'year': earthquake.year }, 200

    return jsonify(response)

# add view to get earthquakes matching a minimum magnitude value.
@app.route('/earthquakes/magnitude/<float:magnitude>')
def earthqualke_matching_minimum_Magnitude(magnitude):
    earthquakes = Earthquake.query.get(Earthquake.magnitude >= magnitude).all()
    if Earthquake.magnitude >= magnitude:
        for quake in Earthquake:
            quake_list = quake
            return len(quake_list)
        
        response = {
            'count':len(earthquakes),
            'earthquakes':[]
        }

        for quake in earthquakes:
            response['earthquake'].append({
                'id': quake.id,
                'location': quake.location,
                'magnitude': quake.magnitude,
                'year': quake.year
            })

        return jsonify(response)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
