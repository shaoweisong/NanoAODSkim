import os

directory = '/eos/cms/store/group/phys_b2g/shsong/nanoAODnTuples/nanoAOD_Apr2025/UL2017_YHSLsignal_3TeV_4TeV/UL2017'
output_file = 'sample_list_UL2017_YH_SL2.dat'

subdirs = [os.path.join(directory, subdir) for subdir in os.listdir(directory) if os.path.isdir(os.path.join(directory, subdir))]

with open(output_file, 'w') as file:
    file.write('\n'.join(subdirs))

# 
# m_X_HY_full = [240, 280, 300, 320, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2500, 2600, 2800, 3000, 3500, 4000]
# m_Y_full = [50, 60, 70, 80, 90, 95, 100, 125, 150, 170, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2300, 2400, 2600, 2800, 3000, 3300, 3500, 3800]
# samples = 0
# official_sample=[]
# for mx in m_X_HY_full:
#     for my in m_Y_full:
#         if( mx > my + 125) & (mx <= 3000) & (mx >= 300)  & (my >= 160):
#             samples += 1
#             print(samples, mx, my)
#             official_sample.append("MX-"+str(mx)+"_MY-"+str(my))
# oursample="/afs/cern.ch/user/s/shsong/CMSSW_10_6_20/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/nanoAOD_skim/input_data_Files/sample_list_UL2017_all_graviton_all.txt"
# # loop line by line, extract the x, y number in str "MX-x_MY-y" and then create a new line with the format "MX-x_MY-y" and write it to the file
# our_sample_list = []
# with open(oursample, 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         our_sample_list.append(line.strip())
# # compare the two lists and print the difference
# missing_samples = []
# for sample in official_sample:
#     if sample not in our_sample_list:
#         missing_samples.append(sample)
# print("missing samples:", missing_samples)
