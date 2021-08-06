from datetime import datetime


class log_the_search_result:
    def __init__(self) -> None:

        # getting current time.
        now = datetime.now()
        formated_time = now.strftime("%I-%M%p %d.%m.%Y")

        # creating output file
        self.output = open(f"search_output {formated_time}.txt", "w")
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
