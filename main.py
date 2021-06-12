import sys, os
import time
from search_engine import search_movie
from guessit import guessit


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
        return self.movie_data_obj["title"]

    def get_year(self):
        return self.movie_data_obj["year"]


class log_the_search_result:
    def __init__(self) -> None:
        # creating output file
        self.output = open("search_output.txt", "w")
        self.output.write("script for searching movies in circleftp.net\n")
        self.output.write("Created By MD. Shimul. ;)\n")
        self.output.write("---------------------------------\n")

    def log_movie_result(self, **kwargs):
        # extracting data from given obj from **kwargs
        movie_title = kwargs["movie_title"]
        found = kwargs["found"]
        result = kwargs["result"]

        # writing movie name.
        self.output.write("\n")
        self.output.write("---------------------\n")
        self.output.write(f"Movie: {movie_title} {found}.\n")
        self.output.write(f"+---------\n")
        self.output.write(f"|\n")

        # writing movie search result
        for movie in result:
            title = movie["title"]
            link = movie["link"]
            direct_download_link = movie["direct_download_link"]
            self.output.write(f"+---{title}\n")
            self.output.write(f"|   \---{link}\n")
            if len(direct_download_link) > 0:
                self.output.write("|      |\n")
                self.output.write(f"|      \---{direct_download_link}\n|\n")

        self.output.write("|\n")

    def save_file(self):
        # this will save the output file.
        self.output.close()


def searcher(text_line: str, log):

    # checking if line empty or not. if empty then don't process.
    if len(text_line.strip()) == 0:
        return

    # getting movie title and year..
    try:
        movie_title_info = movie_title_data(text_line)
        movie_title = movie_title_info.get_title()
        movie_year = movie_title_info.get_year()
    except KeyError:
        print(
            f"{text_line} -----> didn't contain movie title or year.. maybe not both. :')"
        )
        return

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
    file_name = read_command_args()

    # getting all the line of the text as a list.
    text_all_line_list = red_text_file(file_name)

    # this will process 1 by 1 movie to the searcher.
    # then searcher will extract and search the movie in our site.
    for line in text_all_line_list:
        try:
            searcher(line, log)
        except:
            print(
                f"{line} -----> didn't contain movie title or year.. maybe not both. :')"
            )

    # this will save the search_result log file.
    log.save_file()


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)

    print("DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(10)
