from bs4 import BeautifulSoup
import requests
# import requests
#
#
# with open('./website.html', encoding="utf8") as f:
#
#     contents = f.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     #print(f"Text : {tag.get_text()},  href : {tag.get('href')}")
#     pass
#
# heading = soup.find(name="h1", id="name")
# # print(heading.getText())
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get_text())
# # print(section_heading.name)
# # print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# heading_list = soup.select(selector=".heading")
# print(heading_list)





















# response = requests.get(url="https://news.ycombinator.com/")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
#
# all_title_list = soup.find_all(name="span", class_="titleline")
# all_subtext_list = soup.select(selector=".subtext .score")
#
# article_title = []
# article_link = []
# article_upvote = []
#
# for title, sub_text in zip(all_title_list, all_subtext_list):
#     article_title.append(title.find_next(name='a').getText())
#     article_link.append(title.find_next(name='a').get('href'))
#     # article_upvote.append(int(sub_text.getText().split()[0]))
#
#
# article_upvote = [int(sub_text.getText().split()[0]) for sub_text in all_subtext_list]
# max_index = article_upvote.index(max(article_upvote))
#
# print(f"Title : {article_title[max_index]}, Link : {article_link[max_index]}, Points : {article_upvote[max_index]}")























response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")

movie_div_list = soup.find_all(name="h3", class_="title")

movie_list = [title.getText() for title in movie_div_list]
movie_list = movie_list[::-1]

with open(file="./100_movie.txt", mode="w+", encoding="utf8") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")



