# Best Time to Buy and Sell Stock

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

def BruteForce(prices):
  max_reward = 0
  for i in range(len(prices)):
    for j in range(i+1,len(prices)):
      max_reward = max(max_reward, prices[j]-prices[i])

  return max_reward

def one_pass(prices):
  min_price = 2**64
  max_reward = 0
  for price in prices:
    if price < min_price:
      min_price = price
    max_reward = max(price - min_price, max_reward)
  return max_reward
if __name__ == '__main__':
  inputs =  [7,1,5,3,6,4]
  print(BruteForce(inputs))
  print(one_pass(inputs))