list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = list(zip(list_1, list_2))
print(list_3)

list_2 = list_2[::-1]
list_4 = list(zip(list_1, list_2))
print(list_4)

stocks = ["reliance", "tcs", "apple"]
prices = [1200,1450,2000]
dict_1 = dict(stocks:prices, for stocks, prices in zip(stocks,prices))
