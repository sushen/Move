import webbrowser

class Movie():
    def __init__(self, move_title, move_storyline, poster_image, trailer_youtube):
        self.title = move_title
        self.storyLine = move_storyline
        self.poster_image_url = poster_image
        self.trailr_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailr_youtube_url)