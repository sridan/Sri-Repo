#Print characters from a string that are present at an even index number.
def return_characters(message):
  even_index = []
  
  for i in range(len(message)):
    
    if i%2 == 0:
     even_index += message[i]

  return even_index

message = input('Enter any string:')
print(f'Characters present at even index number are:{return_characters(message)}')
#Print the length of the string.
print(f'The length of the string is:{len(message)}')