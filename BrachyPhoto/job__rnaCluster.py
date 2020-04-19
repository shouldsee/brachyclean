import pymisca.ext as pyext;
pyext.base__check()
# pyext.os.environ['BASE'] = '/home/feng/work'

suc,res = pyext.job__script(
    pyext.base__file('BrachyPhoton/0129__cluster__Brachy-RNA-all.py'),
#     env=env,
)
assert suc,res

suc,res = pyext.job__script(
    pyext.base__file('BrachyPhoton/0129__showCluster__Brachy-RNA-all.py'),
#     env=env,
)
assert suc,res

suc,res = pyext.job__script(
    pyext.base__file('BrachyPhoton/0128__heatmap__Brachy.py'),
#     env=env,
)
assert suc,res