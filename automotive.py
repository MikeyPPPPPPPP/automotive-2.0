import concurrent.futures
import requests
import time
import os

class movieDownloader:
    def __init__(self, url: str, movie_name: str):
        self.url = url
        self.movie_name = movie_name.title()
        self.filename = movie_name.title().replace(' ', '-')

        self.errors = 0
        self.downloaded_segment_names = []
        self.threads = 10

        if not os.path.exists(self.filename):
            os.mkdir(self.filename)


    def build_concat_file(self):
        self.downloaded_segment_names.sort()
        time.sleep(5)
        with open("videos.txt","w") as video_file:
            for index in self.downloaded_segments:
                video_file.write(f"file '{index}'\n")

        os.system(f'ffmpeg -f concat -i videos.txt -c copy {self.movie_name}.mp4')
        



    def downloadSegmant(self, segment_number: int):
        if self.errors > 10:
            pass
        else:
            format_int = '%04d'%segment_number+'.txt'# 0002.txt, 0212.txt, 0021.txt

            r = requests.get(url+'%04d'%segment_number+'.txt')
            if r.status_code == 200:
                print('Downloading: '+'%04d'%segment_number)
                self.downloaded_segment_names.append('%04d'%segment_number+'.txt')
                with open(self.filename+'/'+'%04d'%segment_number+'.txt', 'wb') as file:
                    file.write(r.content)

            elif r.status_code == 404:
                self.errors += 1

    def ripper(self):

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.downloadSegmant, [x for x in range(0,9999)])

url = ""
mov = movieDownloader(url, "tetris")
mov.ripper()
mov.build_concat_file()
            
