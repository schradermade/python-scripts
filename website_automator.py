import sys
import webbrowser

URLS = {
  "work": ["https://www.slack.com", "https://www.google.com"],
  "personal": ["https://www.netflix.com", "https://www.spotify.com", "https://www.youtube.com"]
}

def open_webpages(urls):
  for url in urls:
    webbrowser.open(url)

if __name__ == "__main__":
  set_name = sys.argv[1]
  urls = URLS[set_name]
  open_webpages(urls)