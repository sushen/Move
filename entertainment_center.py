import fresh_tomatoes
import media

# Toy Story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# School of Rock
school_of_rock = media.Movie("School of Rock",
                             "About School of Rock",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# Ratatouille
ratatouille = media.Movie("Ratatouille",
                          "About a rat that can cook!",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# Midnight in Paris
midnight_in_paris = media.Movie("Mightnight in Paris",
                                "About a mightnight in Paris",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

# Hunger Game
hunger_game = media.Movie("Hunger Game",
                          "About Hunger Game",
                          "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=SMGRhAEn6K0")

# Build website
movies = [toy_story, avatar, school_of_rock,
          ratatouille, midnight_in_paris, hunger_game]

fresh_tomatoes.open_movies_page(movies)