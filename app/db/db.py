import os
import uuid
import pytz
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine, ForeignKey, Float,
)

from app.db.utils import Base

TIME_ZONE = pytz.timezone("America/Mexico_City")

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    rating = Column(Integer)
    name = Column(String)
    site = Column(String)
    email = Column(String)
    phone = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    lat = Column(Float)
    lng = Column(Float)

    def to_dict(self):
        return {
            'id': str(self.id),
            'rating': self.rating,
            'name': self.name,
            'site': self.site,
            'email': self.email,
            'phone': self.phone,
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'lat': self.lat,
            'lng': self.lng
        }