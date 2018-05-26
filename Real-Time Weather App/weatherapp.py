import bs4
import requests
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'loc, temp, scale, condition')

def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather/{}'.format(zipcode)
    # print(url)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[:250])
    return response.text


def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
        # $('#inner-content div.city-header div.region-content-header h1').textContent
        # $('..region-content-header h1').textContent
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()
    condition = soup.find(class_='condition-icon').get_text()

    loc = cleanup_text(loc)
    temp = cleanup_text(temp)
    condition = cleanup_text(condition)
    scale = cleanup_text(scale)

    # print(loc, temp, scale, condition)
    report = WeatherReport(loc, temp, scale, condition)
    return report


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == "__main__":
    # get zip code from user
    zipcode = input('What zip code do you want the weather for? ')

    # get html from web
    html = get_html_from_web(zipcode)

    # parse the html from wunderground.com using beautifulsoup
    report = get_weather_from_html(html)

    # display weather forecast
    print('The temp in {} is {} {} and {}.'.format(report.loc, report.temp, report.scale, report.condition))
