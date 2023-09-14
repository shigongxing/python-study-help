#!/usr/bin/env python
# encoding: utf-8
'''
@author: rock
@技术交流: QQ+vx: 940947367
@desc:
'''
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor

pd.set_option('display.width', 1000)
train = pd.read_csv('train.csv', encoding='ANSI')
test = train.sample(frac=0.3, replace=False, random_state=1)



print(test.head(5))

# 挑选特征值

selected_features = ['小区房屋出租数量', '楼层', '总楼层', '房屋面积', '卧室数量', '厅的数量', '卫的数量', '区', '地铁线路', '距离', '位置']

class_mapping = {label: idx for idx, label in enumerate(set(train['房屋朝向']))}

X_train = train[selected_features]
X_test = test[selected_features]

Y_train = train['月租金']


# # 补充特征缺失值
Y_train.fillna(0, inplace=True)
X_train['小区房屋出租数量'].fillna(0, inplace=True)
X_train['楼层'].fillna(0, inplace=True)
X_train['总楼层'].fillna(0, inplace=True)
X_train['房屋面积'].fillna(0, inplace=True)
X_train['卧室数量'].fillna(0, inplace=True)
X_train['厅的数量'].fillna(0, inplace=True)
X_train['区'].fillna(0, inplace=True)
X_train['地铁线路'].fillna(0, inplace=True)
X_train['距离'].fillna(0, inplace=True)
X_train['位置'].fillna(0, inplace=True)

X_test['小区房屋出租数量'].fillna(0, inplace=True)
X_test['楼层'].fillna(0, inplace=True)
X_test['总楼层'].fillna(0, inplace=True)
X_test['房屋面积'].fillna(0, inplace=True)
X_test['卧室数量'].fillna(0, inplace=True)
X_test['厅的数量'].fillna(0, inplace=True)
X_test['区'].fillna(0, inplace=True)
X_test['地铁线路'].fillna(0, inplace=True)
X_test['距离'].fillna(0, inplace=True)
X_test['位置'].fillna(0, inplace=True)

# X_train['房屋朝向'] = X_train['房屋朝向'].map(class_mapping)
# X_test['房屋朝向'] = X_test['房屋朝向'].map(class_mapping)
# print(X_train.head(5))


# 3 训练数据和测试数据进行标准化处理
ss_x = StandardScaler()
X_train = ss_x.fit_transform(X_train)
X_test = ss_x.transform(X_test)

# 4 三种集成回归模型进行训练和预测
# 随机森林回归
rfr = RandomForestRegressor()
# 训练
rfr.fit(X_train, Y_train)
# 预测 保存预测结果
rfr_y_predict = rfr.predict(X_test)

# 极端随机森林回归
etr = ExtraTreesRegressor()
# 训练
etr.fit(X_train, Y_train)
# 预测 保存预测结果
etr_y_predict = rfr.predict(X_test)

# 梯度提升回归
gbr = GradientBoostingRegressor()
# 训练
gbr.fit(X_train, Y_train)
# 预测 保存预测结果
gbr_y_predict = gbr.predict(X_test)

Y_test = test['月租金']
#衡量模型拟合度的一个量，是一个比例式，比例区间为[0,1],越接近1，表示模型拟合度越高
print("随机森林回归的R_squared值为：", r2_score(Y_test, rfr_y_predict))
print("极端随机森林回归的R_squared值为：", r2_score(Y_test, etr_y_predict))
print("梯度提升回归回归的R_squared值为：", r2_score(Y_test, gbr_y_predict))

# 输出结果
# rfr_submission = pd.DataFrame({'id': test['id'], 'price': gbr_y_predict})
# rfr_submission = rfr_submission.sort_values(by='id', ascending=True)
# rfr_submission.to_csv('sample.csv', index=False)
# print(rfr_submission.head(5))
