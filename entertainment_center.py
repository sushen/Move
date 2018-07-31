import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Story of a boy and his toy",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=tN1A2mVnrOM")

avatar = media.Movie("Avatar",
                     "A marin vesit on alian planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

life_of_Pi = media.Movie("Life of Pi",
                     "A young man who survives a disaster at sea is hurtled into an epic journey of adventure and discovery",
                     "https://m.media-amazon.com/images/M/MV5BNTg2OTY2ODg5OF5BMl5BanBnXkFtZTcwODM5MTYxOA@@._V1_.jpg",
                     "https://www.imdb.com/title/tt0454876/videoplayer/vi2646320921")

dreams = media.Movie("Dreams",
                     "A collection of tales based upon the actual dreams of director Akira Kurosawa.",
                     "https://m.media-amazon.com/images/M/MV5BYWMxYmI5OTAtOWUwZi00YzRhLTkwMzMtNTNmNzJjZGVlMWQ3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,708,1000_AL_.jpg",
                     "https://www.imdb.com/title/tt0100998/videoplayer/vi105028633")

gladiator = media.Movie("Gladiator",
                     "When a Roman General is betrayed, and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=lKn-Agk-yAI")

three_iron = media.Movie("3-Iron",
                     "A transient young man breaks into empty homes to partake of the vacationing residents' lives for a few days.",
                     "https://m.media-amazon.com/images/M/MV5BMTM1ODIwNzM5OV5BMl5BanBnXkFtZTcwNjk5MDkyMQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=S-S5n0JniDw")

movies = [toy_story, avatar, life_of_Pi, dreams, gladiator, three_iron]

fresh_tomatoes.open_movies_page(movies)