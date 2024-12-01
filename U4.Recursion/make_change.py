def make_change_1(coin_denoms,change):#重复计算多，效率很低
	if change in coin_denoms:return 1
	min_coins=float('inf')
	for i in [c for c in coin_denoms if c <=change]:
		num_coins=1+make_change_1(coin_denoms,change-i)
		min_coins=min(num_coins,min_coins)
	return min_coins

def make_change_2(coin_value_list,change,known_results):
	min_coins=change
	if change in coin_value_list:
		known_results[change]=1
		return 1
	elif known_results[change]>0:return known_results[change]
	else:
		for i in [c for c in coin_value_list if c<=change]:
			num_coins=1+make_change_2(coin_value_list,change-i,known_results)
			if num_coins<min_coins:
				min_coins=num_coins
			known_results[change]=min_coins
	return min_coins

def make_change_4(coin_value_list,change,min_coins,coin_used):
	for cents in range(change+1):
		coin_count=cents
		new_coin=1
		for j in [c for c in coin_value_list if c <=cents]:
			if min_coins[cents-j]+1<coin_count:
				coin_count=min_coins[cents-j]+1
				new_coin=j
		min_coins[cents]=coin_count
		coin_used[cents]=new_coin
	return min_coins[change]

def print_coins(coins_uses,change):
	coin=change
	while coin>0:
		this_coin=coins_uses[coin]
		print(this_coin,end=' ')
		coin=coin-this_coin
	print()

if __name__=='__main__':
	#print(make_change_1((1,5,10,25),63))
	#print(make_change_2([1,5,10,25],63,[0]*64))
	amnt=63
	clist=[1,5,10,21,25]
	coins_used=[0]*(amnt+1)
	coin_count=[0]*(amnt+1)

	print('requires the following {} coins'.format(make_change_4(clist,amnt,coin_count,coins_used)))
	print_coins(coins_used,amnt)
	print(coins_used)