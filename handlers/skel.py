import sys

from tornado import gen
from tornado_jwt import Authenticated

from math import ceil
from bson.objectid import ObjectId


class SkelHandler(Authenticated):

    def format(self, item):
        item['_id'] = str(item['_id'])
        return item

    def send_result(self, data=None, status=None):
        if data:
            self.send_json(status or 200, map(self.format, data))
        else:
            self.send_error(status or 204, reason='resource not found')

    @gen.coroutine
    def get(self):
        payload = None
        try:
            # get collection
            col = self.settings['crawler_db'].bill

            # get request arguments
            items = min(int(self.get_query_argument('items', 10)), 50)
            page = int(self.get_query_argument('page', 0))

            # prepare database query
            q = self.get_query_argument('q')
            payload = col.find({ '$text': { '$search': q } })

            # set response headers
            count = yield payload.count()
            self.add_header('Page', page)
            self.add_header('Items', count)
            self.add_header('Pages', str(int(ceil(float(count) / float(items)))))
            self.add_header('Items-Per-Page', items)

            # query database
            payload = yield payload.skip(items * page).limit(items).to_list(length=items)
        except Exception, error:
            # handle errors
            self.send_error(500, reason=error.message, exc_info=sys.exc_info())
        else:
            # send response
            self.send_result(payload)
