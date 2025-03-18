python post_proc.py --entriesToRun 100 --inputFile /eos/user/s/shsong/5B123882-8484-1B47-9A07-57F8F526F6EF.root -m True -y 2018
python condor_setup_lxplus.py  --input_file sample_list_v9_2018FH.dat --eos_output_path /eos/cms/store/group/phys_b2g/shsong/nanoAODnTuples/nanoAODsys_Mar2024/UL2018_HHsignal/ --use_custom_eos --submission_name Run2018_FH --year 2018 --isMC --DontCreateTarFile
python condor_setup_lxplus.py  --input_file sample_list_v9_2018SL.dat --eos_output_path /eos/cms/store/group/phys_b2g/shsong/nanoAODnTuples/nanoAODsys_Mar2024/UL2018_HHsignal/ --use_custom_eos --submission_name Run2018_SL --year 2018 --isMC --DontCreateTarFile
python condor_setup_lxplus.py  --input_file sample_list_v9_2018bbgg.dat --eos_output_path /eos/cms/store/group/phys_b2g/shsong/nanoAODnTuples/nanoAODsys_Mar2024/UL2018_HHsignal/ --use_custom_eos --submission_name Run2018_bbgg --year 2018 --isMC --DontCreateTarFile
python condor_setup_lxplus.py  --input_file sample_list_v9_2017signal.dat --eos_output_path /eos/cms/store/group/phys_b2g/shsong/nanoAODnTuples/nanoAODsys_Mar2024/UL2017_HHsignal/ --use_custom_eos --submission_name Run2017 --year 2017 --isMC --DontCreateTarFile

python condor_setup_lxplus.py  --input_file sample_hzg2017.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/shsong/Customized/HZgMCUL17 --submission_name Run2017HZG --year "2017" --isMC 



python condor_setup_lxplus.py  --input_file sample_test.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/shsong/Customized/HZgMCUL17 --submission_name Run2017HZG --year "2017" --isMC --DontCreateTarFile
python post_proc.py --entriesToRun 0 --inputFile root://xrootd-cms.infn.it//store/mc/RunIISummer20UL17NanoAODv9/ttHToZG_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/106X_mc2017_realistic_v9-v2/2520000/07D6096D-7AEF-2B49-96B5-71C412A6BE24.root  -m True -y 2017 
