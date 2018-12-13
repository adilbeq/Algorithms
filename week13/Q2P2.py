def brute_force_histogram(text):
    dictionary = {}
    text_arr = text.split(" ")
    for word in text_arr:
         if word in dictionary:
             dictionary[word]+=1
         else:
             dictionary[word]=1
    for key,value in dictionary.items():
        print(key+" : "+str(value))
    
brute_force_histogram("hello worlds smdk smdk df df")
