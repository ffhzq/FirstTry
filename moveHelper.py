import os
from shutil import move

CWDPath = os.getcwd()
#print(CWDPath)
DataPath = CWDPath + '\\archive\\'
imagesPath = DataPath + 'images\\'
annotationsPath = DataPath + 'annotations\\'
labelsPath = DataPath + 'labels\\'


trainImgPath = imagesPath + 'Training\\'
trainLabelPath = labelsPath + 'Training\\'
os.makedirs(trainImgPath, exist_ok = True)
os.makedirs(trainLabelPath, exist_ok= True)
#print(trainImgPath)
validationImgPath = imagesPath + 'Validation\\'
validationLabelPath = labelsPath + 'Validation\\'
os.makedirs(validationImgPath, exist_ok = True)
os.makedirs(validationLabelPath, exist_ok= True)

testImgPath = imagesPath + 'Test\\'
testLabelPath = labelsPath + 'Test\\'
os.makedirs(testImgPath, exist_ok = True)
os.makedirs(testLabelPath, exist_ok= True)

mainPath = CWDPath + '\\archive\\labels\\'
trainPath = mainPath +'\\Training'
validPath = mainPath +'\\Validation'
testPath = mainPath + '\\Test'

trainFileName = os.listdir(trainPath)
validFileName = os.listdir(validPath)
testFileName = os.listdir(testPath)

List1 = []
List2 = []
List3 = []

configName = CWDPath + '\\datasetImigration.txt'

f = open(configName,'r')

MList1 = []
MList2 = []
MList3 = []

lines = f.readlines()
t = 0

for line in lines:
    line = line.strip('\n')
    if line == "train":
        t = 1
    elif line == "val":
        t = 2
    elif line == "test":
        t = 3
    else:
        if t==1:
            MList1.append(line)
        elif t==2:
            MList2.append(line)
        elif t==3:
            MList3.append(line)

for name in MList1:
    imageName = f'{name}.png'
    move(imagesPath + imageName, trainImgPath + imageName)

for name in MList2:
    imageName = f'{name}.png'
    labelName = f'{name}.txt'
    move(imagesPath + imageName, validationImgPath + imageName)

for name in MList3:
    imageName = f'{name}.png'
    labelName = f'{name}.txt'
    move(imagesPath + imageName, testImgPath + imageName)