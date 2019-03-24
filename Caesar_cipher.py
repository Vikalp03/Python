#Python code to implement Caesar Cipher

message=input()
key=int(input())
LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
translated=''
p=''
message=message.upper()

#encryption part begin
print("Encryption  is -")   
for symbol in message:
	if symbol in LETTERS:
		num=LETTERS.find(symbol)
		num=num +key
		if num>=len(LETTERS):
			num=num-len(LETTERS)
		elif num<0:
			num=num+len(LETTERS)
		translated=translated+LETTERS[num]
	else:
		translated=translated+symbol
print(translated)

#decryption part begin
print("Decryption is - ")         
for symbol in translated:
  if symbol in LETTERS:
    num=LETTERS.find(symbol)
    num=num-key
    if num>=len(LETTERS):
      num=num-len(LETTERS)
    elif num<0:
      num=num+len(LETTERS)
    p=p+LETTERS[num]
  else:
    p=p+symbol
print(p)
        
        

