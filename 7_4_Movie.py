import random
list = []
movie_list = []
serial_list = []


class MovieCatalog:
    def __init__(self, title, year, genre, number_review):
        self.title = title
        self.year = year
        self.genre = genre
        self.number_review = number_review

    def __str__(self):
        return f"{self.title} ({self.year})"

    def play(self, review_step=1):
        self.number_review += review_step


def Add_Movie(movie_name, movie_year, movie_genre):
    list.append(movie_name)
    movie_list.append(movie_name)
    movie_name=MovieCatalog(movie_name, movie_year, movie_genre, 0)



#by_last_name = sorted(persons, key=lambda person_ID: person_ID.last_name)
if __name__ == "__main__":

#get_movie


#find
search_movie=input("Podaj nazwę filmu/serialu: ")
if list.find(search_movie) != -1:
    print("Film nie znajduję się w twojej liście")
else:
    if movie_list.find(search_movie) != -1:
        print("Serial znajduje się na liście")
    else:
        print("Film znajduje się na liście")

#losowe dodawanie odtworzeń
def generate_views():
    list_len=len(list)
    movie_add_review=list[random.randrange(list_len)]
    movie_add_review.play = random.randrange(1, 101)

def xgenerate_views():
    for i in range (10):
        generate_views()

def top_titles(top_number):
    if content_type == "movie":
        movie_list_sort = []
        movie_list_sort = sorted(movie_list, key=lambda movie_name: movie_name.number_review)
        for i in (top_number):
            print (movie_list_sort[i])
