from Imdb import IMDB


class App:
    def menu(self):
        imdb=IMDB()
        while True:
            secim=input("1-Top Rated Movies\n2-Most Popular Movies\n3-Exit")
            if secim=="3":
                break
            else:
                if secim=="1":
                    imdb.topRatedMovies()
                elif secim=="2":
                    imdb.mostPopularMovies()
                else:
                    print("Wrong input")

app=App()
app.menu()