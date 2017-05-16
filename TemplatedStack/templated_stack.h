#include <string>
template <typename T>
class mNode {
public:
	T data;
	mNode* next;
	mNode() { }
	mNode(T d) { 
		data = d;
		next = NULL;
	}
	
};
template <typename T>
class mStack {
	mNode<T> *topOfStack;
	mStack() {
		topOfStack = NULL;
	}		
	void push(T data) {
		mNode<T>* newNode = new mNode<T>(data);
		newNode->next = topOfStack;
		topOfStack = newNode;
	}
	T pop() {
		T data = topOfStack->data;
		topOfStack = topOfStack->next;
		return data;
	}
};
