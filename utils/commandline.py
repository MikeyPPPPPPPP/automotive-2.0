def run_ffmpeg(source_file: str, video_name: str) -> int:
    from os import system
    system(f'ffmpeg -v quiet -stats -f concat -i {source_file+"/"}videos.txt -c copy "{source_file+"/"+video_name}.mp4"')

def run_proxy() -> int:
    from os import system
    from utils.proxy_file_check import validate_proxy_file
    validate_proxy_file()
    system(f'mitmproxy -s utils\\proxy.py')