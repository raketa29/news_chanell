from news_loader import GalaxyParser
from bs4 import BeautifulSoup as BS
import lxml
import json

url = "https://nv.ua/ru"

gp = GalaxyParser(url)


def load_page():
    data = gp.load_page_data()
    # print(data)
    soup = BS(data, "lxml")

    all_posts = soup.find_all('div', class_='feed-item')
    breaking_news_nv_ua = {}
    for post in all_posts:
        news_title = post.find_next('a').text.strip()
        link = post.find_next('a').get('href')
        print(news_title, link)
        breaking_news_nv_ua[news_title] = link

    return breaking_news_nv_ua


def save_news():
    data_news = load_page()
    with open("breaking_news_nv_ua.json", "w", encoding="utf-8") as file:
        json.dump(data_news, file, indent=4, ensure_ascii=False)


def main():
    # load_page()
    save_news()


if __name__ == '__main__':
    main()
