# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:51:20 2020

@author: douzi
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:40:08 2020

@author: douzi
"""
import struct
import math

def readFile(url):
    wds = """2 88 59 83 87 65 38 72 70 76 50 62 4 76 68 70 50 60 13 74 66 60 8 28 97 94 99 52 6 90 69 60 54
83 76 89 64 73 48 69 83 28 84 67 14 50 99 86 35 36 5 82 67 36 92 99 44 27 53 76 24 45 27 19 14
65 86 69 47 80 96 96 10 68 60 91 87 25 15 50 8 18 3 15 85 88 14 8 2 64 63 62 70 58 62 93 51 66
62 73 75 6"""
    with open('./file/file2_2017.txt', 'wb+') as f:
        line = wds.split()
        for i in line:
            elem = struct.pack('i', int(i))
            f.write(elem)
    
    res = []
    with open(url, 'rb+') as f:
        while True:
            data = f.read(8)
            if not data:
                break
            elem = struct.unpack('2i', data)
            res.append(elem)
    return res


def distance(a, target):
    return math.sqrt(math.pow(abs(a[0] - target[0]), 2) + math.pow(abs(a[1] - target[1]), 2))

def density(count, r):
    return count / (r*r*math.pi)

def main():
    points = readFile('./file/file2_2017.txt')
    print(points)
    
#    points = [elem for elem in points if (elem[0] > 0 and elem[1] > 0)]
    
    polen = len(points)
    
    circle = []    # 距离
    # 以每个坐标点为圆心，以 该点 与 其后面第一个点 的欧氏距离为半径 r
    # 计算每个圆包含的坐标点数. 计算 最后一个点 以其和 第一个点 的欧氏距离为半径.
    for i in range(0, polen):
        circle.append(distance(points[i], points[(i+1)%polen]))
    
    # 计算 每个圆 包含的坐标 点数     
    count = [0 for i in range(0, polen)]   # 圆包含的点数
    for i in range(0, polen):
        for j in range(0, polen):
            if (distance(points[i], points[j]) <= circle[i]):
                count[i] += 1
        
    # 求 点密度
    densitys = []
    for i in range(0, polen):
        densitys.append(density(count[i], math.sqrt(circle[i])))
        
    # [points[i], count[i], densitys[i]]
    combine = []
    for i in range(0, polen):
        combine.append([points[i], count[i], densitys[i]])

    combine.sort(key=lambda x:(x[2]), reverse=True)
    for i in range(0, 5):
        print("坐标点:{0}, 包含点数:{1}, 点密度:{2:.2f}".format(combine[i][0], combine[i][1], combine[i][2])) 
    
    
if __name__=='__main__':
    main()
        
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    