import model
import csv
from datetime import datetime

def load_users(session):
    # use u.user
    f = open("seed_data/u.user")
    rows = f.read().split("\n")
    for string in rows:
        row_list = string.split("|")
        user = model.User(age=row_list[1], zipcode=row_list[-1])
        user.id=row_list[0]
        session.add(user)
    session.commit()

def load_movies(session):
    # use u.item
    f = open("seed_data/u.item")
    rows = f.read().split("\n")
    for string in rows:
        row_list = string.split("|")
        unformatted_date = row_list[2]
        # make sure it doesn't format an empty string
        if unformatted_date != "":
            formatted_date = datetime.strptime(unformatted_date, "%d-%b-%Y")
        else:
            formatted_date = datetime.strptime("01-Jan-1900", "%d-%b-%Y")
        # make an instance of a Movie
        movie = model.Movie(name=row_list[1], released_at=formatted_date, imdb_url=row_list[4])
        movie.id=row_list[0]
        session.add(movie)
    session.commit()

def load_ratings(session):
    # use u.data
    # print "id:", movie.id
    # print "name:", movie.name
    # print "released at:", movie.released_at
    # print "imdb:", movie.imdb_url
    pass

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)
    load_movies(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)