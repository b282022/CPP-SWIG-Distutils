// #include <bits/stdc++.h>
// #include <string>
template <typename T>
class mNode {
public:
	T data;
	mNode* next;
	mNode(T d);
	
};
template <class T> mNode<T>::mNode(T d) {
	data = d;
	next = NULL;
}
template <typename T>
class mStack {
public:
	mNode<T> *topOfStack;
	mStack();	
	void push(T data);
	T pop();
};

template <class T> mStack<T>::mStack() {
	topOfStack = NULL;
}

template <class T> void mStack<T>::push(T data) {
	mNode<T>* newNode = new mNode<T>(data);
	newNode->next = topOfStack;
	topOfStack = newNode;
}

template <class T> T mStack<T>::pop(void) {
	mNode<T>* tempTop = topOfStack;
	T dataToBePopped = tempTop->data;
	topOfStack = topOfStack->next;
	delete tempTop;
	return dataToBePopped;
}
