# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 18:06:22 2018

@author: DS00331004
"""

import media 

toy_story=media.Movie("toy_story","a story of a boy and his toys which came to life",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")


toy_story1=media.Movie("toy_story2","a story of a boy and his toys which came to life2",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story1.movie_storyline)
toy_story1.show_trailer()
