#!/bin/bash

# First parameter is file name
# Second parameter is module name

i_extension='.i'
i_file=$1$i_extension

flag1='-c++'
flag2='-python'


wrap_extension='_wrap.cpp'
wrap_file=$1$wrap_extension

library_include_of_python=' -I/usr/include/python2.7'

# echo $i_file
# echo $wrap_file

#Swig command
swig_command='swig '$flag1' '$flag2' -o '$wrap_file' '$i_file
echo $swig_command
eval $swig_command

#G++ on the wrapper code
compile_command_wrapper='g++ -c -fPIC '$wrap_file$library_include_of_python
# echo $compile_command_wrapper
eval $compile_command_wrapper

#Making the shared library
o_extension='.o'
object_file=$1$o_extension
shared_library_name='_'$2
shared_library_command='g++ -shared -o '$shared_library_name'.so '$1'_wrap'$o_extension
eval $shared_library_command
