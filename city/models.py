from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class DBCity(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    additional_info = Column(String(511), nullable=False)

    temperatures = relationship("DBTemperature", back_populates="city")