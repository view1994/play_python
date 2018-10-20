# -*- coding: utf-8 -*-
#
import time
def maxArea1( height):
    """
    :type height: List[int]
    :rtype: int
    """
    area = 0
    h = 0
    while (height):
        h_l = height.pop()
        if h_l < h:
            continue
        if height:
            if min(height) >= h_l:
                area = area if area > h_l * len(height) else h_l * len(height)
                continue
        else:
            continue
        w_l = len(height)
        for i in range(len(height)):
            if h > height[i]:
                continue
            h = h_l if h_l < height[i] else height[i]
            w = w_l - i
            area = area if area > h * w else h * w
    return area

def maxArea( height):
    area = 0
    while len(height) - 1:
        n1 = height.pop(0)
        n2 = height.pop(-1)
        if n1 < n2:
            temp = n1 * (len(height) + 1)
            height.append(n2)
        else:
            temp = n2 * (len(height) + 1)
            height.insert(0, n1)
        area = area if area > temp else temp
    else:
        return area

def main():
    li=[i for i in range(15000,0,-1)]
    print(li)
    t=time.time()
    print(maxArea(li))
    print(time.time()-t)


if __name__ == '__main__':
    main()