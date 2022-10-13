import shelve

# dic={'a':1,'b':2}
#
# d=shelve.open(r'db.shl')
# d['egon']={'pwd':'123','age':18}
# d['alex']={'pwd':'123465','age':18}
# d['x']=dic
#
#
# d.close()



obj=shelve.open(r'db.shl')
print(obj['x']['a'])

obj.close()