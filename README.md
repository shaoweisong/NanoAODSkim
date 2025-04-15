# NanoAOD Skim
nanoAOD skiming code for H->ZGamma studies.

## Code setup

1. No brainer steps

   ```bash
   cmssw-el7
   cmsrel CMSSW_10_6_20
   cd CMSSW_10_6_20/src
   cmsenv
   git cms-init
   git cms-merge-topic cbernet:heppy_8_0_11
   cmsenv
   source /afs/cern.ch/user/s/shsong/public/Heppyconflict/mergeconflict.sh
   scram b

   cd PhysicsTools/
   git clone -b HZG git@github.com:shaoweisong/NanoAODTools.git 
   cd NanoAODTools
   scram b


   cd $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/
   rm -rf nanoAOD_skim
   git clone -b HZG git@github.com:shaoweisong/NanoAODSkim.git nanoAOD_skim
   cd $CMSSW_BASE/src/
   cmsenv
   # patch PhysicsTools/NanoAODTools/python/postprocessing/analysis/nanoAOD_skim/nanoAOD_tools.patch
   cp PhysicsTools/NanoAODTools/python/postprocessing/analysis/nanoAOD_skim/data/btag/*.csv PhysicsTools/NanoAODTools/data/btagSF/.
   scram b
   voms-proxy-init --voms cms --valid 168:00
   cd $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/nanoAOD_skim
   #try this for test
   python post_proc.py --entriesToRun 100 --inputFile /eos/project/h/htozg-dy-privatemc/shsong/Customized/E3D30224-C63D-CC48-9259-B0BE9FED9BB1.root -m True -y 2017
   
   if there is Skimmed.root output, you can submit jobs through condor:
   python condor_setup_lxplus.py  --input_file {sample.dat} --eos_output_path /eos/project/h/htozg-dy-privatemc/{your_dir} --submission_name {any_name} --year {str_year} --isMC 
   python condor_setup_lxplus.py  --input_file sample_hzg2017.dat --year "2017" --isMC --submission_name hzg2017sig --DontCreateTarFile
   python condor_setup_lxplus.py  --input_file sample_hzg2018.dat --year "2018" --isMC --submission_name hzg2018sig --DontCreateTarFile
   python condor_setup_lxplus.py  --input_file sample_hzg2016pre.dat --year "2016preVFP" --isMC --submission_name hzg2016presig --DontCreateTarFile
   python condor_setup_lxplus.py  --input_file sample_hzg2016post.dat --year "2016postVFP" --isMC --submission_name hzg2016postsig --DontCreateTarFile
   python condor_setup_lxplus.py  --input_file sample_hzg2022preEE.dat --year "2022preEE" --isMC --submission_name hzg2022presig --DontCreateTarFile
   python condor_setup_lxplus.py  --input_file sample_hzg2022postEE.dat --year "2022postEE" --isMC --submission_name hzg2022postsig --DontCreateTarFile
   python condor_setup_lxplus.py  --input_file sample_hzg2023preBPix.dat --year "2023preBPix" --isMC --submission_name hzg2023presig --DontCreateTarFile
   python condor_setup_lxplus.py  --input_file sample_hzg2023postBPix.dat --year "2023postBPix" --isMC --submission_name hzg2023postsig --DontCreateTarFile
   
   ```
   For background:
   ```
   python condor_setup_lxplus.py  --input_file hzg_bkg2017.dat --DontCreateTarFile --submission_name Run2017HZG_bkg --year "2017" --isMC 
   python condor_setup_lxplus.py  --input_file hzg_bkg2018.dat --DontCreateTarFile --submission_name Run2018HZG_bkg --year "2018" --isMC 
   python condor_setup_lxplus.py  --input_file hzg_bkg2016pre.dat --DontCreateTarFile --submission_name Run2016preHZG_bkg --year "2016preVFP" --isMC 
   python condor_setup_lxplus.py  --input_file hzg_bkg2016post.dat --DontCreateTarFile --submission_name Run2016postHZG_bkg --year "2016postVFP" --isMC 
   
   ```
