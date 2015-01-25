# -*- coding: utf-8 -*-
from scrapy import log
from twisted.enterprise import adbapi
import datetime
import MySQLdb
import MySQLdb.cursors


class MySQLStorePipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool(
            'MySQLdb',
            db='testdb',
            user='root',
            passwd='huyiyang',
            cursorclass=MySQLdb.cursors.DictCursor,
            charset='utf8',
            use_unicode=False
        )

    def process_item(self, item, spider):

        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

        return item

    def _conditional_insert(self, tx, item):

        tx.execute("select * from blog2 where url = %s", (item['url']))
        result = tx.fetchone()
        if result:
            log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
        else:
            tx.execute(\
                "insert into blog2 (Title, url)"
                "values (%s, %s)",
                (item['Title'], item['url'])
            )
            log.msg("Item stored in db: %s" % item, level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)
