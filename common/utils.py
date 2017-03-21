# coding: utf-8

import hashlib
import lxml.html


def to_hash(*args):
    m = hashlib.md5()
    for arg in args:
        if isinstance(arg, unicode):
            arg = arg.encode('utf8')
        m.update(str(arg))
    return m.hexdigest()


class ParseItem(dict):
    def __getattr__(self, item):
        return self.get(item)

    def __setattr__(self, key, value):
        self[key] = value


def parse_doc(html):
    if not isinstance(html, unicode):
        html = html.decode('utf8')
    return lxml.html.fromstring(html)
