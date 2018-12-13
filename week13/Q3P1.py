def find_key(text,key):
    array=[]
    counter = 0
    for word in text.split(" "):
         if key in word:
             array.append(word)
        
    print(array)

find_key("This is text and it has key word is",'is')
