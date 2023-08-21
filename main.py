import webbrowser
import random
import string
import os

Generated = "NT" + random.choice(string.ascii_letters) + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)) + "." + random.choice(string.ascii_letters).upper() + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)) + "" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)) + "@zbock.com"
RestoreCloud = "?redirect_to=%2Foauth2%2Fauthorize%3Fclient_id%3D1140628722161041449%26redirect_uri%3Dhttps%3A%2F%2Frestorecord.com%2Fapi%2Fcallback%26response_type%3Dcode%26scope%3Didentify%2Bguilds.join%26state%3D1141458327319101661"

os.system("taskkill /im chrome.exe /f")
def open_incognito_url(url):
    try:
        os.system(f"start chrome --incognito {url}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    url_to_open = "https://discord.com/register?email=" + Generated #+ RestoreCloud + "?test"
    open_incognito_url(url_to_open)
    
#print('Email:', Generated,"@zbock.com")
print('Email:', Generated, end='.\n')
#webbrowser.open_new("https://discord.com/register?email=" + Generated + "@zbock.com")