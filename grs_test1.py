# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from grs import BestFourPoint
from grs import Stock

stock = Stock('2618')
result = BestFourPoint(stock)
print result.best_four_point_to_buy()       # 判斷是否為四大買點
print result.best_four_point_to_sell()      # 判斷是否為四大賣點
print result.best_four_point()              # 綜合判斷