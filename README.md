# automotive-2.0
I wrote code to download movies from an illegal streaming  website. Enjoy


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

The site lets you stream basically any movie or show you want for free. I've done this on another site, 
but they fix bug also there selection was ... meh. This site is very popular and has had numerous UI/UX 
updates. Theres a Cloudflare WAF along with a bunch of anti-dubugging techniques being used. Unfortunately 
for them, I've learned that with enough time and effort - anything is possible, especially with code. 
