'''
Today we will use a dictionary to implement a very simple database.
The key will be an actor/actress and the value will be the movies he/she performed in.
This is adapted from a homework assignment in a past semester.
'''

def setup():
    '''
    Returns an empty dictionary as an implementation of a database.
    '''

    actor_data = {}

    return actor_data

def insert_actor_movies(db, actor, movies):
    '''
    Inserts an actor/actress (key) with the movies he/she performed in (value).
    If the actor (key) is already in the database, add his/her movies (value).
    If the actor (key) is not in the database, insert the actor (key) and add his/her movies (value).

    Note: Actors/actresses (keys) are always stored in the database as lowercase.
        The given actor/actress may or may not be in lowercase.
    '''
    actor1 = db.get(actor)
    
    if (actor1 == actor):
        actor1.append[movies]
    else:
        db[actor] = movies

    return

def where_actor_in(actor, db):
    '''
    Returns a list of movies that the given actor/actress performed in.

    Note: Actors/actresses (keys) are always stored in the database as lowercase.
        The given actor/actress may or may not be in lowercase.
    '''

    movies1 = db.get(actor)
    movies = movies1.lower()

    return movies

def where_movie_is(movie, db):
    '''
    Returns a list of actors/actresses who performed in the given movie.
    '''

    

def common_movies(actor1, actor2, db):
    '''
    Returns all movies that both actor1 and actor2 performed in.

    Note: Actors/actresses (keys) are always stored in the database as lowercase.
        The given actors/actresses may or may not be in lowercase.
    '''

def common_actors(movie1, movie2, db):
    '''
    Finds all actors/actresses who performed in both given movies.
    '''

def get_co_actors(actor, db):
    '''
    Finds all other actors/actresses who are also in one of the movies that the given actor/actress performed in.
    '''

def init_db(file, db):
    '''
    Loads the given file and splits each line into an actor/actress and movies he/she performed in.
    Populates the given with each actor/actress (key) and his/her movies (value).
    '''

    f = open("moviedata.txt")
    for line in f:
        line = line.strip()
        actorAndMovies = line.split(",")
        actor = actorAndMovies[0]
        movies = [x.strip().lower() for x in actorAndMovies[1:]]
        insert_actor_movies(db, actor, movies)

    f.close()

def main():
    #get db
    db = setup()

    #load data into db
    init_db("moviedata.txt", db)

    #implement code to do the following:
    #    print the movies that 'toM Hanks' performed in
    #    print the actors/actresses who performed in the movie 'the post'
    #    print the movies both 'Meryl Streep' and 'tom hanks' performed in
    #    print the actors/actresses who performed in a movie with 'Meryl Streep'
    #    print all actors/actresses who performed in both 'the post' and 'doubt'


if __name__ == '__main__':
    main()
