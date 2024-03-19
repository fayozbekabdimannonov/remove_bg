import requests


def bg_change_color(FILE_NAME,color):
    rasm=''
    API_KEY ='VWZAWVBsVgN1HVmYmiQks32j'


    response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': FILE_NAME,
        'size': 'auto',
        'bg_color':color
    },
    files = {
        
    },
    headers={'X-Api-Key': API_KEY},
)
    if response.status_code == requests.codes.ok:
      
        rasm = response.content
    else:
        print("Error:", response.status_code, response.text)
    return rasm