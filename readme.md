This script only useable for circle network users. It will search movies in bulk in circleftp. You have to provide the movie's name in a text file.

Then this script will search all those movies in circleftp.net and the script will give you another text file back with all search result and does it exist on circleftp or not confirmation.

## Example.

In `input.txt`, you added some movie's name and year. Then script will return you the search result of those movies.

in `input.txt`

```
Go Goa Gone 2013 1080p Gplay WEB-DL DDP 5.1 x264
Delhi Belly 2011 1080p NF WEB-DL x264 AVC Dual Audio [Hindi DD 5.1 + English DDP 5.1] ESubs

Say Salaam India 2007

```

The script will return another file that contains the result like below.

This text file will be auto-generated by the script.

You will get all the search results and links that match with your entered movies in this file.

`output.txt`

```
---------------------
Movie: Go Goa Gone 2013 1080p Gplay WEB-DL DDP 5.1 x264 already exist in the server..
+---------
|
+---Go Goa Gone (2013) HDRip
|   \---http://circleftp.net/cn/go-goa-gone-2013-hdrip/
|      \---http://index1.circleftp.net/FILE/Hindi%20Movies/2013/Go%20Goa%20Gone%20%282013%29%20HDRip%20%5BOpenTsubasa%5D/Go%20Goa%20Gone%20%282013%29%20HDRip%20%5BOpenTsubasa%5D.mp4
|
+---Mickey Mouse Mixed-Up Adventure (TV Series 2017-) Anime
|   \---http://circleftp.net/cn/mickey-mouse-mixed-up-adventure-tv-series-2017-anime/
+---Taarak Mehta Ka Ooltah Chashmah (TV Series 2008-) (001-2900Episodes)
|   \---http://circleftp.net/cn/taarak-mehta-ka-ooltah-chashmah-tv-series-2008-001-2900episodes/
|

---------------------
Movie: Delhi Belly 2011 1080p NF WEB-DL x264 AVC Dual Audio [Hindi DD 5.1 + English DDP 5.1] ESubs already exist in the server..
+---------
|
+---Delhi Belly (2011) Hindi 720p HDRip x264 AAC
|   \---http://circleftp.net/cn/delhi-belly-2011-hindi-720p-hdrip-x264-aac/
|      \---http://index1.circleftp.net/FILE/Hindi%20Movies/2011/Delhi%20Belly%20%282011%29%20Hindi%20720p%20HDRip%20x264%20AAC/Delhi%20Belly%20%282011%29%20Hindi%20720p%20HDRip%20x264%20AAC.mp4
|
+---Blitz (2011) 1080p 10bit Bluray [Dual Audio] [Hindi+English] x265 ESubs
|   \---http://circleftp.net/cn/blitz-2011-1080p-10bit-bluray-dual-audio-hindienglish-x265-esubs/
|      \---http://index.circleftp.net/FILE/English%20%26%20Foreign%20Dubbed%20Movies/2011/Blitz%20%282011%29%201080p%2010bit%20Bluray%20%5BDual%20Audio%5D%20%5BHindi%2BEnglish%5D%20x265%20ESubs/Blitz%20%282011%29%201080p%2010bit%20Bluray%20%5BDual%20Audio%5D%20%5BHindi%2BEnglish%5D%20x265%20ESubs.mkv
|
+---Super Bear (2019) 1080p WEBRip [Dual Audio] [Hindi+Turkish]
|   \---http://circleftp.net/cn/super-bear-2019-1080p-webrip-dual-audio-hinditurkish/
|      \---http://ftp5.circleftp.net/FILE/Animation%20Dubbed%20Movies/Super%20Bear%20%282019%29%201080p%20WEBRip%20%5BDual%20Audio%5D%20%5BHindi%2BTurkish%5D/Super%20Bear%20%282019%29%201080p%20WEBRip%20%5BDual%20Audio%5D%20%5BHindi%2BTurkish%5D%20.mkv
|
+---Mine (2016) 1080p BluRay x264
|   \---http://circleftp.net/cn/mine-2016-1080p-bluray-x264/
|      \---http://index.circleftp.net/FILE/English%20Movies/2016/Mine.2016.1080p.BluRay.x264-%5BYTS.AG%5D/Mine.2016.1080p.BluRay.x264-%5BYTS.AG%5D.mp4
|
|

---------------------
Movie: Say Salaam India 2007 not Found in the server..
+---------
|
|
```

## Installation and setup.

#### 1st step.

First of all, you have to install python.
Click this link below and download python from the official website.

https://www.python.org/

During installation click,`add python to path`. This is an essential part of python installation.

![ScreenShot](screenshot/add_Python_to_Path.png)

#### 2nd step.

Download this entire git repo by clicking `code > Download Zip`.

![ScreenShot](screenshot/download.png)

After download complete. Extract the file.

#### 3rd step.

After extracting, open extracted folder and click in the place of the folder path. Type `cmd` and hit `Enter`.

![ScreenShot](screenshot/1623438770968.png)

In that cmd prompt, type `pip install -r requirements.txt` and hit `Enter`. Then wait for the completion.

![ScreenShot](screenshot/install.png)

Installation is done!
