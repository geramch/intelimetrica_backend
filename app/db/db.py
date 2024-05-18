import os

import pytz
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine, ForeignKey, Float,
)

TIME_ZONE = pytz.timezone("America/Mexico_City")

POSTGRESQL_URL = os.getenv("POSTGRESQL_URL")
print(POSTGRESQL_URL)

if POSTGRESQL_URL is None:
    raise ValueError("The POSTGRESQL_URL environment variable is not set.")


engine = create_engine(
    POSTGRESQL_URL
)

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(String, primary_key=True)
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