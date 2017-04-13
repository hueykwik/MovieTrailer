# MovieTrailer
A simple movie trailer website project.

## Download
The files for the project may be [downloaded here](https://github.com/hueykwik/MovieTrailer/archive/master.zip).

## Quick Start
To generate a default `fresh_tomatoes.html` file, simply run the following command:

`python fresh_tomatoes.py`

To create your own, you can use this example script:

```
import media
import fresh_tomatoes

# Information for object arguments
title = "Pulp Fiction"
poster_url = "http://goo.gl/V5fb9n"
trailer = "https://www.youtube.com/watch?v=ewlwcEBTvcg"

# Create Movie object
pulp_fiction = media.Movie(title, year, poster_url, trailer_url)

# Create movie trailer page with array of one movie
fresh_tomatoes.open_movies_page([pulp_fiction])



