import requests

def fectch_random_user_freeapi():
      url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
      response = requests.get(url)
      data = response.json()
      
      if data ["success"] and "data" in data:
         user_data = data["data"]
         username = user_data["login"]["username"]
         country = user_data["location"]["country"]
         gender = user_data["gender"]
         return [username, country, gender]
      else:
        raise Exception ("Failed to fecth user data")
      
  
def main(): 
   try:
    username, country, gender =  fectch_random_user_freeapi()
    print(f"Username: {username} \nCountry: {country} \nGender: {gender}")
   except Exception as e:
     print(str(e))
     
if __name__ == "__main__":
    main()
         
         
      
      
      