import requests
from bs4 import BeautifulSoup

class IMDB:
    def __init__(self):
        self.url="https://www.imdb.com/"

    def topRatedMovies(self):
        result=requests.get(self.url+"chart/top/?ref_=nv_mv_250")
        bs=BeautifulSoup(result.text,'html.parser')
        result=bs.find("tbody").find_all("tr")
        for movie in result:
            title=movie.find("td",{"class":"titleColumn"}).find("a").text
            rating=movie.find("td",{"class":"ratingColumn"}).find("strong").text
            print(f"Name:{title}******Rating:{rating}")

    def mostPopularMovies(self):
        result=requests.get(self.url+"chart/moviemeter/?ref_=nv_mv_mpm")
        bs=BeautifulSoup(result.text,'html.parser')
        result=bs.find("tbody").find_all("tr")
        for movie in result:
            title=movie.find("td",{"class":"titleColumn"}).find("a").text
            # rating=movie.find("td",{"class":"ratingColumn"}).find("strong").text
            print(f"Name:{title}")
