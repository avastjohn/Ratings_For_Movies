from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

# allows querying to session directly
engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations
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

### Flask functions

# Create a new user (signup)
def create_new_user(session, new_email, new_pw, new_age, new_zip):
    new_user = User(email=new_email, 
                    password=new_pw, 
                    age=new_age, 
                    zipcode=new_zip)
    session.add(new_user)
    session.commit()
    print "@#$#@#$%#@@$$%#@@$$%##@#$%$#@@$%$#@#$$#@$#@$#@$#@$#@$#@$#@$#@"
    print "Added new user to users database"

# Log in as a user
def authenticate(email, password):
    # for user in session.query(User):
#        if user.email == email and user.password == password:
    print session.query(User)

# View a list of all users

# Click on a user and view the list of movies they've rated, as well as the ratings

# When logged in and viewing a record for a movie, either add or update a personal rating for that movie.



def main():
    authenticate("harry@potter.com", "ginny")

if __name__ == "__main__":
    main()