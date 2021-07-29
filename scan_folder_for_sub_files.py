import glob, os


def get_all_the_sub_files(folder_path: str):
    return [files for files in os.walk(folder_path)][0][2]


if __name__ == "__main__":
    print(get_all_the_sub_files(r"Z:\.temp\ggg"))
