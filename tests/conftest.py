import pytest

SUPPORTED_BROWSERS = ['chrome', 'firefox', 'edge']


def pytest_addoption(parser):
    '''
    Register new command line argument with pytest
    '''
    parser.addoption('--browser', action='store', default='firefox')


@pytest.fixture(scope='session', autouse=True)
def browser(request):
    '''
    Reads the command line argument value and returns it
    '''
    value = request.config.option.browser
    if value not in SUPPORTED_BROWSERS:
        raise ValueError(f'Unsupported browser "{value}". Supported: {", ".join(SUPPORTED_BROWSERS)}')
    print(value)
    return value
