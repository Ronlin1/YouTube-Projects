import pyshorteners as s

url = "https://drive.google.com/\
file/d/1R8vVpFgmneS5DCrO8AsxmLoqQ7W-ZuAf/view?usp=sharing"

short_ = s.Shortener()
url_short = short_.tinyurl.short(url)

print(url)
print('_____SHORTENED____VERSION_______')
print(url_short)
