class KeyValue:
	def __init__(self,key,value):
		self.key=key
		self.value=value


class HashTable:
	def __init__(self):
    	self.list=[]

        def hash(n):
            h = 0
            for i in n:
                h = h + ord(i)
            return h % 1000
        	
	def get(self,key):
		for item in self.list:
			if item.key == key:
				return item.value
				break
		return "not found"
	
	def set(self,key,value):
		keyValue = KeyValue(key,value)
		self.list.append(keyValue)
    
