# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class Website(Item):

    Title = Field()
    Tag = Field()
    url = Field()
