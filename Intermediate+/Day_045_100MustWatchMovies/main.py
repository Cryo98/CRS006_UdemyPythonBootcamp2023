from pathlib import Path
from bs4 import BeautifulSoup
import requests

# cwd = Path(__file__).parent
# website_file = cwd / "website.html"
# with open(website_file, "r", encoding="utf-8") as site:
#     contents = site.read()

# LINK = "https://news.ycombinator.com"
LINK = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(LINK)
contents = response.content

soup = BeautifulSoup(contents, 'html.parser')

# ">" works as a way to say that we want tags directly below
# all_articles = soup.select("span.titleline > a")
# all_scores = soup.find_all(name="span", class_="score")
# scores = [int(score.getText().split()[0]) for score in all_scores]
# highest_article = scores.index(max(scores))
# print(f"{all_articles[highest_article].getText()} (link: {all_articles[highest_article].get('href')}): {scores[highest_article]} upvotes")
# for article, score in zip(all_articles, all_scores):
#     print(f"{article.getText()}: {score.getText()}")

# The list is reversed, 100 to 1
titles_tag = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
titles_list = [title.getText() for title in titles_tag]

with open("top_100_movies.txt", "w") as f:
    for title in titles_list[::-1]:
        f.write(title)
        f.write("\n")
