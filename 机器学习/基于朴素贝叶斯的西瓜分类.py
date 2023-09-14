import pandas as pd
'''
@author: rock
@技术交流: QQ+vx: 940947367
@desc:
'''

# 计算好瓜和坏瓜的先验概率，即P(‘好瓜’)和P(‘坏瓜’)
def Y_prob(Y):
    y = Y.values
    # 请在此处填写代码，计算好瓜的先验概率
    true_prob = sum(y)/len(y)

    return {0: 1 - true_prob, 1: true_prob}


# 计算好瓜和坏瓜各特征属性的条件概率，即求p(特征|类别)
# 传入参数：特征数据, 分类数据，用字典的形式存储返回
def x_y_prob(feature, y):
    # 创建空字典，存储条件概率
    x_y = {}
    # 循环处理每个特征
    for f in feature.columns:
        # 获取特征的list
        for i in feature[f].value_counts().keys():
            index_True = y[y == True].index
            index_False = y[y == False].index

            # 提示：可以使用loc索引，参数1为行索引，参数2为列索引
            # 请在此处填写代码，计算好瓜和坏瓜的条件概率
            sample_True = data.loc[index_True, f] == i
            prob_true = len(sample_True.loc[sample_True == True]) / len(index_True)
            strings_True = str(f) + '=' + str(i) + '|' + 'y=1'

            sample_False = data.loc[index_False, f] == i
            prob_False = len(sample_False.loc[sample_False == True]) / len(index_False)
            strings_False = str(f) + '=' + str(i) + '|' + 'y=0'

            x_y[strings_True] = prob_true
            x_y[strings_False] = prob_False
    return x_y


if __name__ == '__main__':
    # 读取数据集
    data = pd.read_csv('dataset.csv')
    print(data)
    feature = data.columns.values[:-1]
    print(data[feature])

    x_y = x_y_prob(data[feature], data['好瓜'])  # 用字典存储p(特征|类别)
    y_prob = Y_prob(data['好瓜'])

    # 测试数据
    test_data = ['青绿', '蜷缩', '沉闷', '稍糊', '凹陷', '硬滑']

    # 将测试数据转化为字典可以搜索的格式
    test_true = [str(feature[i]) + '=' + str(test_data[i]) + '|' + 'y=1' for i in range(len(feature))]
    test_false = [str(feature[i]) + '=' + str(test_data[i]) + '|' + 'y=0' for i in range(len(feature))]
    p_true = y_prob[1]
    p_false = y_prob[0]

    # 计算每一类的概率，即朴素贝叶斯判别公式
    for i in range(len(feature)):
        p_true *= x_y[test_true[i]]
        p_false *= x_y[test_false[i]]

    print('待分类西瓜特征为{}'.format(test_data))
    print('好瓜概率：{:.8f}，坏瓜概率：{:.8f}'.format(p_true, p_false))
    print('西瓜分类模型预测结果：' + '好瓜' if p_true > p_false else '坏瓜')


