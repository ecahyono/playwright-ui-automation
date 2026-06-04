from pages.home_page import HomePage


def test_search_product(page):
    home = HomePage(page)

    home.open()
    home.search_product("computer")

    assert "Search" in page.title()
    assert page.locator(".product-item").first.is_visible()