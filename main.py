#Print characters from a string that are present at an even index number.

def reverse_string(message):
  even_index=[]
  for i in range(len(message)):
    if i%2==0:
     even_index+=message[i]

  return even_index


message = input('Enter any string:')
print(f'Characters present at even index number are:{reverse_string(message)}')


