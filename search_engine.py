import requests, re
from bs4 import BeautifulSoup
from difflib import SequenceMatcher, get_close_matches
from guessit import guessit


def search_movie(movie_name: str, movie_year: int):
    # this will request a page with movie title and scrap that page.
    search = requests.get(f"http://circleftp.net", params={"s": movie_name})

    # if page status code not == 200 raise error.
    if search.status_code != 200:
        raise Exception("request failed. status code not 200.")

    content = search.content
    html_soup = BeautifulSoup(content, "html.parser")
    all_article = html_soup.find_all("article")

    # all movie will be added to search result obj.
    search_result = []
    # found will be True when the movie name and year will be match to the searching movie.
    found = False
    for article in all_article:
        # getting movie name and link from html document.
        found_name = article.find("h3", class_="entry-title").text.strip()
        link = article.find("h3", class_="entry-title").find("a").get("href")

        # getting direct download for the movie.
        try:
            direct_download_link = article.find("a", class_="downloadbtn").get(
                "download"
            )
        except:
            direct_download_link = ""
        # extacting movie name and year from full title.
        try:
            title = guessit(found_name)
        except:
            continue
        try:
            title_name = title["title"]
            try:
                title_year = title["year"]
            except:
                title_year = re.search(r"\d\d\d\d", found_name)[0]

            # this will return a matched % between 2 strings. in my case 2 movie name.
            match_ratio = SequenceMatcher(None, title_name, movie_name).ratio() * 100

            # if both movie title ratio match more then 70% and also year are same..
            # thats means movie already avaliable in server. found = true else movie not available in server.
            if match_ratio >= 70:
                if title_year == movie_year:
                    found = True

            # if movie name didn't  match more then 50% or a series then proccess will be stopped.
            if match_ratio <= 50 or "series" in found_name.lower():
                continue

            search_result.append(
                {
                    "title": found_name,
                    "link": link,
                    "direct_download_link": direct_download_link,
                }
            )

        except:
            pass

    return {"found": found, "search_result": search_result}


if __name__ == "__main__":
    print(search_movie("Anand", 1971))
