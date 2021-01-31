from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_profile_name():
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    h2_tag = soup.find("h2")
    return h2_tag.getText()


if __name__ == '__main__':
    profile_name = get_profile_name()
    print(profile_name)
