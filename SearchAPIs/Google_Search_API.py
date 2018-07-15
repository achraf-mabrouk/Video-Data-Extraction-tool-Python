import json
import requests
from Model.Video import Video

# Google Search Api Key
key = "AIzaSyAVsZwhO2ZsSG4voSi7Ed6Jbf9jo4T68k0"
# Google Custom Search Engine ID
cx = "011096312765146532629:hs-b00pa7j0"
#  endpoint url :
url = "https://www.googleapis.com/customsearch/v1"


def search(searchTerm):
    parameters = {"q": searchTerm + " video",
                  "cx": cx,
                  "key": key,
                  "safe": "medium",
                  }
    videos_list = []
    i = 0
    while i < 3:  # 30 results(max) by doing 3 requests
        page = requests.request("GET", url, params=parameters)
        results = json.loads(page.text)
        # if no results for the search then break While loop
        if results is None:
            break
        else:
            try:
                for item in results["items"]:
                    videos_list.append(Video(searchTerm, item["title"], item["link"]))
                parameters["start"] = results["queries"]["nextPage"][0]["startIndex"]
            # if nextPage not exist break the while loop
            except KeyError:
                break
        i += 1
    return videos_list
