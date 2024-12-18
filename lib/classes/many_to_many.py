class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        self.__class__.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if (
            isinstance(value, str)
            and 5 <= len(value) <= 50
            and not hasattr(self, "title")
        ):
            self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if type(value) == Author:
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if type(value) == Magazine:
            self._magazine = value


class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0 and not hasattr(self, "name"):
            self._name = value

    def articles(self):
        return [article for article in Article.all if self == article.author]

    def magazines(self):
        return list(
            set(
                [
                    article.magazine
                    for article in self.articles()
                    if self == article.author
                ]
            )
        )

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if self == article.magazine]

    def contributors(self):
        return list(
            set(
                [
                    article.author
                    for article in self.articles()
                    if self == article.magazine
                ]
            )
        )

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
