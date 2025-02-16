#loop

for i in range(0, 10):
    print(i)

name = "Muhammad"

for i in name:
    print(i)

for i,v in enumerate(name):
    print(i,v)

#While loop

#string

text = "Salam my name is Muhammad"

print(len(text))
print(text.count("a"))
print(text.upper())
print(text.lower())
print(text.replace("Muhammad", "Abdul Hakeem"))
print(text.split(" "))
chunks = text.split(" ")
print(chunks)
name = " ".join(chunks)
print(name)

#To check if a word exists?

print("Salam" in name)
