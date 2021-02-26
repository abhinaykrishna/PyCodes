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

def is_consective(str1,str2):
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
      if is_consective(i[0],i[1]):
        count+=1
        result.append(i)
  
  print("There are {} Consecutive words - {}".format(count,result))

# Time Complexity = O(n)

count_consecutive("Abbrevation denoting the senate and people of Rome")


def twin_primes(number):
    prime_numbers = []
    output = '2'
    for num in range(2, number + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)

    for i in range(len(prime_numbers)-1):
        if prime_numbers[i+1] - prime_numbers[i] == 2:
            output+= str(prime_numbers[i])+":"+str(prime_numbers[i+1])+","
    
    if len(output) == 0:
        return 0
    else:    
        return output[0:len(output)-1]

# user_input = int(input("Enter a number\n"))
# print(twin_primes(user_input))


from collections import OrderedDict

def validate_string(inputstring):
    list_converter = inputstring.split(',')
    first,second,third = OrderedDict.fromkeys(list_converter[0], 0), OrderedDict.fromkeys(list_converter[1], 0), OrderedDict.fromkeys(list_converter[2], 0)
    source_index = []
    for ch in list_converter[0]:
        first[ch]+=1
    for ch in list_converter[1]:
        second[ch]+=1
    for ch in list_converter[2]:
        third[ch]+=1
    print(first)
    print(second)
    print(third)
    print((list_converter))
    # print(third.keys())
    #print(first.get('XS'))
    for ch in list_converter[2]:
        if first.get(ch,0) + second.get(ch,0) >= third[ch]:
            if (ch in list_converter[0]) and (ch in list_converter[1]):
                if list_converter[0].index(ch) > list_converter[1].index(ch):
                    source_index.append(list_converter[0].index(ch))
                else:
                    source_index.append(list_converter[1].index(ch))
            elif ch in list_converter[0]:
                source_index.append(list_converter[0].index(ch))
            elif ch in list_converter[1]:
                source_index.append(list_converter[1].index(ch))
            else:
                print("character "+str(ch)+" not found in string1 & string2")
                break
        else:
            return 0
    print(source_index)
    if sorted(source_index) == source_index :
        return 1
    else:
        return 0

sample_inputs = ["rkpesh#@,mdn,rmde#@","rkpesh#@,mdn,rdme#@","rkpesh,mdn","exAmpLe,Template,temperature"]

#print(validate_string(sample_inputs[3]))


def DNA_Transcription(inp):
    output = ''
    dna_dict = {"G":"C","C":"G","T":"A","A":"U"}
    for i in inp:
        if i in dna_dict.keys():
            output+=dna_dict[i]
        else:
          return "Invalid Input"
    return output

print(DNA_Transcription("T"))


name = input('')
d = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
result = ''
for _ in name:
    if _ not in d:
        result = 'Invalid Input'
        break
    else:
        result = result + d.get(_)
print(result)
