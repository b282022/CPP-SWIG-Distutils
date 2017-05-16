from distutils.core import setup, Extension
# Name of the module
name_of_module = "list_swig"
# Version of the module
version_of_module = "1.0"
# List of all modules to be placed inside a single package
external_modules = []
# Must specify that this is a c++ extension, this can be done via swig_opts parameter
external_modules.append(Extension(name = '_list_swig', sources = ['list.i'],
				include_dirs = [], swig_opts = ["-c++"]))
setup(name = name_of_module, version = version_of_module, ext_modules = external_modules)
