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
   source /afs/cern.ch/user/p/pelai/public/Heppyconflict/mergeconflict.sh
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
   python post_proc.py --entriesToRun 100 --inputFile /eos/project/h/htozg-dy-privatemc/2016APVDY_1/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8__RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1__privateProduction__job-9.root -m True -y 2017
   python post_proc.py --entriesToRun 100 --inputFile root://cms-xrd-global.cern.ch//store/mc/Run3Summer22NanoAODv12/DYGto2LG-1Jets_MLL-50_PTG-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/f12fcbb3-a0d9-4050-87ae-708bd6499461.root -m True -y 2022preEE

   if there is Skimmed.root output, you can submit jobs through condor:
   python condor_setup_lxplus.py  --input_file {sample.dat} --eos_output_path /eos/project/h/htozg-dy-privatemc/{your_dir} --submission_name {any_name} --year {str_year} --isMC 
   python condor_setup_lxplus.py  --input_file sample_hzg2017.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/{your_dir} --submission_name Run2017HZG --year "2017" --isMC 
   python condor_setup_lxplus.py  --input_file sample_hzg2018.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/{your_dir} --submission_name Run2018HZG --year "2018" --isMC 
   python condor_setup_lxplus.py  --input_file sample_hzg2016pre.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/{your_dir} --submission_name Run2016preHZG --year "2016preVFP" --isMC 
   python condor_setup_lxplus.py  --input_file sample_hzg2016post.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/{your_dir} --submission_name Run2016postHZG --year "2016postVFP" --isMC 
   ```
   For background:
   ```
   python condor_setup_lxplus.py  --input_file hzg_bkg2017.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/{your_dir} --submission_name Run2017HZG_bkg --year "2017" --isMC 
   python condor_setup_lxplus.py  --input_file hzg_bkg2018.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/{your_dir} --submission_name Run2018HZG_bkg --year "2018" --isMC 
   python condor_setup_lxplus.py  --input_file hzg_bkg2016pre.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/{your_dir} --submission_name Run2016preHZG_bkg --year "2016preVFP" --isMC 
   python condor_setup_lxplus.py  --input_file hzg_bkg2016post.dat --eos_output_path /eos/project/h/htozg-dy-privatemc/{your_dir} --submission_name Run2016postHZG_bkg --year "2016postVFP" --isMC 
   
   ```
