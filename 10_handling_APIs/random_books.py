import requests

def random_books():
    url = "https://api.freeapi.app/api/v1/public/books?page=1&limit=10&inc=kind%2Cid%2Cetag%2CvolumeInfo&query=tech"
    
    response = requests.get(url)
    data = response.json()
    # print(data)
    
    if data ["success"] and "data" in data:
       book_data = data["data"]
       prop_book = book_data["data"][0]["volumeInfo"]
        
    
    