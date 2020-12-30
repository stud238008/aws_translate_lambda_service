import requests

response = requests.post(
    'YOUR URL',
    json={
        'text': "hello",
        'source_language': "en",
        'target_language': "de"
    }
)

print(response.json())
