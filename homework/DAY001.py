from urllib.request import urlretrieve
import os
path='Users\\cupoy\\Desktop\\Data'

try:
    os.makedirs( 'Users\\cupoy\\Desktop\\Data', exist_ok=True )
    urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "Users\\cupoy\\Desktop\\Data\\Homework.txt")
except:
    print('發生錯誤！')

# 要檢查的檔案路徑
filepath = "Users\\cupoy\\Desktop\\Data\\Homework.txt"

# 檢查檔案是否存在
if os.path.isfile(filepath):
    with open("Homework.txt", "w") as file:
        file.write("Hello World") 
    print('[O] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')
else:
    print('[X] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')

with open("Homework.txt", "r") as file:
    f=file.read()

if len('Hello World') == len(f):
    print('[O] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')
else:
    print('[X] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')