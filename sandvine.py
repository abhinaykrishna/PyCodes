def count_ones(n):
  count = 0
  for i in range(n+1):
    k = str(i)
    for j in range(len(k)):
      if k[j] == "1":
        count+=1

  print(count)

count_ones(100)

def convert_roman(roman):
  result = 0
  my_dict = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
  for i in roman:
    if i in my_dict.keys():
      result+= my_dict[i]

  print(result)

convert_roman("MCDXLIV")





import string
source = string.ascii_lowercase

def s_func(str1,str2):
  if source.index(str2) - source.index(str1) == 1:
    return True
  else:
    return False

def count_consecutive(str):
  count = 0 
  result = [] 
  convert_lower = str.lower()
  my_list = convert_lower.split(" ")
  for i in my_list[:2]:
      if s_func(i[0],i[1]):
        count+=1
        result.append(i)
  
  print("There are {} Consecutive words - {}".format(count,result))

# Time Complexity = O(n)

count_consecutive("Abbrevation denoting the senate and people of Rome")