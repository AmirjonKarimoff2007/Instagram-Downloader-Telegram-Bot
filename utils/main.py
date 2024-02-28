import json
import requests

async def instadown(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
    querystring = {"url": link}
    headers = {"X-RapidAPI-Key": "92e2b98529msh6afc088a135b654p1714dajsn343f06db9b1f",
               "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"}
    response = requests.get(url, headers=headers, params=querystring)
    response = requests.get(url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    # Create a dictionary to store the results
    result_dict = {'type': '', 'media': ''}

    if 'Type' in rest:
        if rest['Type'] == "Post-Image":
            result_dict['type'] = 'image'
            result_dict['media'] = rest['media']
        elif rest['Type'] == "Post-Video":
            result_dict['type'] = 'video'
            result_dict['media'] = rest['media']
        elif rest['Type'] == "Carousel":
            result_dict['type'] = 'carousel'
            result_dict['media'] = rest['media']
    else:
        # Return 'Bad' if 'Type' is not present in the response
        return 'Bad'

    return result_dict
