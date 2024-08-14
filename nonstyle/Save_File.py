import os

dir = "保存する場所" #"C:\"など
file = "aaa.txt"
os.path.join(dir, file)

fp = open(file, "w")
fp.write("書き込みたい内容")
fp.close()


