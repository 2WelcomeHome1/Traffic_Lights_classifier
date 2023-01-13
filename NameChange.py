import os
import pathlib

dirs_list = []
for root, dirs, files in os.walk("./train"):  
    for dirs in dirs:
        path = pathlib.Path('./train/' + dirs)
        print (path)
        for i, path in enumerate(path.glob('*.jpg')):
            new_name = dirs + '.' + str(i) + '.jpg'
            path.rename('./train/' + new_name)
print ('ready')


# path = pathlib.Path('./train/yellow')
# for i, path in enumerate(path.glob('*.png')):
#     new_name = 'yellow' + '.' + str(i) + '.jpg'
#     print(new_name)
#     path.rename('./Train/yellow/' + new_name)