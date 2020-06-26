"""part of a challenge of translating words into "pig latin" by taking the first letter of a sentence
then placing it behind the following letters with an extra "ay" at the end """

speak = input("say sumtin: ")
slit = speak.split()
x = 0  #list number


while x <= len(slit) - 1:
    take_out = slit[x].translate({ord(slit[x][0]): None})
    add_in = take_out + slit[x][0] + "ay"
    final_product = slit[x].replace(slit[x], add_in)
    slit[x] = final_product
    x += 1

sentence_join = " ".join(slit)
print(sentence_join)






