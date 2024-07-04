import csv
from os import walk
from os import path
from os import makedirs
import shutil

labelindex = [ 'front', 'front-right','right','back-right','back','back-left','left','front-left' ]

classes = set()
amountSuccess=0

makedirs('orientation-estimation/labels/', exist_ok=True)

with open('./orientation-estimation/labels.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        
        class_name = row['class_namefile_name']
        if  class_name not in classes:
            classes.add(class_name)

        folder=row['file_name'].partition('/')[0]
        filename=row['file_name'].partition('/')[2].partition('.')[0]
        if path.exists(f'./orientation-estimation/boundingboxes/frames_rgb/{folder}/labels/{filename}.txt'):
            frame_bb_file=open(f'./orientation-estimation/boundingboxes/frames_rgb/{folder}/labels/{filename}.txt')
            frame_bb_lines=frame_bb_file.readlines()

            countPersons = 0
            labelsPerson = set()
            for line in frame_bb_lines:
                if line.partition(' ')[0]=='0':
                    countPersons=countPersons+1
                    labelsPerson.add(line)

            if countPersons==1:
                bb = labelsPerson.pop().partition(' ')[2]
                class_index=labelindex.index(class_name)
                label=f'{class_index} {bb}'

                newfile=open(f'./orientation-estimation/labels/{folder}_{filename}.txt',"x")
                newfile.write(label)
                newfile.close

                amountSuccess=amountSuccess+1
            




if not len(classes)==8:
    exit(1)
print(f'Amount of labels produced: {amountSuccess}')
