# coding: utf8

import sys
import signal
import urllib

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebPage


class Crawler(QWebPage):
    def __init__(self, url, file, js):
        QWebPage.__init__(self)
        self._url = url
        self._file = file
        self._js = js

    def crawl(self):
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.connect(self, SIGNAL('loadFinished(bool)'), self._finish_loading)
        print('载入网页..')
        self.mainFrame().load(QUrl(self._url))

    def _finish_loading(self, result):
        print('执行脚本..')
        self.mainFrame().evaluateJavaScript(urllib.urlopen("http://reus.me/jquery.js").read())
        self.mainFrame().evaluateJavaScript(self._js)
        print('写入文件..')
        file = open(self._file, 'w')
        file.write(self.mainFrame().toHtml().toUtf8())
        file.close()
        sys.exit(0)


def main():
    url = 'http://bbs.jnustu.net'
    file = 'fs'
    js = "$('body').html('YE?')"

    app = QApplication(sys.argv)
    crawler = Crawler(url, file, js)
    crawler.crawl()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()