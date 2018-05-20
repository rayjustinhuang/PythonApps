import requests


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather/{}'.format(zipcode)
    # print(url)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[:250])
    return response.text


if __name__ == "__main__":
    # get zip code from user
    zipcode = input('What zip code do you want the weather for? ')

    # get html from web
    html = get_html_from_web(zipcode)

    # parse the html from wunderground.com using beautifulsoup

    # display weather forecast
