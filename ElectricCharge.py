#coding utf-8
#
import numpy as np
import matplotlib.pyplot as plt
class EleData(object):
    num_count=0
    def __init__(self,month,date,record):
        self.month=month
        self.date=date
        self.record=record
        EleData.num_count+=1
    def __del__(self):
        EleData.num_count-=1
#定义函数来显示柱状上的数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()-0.2, 1.002*height, '%s' % float(height))

def main():
    x=[]
    y=[]
    r=[]
    data = {'6.4': 394.5, '6.6': 375.33, '6.7': 366.4, '6.8': 357.06,
            '6.10': 347.06, '6.11': 344, '6.12': 342, '6.13': 339.04,
            '6.14': 336.21, '6.15': 332.61, '6.16': 330.25, '6.17': 329.69,
            '6.18': 325.62, '6.19':319.01, '6.20':310.46, '6.21':301.45,
            '6.22':294.89, '6.23':292.21, '6.24':286.8, '6.25':286.29,
            '6.26':285.11, '6.27':284.03, '6.28':281.35, '6.29':280,
            '6.30':279}
    data_set=[]
    for i in data:
        d={'month':int(i.split('.')[-2]),'date':int(i.split('.')[-1]),
           'rest':data[i]}
        data_set.append(d)
    data_set.sort(key=lambda x:x['date'])
    #print(data_set)
    for i in range(len(data_set)):
            if i==0:
                data_set[i]['cost_per_day']=0
            else:
                data_set[i]['cost_per_day'] =round((data_set[i-1]['rest']-data_set[i]['rest'])/(data_set[i]['date']-data_set[i-1]['date']),2)
                y.append(data_set[i]['cost_per_day'])
                x.append(data_set[i]['date'])
                r.append(data_set[i]['rest'])
    '''
    # plt.xticks(x, x_1,rotation=0)
    fig, left_axis = plt.subplots()

    p1, = left_axis.bar(x, y, 'ro-')
    right_axis = left_axis.twinx()
    p2, = right_axis.plot(x, r, 'bo-')
    plt.xticks(x, x, rotation=0)  # 设置x轴的显示形式

    # 设置左坐标轴以及右坐标轴的范围、精度
    left_axis.set_ylim(0, 10)
    left_axis.set_yticks(np.arange(0, 10, 1))
    right_axis.set_ylim(0, 400)
    right_axis.set_yticks(np.arange(0, 400, 100))

    # 设置坐标及标题的大小、颜色
    left_axis.set_title('RealAndSimulation-Iter6600')
    left_axis.set_xlabel('Labels')
    left_axis.set_ylabel('Number of training sets',  color='r')
    left_axis.tick_params(axis='y', colors='r')
    right_axis.set_ylabel('Accuracy',  color='b')
    right_axis.tick_params(axis='y', colors='b')
    plt.show()
'''
    #print(data_set)
        # X轴，Y轴数据

    #fig, ax1 = plt.subplots()
    fig = plt.figure()  # 创建绘图对象
    ax1 = plt.bar(x , y , width=0.8)      #画柱状图
    autolabel(ax1)
    #plt.show()  # 显示图#柱状图上添加数值
    #ax1.legend(loc=1)
    #ax2 = ax1.twinx()  # this is the important function
    #ax2 = fig.subplots()
    #ax2 = plt.plot(x, r, "b--", linewidth=1)  #画折线图 在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
    #ax2.set_ylim(0, 400)
    #ax2.legend(loc=2)

    plt.xlabel("date(D)")  # X轴标签
    plt.ylabel("eCharge(RMB)")  # Y轴标签
    plt.title("Electric Charge of 1102 in June")  # 图标题
    plt.show()  # 显示图
    plt.savefig("ElectricChargeOf1102inJune.jpg")  # 保存图

 ###########################################


if __name__ == '__main__':
    main()