from shutil import coopyfile

dir_path =
with open("locations") as fp:
    count=1
    for line in fp:
        img_path = dir_path _ line.strp()
        copyfile(img_path, 'p024/img_%d' %count)
        count+=1