# automotive-2.0
I wrote code to download movies from an illegal streaming  website. Enjoy

# Warning

The FBI has taken down the site so this code is now useless. bflix.to

# Why?
They advertised a download option but I reverse engineered the javascript and found that to be false.


# Requirments:
## Python modules
```
requests
mitmproxy
```

## Installed
```
FoxyProxy (Chrome Browser extention)
mitmproxy (install guide https://docs.mitmproxy.org/stable/overview-installation/)
ffmpeg    (install guide https://www.ffmpeg.org/documentation.html)
```


# How To:

1. Start the program and enter the movie name
2. Setup your browser proxy to connect to *:8080 (basicly one click with Foxy Proxy)
3. Play the movie normaly until the program starts downloading (This should be instant from pressing play on the movie)
4. Enjoy!

 # Demo Video (Youtube)
https://www.youtube.com/watch?v=CeK18eqvpwo

# Info

The site allows you to stream virtually any movie or show for free. I’ve used 
a similar platform before, but their bug fixes were lackluster, and the selection
was mediocre. This site, however, is much more polished, boasting a popular
reputation and frequent UI/UX updates. It employs a Cloudflare WAF and various
anti-debugging techniques. Still, with enough time and effort, I’ve found that
virtually any code can be cracked. 


