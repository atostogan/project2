import pytest

SUPPORTED_BROWSERS = ['chrome', 'firefox', 'edge']


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')


@pytest.fixture(scope='session', autouse=True)
def browser(request):
    value = request.config.option.browser
    if value not in SUPPORTED_BROWSERS:
        raise ValueError(f'Unsupported browser "{value}". Supported: {", ".join(SUPPORTED_BROWSERS)}')
    print(value)
    return value
