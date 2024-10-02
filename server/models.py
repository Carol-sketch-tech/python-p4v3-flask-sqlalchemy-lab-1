from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthqauke(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer(), primary_key=True)
    magnitude = db.Column(db.Float())
    location = db.Column(db.String())
    year = db.Column(db.Integer())

    def __repr__(self):
        return f'Id:{self.id},'+ \
        f'magnitude:{self.magnitude},' + \
        f'location:{self.location},' + \
        f'year:{self.year}'


