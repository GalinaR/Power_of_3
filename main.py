def is_power_of_three(number):
  """
  The function determines if the passed number is a natural power of 3.
  """
  n = 0 
  # n is a power of 3
  while 3**n <= number:
    if 3**n == number:
      return True
    n += 1
  return False
