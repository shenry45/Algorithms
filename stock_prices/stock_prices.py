#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # find first smallest number looping through prices len(prices) - 1
  current_min_price_so_far = prices[0]
  current_max_price_so_far = 0
  
  for numb in range(1, len(prices)):
    # if at last iteration
    if numb == len(prices) - 1:

      # if last numb is bigger than max, replace
      if current_max_price_so_far < prices[numb]:
        current_max_price_so_far = prices[numb]
      
      return current_max_price_so_far - current_min_price_so_far  

    # if minimum is more than next numb
    if current_min_price_so_far > prices[numb]:
      # replace current_min_price_so_far
      current_min_price_so_far = prices[numb]

    # elif current_max_price_so_far < prices[numb + 1]:
    elif current_max_price_so_far < prices[numb]:
      current_max_price_so_far = prices[numb]

  return current_max_price_so_far - current_min_price_so_far


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))