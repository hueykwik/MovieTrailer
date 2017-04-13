class Movie:
    """A class that represents a single movie.

    Attributes:
        title: A string representing the movie tile.
        poster_image_url: A string URL for the movie's poster image.
        trailer_youtube_url: A string URL for the movie's trailer on YouTube.
        eg
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
