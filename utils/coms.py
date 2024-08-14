from requests import Response

def download_segmants(url: str | bytes, segment_number: int) -> Response:
    from requests import get
    format_int = '%04d'%segment_number+'.txt'
    r = get(url+format_int, timeout=5)
    return r


def ripper(DownloadedSegmant, threads=50):
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(DownloadedSegmant, [x for x in range(0,9999)])