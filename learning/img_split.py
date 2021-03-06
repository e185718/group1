'''FaceEditedフォルダにある画像の２割をテストフォルダに移行するプログラム。
'''
import shutil
import random
import glob
import os
members = ["松本潤","二宮和也","相葉雅紀","櫻井翔","大野智"]
for name in members:
    in_dir = "./FaceEdited/"+name+"/*"
    in_jpg=glob.glob(in_dir)
    img_file_name_list=os.listdir("./FaceEdited/"+name+"/")
    #img_file_name_listをシャッフル、そのうち2割をtestフォルダに入れる。
    random.shuffle(in_jpg)
    os.makedirs('./Test/' + name, exist_ok=True)
    for t in range(len(in_jpg)//5):
        shutil.move(str(in_jpg[t]), "./Test/"+name)
