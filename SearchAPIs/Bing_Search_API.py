import requests
from Model.Video import Video

# the Subscription key of the API
subscription_key = "94505fad7f7d403f86f0270526c78b3f"
assert subscription_key

search_url = "https://api.cognitive.microsoft.com/bing/v7.0/videos/search"
# prepare headers of the request
headers = {"Ocp-Apim-Subscription-Key": subscription_key}


# search_term : is the search keywords
# returns List of Videos
def search(search_term):
    # Query parameters
    params = {"q": search_term, "count": 100, "pricing": "free"}

    response = requests.get(search_url, headers=headers, params=params)
    # raise_for_status : is gonna raise an error exception if it exist
    response.raise_for_status()
    search_results = response.json()

    videos_list = []
    for x in range(len(search_results["value"])):
        # create video object and append it to the list
        try:
            videos_list.append(Video(search_term, search_results["value"][x]["name"],
                                     search_results["value"][x]["contentUrl"]))
        except KeyError:
            break
    return videos_list
