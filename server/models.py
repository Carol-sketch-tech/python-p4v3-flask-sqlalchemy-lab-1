from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthqauke(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id = Column(Integer(), primary_key=True)
    magnitude = Column(Float())
    location = Column(String())
    year = Column(Integer())

    def __repr__(self):
        return f'Id:{self.id},'+ \
        f'magnitude:{self.magnitude},' + \
        f'location:{self.location},' + \
        f'year:{self.year}'


