import os

url="https://custom-writing.org/blog/wp-content/uploads/custom-writing.org/2017/01/"

for i in range(12):
    os.system("wget "+ url + str(i+1) + ".mp3")









