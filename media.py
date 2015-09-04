class Movie():
    """A simple class of the attributes of a movie.

    Attributes:
        title: A string of the title of the movie.
        storyline: A string of the storyline.
        poster_image_url: A string of the poster image of the movie's url.
        trailer_youtube_url: A string of the youtube trailer of the movie's url.
    """
    def __init__(self, mov_title, mov_storyline, mov_poster, mov_youtube,
                 mov_characters):
        self.title = mov_title
        self.storyline = mov_storyline
        self.poster_image_url = mov_poster
        self.trailer_youtube_url = mov_youtube
        self.character_list = mov_characters

class Character():
    """Another simple class of the attributes of a character of a movie.

        Attributes:
            name: The name of the character.
            actor: The name of the actor portraying that character.
    """

    def __init__(self, actor_name, character_name):
        self.name = character_name
        self.actor = actor_name
