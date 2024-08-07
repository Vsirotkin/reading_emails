import requests

url = 'http://localhost:8000/api/email-messages/'
data = {
    'subject': 'Test Subject',
    'sender': 'test@example.com',
    'body': 'Test message from script'
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print('Message sent successfully')
else:
    print(f'Failed to send message. Status code: {response.status_code}')
    print(response.json())