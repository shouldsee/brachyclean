import pymisca.ext as pyext;
pyext.base__check()

suc,res = pyext.job__script(
    pyext.base__file('BrachyPhoton/0130__makePeakWindows__Brachy-ELF3.py'),
#     env=env,
)
assert suc

suc,res = pyext.job__script(
    pyext.base__file('BrachyPhoton/0130__chipSummary__Brachy-ELF3.py')
)
assert suc

suc,res = pyext.job__script(
    pyext.base__file('BrachyPhoton/0130__callDiffTarg__Brachy-ELF3.py')
)
assert suc