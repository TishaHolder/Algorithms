import argparse

def find_max_profit(prices):
 
  max_profit_so_far = 0
  max_profit = -9999999

  smallest_value_so_far = prices[0]
  smallest_value = prices[0]
  smallest_index = 0

  #using python's built in function to find the minum number in the list and it's index
  """smallest_value = min(prices)
     smallest_value_index = prices.index(min(prices))"""

  
  #len(prices) - 1 because the last value is not counted as a smallest value
  #because a larger number must come after the smallest value to calculate the max profit
  #usually a for loop to find the minimum number in a list must iterate 1 past the last index or len(prices)
  for p in range(0, len(prices)-1):
    if prices[p] <= smallest_value:
       smallest_value = prices[p]   
       smallest_index = p

  for p in range(0, len(prices)-1):
    if prices[p] > smallest_value and p > smallest_index:
      max_profit_so_far = prices[p] - smallest_value       

    if max_profit_so_far > max_profit:
       max_profit = max_profit_so_far      

  print("smallest value %d" %(smallest_value))  
  print("smallest index %d" %(smallest_index))
  print("max profit %d" %(max_profit))

  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
       

