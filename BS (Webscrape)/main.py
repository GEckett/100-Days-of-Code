from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_page = response.text
soup = BeautifulSoup(yc_page, "html.parser")

article_tags = soup.find_all(name="a", rel="noreferrer")
article_texts = []
article_links = []
for article in article_tags:
    text = article.get_text()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_upvote_index = article_upvotes.index(max(article_upvotes))
print(max_upvote_index)

print(article_texts[max_upvote_index])
print(article_links[max_upvote_index])
print(article_upvotes[max_upvote_index])

#with open(file="website.html", mode="r", encoding="utf8") as data:
#    site_text = data.read()

#soup = BeautifulSoup(site_text, "html.parser")

#print(soup.h1.string)
