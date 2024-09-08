import json
from datetime import datetime


def release_format(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    return date.year > 2000


def release_format2(date_string2):
    date = datetime.strptime(date_string2, "%Y-%m-%d")
    return 2000 > date.year


def get_release_year(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").year


filtered_movies = []

with open("movies.json", "r") as file_json:
    movies = json.load(file_json)
    for item in movies:
        for movie in item["results"]:
            movie["genres"] = ["New_Crime" if genre == "Crime" else genre for genre in movie["genres"]]
            movie["genres"] = ["Old_Drama" if genre == "Drama" else genre for genre in movie["genres"]]

            release_year = get_release_year(movie["release_date"])
            if release_year == 2000:
                movie["genres"].append("New_Century")

            if (release_format(movie["release_date"]) or release_format2(movie["release_date"])) and "New_Crime" in \
                    movie["genres"]:
                filtered_movies.append(movie)

with open("finishedMovies.json", "w") as file_json:
    json.dump(filtered_movies, file_json, indent=4)

print("Operation Went Successfully!")
