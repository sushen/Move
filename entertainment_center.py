import media

toy_story = media.Movie("Toy Story",
                        "Story of a boy and his toy",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=tN1A2mVnrOM")
print(toy_story.storyLine)

avatar = media.Movie("Avatar",
                     "A marin vesit on alian planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

print(avatar.storyLine)
avatar.show_trailer()