import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url:str, mock: bool = True):
    

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/subhamoy-burman/0c9f9d8857b4d7c3e476c74ffc0aaef2/raw/bill_gates_scrapped.json"
        response = requests.get(linkedin_profile_url, timeout=10)
        print("Raw response content:", response.text)  # Debugging line
        response_text = response.text.lstrip('\ufeff')  # Strip BOM if present
        try:
            data = json.loads(response_text)
            print(data)
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)
    else:
        url = "https://nubela.co/proxycurl/api/v2/linkedin"
        headers = {'Authorization': f'Bearer {os.environ['PROXY_CURL_API_KEY']}'}
        # Example: Scrape a LinkedIn profile
        params = {
        'linkedin_profile_url': 'https://www.linkedin.com/in/williamhgates/',
        'use_cache': 'if-recent'}
        response = requests.get(url, headers=headers, params=params)


#https://gist.github.com/subhamoy-burman/0c9f9d8857b4d7c3e476c74ffc0aaef2
#https://gist.githubusercontent.com/subhamoy-burman/0c9f9d8857b4d7c3e476c74ffc0aaef2/raw/fc9885097eb402e5af1e228024d863c0a8d8af4f/bill_gates_scrapped.json
    print(response.json())

    data = response.json()

    data = {
        k: v for k, v in data.items()
        if(v not in ([], "","", None)) and k not in ["certifications", "education", "experience", "skills"]
    }

    return data
    
if __name__ == "__main__":
    scrape_linkedin_profile("https://www.linkedin.com/in/williamhgates/", mock=True)    
