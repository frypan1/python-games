import random
original_no = str(random.randint(100,999))
for i in range(len(original_no)):
  temp = original_no[i]
  for j in range(i+1,len(original_no)):
    if temp == original_no[j]:
      original_no = str(random.randint(100,999))

print(original_no)

def result(guess_no,original_no):
  fermi = [i for i in range(len(guess_no)) if guess_no[i]==original_no[i]]
  pico = [i for i in range(len(guess_no)) if guess_no[i] in original_no and i not in fermi]
  print("Fermi"*len(guess_no) if guess_no == original_no else "Fermi"*len(fermi),"Pico"*len(pico) if  len(fermi)!=0 or len(pico)!=0 else "Bagels")

for i in range(20):
  guess_no = input("Your guess or 'g' to give up: ")
  if guess_no == 'g':
    print(original_no)
    break
  result(guess_no,original_no)
