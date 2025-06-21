"""
this script designed to scrape off information from two major movie rating websites: IMDB and Rotten Tomatoes
twelve movie ratings are obtained from each source.
"""
from bs4 import BeautifulSoup as SOUP
import re
import requests
from math import log

def locate_url(user_emotion):

    file_path = "url/"
    emotions = ["Happy", "Sad", "Disgusted", "Angry",
                "Neutral", "Fearful", "Surprised"]

    url_lst = []
    with open(file_path + "IMDB.txt") as f1, open(file_path + "RT.txt") as f2:
        f1_lst = f1.readlines()
        # print(f1)
        f2_lst = f2.readlines()
        # print(f2)
        for i in range(len(emotions)):
            if emotions[i] in user_emotion:
                IMDB = f1_lst[i]
                RT = f2_lst[i]
                url_lst.append(IMDB)
                url_lst.append(RT)
    # print(url_lst)
    return url_lst

"""sort movies based on their rating, from high to low
   through this function, the recommender is able to select the movie with highest weighted rating
"""
def rank_movies(movie_dict):
    ranked_dict = {}
    rating = []
    for movie_info in movie_dict.values():
        if type(movie_info[-1]) == float:
            rating.append(movie_info[-1])
    rating = sorted(rating, reverse = True)
    for r in rating:
        for k in movie_dict.keys():
            if movie_dict[k][-1] == r:
                ranked_dict[k] = movie_dict[k]
    return ranked_dict 

# IMDB should be a single link
def scrape_IMDB(IMDB, num, folder_path = None): 
    # folder_path = "movie_summary/" # you only need the folder_path when you need to store movie summary
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    response = requests.get(IMDB, headers=headers)
    # print(response.text)
    data = SOUP(response.text, 'lxml')
    movie_list = data.find('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM detailed-list-view ipc-metadata-list--base")

    # Extract all <h3> elements
    title_tags = movie_list.find_all('h3', class_="ipc-title__text ipc-title__text--reduced")

    # Get inner text
    movie_titles = [tag.get_text(strip=True)[3:].strip() for tag in title_tags]
    # print(movie_titles)

    summaries=movie_list.find_all('div', class_="ipc-html-content-inner-div")

    # Extract the text from each <div> element
    movie_summaries = [summary.get_text(strip=True) for summary in summaries]
    # print(movie_summaries)

    # we hope to have movie's name, grading, runtime, and rating
    IMDB_dict = {}
    title_lst = []


    # IMDB lists top 50 from each genre

    for i in range(len(movie_titles)):
        title = movie_titles[i]
        summary = movie_summaries[i]
        IMDB_dict[title] = []
        title_lst.append(title)

        # movie summary
        if summary != None:
            IMDB_dict[title].append(summary)


    return IMDB_dict

# # RT should be a single link
# def scrape_rt(RT, num):
#     response = requests.get(RT)
#     data = SOUP(response.text, 'lxml')
#     RT_dict = {}
#     title_lst = []
#     rel_lst = []
#     reviews_lst = []

#     # Rotten Tomatoes lists top 100 from each genre

#     # as above, we hope to obtain name, grading, runtime, and rating
#     for movie in data.find_all('tr'):
#         # title
#         title = movie.find("a", class_ = "unstyled articleLink")
#         if title != None:
#             cleanTitle = str(title).split('">')[1].split(" (")[0].strip('\n').strip()
#             RT_dict[cleanTitle] = []
#             title_lst.append(cleanTitle) #100

#             # link to movie profile
#             rel_link = str(title).split('href="')[1].split('">\n')[0]
#             link = "https://www.rottentomatoes.com/" + rel_link
#             RT_dict[cleanTitle].append(link)

#         # numbers of reviews:
#         num_reviews = movie.find('td', class_ = "right hidden-xs")
#         if num_reviews != None:
#             num_reviews = int(str(num_reviews).split('">')[1].split('</')[0]) #100

#             # collect number of reviewers for later movie score adjustments
#             reviews_lst.append(num_reviews)

#     # rating
#     for review, title, movie in zip(reviews_lst, title_lst, data.find_all('span', class_ = 'tMeterIcon tiny')):
#         rating = movie.find('span', class_ = "tMeterScore")
#         rating = str(rating).split('">\xa0')[1].split('%</')[0]
#         # transform RT rating into the same scale as IMDB rating (out of 10)
#         weightedRating = int(rating)/10

#         # score adjustments
#         weightedRating = weightedRating * log(log(review, 4),5)
#         weightedRating = round(weightedRating, 1)
#         RT_dict[title].append(weightedRating)

#     # to increase the efficiency of the script,
#     # we are going to rank movies based on rating
#     # and only look up movie profiles of top-ranked movies

    

#     ranked_dict = rank_movies(RT_dict)
#     ranked_dict = dict(list(ranked_dict.items())[0: num])
#     for value in ranked_dict.values():
#         rel_lst.append(value[0])
#         value.pop(0)


#     new_title_lst = list(ranked_dict.keys())

#     # # grading and runtime information are inside movie profile links

#     for title, link in zip(new_title_lst, rel_lst): 
#         response = requests.get(link)
#         data_1 = SOUP(response.text, 'lxml')

#         #movie summary
#         for div_tag in data_1.find_all('div', {'class':'movie_synopsis clamp clamp-6 js-clamp'}):
#             summary = str(div_tag.text).replace("\n","")
#             ranked_dict[title].insert(0, summary)

#         for div_tag in data_1.find_all('li', {'class':'meta-row clearfix'}):
#             movie_label= div_tag.find('div', {'class': 'meta-label subtle'}).text
#             if movie_label == "Rating:":
#                 rating_info = div_tag.find('div', {'class': 'meta-value'}).text
#                 rating_info = rating_info.replace("\n","").replace(" ", "")
#                 ranked_dict[title].insert(1, rating_info)
#             elif movie_label == "Runtime:":
#                 runtime_info = div_tag.find('div', {'class': 'meta-value'}).text
#                 runtime_info = runtime_info.replace("\n","").replace(" ", "")

#                 ranked_dict[title].insert(2, runtime_info)

#     return ranked_dict

## (DO NOT RUN) For Testing Purpose:
user_emotion = 'Happy'
RT_url = locate_url(user_emotion)[1]
IMDB_url = locate_url(user_emotion)[0]
print(scrape_IMDB(IMDB_url, 12))
# print(scrape_rt(RT_url, 12))

movie_dict = {}
# movie_dict.update(scrape_rt(RT_url, 12))
movie_dict.update(scrape_IMDB(IMDB_url, 12))
# movie_dict = rank_movies(movie_dict)
    
