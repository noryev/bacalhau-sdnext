import requests
import json
import os

api_url = os.environ['SDNEXT_API']
data = {
    'prompt': 'a photo of a cat',
    'negative_prompt': 'dog',
    'steps': 20,
    'sampler_name': 'Euler a',
    'cfg_scale': 7,
    'seed': 42,
    'width': 512,
    'height': 512
}

response = requests.post(f'{api_url}/process', json=data)
print(json.dumps(response.json(), indent=2))