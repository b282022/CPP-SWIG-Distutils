swig -c++ -python -o templated_stack_wrap.cpp templated_stack.i
g++ -c -fPIC templated_stack_wrap.cpp -I/usr/include/python2.7
g++ -shared -o _TemplatedStack.so templated_stack_wrap.o

