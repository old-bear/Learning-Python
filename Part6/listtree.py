#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Fri Apr  8 00:11:42 2016

"""An inspection mix-in class to show the entire class tree
and all its attributes
"""

class ListTree:
    """
    Mix-in that returns an __str__ trace of the entire class tree and all 
    its objects' attrs at and above self;  run by print(), str() returns 
    constructed string;  uses __X attr names to avoid impacting clients;  
    recurses to superclasses explicitly, uses str.format() for clarity;
    """
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith("_ListTree__"): continue
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result

    def __superclasses(self, aclass):
        result = ', '.join(cls.__name__ for cls in aclass.__bases__)
        return '(' + result + ')' if result else ''

    def __listclass(self, aClass, indent):
        if aClass is ListTree:
            # No need to list itself
            return ''
        
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}{2}:, address {3}: (see above)>\n'.format(
                           dots, 
                           aClass.__name__,
                           self.__superclasses(aClass),
                           id(aClass))
        else:
            self.__visited[aClass] = True
            here  = self.__attrnames(aClass, indent)
            above = ''
            for super in aClass.__bases__:
                above += self.__listclass(super, indent+4)
            return '\n{0}<Class {1}{2}, address {3}:\n{4}{5}{6}>\n'.format(
                           dots, 
                           aClass.__name__,
                           self.__superclasses(aClass),
                           id(aClass), 
                           here, above, 
                           dots)

    def __str__(self):
        self.__visited = {}
        here  = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return '<Instance of {0}{1}, address {2}:\n{3}{4}>'.format(
                           self.__class__.__name__,
                           self.__superclasses(self.__class__),
                           id(self),
                           here, above)

    
if __name__ == '__main__': 
    from urllib2 import HTTPSHandler
    class MyHandler(ListTree, HTTPSHandler): pass
    test = MyHandler()
    print("CLASS TREE OF urllib.request.HTTPSHandler:\n\n", test)
