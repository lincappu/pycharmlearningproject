#cp source_file dst_file
import sys

sfile=sys.argv[1]
dfile=sys.argv[2]

# with open(sfile,'rb') as read_f:
#     data=read_f.read()
#
# with open(dfile,'wb') as write_f:
#     write_f.write(data)
#
with open(sfile,'rb') as read_f,open(dfile,'wb') as write_f:
    # data=read_f.read()
    # write_f.write(data)
    for line in read_f:
        write_f.write(line)
        write_f.flush()