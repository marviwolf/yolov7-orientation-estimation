import shutil
from os import walk
from os import makedirs
import random

files=[]
for _,_,filename in walk('./orientation-estimation/labels'):
    files = (filename)

amountall = 0
amounttrain=0
amountval=0
amounttest=0

makedirs(f'./orientation-estimation/train_rgb/', exist_ok=True)
makedirs(f'./orientation-estimation/train_rgb/images/', exist_ok=True)
makedirs(f'./orientation-estimation/train_rgb/labels/', exist_ok=True)
makedirs(f'./orientation-estimation/val_rgb/', exist_ok=True)
makedirs(f'./orientation-estimation/val_rgb/images/', exist_ok=True)
makedirs(f'./orientation-estimation/val_rgb/labels/', exist_ok=True)
makedirs(f'./orientation-estimation/test_rgb/', exist_ok=True)
makedirs(f'./orientation-estimation/test_rgb/images/', exist_ok=True)
makedirs(f'./orientation-estimation/test_rgb/labels/', exist_ok=True)

for file in files:
    if file.startswith("Depth"):

        foldername=f'{file.partition(".tcfa")[0]}.tcfa'
        filename=f'{file.partition(".txt")[0].partition(".tcfa_")[2]}.png'
        labelname=f'{foldername}_{filename}'
        labelname=f'{labelname.partition(".png")[0]}.txt'

        rand = random.randint(1, 100)

        if rand <=70:
                shutil.copyfile(f'./frames_rgb/{foldername}/{filename}',f'./orientation-estimation/train_rgb/images/{foldername}_{filename}')
                shutil.copyfile(f'./orientation-estimation/labels/{labelname}',f'./orientation-estimation/train_rgb/labels/{labelname}')
                print(f'adding {file} to train data')
                amounttrain+=1
                amountall+=1

        if rand > 70 and rand <= 90:
                shutil.copyfile(f'./frames_rgb/{foldername}/{filename}',f'./orientation-estimation/val_rgb/images/{foldername}_{filename}')
                shutil.copyfile(f'./orientation-estimation/labels/{labelname}',f'./orientation-estimation/val_rgb/labels/{labelname}')
                print(f'adding {file} to val data')
                amountval+=1
                amountall+=1

        if rand > 90:
                shutil.copyfile(f'./frames_rgb/{foldername}/{filename}',f'./orientation-estimation/test_rgb/images/{foldername}_{filename}')
                shutil.copyfile(f'./orientation-estimation/labels/{labelname}',f'./orientation-estimation/test_rgb/labels/{labelname}')
                print(f'adding {file} to test data')
                amounttest+=1
                amountall+=1
            
print(f'Added {amounttrain} from {amountall} to train data ({amounttrain/amountall})')
print(f'Added {amountval} from {amountall} to val data ({amountval/amountall})')
print(f'Added {amounttest} from {amountall} to test data ({amounttest/amountall})')