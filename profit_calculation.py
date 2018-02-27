import os

#import trade history

def change_acquisition_price(old_price,old_amount,buy_price,buy_amount):
	new_price = (old_price*old_amount + buy_price*buy_amount)/ (old_amount + buy_amount)
	return new_price

#bitflyer
f_history = open('tradehistory.csv','r')

#N_trade = 131
info = f_history.readline()

BTC_acquisition = 0
BTC_amount = 0
BTC_income = 0

ETH_acquisition = 0
ETH_amount = 0
ETH_income = 0

BCH_acquisition = 0
BCH_amount = 0
BCH_income = 0

BTC_get = []
count = 0

data_tmp = [[]]

for line in f_history:
	count += 1
	data_tmp.append(line.split(','))

N_trade = count
print(data_tmp)
print(N_trade)
print(data_tmp[N_trade])
print(len(data_tmp))

#data = [[]]
#for i_trade in range(N_trade):
#	data.append(data_tmp[N_trade- i_trade])
#print(data[1])


for i_trade in range(N_trade):
	data = data_tmp[N_trade - i_trade]
	#print(data)
	BTC = float(data[4])
	JPY = float(data[7])
	ETH =float(data[9])
	BCH = float(data[18])

	rate = float(data[3])
	BTC_fee = float(data[5])
	ETH_fee = float(data[10])
	BCH_fee = float(data[19])

	#fee_ETH = float(data[])
# selling crypto currency
	if JPY > 0:
		if BTC < 0:
			BTC_income += (JPY + BTC_acquisition * BTC - rate * BTC_fee)
		print(i_trade,'sell BTC   income = ',BTC_income, BTC_acquisition)

		#else pattern include deposit(nyuukin)

#buying crypto currency
	#
	
	if JPY < 0:
		if BTC > 0:
			buy_amount = BTC
			buy_price = -JPY / buy_amount

			BTC_acquisition = change_acquisition_price(BTC_acquisition,BTC_amount,buy_price,buy_amount)
			BTC_amount = BTC_amount + buy_amount
			print(i_trade,'JPY -> BTC  BTC_acquisition=',BTC_acquisition)
	
		#else pattern include withdraw(syukkin)
	#print(JPY)

#changing currency to currency
	# BTC -> ETH fee is ETH
	if ETH > 0:
		if BTC < 0 :
			buy_amount = ETH_amount + ETH_fee
			buy_price = rate * (ETH_amount/(ETH_amount+ETH_fee)) * BTC_acquisition # ETH/JPY is not recorded

			#BTC_income += rate * fee_ETH * BTC_acquisition
			BTC_amount += BTC

			ETH_acquisition = change_acquisition_price(ETH_acquisition,ETH_amount,buy_price,buy_amount)
			ETH_amount = ETH_amount + buy_amount
			print(i_trade,'BTC -> ETH  ETH_acquisition=',BTC_acquisition)

	# ETH -> BTC fee is ETH
	if ETH <0 :
		if BTC > 0 :
			buy_amount = BTC
			buy_price = -(ETH + ETH_fee)/BTC * ETH_acquisition

			ETH_amount += ETH + ETH_fee

			BTC_acquisition = change_acquisition_price(BTC_acquisition,BTC_amount,buy_price,buy_amount)
			print(i_trade,'ETH -> BTC  BTC_acquisition=',BTC_acquisition)

	# BCH -> BTC fee is BCH
	if BCH <0 :
		if BTC > 0 :
			buy_amount = BTC
			buy_price = -(BCH + BCH_fee)/BTC * BCH_acquisition

			BCH_amount += BCH + BCH_fee

			BTC_acquisition = change_acquisition_price(BTC_acquisition,BTC_amount,buy_price,buy_amount)

			print(i_trade,'BCH -> BTC  BTC_acquisition=',BTC_acquisition)

#emerge BTC
	if BTC > 0 and ETH == 0 and BCH == 0 and JPY == 0:
		buy_amount = BTC
		buy_price = 0

		BTC_acquisition = change_acquisition_price(BTC_acquisition,BTC_amount,buy_price,buy_amount)
		BTC_amount = BTC_amount + buy_amount

		print(i_trade,'BTC service  BTC_acquisition=',BTC_acquisition)

#emerge BCH
	if BCH > 0 and ETH == 0 and BTC == 0 and JPY == 0:
		buy_amount = BCH
		buy_price = 0

		BCH_acquisition = change_acquisition_price(BCH_acquisition,BCH_amount,buy_price,buy_amount)
		BCH_amount = BCH_amount + buy_amount

		print(i_trade,'BCH service  BCH_acquisition=',BCH_acquisition)

#send BTC
	if BTC < 0 and ETH == 0 and BCH == 0 and JPY == 0:
		BTC_amount += BTC
		print(i_trade,'send BTC  amount=',BTC)

