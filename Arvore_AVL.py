import os
import time
#============================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#============================================
	#AVL TREE NODE
class Node():
	#Node constructor
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key
	def __str__(self):
		return "%s" % self.key
#============================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#============================================



#============================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#============================================
 	#AVL TREE
class AVLtree():
	
	def __init__(self):
		self.node=None
		self.height=-1
		self.balance=0
	
	#INSERTION
	def insert(self,key):
		#create new node
		n=Node(key)

		#initial tree
		if(self.node==None):
			self.node=n
			self.node.left=AVLtree()
			self.node.right=AVLtree()
		#Insert Key to the left subtree
		elif(key[0] < self.node.key[0]):
			self.node.left.insert(key)
		#Insert key to the right subtree
		elif(key[0] > self.node.key[0]):
			self.node.right.insert(key)

		#key is in the tree, now we need to balance
		self.rebalance()

	#REBALANCE TREE
	def rebalance(self):
		'''
		It's necessary to check the node's ancestors
		to compare with the of the AVL tree
		'''
		#check if we need to rebalance the tree
			#UPDATE HEIGHT
			#BALANCE TREE
		self.update_heights(recursive=False)
		self.update_balances(False)

		while( (self.balance < -1) or (self.balance > 1) ):
			#left > right
			if(self.balance > 1):
				#Case: with we need qa double rotation
				if(self.node.left.balance < 0):
					self.node.left.rotate_left()
					self.update_heights()
					self.update_balances()
				self.rotate_right()
				self.update_heights()
				self.update_balances()
			#Right > left
			if(self.balance < -1):
				#Case: with we need a double rotation
				if(self.node.right.balance > 0):
					self.node.right.rotate_right()
					self.update_heights()
					self.update_balances()
				self.rotate_left()
				self.update_heights()
				self.update_balances()

	def update_heights(self,recursive=True):
		if(self.node):
			if(recursive):
				if(self.node.left):
					self.node.left.update_heights()
				if(self.node.right):
					self.node.right.update_heights()
			'''
			PS: "MAX" its a function from PYTHON 
			that returns the larger number
			'''
			self.height = 1 + max(self.node.left.height, self.node.right.height)
		else:
			self.height = -1

	def update_balances(self, recursive=True):
		#PS: Balance = height(left) - height(right)
		if(self.node):
			if(recursive):
				if(self.node.left):
					self.node.left.update_balances()
				if(self.node.right):
					self.node.right.update_balances()
			self.balance = self.node.left.height - self.node.right.height
		else:
			self.balance=0

	#ROTATION OF THE TREE
	def rotate_right(self):
		new_root= self.node.left.node
		new_left_subtree=new_root.right.node
		old_root=self.node

		self.node=new_root
		old_root.left.node=new_left_subtree
		new_root.right.node=old_root

	def rotate_left(self):
		new_root=self.node.right.node
		new_left_subtree=new_root.left.node
		old_root=self.node

		self.node=new_root
		old_root.right.node=new_left_subtree
		new_root.left.node=old_root

	#DELETION OF NODES
	def delete(self,key):
		if self.node != None:
			if int(self.node.key[0]) == key:
				#Key found in leaf node => just erase it
				if not self.node.left.node and not self.node.right.node:
					self.node = None
				#Node has only one subtree (right) => replace root with that one
				elif not self.node.left.node:                
					self.node = self.node.right.node
				#Node has only one subtree (left) => replace root with that one
				elif not self.node.right.node:
					self.node = self.node.left.node
				else:
					#Find  successor as smallest node in right subtree or
					#predecessor as largest node in left subtree
					successor = self.node.right.node  
					while successor and successor.left.node:
						successor = successor.left.node
					if successor:
						self.node.key = successor.key

						# Delete successor from the replaced node right subree
						self.node.right.delete(successor.key)
			elif key < int(self.node.key[0]):
				self.node.left.delete(key)
			elif key > int(self.node.key[0]):
				self.node.right.delete(key)
			# Rebalance tree
			self.rebalance()
		else:
			print("Erro")

	def query(self,data):
		if(self.node!=None):
			if data == int(self.node.key[0]):
				return True
			elif data < int(self.node.key[0]):
				if self.node.left!=None:
					return self.node.left.query(data)
				else:
					return False
			elif data > int(self.node.key[0]):
				if self.node.right!=None:
					return self.node.right.query(data)
				else:
					return False
		else:
			return False

	def postorder_tree(self):
		result = []

		if not self.node:a
			return result
        
		result.extend(self.node.left.postorder_tree())
		result.extend(self.node.right.postorder_tree())
		result.append(self.node.key)

		return result
#============================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#============================================


#~~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~~~~~
tree=AVLtree()
data=[]
caminho=raw_input("\nDigite o nome do arquivo\n")
with open(caminho) as arquivo:
	for line in arquivo:
		data.append(line.split(','))
print("\nInserindo elementos ...\n")
for key in data:
	tree.insert(key)
var=0
while(var!=4):
	print("1 - Printar arvore (posorder)\n")
	print("2 - Deletar elemento\n")
	print("3 - Procurar elemento\n")
	print("4 - sair\n")
	var=int(input())
	if (var==1):
		os.system('cls' if os.name == 'nt' else 'clear')
		print (tree.postorder_tree())
	elif (var==2):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("\nQue elemento (pela chave) deseja excluir?\n")
		elm=int(input())
		tree.delete(elm)
	elif (var==3):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("\nInforme o elemento (chave) para a procura:\n")
		elm=int(input())
		booleana=tree.query(elm)
		result='\nResultado: {} \n'.format(booleana)
		print(result)
#~~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~~~~~
