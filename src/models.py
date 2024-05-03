import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, autoincrement = True)
    name_user = Column(String(250), unique=True, nullable=False)
    name = Column (String(250))
    password = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    birthday = Column (Date)
    biography = Column (String(250))
    image_user = Column (String(250))
    
    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship(Users)
    quote = Column(String(250))
    image = Column(String(250), nullable=False)
    video = Column (String(250),nullable=False)
    likes = Column(Integer, default = 0)
    comments = Column(Integer, default = 0)

    def to_dict(self):
        return {}

class Likes(Base):
    __tablename__ = 'likes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, autoincrement = True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    user = relationship(Users)
    post_id = Column(Integer, ForeignKey('post.id'), nullable = False)
    post = relationship(Post)
    
    

    def to_dict(self):
        return {}



class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, autoincrement= True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable= False)
    user = relationship(Users)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship(Post)
    text = Column(string(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
