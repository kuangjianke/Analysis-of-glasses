from flask_dome import Flask, render_template
from tanshiji.flask_data.flask_total import *

flask = FLASK_DATA()
app = Flask(__name__)


@app.route('/1')  # 玫瑰图
def flasks_1():
    return render_template('玫瑰图.html', lists=flask.flask_1()[0], data_coun=flask.flask_1()[1])


@app.route('/2')  # 雷达图
def flasks_2():
    return render_template('雷达图.html', counts=flask.flask_2()[0], price_list=flask.flask_2()[1])


@app.route('/3')  # 漏斗图
def flasks_3():
    return render_template('漏斗图.html', lists=flask.flask_3()[0], data_list=flask.flask_3()[1])


@app.route('/4')  # 柱状图和折线图
def flasks_4():
    return render_template('柱状图和折线图.html', data1=flask.flask_4()[0], data2=flask.flask_4()[1],
                           data3=flask.flask_4()[2])


@app.route('/5')  # 折线图
def flasks_5():
    return render_template('折线图.html', lists=flask.flask_5()[0], list1=flask.flask_5()[1], list2=flask.flask_5()[2])


@app.route('/6')  # 散点图
def flasks_6():
    return render_template('散点图.html', list_data=flask.flask_6())


@app.route('/7')  # 柱状图
def flasks_7():
    return render_template('柱状图.html', lists=flask.flask_7()[0], counts=flask.flask_7()[1])


@app.route('/8')  # 金字塔图
def flasks_8():
    return render_template('金字塔图.html', lists=flask.flask_8()[0], data_list=flask.flask_8()[1])


@app.route('/9')  # 饼图
def flasks_9():
    return render_template('饼图2.html', lists=flask.flask_9()[0], data_coun=flask.flask_9()[1])


@app.route('/10')  # 折线图2
def flasks_10():
    return render_template('折线图2.html', lists=flask.flask_10()[0], counts=flask.flask_10()[1],
                           price_data=flask.flask_10()[2])


if __name__ == '__main__':
    app.run(debug=True)
