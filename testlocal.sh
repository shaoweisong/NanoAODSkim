python post_proc.py --entriesToRun 100 --inputFile /eos/user/s/shsong/5B123882-8484-1B47-9A07-57F8F526F6EF.root -m True -y 2018
python condor_setup_lxplus.py  --input_file sample_list_v9_2018FH.dat --eos_output_path /eos/cms/store/group/phys_b2g/shsong/nanoAODnTuples/nanoAODsys_Mar2024/UL2018_HHsignal/ --use_custom_eos --submission_name Run2018_FH --year 2018 --isMC --DontCreateTarFile
python condor_setup_lxplus.py  --input_file sample_list_v9_2018SL.dat --eos_output_path /eos/cms/store/group/phys_b2g/shsong/nanoAODnTuples/nanoAODsys_Mar2024/UL2018_HHsignal/ --use_custom_eos --submission_name Run2018_SL --year 2018 --isMC --DontCreateTarFile
python condor_setup_lxplus.py  --input_file sample_list_v9_2018bbgg.dat --eos_output_path /eos/cms/store/group/phys_b2g/shsong/nanoAODnTuples/nanoAODsys_Mar2024/UL2018_HHsignal/ --use_custom_eos --submission_name Run2018_bbgg --year 2018 --isMC --DontCreateTarFile
python condor_setup_lxplus.py  --input_file sample_list_v9_2017signal.dat --eos_output_path /eos/cms/store/group/phys_b2g/shsong/nanoAODnTuples/nanoAODsys_Mar2024/UL2017_HHsignal/ --use_custom_eos --submission_name Run2017 --year 2017 --isMC --DontCreateTarFile

python condor_setup_lxplus.py  --input_file sample_hzg2017.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/shsong/Customized/HZgMCUL17 --submission_name Run2017HZG --year "2017" --isMC 


python post_proc.py --entriesToRun 100 --inputFile root://xrootd-cms.infn.it//store/mc/RunIISummer20UL17NanoAODv9/ttHToZG_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/106X_mc2017_realistic_v9-v2/2520000/07D6096D-7AEF-2B49-96B5-71C412A6BE24.root  -m True -y 2017 

# What HiggsDNA DYGto2LG_10to50_2022preEE job_1 uses
python post_proc.py --entriesToRun 100 --inputFile root://cms-xrd-global.cern.ch//store/mc/Run3Summer22NanoAODv12/DYGto2LG-1Jets_MLL-50_PTG-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_v5-v2/2520000/98de45c2-e825-4189-9384-81e7dae263d3.root -m True -y 2022preEE


# What HiggsDNA DYJetsToLL_2016preVFP job_1 uses
python post_proc.py --entriesToRun 100 --inputFile root://xrootd-cms.infn.it//store/mc/RunIISummer20UL16NanoAODAPVv9/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/25DA20B0-D01E-8D4E-9F29-FD7DD57BF214.root -m True -y 2016preVFP