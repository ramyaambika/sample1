char = input("Enter a character: ")
if char=='0':
  exit
else:
  if((char>='a' and char<= 'z') or (char>='A' and char<='Z')):
     print(char, " Alphabet")
  else:
     print(char, "is not an Alphabet")
