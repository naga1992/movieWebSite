# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:40:52 2018

@author: DS00331004

"""

import webbrowser
class Movie():
     def __init__(self,movie_title,movie_storyline,movie_poster,movie_youtube_url):
         self.title=movie_title
         self.storyline=movie_storyline
         self.poster_image_url=movie_poster
         self.trailer_youtube_url=movie_youtube_url
         
         
     def show_trailer(self):
        webbrowser.open(self.movie_youtube_url)