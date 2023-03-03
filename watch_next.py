"""
Program compares the similarity of movie descriptions found in the file "movies.txt" to the movie description of
Planet Hulk. This is done within a function movie_recommender and by use of the spacy module. This function returns the
movie that is most similar to Planet_Hulk The function is called and the result printed to terminal.
"""
import spacy
nlp = spacy.load('en_core_web_md')

planet_hulk = nlp("""Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.""")

movie_database_file = "movies.txt"


def movie_recommender(movie_viewed, movies_file):
    """function takes the description of movie viewed and a database of movies in movies_file and compares the
    similarity of all descriptions in the database with the movie viewed. The function returns a string containing a
    recommendation for the movie title with the highest similarity score along with the similarity score and the movie's
     description"""
    with open(movies_file, "r") as file:
        # 2D list of [movie_title, movie_description, movie_similarity_to_movie_viewed]
        # string slicing is used to separate the movie title and movie description
        movies_list = [[movie[:7], nlp(movie[9:].strip("\n")), nlp(movie[9:].strip("\n")).similarity(movie_viewed)]
                       for movie in file.readlines()]

    # sorting movies based on similarity
    sorted_movies = sorted(movies_list, key=lambda movie: movie[2], reverse=True)
    # returning the movie with the highest similarity
    return f"For viewers who enjoyed Planet Hulk, we recommend: {sorted_movies[0][0]}, similarity " \
           f"{100*round(sorted_movies[0][2], 2)}%, description: {sorted_movies[0][1]}.\n We hope you enjoy!"


print(movie_recommender(planet_hulk, movie_database_file))
