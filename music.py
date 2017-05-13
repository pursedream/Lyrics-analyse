import xlrd
import jieba
import numpy
import codecs
import pandas

file = codecs.open("C:\\Users\dreamboy\Desktop\薛之谦.txt",'r','utf-8')
# 中文utf-8读写
content = file.read()
file.close()
segments = []
# segs = jieba.lcut(content)
segs = jieba.cut(content, cut_all=False);
# 使用精确模式进行分词
for seg in segs:
    if len(seg) > 1:
        segments.append(seg)

segmentDF = pandas.DataFrame({'segment':segments})
# 生成一个DataFrame

df = segmentDF.groupby("segment")["segment"].agg({"计数": numpy.size}).sort_values( ['计数'],ascending = False)
# 进行汇总计数并从小往大计数
# https://my.oschina.net/lionets/blog/280332
# print(df.head(100))
df.to_excel('薛之谦歌词-分词.xls', sheet_name='sheet1')
