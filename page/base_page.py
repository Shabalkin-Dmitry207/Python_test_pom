# Базовый класс для всех страниц
# Здесь будут общие методы: open, get_title, screenshot

class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)
        return self