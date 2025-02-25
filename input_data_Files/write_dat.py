import os

directory = '/eos/cms/store/group/phys_b2g/zhenxuan/custom_nanoAOD/Graviton_beforeSKIM/UL2017_graviton/UL2017'
output_file = 'sample_list_UL2017_all_graviton.dat'

subdirs = [os.path.join(directory, subdir) for subdir in os.listdir(directory) if os.path.isdir(os.path.join(directory, subdir))]

with open(output_file, 'w') as file:
    file.write('\n'.join(subdirs))
