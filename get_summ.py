"""задание 1 по функциям"""

def get_summ(one,two, delimiter='&'):
  line = str(one) + delimiter + str(two)
  print(line.upper())

c = get_summ('Learn','python')
print(c)