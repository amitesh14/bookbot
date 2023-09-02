with open("books/frankenstein.txt") as f:
    file_contents = f.read()
def number_words():
    words=file_contents.split()
    w1=len(words)
    return w1 

def number_character():
    count=0
    dict={}
    for i in file_contents:
        if(i!=' '):
            i=i.lower()
            if(  i in dict.keys()):
                dict[i]=dict.get(i)+1
            elif(i.isalpha()):
                dict.update({i:1})
    return dict

print("------------------------------Begning of report--------------------------------------------------")
print(f"the number of words in the book is {number_words()}")
print()
p=number_character()
myKeys = list(p.keys())
myKeys.sort()
sorted_dict = {i: p[i] for i in myKeys}

for i in sorted_dict.keys():
            print(f"the {i} was found {sorted_dict.get(i)} times")
print("----------------------------------end of rerport---------------------------------------------------")            
