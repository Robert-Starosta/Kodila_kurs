import random
from datetime import datetime
list = []
movie_list = []
serial_list = []
today = datetime.today()
data1 = today.strftime("%d/%m/%Y")

class MovieCatalog:
    def __init__(self, title, year, genre, number_review):
        self.title = title
        self.year = year
        self.genre = genre
        self.number_review = number_review

    def __str__(self):
        return f"{self.title} {self.year}"

    def play(self, review_step=1):
        self.number_review += review_step


class SerialCatalog(MovieCatalog):
    def __init__(self, episode_number, sezon_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.sezon_number = sezon_number


def Add_Movie(movie_name, movie_year, movie_genre):
    list.append(movie_name)
    movie_list.append(movie_name)
    movie_name = MovieCatalog(movie_name, movie_year, movie_genre, 0)

def add_serial(serial_name, serial_year, serial_genre, serial_episode, serial_sezon):
    list.append(serial_name)
    serial_list.append(serial_name)
    serial_name = SerialCatalog(
        title=serial_name,
        year=serial_year,
        genre=serial_genre,
        number_review="0",
        episode_number=serial_episode,
        sezon_number=serial_sezon
    )

#losowe dodawanie odtworzeń
def generate_views():
    list_len=len(list)
    movie_add_review = list[random.randrange(list_len)]
    movie_add_review.play(random.randrange(2, 101))

def xgenerate_views():
    for i in range (10):
        generate_views()

def top_titles(top_number):
    movie_list_sort = []
    movie_list_sort = sorted(movie_list, key=lambda title: title.number_review)
    movie_list_sort = movie_list_sort[::-1]
    serial_list_sort = []
    serial_list_sort = sorted(serial_list, key=lambda title: title.number_review)
    serial_list_sort = serial_list_sort[::-1]
    top = 0
    print("Filmy:")
    while top < top_number:
        print(movie_list_sort[top])
        top += 1
    print("Serial:")
    while top < top_number:
        print(serial_list_sort[top])
        top += 1

if __name__ == "__main__":
    print("Witaj w bibliotece filmów")
    what_to_do = int(input("1. Dodaj film \n"
                       "2. Dodaj serial \n"
                       "3. Dodaj odtworzenie\n"
                       "4. Najpopularniejszy film\n"
                       "5. Wyświetl top 3\n"
                       "6. Losowe dodanie\n"
                       "Co będziemy robić wybierz od 1-6: "))
    while what_to_do in range (0,6):
        if what_to_do == 1:
            movie_name = input("Podaj nazwę filmu: ")
            movie_year = input("Podaj rok produkcji: ")
            movie_genre = input("Podaj ocene filmu: ")
            Add_Movie(movie_name, movie_year, movie_genre)
        elif what_to_do == 2:
            serial_name = input("Podaj nazwę filmu: ")
            serial_year = input("Podaj rok produkcji: ")
            serial_genre = input("Podaj ocene filmu: ")
            serial_episode = input("Podaj ilość odcinków: ")
            serial_sezon = input("Podaj ilość sezonów: ")
            add_serial(serial_name, serial_year, serial_genre, serial_episode, serial_sezon)
        elif what_to_do == 3:
            generate_views()
        elif what_to_do == 4:
            print(f"Najlepszy film  i serial na dzień {data1}")
            top_titles(1)
        elif what_to_do == 5:
            top_titles(3)
        elif what_to_do == 6:
            xgenerate_views()
        what_to_do = int(input("Co będziemy1 robić wybierz od 1-6: "))

print("Wprowadzono błędną wartość kończymy")