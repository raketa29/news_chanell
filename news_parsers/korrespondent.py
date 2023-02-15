from news_loader import GalaxyParser
from bs4 import BeautifulSoup as BS
import lxml
import json

url = "https://ua.korrespondent.net/"

gp = GalaxyParser(url)


def load_page():
    data = gp.load_page_data()
    # print(data)
    soup = BS(data, "lxml")

    all_articles = soup.find("div", class_='time-articles').find_all("div", class_='article')
    breaking_news_korrespondent = {}
    for article in all_articles:
        link = article.find_next('a').get('href')
        title = article.find_next('a').text.strip()
        print(title, link)
        breaking_news_korrespondent[title] = link
    return breaking_news_korrespondent


def save_news():
    data_news = load_page()
    with open("breaking_news_korrespondent.json", "w", encoding="utf-8") as file:
        json.dump(data_news, file, indent=4, ensure_ascii=False)


# def open_news_data():
#     with open("breaking_news_korrespondent.json", "r", encoding="utf-8") as file:
#         data_news = json.load(file)
#     n = 0
#     try:
#         for k, v in data_news.items():
#             GP = GalaxyParser(url=v)
#             data = GP.load_page_data()
#             s = BS(data, "lxml")
#
#             title = s.find('h1', class_='post-item__title').text.strip()
#             print(title)
#             text_post = s.find('div', class_='post-item__text').text.strip().replace("\n", "")
#             print(text_post)
#     except Exception as ex:
#         print(ex, n + 1)


def main():
    # load_page()
    save_news()
    # open_news_data()


if __name__ == '__main__':
    main()
