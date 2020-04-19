import pymisca.ext as pyext;
pyext.base__check()
# matplotlib.use("Agg")
# pyext.os.environ['BASE'] = '/home/feng/work'

suc,res = pyext.job__script(
    pyext.base__file('BrachyPhoton/0130__lineplot__pfr.py'),
#     env=env,
)
assert suc,res