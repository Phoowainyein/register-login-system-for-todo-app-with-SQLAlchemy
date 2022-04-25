from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP,create_engine, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
Base = declarative_base()

# Create engine
engine = create_engine('sqlite:///todo.db', echo = False)

# Create declarative base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# ---
# TABLES
# ---
#User
class User(Base):
  __tablename__ = "users"
  userId = Column(Integer, primary_key = True, autoincrement = True)
  username = Column(String, nullable = False)
  email = Column(String, unique = True, nullable = False)
  password = Column(String, nullable = False)
  created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
  items = relationship("Item", back_populates = "users", secondary = "useritems")
  
  
# Items
class Item(Base):
  __tablename__ = "items"

  itemId = Column(Integer, primary_key = True)
  name = Column(String)
  created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
  users = relationship("User", back_populates = "items",secondary = "useritems")

#UserItems
class UserItems(Base):
   __tablename__ = 'useritems'
   userId = Column(Integer,ForeignKey('users.userId'),primary_key=True)
   itemId = Column(
      Integer, 
      ForeignKey('items.itemId'),primary_key=True)


# Create the tables
Base.metadata.create_all(engine)

# Create session to interact with the database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()



