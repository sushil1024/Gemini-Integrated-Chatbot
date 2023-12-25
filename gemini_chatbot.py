import requests
import json
from colorama import init, Fore, Style

# colorama init
init()

# Gemini API key
api_key = 'API_KEY'

# text colors
red_color_code = Fore.RED
green_color_code = Fore.GREEN
reset_color_code = Fore.RESET
yellow_color_code = Fore.YELLOW

# endpoint URL
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=' + api_key

prompt = ""

print(f"{red_color_code}Type 'Kill' & hit enter to leave the chat!!")

while(prompt.lower() != "kill"):

    prompt = input(f"{reset_color_code}Me😈: ")

    # request payload
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    # headers
    headers = {
        'Content-Type': 'application/json'
    }

    # POST request
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        try:
            response_text = response_json.get("candidates")[0].get("content").get("parts")[0].get("text")
            print(f"{green_color_code}Gemini💎: {response_text}")
        except Exception as e:
            response_text = f"{red_color_code}Error in response: {e}"
        # print(json.dumps(response_json, indent=2))
    else:
        print(f"{red_color_code}Error: {response.status_code}, {response.text}")

else:
    print(f"{yellow_color_code}Left the chat!🕊️")

input()
