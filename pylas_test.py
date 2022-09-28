import pylas

# Directly read and write
laslas = pylas.read('filename.las')
las = pylas.convert(point_format_id=2)
las.write('converted.las')
# Open data to inspect header and then read
with pylas.open('filename.las') as f:
    if f.header.point_count < 10 ** 8:
        las = f.read()
    print(las.vlrs)
