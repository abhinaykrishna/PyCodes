# Write a python function, encrypt_sentence(msg) which accepts a message and encrypts it based on rules given below and returns the encrypted message.
# Words at odd position -> Reverse It
# Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change
# Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
# Perform case sensitive string operations wherever necessary.
# Example: msg=the sun rises in the east    
# output=eht snu sesir ni eht stea

def encrypt_sentence(msg):
  pass

# Write a Python program to find the number of characters present the given string.

def count_char(sentence):
  print(len(sentence))

count_char("Python Programming")

# Write a Python program to find the numbers of words present in the given sentence.

def count_words(sentence):
  convert_to_list = sentence.split(" ")
  print("No of words in the sentence are : ",len(convert_to_list))

line = "I'm a fan of Cristiano Ronaldo , He plays for Portugal"
count_words(line)

# Write a Python function words_count(sentence) to return a dictionary with the length of words as key and number words with such length as value.
# Example: sentence=“I love python and it so easy to learn” sample output={1:1,4:2,5:1,3:1,2:3,6:1}

def words_count(sentence):
  convert_to_list = sentence.split(" ")
  result = {}
  for i in convert_to_list:
    if len(i) in result.keys():
      result[len(i)] += 1
    else:
      result[len(i)] = 1
  print(result)

sentence = "I love python and it so easy to learn"

words_count(sentence)

# Write a Python function vowel_count(sentence) to return a dictionary with vowels, consonants, others as key and respective number of vowels, consonants, others characters as value.
# Note: Do case insensitive operations
# Example: sentence=“I love python and it so easy to learn”
# sample output={“vowels”:12,”consonants”:17, “others”:8}

import string

vowels = "aeiouAEIOU"
alphabets_lower_upper = string.ascii_letters

def vowel_count(sentence):
  dictionary = {"vowels":0, "consonants":0, "others": 0}
  for i in sentence:
    if i in vowels:
      dictionary["vowels"]+=1
    elif i in alphabets_lower_upper:
      dictionary["consonants"]+=1
    else:
      dictionary["others"]+=1
  
  print( dictionary)

sentence = "I love python and it so easy to learn"

vowel_count(sentence)


# Helpful string module features:
#                 ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#     ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     digits = '0123456789'
#     hexdigits = '0123456789abcdefABCDEF'
#     octdigits = '01234567'
#     printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
#     punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#     whitespace = ' \t\n\r\x0b\x0c'