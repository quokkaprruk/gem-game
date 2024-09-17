#    Main Author(s): Siripa Purinruk
#    Main Reviewer(s): Anthony Sin, Sayeda Insha Fatima Zaidi

class HashTable:

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice as long as it is a hash table

	# Purpose: Initialize the table
	# Parameters:
	# 1. cap: capacity of the table
	# Return Value: None
	# Limitations: None
	def __init__(self, cap=32):
		self.cap = cap
		self.size = 0
		self.table = [None]*self.cap
		self.tombstone = False

    # Purpose: Resize the table when the load factor exceeds 0.7
    # Parameters: None
    # Return Value: None
	# Limitations: None
	def resize(self):
		old_table = self.table
		self.cap *= 2
		self.table = [None]*self.cap
		self.size = 0

		for item in (old_table):
			if item is not None and item is not self.tombstone:
				self.insert(item[0],item[1])

    # Purpose: Insert a key-value pair into the table
    # Parameters:
    # 1. key: the key to be inserted
    # 2. value: the value associated with the key
    # Return Value: True if the pair was inserted, False if the key already exists
	# Limitations: can lead to clustering easily because linear probing places consecutive keys in contiguous slots.
	def insert(self, key, value):
		# If a record with matching key already exists in the table, the function does not add the new key-value pair and returns False.
		# Otherwise, function adds the new key-value pair into the table and returns True. 			
		#  When an insertion causes the HashTable's load factor to exceed 0.7, 
		#  the list used to store the table must be resized.
		index = hash(key) % self.cap

		while self.table[index] is not None and self.table[index] is not self.tombstone and self.table[index][0] != key:
			index = (index + 1) % self.cap
		
		if self.table[index] is None or self.table[index] is self.tombstone:
			self.table[index] = (key, value)
			self.size += 1

			if self.size > self.cap * 0.7:
				self.resize()
			return True
		elif self.table[index][0] == key:
			return False	
				
	# Purpose: Modify/update the value associated with an existing key
    # Parameters:
    # 1. key: the key whose value is to be modified
    # 2. value: the new value to associate with the key
    # Return Value: True if the modification was successful, False if the key doesn't exist
	# Limitations: None
	def modify(self, key, value):
		index = hash(key) % self.cap
		while self.table[index] is not None:
			if self.table[index][0] == key:
				self.table[index] = (key,value)
				return True
			index = (index + 1) % self.cap
			
		return False

 	# Purpose: Remove a key-value pair from the table
    # Parameters:
    # 1. key: the key to be removed
    # Return Value: True if the pair was removed, False if the key doesn't exist
	# Limitations: None
	def remove(self, key):
		index = hash(key) % self.cap
		while self.table[index] is not None:
			# if self.table[index][0] == key:
			if self.table[index] is not self.tombstone and self.table[index][0] == key:
				self.table[index] = self.tombstone
				self.size -= 1
				
				# if don't have tombstone, we need to rehash other elements in the same cluster
				# which will cause O(n^2) 
				return True
			index = (index+1)%self.cap
		return False

	# Purpose: Search for a value associated with a key
    # Parameters:
    # 1. key: the key to search for
    # Return Value: The value associated with the key if found, None otherwise
	# Limitations: None
	def search(self, key):
		index = hash(key) % self.cap
		
		while self.table[index] is not None:
			# if self.table[index][0] == key:
			if self.table[index] is not self.tombstone and self.table[index][0] == key:
				return self.table[index][1]
			index = (index + 1) % self.cap

		return None

	# Purpose: Get the capacity of the table
    # Parameters: None
    # Return Value: The capacity of the table
	# Limitations: None
	def capacity(self):
		return self.cap

	# Purpose: Get the number of key-value pairs in the table
    # Parameters: None
    # Return Value: The number of key-value pairs in the table
	# Limitations: None
	def __len__(self):
		return self.size

