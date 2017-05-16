%module TemplatedStack
%{
        #include "templated_stack.h"
%}

%include "templated_stack.h"

%template(IntStack) mStack <int>;
%template(FloatStack) mStack <float>;
