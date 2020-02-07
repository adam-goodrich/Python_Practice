
class movie():
    def __init__(self, movie_data):
        self.movie_data = movie_data

    def get_movie_title(self):
        return self.movie_data["title"]
        
    def get_movie_rating(self):
        return self.movie_data["rating"]    
  
search_or_rating = 2

def print_single_movie_rating(movie_query):
    '''prints movie title and rating'''
    movie_3 = return_single_movie_object(movie_query, 7)
    print("The rating for", movie_3.get_movie_title(), "is", movie_3.get_movie_rating())

def print_all_ratings(movie_list):
    '''prints all movie titles in movie list that has a great rating'''
    for i in movie_list:
        movie_2 = return_single_movie_object(i, 4)
        print("The movie", movie_2.get_movie_title(), "has a rating of", movie_2.get_movie_rating())
        
def list_search_results(movie_titles):
    '''prints all movies in movie_titles'''
    for movie in movie_titles:
        print(f"    {movie}")

def return_single_movie_object(movie_title, movie_rating):
    '''This will create a movie object'''
    movie_1 = {"title": movie_title, "rating": movie_rating}
    movie_object = movie(movie_1)
    return movie_object
    

def main():
    ''' Main is the entry point into the program, and it calls into the
        search or ratings functions depending on what the user decides to do.'''
    default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]
    print_all_ratings(default_movie_list)
    if search_or_rating == 1:
        list_search_results(default_movie_list)
    elif search_or_rating == 2:
        print_single_movie_rating("Moana")
    else:
        print("Error: Your input must be 1 or 2!")
        

if __name__ == "__main__":
    main()