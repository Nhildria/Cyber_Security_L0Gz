from ctypes import pointer


plaintext = "No good deed will go unpunished "
key = 8

CypherText = [''] * key

for column in range(key):
    pointer = column

    while pointer < len(plaintext):
        CypherText[column] += plaintext[pointer]
  #      print(CypherText) Prints the loop logic for the Transposition Cypher 
        pointer += key 

print("".join(CypherText))