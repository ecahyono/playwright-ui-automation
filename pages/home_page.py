class HomePage:
    def __init__(self, page):
        self.page = page
        self.search_box = page.locator("#small-searchterms")
        self.search_button = page.locator("input[value='Search']")

    def open(self):
        self.page.goto("https://demowebshop.tricentis.com/")

    def search_product(self, keyword):
        self.search_box.fill(keyword)
        self.search_button.click()