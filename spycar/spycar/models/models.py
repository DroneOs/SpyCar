from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    ForeignKey
    )

from . import DBSession, Base


# Create your models here.

class path(Base):
  __tablename__='Path'
  id=Column(Integer, primary_key=True)
  name=Column(Unicode(200))
  children = relationship("coordinates", backref="Path")
  

  
class coordinates(Base):
  __tablename__= 'Coordinates'
  cordi=Column(Integer, primary_key=True)
  path_id=Column(Integer, ForeignKey('Path.id'))
  Point=Column(Unicode(200))
  latitude=Column(Unicode(200))
  longitude=Column(Unicode(200))
  direction=Column(Unicode(200))
  
  #paths=relationship(path, backref=backref("Coordinates"))
  