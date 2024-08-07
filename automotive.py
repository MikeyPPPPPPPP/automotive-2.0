import concurrent.futures
import requests
import time
import os

class movieDownloader:
    def __init__(self, movie_name: str):
        self.url: str = ''
        self.movie_name = movie_name.title()
        self.filename = movie_name.title().replace(' ', '-')

        self.errors = 0
        self.downloaded_segment_names = []
        self.threads = 50

        if not os.path.exists(self.filename):
            os.mkdir(self.filename)

    def start_Proxy(self):
        print("[*] Proxy Started [*]")
        print("[!] Turn on HTTP/HTTPS proxy and start watching movie [!]")
        time.sleep(5)
        os.system('mitmproxy -s proxy.py')

        while True:
            time.sleep(2)
            if os.path.exists('log.txt'):
                print("[*] Extracted Server Info [*]")
                break

        with open('log.txt') as log:
            domain = log.readline().strip('\n')
            uri = log.readline().strip('\n')
            self.url = f"https://{domain}{uri}"
            print(self.url)

        time.sleep(1)
        os.system('rm log.txt')
        print(f"[*] Downloading segments with {str(self.threads)} threads [*]")
        self.ripper()


    def build_concat_file(self):
        self.downloaded_segment_names.sort()
        time.sleep(5)
        with open(self.filename+'/'+'videos.txt',"w") as video_file:
            for index in self.downloaded_segment_names:
                video_file.write(f"file '{index}'\n")

        os.system(f'ffmpeg -v quiet -stats -f concat -i {self.filename+"/"}videos.txt -c copy "{self.filename+"/"+self.movie_name}.mp4"')
        os.system(f'mv "{self.filename+"/"+self.movie_name}.mp4" .')#~/Desktop/movies')
        
        



    def downloadSegmant(self, segment_number: int):
        if self.errors > 10:pass
        else:
            format_int = '%04d'%segment_number+'.txt'# 0002.txt, 0212.txt, 0021.txt

            r = requests.get(self.url+format_int, timeout=5)
            if r.status_code == 200:
                #print('Downloading: '+'%04d'%segment_number)
                print('\r[*] Downloading: '+'%04d'%segment_number +' [*]',end='', flush=True)
                self.downloaded_segment_names.append('%04d'%segment_number+'.txt')
                with open(self.filename+'/'+'%04d'%segment_number+'.txt', 'wb') as file:
                    file.write(r.content)

            elif r.status_code == 404:
                self.errors += 1

    def ripper(self):

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.downloadSegmant, [x for x in range(0,9999)])


def main(mov_name):
    mov = movieDownloader(mov_name)
    mov.start_Proxy()
    mov.build_concat_file()
    time.sleep(1)
    os.system(f'rm -rf {mov.filename}')
            
if __name__ == "__main__":
    mov_name = input("Movie_Name:")
    main(mov_name)
