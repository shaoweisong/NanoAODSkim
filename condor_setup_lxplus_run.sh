#cmssw-el7
#cmsenv

#voms-proxy-init --rfc --voms cms -valid 192:00

#cd /afs/cern.ch/work/p/pelai/HZgamma/CMSSW_10_6_20/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/nanoAOD_skim/

python condor_setup_lxplus.py  --input_file hzg_bkg2022preEE.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/HiggsDNA_skimmed --submission_name Run2022preEE --year "2022preEE" --isMC

python condor_setup_lxplus.py  --input_file hzg_bkg2022postEE.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/HiggsDNA_skimmed --submission_name Run2022postEE --year "2022postEE" --isMC

python condor_setup_lxplus.py  --input_file hzg_bkg2023preBPix.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/HiggsDNA_skimmed --submission_name Run2023preBPix --year "2023preBPix" --isMC

python condor_setup_lxplus.py  --input_file hzg_bkg2023postBPix.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/HiggsDNA_skimmed --submission_name Run2023postBPix --year "2023postBPix" --isMC