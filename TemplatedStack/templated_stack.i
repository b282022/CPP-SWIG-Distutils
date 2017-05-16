%module TemplatedStack
%{
        #include <string>
        #include "templated_stack.h"
%}

%include "templated_stack.h"

%template(IntStack) mStack <int>;

