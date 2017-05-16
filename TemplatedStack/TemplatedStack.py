# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_TemplatedStack', [dirname(__file__)])
        except ImportError:
            import _TemplatedStack
            return _TemplatedStack
        if fp is not None:
            try:
                _mod = imp.load_module('_TemplatedStack', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _TemplatedStack = swig_import_helper()
    del swig_import_helper
else:
    import _TemplatedStack
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class IntStack(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntStack, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntStack, name)
    __repr__ = _swig_repr
    __swig_setmethods__["topOfStack"] = _TemplatedStack.IntStack_topOfStack_set
    __swig_getmethods__["topOfStack"] = _TemplatedStack.IntStack_topOfStack_get
    if _newclass:topOfStack = _swig_property(_TemplatedStack.IntStack_topOfStack_get, _TemplatedStack.IntStack_topOfStack_set)
    def __init__(self): 
        this = _TemplatedStack.new_IntStack()
        try: self.this.append(this)
        except: self.this = this
    def push(self, *args): return _TemplatedStack.IntStack_push(self, *args)
    def pop(self): return _TemplatedStack.IntStack_pop(self)
    __swig_destroy__ = _TemplatedStack.delete_IntStack
    __del__ = lambda self : None;
IntStack_swigregister = _TemplatedStack.IntStack_swigregister
IntStack_swigregister(IntStack)

class FloatStack(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FloatStack, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FloatStack, name)
    __repr__ = _swig_repr
    __swig_setmethods__["topOfStack"] = _TemplatedStack.FloatStack_topOfStack_set
    __swig_getmethods__["topOfStack"] = _TemplatedStack.FloatStack_topOfStack_get
    if _newclass:topOfStack = _swig_property(_TemplatedStack.FloatStack_topOfStack_get, _TemplatedStack.FloatStack_topOfStack_set)
    def __init__(self): 
        this = _TemplatedStack.new_FloatStack()
        try: self.this.append(this)
        except: self.this = this
    def push(self, *args): return _TemplatedStack.FloatStack_push(self, *args)
    def pop(self): return _TemplatedStack.FloatStack_pop(self)
    __swig_destroy__ = _TemplatedStack.delete_FloatStack
    __del__ = lambda self : None;
FloatStack_swigregister = _TemplatedStack.FloatStack_swigregister
FloatStack_swigregister(FloatStack)

# This file is compatible with both classic and new-style classes.


