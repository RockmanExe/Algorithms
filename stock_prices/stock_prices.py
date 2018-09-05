#!/usr/bin/python

import argparse

def find_max_profit(prices,n):
  profit=[0]
  max_price=prices[n-1]

  for i in range (n-2, 0, -1):
    if prices[i]>max_price:
      max_price=prices[i]
      profit[i]= max(profit[i+1], max_price-prices[i])
  
  min_price=prices[0]
  for i in range(1,n):
    if price[i]< min_price:
      min_price=prices[i]
    
    profit[i]=max(profit[i-1], profit[i]+(prices[i]-min_price))

  result= profit[n-1]
  return result


if __name__ == '__main__':
  # You can test your implementation by running 
  # `python stock_prices.py [prices]` where prices is comprised of
  # space-separated integer values
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))