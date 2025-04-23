import pytest
from factories.webdriver_factories import WebdriverFactory

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = WebdriverFactory.get_webdriver(request.param)
    yield driver


