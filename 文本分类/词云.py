#!/usr/bin/env python
# encoding: utf-8
'''
@author: rock
@技术交流: QQ+vx: 940947367
@desc:
'''
from wordcloud import WordCloud
import cv2
import jieba
from wordcloud import WordCloud, STOPWORDS
textPath = './十五大.txt'
bkpic = 'msk.png'
picName = textPath.replace("txt","jpg")
with open(textPath, 'r',encoding='GB2312') as f:
    text = f.read()
    print(text)
cut_text = " ".join(jieba.cut(text))
color_mask = cv2.imread(bkpic)
cloud = WordCloud(
    # 设置字体，不指定就会出现乱码
    font_path=" ../simkai.ttf",
    # font_path=path.join(d,'simsun.ttc'),
    # 设置背景色
    background_color='white',
    # 词云形状
    mask=color_mask,
    # 允许最大词汇
    max_words=2000,
    # 最大号字体
    max_font_size=40
)
wCloud = cloud.generate(cut_text)
wCloud.to_file(picName)
import matplotlib.pyplot as plt
plt.imshow(wCloud, interpolation='bilinear')
plt.axis('off')
plt.show()


txt = open(textPath, 'r', encoding='GBK').read()

wordsls = jieba.lcut(txt)
wcdict = {}
for word in wordsls:
    if len(word) == 1:
        continue
    else:
        wcdict[word] = wcdict.get(word, 0) + 1
wcls = sorted(wcdict.items(), key=lambda item: item[1], reverse=True)
# print(sorted(wcdict.items(), key=lambda item: item[1], reverse=True))

#打印前25的出现频率最高的词
for i in range(25):
    print(wcls[i])
