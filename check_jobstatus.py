import subprocess


jdlfile="/afs/cern.ch/user/s/shsong/YH_UL2017_highmass_coarse_500_1T.txt"
# open the jdl file and get the line starts with Arguments
bad_files = []
outputfiles = []
with open(jdlfile, 'r') as f:
    lines = f.readlines()
    for line in lines:        
        if line.startswith("Arguments"):
            # get the string after the first space
            
            arguments = line.split("root root:")
            filename=arguments[0].split(".root ")[-1]+"root"
            output_path = arguments[1].split("//eosuser.cern.ch/")[-1].split("\n")[0]
            output_file = output_path + "/" + filename
            outputfiles.append(output_file)
def check_root(file):
    cmd = "root -b " + file + " -q"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if "Warning in <TFile::Init>" in stdout or "Warning in <TFile::Init>" in stderr:
        print("Warning detected: TFile initialization issue.")
        bad_files.append(file)    
    return None
# print the processing time for each iteration
import time
start_time = time.time()
for file in outputfiles:
    check_root(file)
end_time = time.time()
print("Processing time: %s seconds" % (end_time - start_time))

# save bad files to a text file
with open("bad_files.txt", 'w') as f:   
    for bad_file in bad_files:
        f.write(bad_file + "\n")
        f.close()

