from os import remove

from hentai import Sort, Format, Utils, Hentai, Tag, Format
from hentai import Hentai
import random

class serach:
    def __init__(self, tags, pages):
        self.tags = tags
        self.pages=pages

    def photos(self):
        self.popo = "tag:" + self.tags
        self.links = []

        for doujin in Utils.search_by_query(query=self.popo, page=self.pages, sort=Sort.PopularMonth):
            self.links.append(doujin.id)

        links2 = random.choice(self.links)

        return links2

    def saveing(self, doujin, save,cout):
        self.doujin=doujin
        self.save=save
        self.cout = cout

class idsearch:


    def saveing(self, doujin, save, cout):
        self.doujin = doujin
        self.save = save
        self.cout = cout

class imageloli():
    def __init__(self,doujin, save,cout):
        self.doujin = doujin
        self.save = save
        self.cout = cout+1








