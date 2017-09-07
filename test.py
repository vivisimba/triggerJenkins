# -*- coding: utf-8 -*-
'''
Created on 2017年6月19日

@author: Simba
'''


import os
import shutil


# print os.listdir(r'C:\Users\Administrator\Desktop\desktop_store\newboss-deploy\deploy-mount\boss-services')


def cleanDir(rootDir):
    filelist = os.listdir(rootDir)
    for f in filelist:
        filepath = os.path.join(rootDir, f)
        if os.path.isfile(filepath):
            os.remove(filepath)
            print filepath + " removed!"
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)
            print "dir " + filepath + " removed!"


def getAllDir(rootPath):
    rootDirTempList = os.listdir(rootPath)
    rootDirList = []
    for i in rootDirTempList:
        rootDirList.append(os.path.join(rootPath, i))
    return rootDirList


def clean():
    t = 0
    for j in getAllDir(r'C:\Users\Administrator\Desktop\desktop_store\newboss-deploy\deploy-mount\boss-services'):
        cleanDir(j)
        t += 1
        print t
    

# 获得指定目录下的，指定后缀名的文件名列表
def getWarNameList(warDir, suffix):
    warNameList = []
    tempList = os.listdir(warDir)
    for i in tempList:
        tempFileName = warDir + os.sep + i
        if os.path.isfile(tempFileName) & tempFileName.endswith(suffix):
            warNameList.append(i)
    return warNameList
    

# 获得去掉war包列表中“.war”后缀的列表，返回war包名称列表
def getRealWarNameList(warNameList):
    realWarNameList = []
    for i in warNameList:
        realWarNameList.append(os.path.splitext(i)[0])
    return realWarNameList


# 复制
def copyWar(fromPath, warName, toPath):
    filename1 = os.path.join(fromPath, warName + '.war',)
    filename2 = os.path.join(toPath, warName + '.war',)
    shutil.copy(filename1, filename2)


def copyAll():
    fromPathRoot = r'C:\Users\Administrator\Desktop\desktop_store\newboss-deploy\package'
    warList = getWarNameList(fromPathRoot, '.war')
    warNameList = getRealWarNameList(warList)
    
    failList = []
    t = 0
    for i in warNameList:
        topath = os.path.join(r'C:\Users\Administrator\Desktop\desktop_store\newboss-deploy\deploy-mount\boss-services', i)
        if os.path.exists(topath):
            t += 1
            copyWar(fromPathRoot, i, topath)
            print t
        else:
            failList.append(i)
    for j in failList:
        print "======="
        print j


copyAll()
# clean()


