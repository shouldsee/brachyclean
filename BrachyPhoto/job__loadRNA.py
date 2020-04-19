import pymisca.ext as pyext;

pyext.base__check()

suc,res = pyext.job__script(
    pyext.base__file('BrachyPhoton/0131__dumpDataRNA__Brachy.py'),
#     env=env,
)
assert suc,res

suc,res = pyext.job__script(
    pyext.base__file('BrachyPhoton/0130__makeTracks-Brachy.py'),
#     env=env,
)
assert suc,res
