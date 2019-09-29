import jqdatasdk
import time
import re

from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

jqdatasdk.auth('15801486884', '221416')

## 兼容聚宽股票代码
def parseStockCode (code):
    regXSHE = r'^(002|000|300|1599|1610)'
    regXSHG = r'^(600|601|603|51)'

    if re.search(regXSHE, code):
        return '.'.join([code, 'XSHE'])
    elif re.search(regXSHG, code):
        return '.'.join([code, 'XSHG'])

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/get_bars')
def get_bars():
	stocks = request.args.get('stocks').split(',')
	date = request.args.get('date')
	data = {}
	query_date = datetime.strptime(date, '%Y-%m-%d')
	total_count = 240
	result = [[] for _ in range(total_count)]
	reply_close = {}
	current_open = {}
	# query_date = '2019-09-24'

	print('stocks => ', stocks)
	print('query_date => ', query_date)

	

	for stock in stocks:
		# print(parseStockCode(stock))
		reply_close[stock] = list(jqdatasdk.get_bars(parseStockCode(stock), 2, unit='1d', fields=['close'], include_now=False, end_dt = query_date, fq_ref_date=None)['close'])[0]
		current_open[stock] = list(jqdatasdk.get_bars(parseStockCode(stock), 1, unit='1d', fields=['open'], include_now=False, end_dt = query_date, fq_ref_date=None)['open'])

		## 获取标的分时图每个点
		stock_bars = list(jqdatasdk.get_bars(parseStockCode(stock), total_count, unit='1m', fields=['close'], include_now=False, end_dt = query_date, fq_ref_date=None)['close'])
		data[stock] = current_open[stock] + stock_bars

	## 统计当日涨幅
	for index in range(0, total_count):
		result[index] = {
			'index': index,
		}

		for stock in data:
			result[index][stock] = round((data[stock][index] - reply_close[stock]) / reply_close[stock] * 100, 2)

	
	print('昨日收盘价')
	print(reply_close)

	print('涨幅')
	print(result)
	return jsonify(result)
	

if __name__ == '__main__':
    app.run()