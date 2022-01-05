from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Get the HTML of the website and parse using beautiful soup
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# Extract all the 100 movie names from the HTML
movies = soup.find_all(name="h3", class_="title")

# Make a list of the movie recommendations
movie_list = [movie.getText() for movie in movies]
movie_list = movie_list[::-1]

# Export the movie list to movies.txt file
with open("movies.txt", "w") as movie_file:
    movie_file.write("\n".join(movie_list))



