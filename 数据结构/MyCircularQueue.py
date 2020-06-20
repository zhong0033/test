#实现循环队列

'''
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。

**示例
MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4
'''
class MyCircularQueue:
 
	def __init__(self, k: int): #and
		"""
		Initialize your data structure here. Set the size of the queue to be k.
		"""
		self.__length = k
		self.queue = [0] * k
		self.__head = 0
		self.__tail = -1
		self.__count = 0
 
	def enQueue(self, value: int) -> bool:
		"""
		Insert an element into the circular queue. Return true if the operation is successful.
		"""
		if self.isFull() == False:
			if self.__tail == self.__length-1: #尾指到最后一个空间了
				self.__tail = 0
			else:
				self.__tail += 1
			self.queue[self.__tail] = value
			self.__count += 1
			return True
		else:
			return False
 
 
	def deQueue(self) -> bool:
		"""
		Delete an element from the circular queue. Return true if the operation is successful.
		"""
		if self.isEmpty() == False :
			self.queue[self.__head] = 0
			self.__count -= 1
			if self.__head != self.__tail:
				if self.__head == self.__length-1:
					self.__head = 0
				else:
					self.__head += 1
			else:
				self.__head = 0
				self.__tail = -1
			return True
		else:
			return False
 
	def Front(self) -> int:
		"""
		Get the front item from the queue.
		"""
		if self.isEmpty():
			return -1
		else:
			return self.queue[self.__head]
 
	def Rear(self) -> int:
		"""
		Get the last item from the queue.
		"""
		if self.isEmpty():
			return -1
		else:
			return self.queue[self.__tail]
 
	def isEmpty(self) -> bool:
		"""
		Checks whether the circular queue is empty or not.
		"""
		if self.__count == 0:
			return True 
		else:
			return False
 
	def isFull(self) -> bool:
		"""
		Checks whether the circular queue is full or not.
		"""
		if self.__count == self.__length:
			return True
		else:
			return False

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(2)
print(param_1)
param_2 = obj.deQueue()
print(param_2)
param_3 = obj.Front()
print(param_3)
param_4 = obj.Rear()
print(param_4)
param_5 = obj.isEmpty()
print(param_5)
param_6 = obj.isFull()
print(param_6)





