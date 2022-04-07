import pymysql
import pandas


class FLASK_DATA(object):
    def mysql_data(self, sql):
        db = pymysql.connect('localhost', 'root', '000000', 'python_data')  # 连接数据库
        cusor = db.cursor()  # 通过获取到的数据库连接db下的cursor()方法来创建游标
        cusor.execute(sql)
        data = pandas.DataFrame(list(cusor.fetchall()))  # 转换为DataFrame
        return data

    def flask_1(self):  # 玫瑰图
        sql = "SELECT shape,avg(counts) as count FROM pymysql_data GROUP BY shape ORDER BY count desc;"  # 查询相对应都数据表
        data = self.mysql_data(sql)
        count = data[1].sum()  # 将第二列的数值相加
        lists, data_coun = ['方形', '圆形', '异形', '猫眼形', '椭圆形', '其它', '蝶形'], []
        for i in lists:
            datas = data[data[0].isin([i])]  # 匹配每一个id
            data_coun.append("{value: " + '%.1f' % (datas[1].sum() / count * 100) + ", name: '" + i + "'}")
        data_coun = str(data_coun).replace('"', '')
        return data[0].to_list(), data_coun

    def flask_2(self):  # 雷达图
        sql = "SELECT timeto,avg(counts),avg(price) FROM pymysql_data GROUP BY timeto;"  # 查询相对应都数据表
        data = self.mysql_data(sql)
        title = ['2017', '2018', '2019', '2020', '往季']
        list1, list2 = [], []
        for i in title:
            datas = data.loc[data[0].str.contains(i)]
            list1.append('%.1f' % (datas[1].mean()))
            list2.append('%.1f' % (datas[2].mean()))
        return list1, list2

    def flask_3(self):  # 漏斗图#
        sql = "SELECT plastic,avg(counts) FROM pymysql_data GROUP BY plastic;"  # 查询相对应都数据表
        data = self.mysql_data(sql)
        lists = list(data[0])
        total = data[1].sum()
        counts, data_list = [], []
        for i in range(len(lists)):
            counts.append('%.1f' % (data[1].iloc[i] / total * 100))
        for j, i in enumerate(counts):
            data_list.append("{value: " + str(i) + ",name:'" + lists[j] + "'}")
        data_list = (str(data_list).replace('"', ''))
        return lists, data_list

    def flask_4(self):  # 柱状图
        sql = "SELECT brand,avg(counts) as count,avg(price),count(brand) FROM pymysql_data  GROUP BY brand ORDER BY count desc LIMIT 40;"  # 查询相对应都数据表
        data = self.mysql_data(sql)
        data2 = list(map(lambda x: int(x), data[1].to_list()))
        data3 = list(map(lambda x: int(x), data[2].to_list()))
        return data[0].to_list(), data2, data3

    def flask_5(self):  # 折线图
        sql = "SELECT frame,avg(counts) FROM pymysql_data WHERE timeto like '%2019%' GROUP BY frame;"  # 查询相对应都数据表
        data = self.mysql_data(sql)
        title_data = data[0].to_list()
        list1, list2 = [], []
        for i in title_data:
            datas = data.loc[data[0].str.contains(i)]
            list1.append('%.1f' % datas[1].mean())
        sql = "SELECT frame,avg(counts) FROM pymysql_data WHERE timeto like '%2020%' GROUP BY frame;"  # 查询相对应都数据表
        data = self.mysql_data(sql)
        title_data = data[0].to_list()
        for i in title_data:
            datas = data.loc[data[0].str.contains(i)]
            list2.append('%.1f' % datas[1].mean())
        return title_data, list1, list2

    def flask_6(self):  # 散点图
        sql = "SELECT avg(price),avg(counts),frame FROM pymysql_data GROUP BY frame;"  # 查询相对应都数据表
        data = self.mysql_data(sql)
        lists, list_data = data[2].to_list(), []
        for i in lists:
            datas = data.loc[data[2].str.contains(i),]
            list_data.append(
                [float('%.1f' % datas[0].astype("float").mean()), float('%.1f' % datas[1].astype("float").mean()),
                 20, i])
        return list_data

    def flask_7(self):  # 条形图
        sql = "SELECT border FROM pymysql_data GROUP BY border;"  # 查询相对应都数据表
        data = self.mysql_data(sql)
        title_data = data[0].to_list()
        data_list = []
        for i in title_data:
            sql = "SELECT count(gender),gender FROM pymysql_data WHERE border='%s' GROUP BY gender;" % i
            data = self.mysql_data(sql)
            data_list.append(data[0].to_list())
        datas1, datas2, datas3 = [], [], []
        for i in range(4):
            datas1.append(data_list[i][0])
            datas2.append(data_list[i][1])
            datas3.append(data_list[i][2])
        return title_data, [datas1, datas2, datas3]

    def flask_8(self):  # 金字塔图
        sql = "SELECT functions,count(functions) FROM pymysql_data GROUP BY functions;"  # 查询相对应都数据表
        data = self.mysql_data(sql)
        lists, counts, data_list = ['防眩光', '防辐射', '变色片', '防蓝光', '防紫外线', '其它'], [], []
        total = data[1].sum()
        for i in lists:
            datas = data.loc[data[0].str.contains(i)]
            counts.append('%.1f' % (datas[1].sum() / total * 100))
        for j, i in enumerate(counts):
            data_list.append("{value: " + str(i) + ",name:'" + lists[j] + "'}")
        data_list = (str(data_list).replace('"', ''))
        return lists, data_list

    def flask_9(self):  # 饼图2
        sql = "SELECT border,avg(counts) FROM pymysql_data GROUP BY border;"  # 查询相对应都数据表
        data = self.mysql_data(sql)
        count = data[1].sum()
        data_coun = []
        for i in data[0]:
            datas = data.loc[data[0].str.contains(i)]
            data_coun.append("{value: " + '%.1f' % (datas[1].sum() / count * 100) + ", name: '" + i + "'}")
        data_coun = str(data_coun).replace('"', '')
        data_lists = list(map(lambda x: x, data[0].to_list()))
        return data_lists, data_coun

    def flask_10(self):  # 折线图2
        sql = "SELECT timeto,avg(counts),avg(price) FROM pymysql_data GROUP BY timeto;"  # 查询相对应都数据表
        data = self.mysql_data(sql)
        price_data, counts = [], []
        listst = data[0].to_list()
        for i in listst:
            datas = data.loc[data[0].str.contains(i)]
            price_data.append(datas[1].mean())
            counts.append(datas[2].mean())
        price_data = (list(map(lambda x: '%.1f' % x, price_data)))
        counts = (list(map(lambda x: '%.1f' % x, counts)))
        return listst, counts, price_data
