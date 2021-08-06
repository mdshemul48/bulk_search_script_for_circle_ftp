import sys, os, re
import time
from search_engine import search_movie
from guessit import guessit
from scan_folder_for_sub_files import get_all_the_sub_files
from logger import log_the_search_result


def read_command_args():
    # this will read command that givin by user :- get text path from user.
    all_args = sys.argv

    # trying to get the file name or path if not given then raise error.
    # later i will handle the error in main exception.
    try:
        if len(all_args[1].strip()) == 0:
            raise FileNotFoundError("no file name given!")
    except:
        raise FileNotFoundError("no file name given!")
    return all_args[1]


def red_text_file(text_file_path: str):

    # this will read text file. make a list of all lines then return.
    text_file = open(os.path.join(os.getcwd(), text_file_path), "r")
    full_text_file = text_file.read()
    full_text_line_list = full_text_file.split("\n")
    return full_text_line_list


class movie_title_data:
    # this object will get movie title and return movie name and year
    def __init__(self, movie_name) -> None:
        self.movie_name = movie_name
        self.movie_data_obj = guessit(movie_name)

    def get_title(self):
        try:
            return self.movie_data_obj["title"]
        except KeyError:
            return re.search(r"\D", self.movie_name)[0]

    def get_year(self):
        try:
            return self.movie_data_obj["year"]
        except KeyError:
            return re.search(r"\d\d\d\d", self.movie_name)[0]


def searcher(text_line: str, log):

    # checking if line empty or not. if empty then don't process.
    if len(text_line.strip()) == 0:
        return

    # getting movie title and year..
    try:
        movie_title_info = movie_title_data(text_line)
        movie_title = movie_title_info.get_title()
        movie_year = movie_title_info.get_year()
    except KeyError as err:
        print(f"{text_line} -----> didn't contain movie {err}. :')")
        return

    # from here starting search.
    print(f"searching: {text_line}..")

    # searching the movie and getting the result..
    searching = search_movie(movie_title, movie_year)
    is_found = searching["found"]
    result = searching["search_result"]

    if is_found:
        found = "already exist in the server."
    else:
        found = "not Found in the server."
    # this will print movie found or not.
    print(found)

    # this will log the movie in log text file.
    log.log_movie_result(movie_title=text_line, found=found, result=result)

    # task done.
    print("boo")


def main():
    # this log will create another text file and log every result.
    log = log_the_search_result()
    # getting user input (text file path)
    try:

        file_name = read_command_args()
        text_all_line_list = red_text_file(file_name)
    except:
        folder_path_to_scan = input("No search files given. Please enter folder path: ")
        text_all_line_list = get_all_the_sub_files(folder_path_to_scan)

    # getting all the line of the text as a list.

    # this will process 1 by 1 movie to the searcher.
    # then searcher will extract and search the movie in our site.
    for line in text_all_line_list:
        try:
            searcher(line, log)
        except Exception as err:
            print("Error: ", err)

    # this will save the search_result log file.
    log.save_file()


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)

    print("DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(10)
