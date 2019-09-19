#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def toOurSuspiciousNumber(x):
    if len(list(str(x))) % 2 == 0:
        return list(str(x))
    else:
        return list('0')+list(str(x))
def polyndromQ(x):
    if toOurSuspiciousNumber(x)[:len(toOurSuspiciousNumber(x))//2]==toOurSuspiciousNumber(x)[len(toOurSuspiciousNumber(x))//2:][::-1]:
        return print("True")
    else:
        return print("False")

