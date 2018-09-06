
# # # 
# could make transactions as many as you want to make best profit


def brute_force(arr, start):
  if start >= len(arr):
    return 0
  max_profit = 0
  for i in range(start, len(arr)):
    tmp_max_profit = 0
    for j in range(start+1, len(arr)):
      if arr[j] > arr[i]:
        profit = brute_force(arr, j+1) + arr[j] - arr[i]
        if profit > tmp_max_profit:
          tmp_max_profit = profit
    if tmp_max_profit>max_profit:
      max_profit = tmp_max_profit
  return max_profit

def Peak_Valley(prices):
  valley = prices[0]
  peak  = prices[0]
  idx = 0
  max_profit = 0
  while idx < len(prices)-1:
    while idx < len(prices)-1 and prices[idx+1] <= prices[idx]:
      idx+=1
    vally = prices[idx]
    while idx < len(prices)-1 and prices[idx+1] > prices[idx]:
      idx+=1
    peak = prices[idx]
    max_profit += peak-vally
  return max_profit  

def One_Pass(prices):
  max_profit = 0
  for idx, price in enumerate(prices):
    if idx > 0 and price > prices[idx-1]:
      max_profit += price-prices[idx-1]
  return max_profit
if __name__ == '__main__':
  prices = [7, 1, 5, 3, 6, 4]
  print(One_Pass(prices))