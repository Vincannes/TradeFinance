from PySide2 import QtWidgets, QtCore
from libs.thread_pool import ThreadPool
from libs.articles.get_articles import Articles
from libs.widgets.article_itemwidget import ArticlesWidgetItem


class ArticlesWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None, ticker=None):
        super(ArticlesWidget, self).__init__(parent)

        self.thread_pool = ThreadPool()
        self.get_articles(ticker)

    @QtCore.Slot(str)
    def get_articles(self, ticker):

        articles = self._get_articles_dict(ticker=ticker).articles
        self.clear()

        for index, i in enumerate(articles):
            title = i["title"]
            date = i["date"]
            description = i["descritpion"]
            link = i["link"]
            article = ArticlesWidgetItem(
                parent=self
            )
            article.set_title(title)
            article.set_date(date)
            article.set_description(description)
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(article.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, article)

    def _get_articles_dict(self, ticker):
        return Articles(ticker=ticker)


