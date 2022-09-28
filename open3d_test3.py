import h5py

filename = '/Users/json/Documents/point_cloud_compression/point_cloud.h5'
with h5py.File(filename, 'r') as h5f:
    ply_ds = h5f['complete_pcds']
    print(ply_ds.shape, ply_ds.dtype)
    for cnt, row in enumerate(ply_ds):
        v_cnt = row.shape[0]
        with open(f'pcds_{str(cnt)}.ply', 'w') as ply_f:
            ply_f.write('ply\n')
            ply_f.write('format ascii 1.0\n')
            ply_f.write(f'comment row {cnt} exported from:{filename}\n')
            ply_f.write(f'element vertex {v_cnt}\n')  # variable # of vertices
            ply_f.write('property float x\n')
            ply_f.write('property float y\n')
            ply_f.write('property float z\n')
            ply_f.write('end_header\n')
            for vertex in row:
                ply_f.write(f'{vertex[0]:#6.3g} {vertex[1]:#6.3g} {vertex[2]:#6.3g}\n')
