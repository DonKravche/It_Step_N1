# Movies Filtering and Genre Update

## Overview

This script processes a JSON file `movies.json`, filtering and updating movie genre information based on their release dates and genres. The script creates a new JSON file `finishedMovies.json` with the updated data.

## Instructions

1. **Input File**: 
   - The input file should be named `movies.json`.
   - This file should contain a list of movies in JSON format, with each movie having a `release_date` and `genres`.

2. **Output File**:
   - The script generates an output file named `finishedMovies.json`.

## Task Description

1. **Filter and Update Genres**:
   - **Crime Genre Movies (Released after 2000)**:
     - Update the genre "Crime" to "New_Crime".
     - Include these movies in the output if their release date is after 2000.
   
   - **Drama Genre Movies (Released before 2000)**:
     - Update the genre "Drama" to "Old_Drama".
     - Include these movies in the output if their release date is before 2000.
   
   - **Movies Released in the Year 2000**:
     - Add the genre "New_Century" to these movies.
     - Include these movies in the output regardless of other genres.

3. **Write to Output**:
   - The filtered and updated movies are written to `finishedMovies.json`.

## Code Description

```python
# Update genre names
movie["genres"] = ["New_Crime" if genre == "Crime" else genre for genre in movie["genres"]]
movie["genres"] = ["Old_Drama" if genre == "Drama" else genre for genre in movie["genres"]]

# Add "New_Century" if the movie is from the year 2000
release_year = get_release_year(movie["release_date"])
if release_year == 2000:
    movie["genres"].append("New_Century")

# Filter based on release date and genre
if (release_format(movie["release_date"]) or release_format2(movie["release_date"])) and "New_Crime" in movie["genres"]:
    filtered_movies.append(movie)
```

## Requirements

- Python 3.x
- JSON file formatted correctly as described

## Execution

1. Ensure that `movies.json` is in the same directory as the script.
2. Run the script using Python:
   ```bash
   python HomeWork N21 Serialisation & DeSerialisation.py
   ```
3. Check the `finishedMovies.json` file for the filtered and updated movies.