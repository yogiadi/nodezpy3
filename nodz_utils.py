import os
import json
import re
from PySide2 import QtCore , QtGui

def _convertDataToColor(data=None, alternate=False, av=20):
    if len(data) == 3:
        color = QtGui.QColor(data[0],data[1],data[2])
        if alternate:
            mult = _generateAlternateColorMultiplier(color, av)
            color = QtGui.QColor(max(0, data[0]-(av*mult)), max(0, data[1]-(av*mult)), max(0, data[2]-(av*mult)))
            return color
        elif len(data) == 4:
            color = QtGui.QColor(data[0], data[1], data[2], data[3])
            if alternate:
                mult = _generateAlternateColorMultiplier(color, av)
                color = QtGui.QColor(max(0, data[0] - (av * mult)), max(0, data[1] - (av * mult)),
                                     max(0, data[2] - (av * mult)), data[3])
            return color
        else:
            print('Color from configuation is not recognised:',data)
            print('Can only be [R,G,B] or [R,G,B,A]')
            print('Using default color!')
            color = QtGui.color(120,120,120)
            if alternate :
                color = QtGui.Qcolor(120-av,120-av,120-av)
            return color
def _generateAlternateColorMultiplier(color, av):
    lightness = color.lightness()
    mult = float(lightness)/255
    return mult
def _createPointerBoundingBox(pointerPos,bbSize):
    point = pointerPos
    mbbPos= point
    point.setX(point.x()-bbSize/2)
    point.setY(point.y()-bbSize/2)
    size=QtCore.QSize(bbSize,bbSize)
    bb = QtCore.QRect(mbbPos,size)
    bb = QtCore.QRectF(bb)
    return bb
def _swapListIndices(inputList,oldIndex,newIndex):
    if oldIndex == -1:
        oldIndex = len(inputList)-1
    if newIndex == -1:
        newIndex = len(inputList)
    value = inputList[oldIndex]
    inputList.pop(oldIndex)
    inputList.insert(newIndex,value)
def _loadConfig(filePath):
    with open(filePath,'r') as myfile:
        fileString=myfile.read()
        cleanString = re.sub('//.*?\n|/\*.*?\*/','',fileString,re.S)
        data = json.loads(cleanString)
        return data
def _saveData(filePath,data):
    f = open(filePath,"w")
    f.write(json.dumps(data,sort_keys=True,indent=4,ensure_ascii=False))
    f.close()
    print("Data successfully saved!")
def _loadData(filePath):
    with open(filePath) as json_file:
        j_data=json.load(json_file)
        json_file.close()
    print('Data successfully loaded')
    return j_data