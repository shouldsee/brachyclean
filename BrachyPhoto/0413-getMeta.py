FNAME = 'results/data/0413-dumpRunData/199R_201R/TPM.csv'
dfc = pyext.readData(FNAME,header=[0,1])
vals = dfc.columns.values
vals = np.array(map(list,vals))
ser = pd.Series(vals[:,1],index=vals[:,0])
dfcc = ser.str.split('-',expand=True)
dfcc.insert(0,'bname',vals[:,1])
dfcc.to_csv('0413-getMeta.csv')