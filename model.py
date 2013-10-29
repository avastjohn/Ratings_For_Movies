from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

# allows querying to session directly
engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class Rating(Base):
    # Association
    __tablename__ = "ratings"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    rating = Column(Integer)
    user = relationship("User", backref=backref("ratings", order_by=id))
    movie = relationship("Movie", backref=backref("ratings", order_by=id))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)
    # movie = relationship("Rating", backref="users")

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key = True)
    name = Column(String(32), nullable=True)
    released_at = Column(Date(), nullable=True)
    imdb_url = Column(String(140), nullable=True)
    # user = relationship("Rating", backref="movies")

# A user has many ratings
# A rating belongs to a user
# A movie has many ratings
# A rating belongs to a movie
# A user has many movies through ratings
# A movie has many users through ratings

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()