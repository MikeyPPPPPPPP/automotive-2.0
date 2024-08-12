from utils.fileandfolder import move_file, move_folder, remove_file, remove_folder, check_exits, make_directory, make_backup_folder, validate_folder_path
from utils.commandline import run_ffmpeg, run_proxy
from utils.timings import take_rest, take_nap, take_sleep
from utils.coms import download_segmants, ripper
from utils.configuring import reset_destination

class movieDownloader:
    def __init__(self, movie_name: str, destination: str):
        self.url: str = ''
        self.movie_name = movie_name.title()
        self.filename = movie_name.title().replace(' ', '-')
        self.destination = destination
        if self.destination == None or self.destination == '' and not validate_folder_path(self.destination):
            print(f"[!] The destination {self.destination} was not available. [!]")
            print("[!] Using self generated movies folder instead. [!]")

        self.errors = 0
        self.downloaded_segment_names = []
        self.threads = 50

        make_directory(self.filename)


    def start_Proxy(self):
        print("[*] Proxy Started [*]")
        print("[!] Turn on HTTP/HTTPS proxy and start watching movie [!]")
        take_sleep()
        run_proxy()

        while True:
            take_nap()
            if check_exits('log.txt'):
                print("[*] Extracted Server Info [*]")
                break

        with open('log.txt') as log:
            domain = log.readline().strip('\n')
            uri = log.readline().strip('\n')
            self.url = f"https://{domain}{uri}"
            print(self.url)

        take_rest()
        remove_file('log.txt')
        print(f"[*] Downloading segments with {str(self.threads)} threads [*]")
        ripper(self.downloadSegmant)


    def build_concat_file(self):
        self.downloaded_segment_names.sort()
        take_sleep()
        with open(self.filename+'/'+'videos.txt',"w") as video_file:
            for index in self.downloaded_segment_names:
                video_file.write(f"file '{index}'\n")

        run_ffmpeg(self.filename, self.movie_name)
        if self.destination == None or self.destination == '' and not validate_folder_path(self.destination):
            reset_destination()
            self.destination = make_backup_folder()
        move_file(f"{self.filename+"/"+self.movie_name}.mp4", f"{self.destination+"/"+self.movie_name}.mp4")
        

    def cleanup(self):
        take_rest()
        remove_folder(self.filename)


    def exe_cleanup(self):
        take_rest()
        remove_folder('utils')


    def downloadSegmant(self, segment_number: int):
        if self.errors > 10:pass
        else:
            r = download_segmants(self.url, segment_number)
            if r.status_code == 200:
                print('\r[*] Downloading: '+'%04d'%segment_number +' [*]',end='', flush=True)
                self.downloaded_segment_names.append('%04d'%segment_number+'.txt')
                with open(self.filename+'/'+'%04d'%segment_number+'.txt', 'wb') as file:
                    file.write(r.content)

            elif r.status_code == 404:
                self.errors += 1
