# NanoAOD Skim
nanoAOD skiming code for H->ZZ->2l2Q studies.

## Code setup

1. Step: 1: Get CMSSW release

   ```bash
   cmsrel CMSSW_10_6_30
   cd CMSSW_10_6_30/src
   cmsenv
   ```

2. Step: 2: Get  nanoAODTools

   ```bash
   git clone -b HHWWgg git@github.com:shaoweisong/NanoAODTools.git 
   cd PhysicsTools/NanoAODTools
   ```

3. Step: 3: Get our analysis repository

   ```bash
   cd $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/
   git clone -b HH_WWgg_dev git@github.com:shaoweisong/NanoAODSkim.git
   cd $CMSSW_BASE/src/
   cmsenv
   # patch PhysicsTools/NanoAODTools/python/postprocessing/analysis/nanoAOD_skim/nanoAOD_tools.patch
   cp PhysicsTools/NanoAODTools/python/postprocessing/analysis/nanoAOD_skim/data/btag/*.csv PhysicsTools/NanoAODTools/data/btagSF/.
   scram b
   voms-proxy-init --voms cms --valid 168:00
   ```

   (Optional: Fix git repo)

   ```bash
   find PhysicsTools/NanoAODTools/python/postprocessing/analysis/nanoAOD_skim/.git/ -name "*.py*" -delete
   ```

4. Step: 4: interactive running

   ```bash
   cd $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/nanoAOD_skim
   python post_proc.py --entriesToRun 100 --inputFile /eos/cms/store/group/phys_b2g/zhenxuan/custom_nanoAOD/nanoAOD_24Oct2023/UL2018_signal_FH/UL2018/GluGluToRadionToHHTo2G2WTo2G4Q_M-1600/GluGluToRadionToHHTo2G2WTo2G4Q_M-1600_9042687_2.root -m True -y 2018
   ```

5. batch job submission.
   1. Step: 5 (a): Condor-job submission (recommended)
      1. In the file [condor_setup_lxplus.py](condor_setup_lxplus.py), specify the correct input text file (present inside directory [input_data_Files](input_data_Files)) from which you need to take input NanoAOD DAS names. Also, updated the output EOS path. Then do the following:

         ```bash
         cd $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/nanoAOD_skim
         # Use the arguments that you need.
         python condor_setup_lxplus.py --input-file sample_list_v9.dat
         # Set proxy before submitting the condor jobs.
         voms-proxy-init -voms cms --valid 200:00
         condor_submit <Files-created-from-above-command>.jdl
         ```

   1. Step: 5(b): Crab-job submission (Not tested recently)
      ```bash
      cd crab/
      voms-proxy-init -voms cms --valid 200:00
      source /cvmfs/cms.cern.ch/crab3/crab.sh
      crab submit -c crab_cfg.py
      ```

## Few additioanl scripts

1. [condor_setup_lxplus.py](condor_setup_lxplus.py): This script can be used to setup the condor jobs. It takes the input text file (present inside directory [input_data_Files](input_data_Files)) from which you need to take input NanoAOD DAS names. Also, updated the output EOS path. Then do the following:

   ```bash
   python condor_setup_lxplus.py --input-file sample_list_v9.dat
   ```
   This will create the condor job files and the condor log files.

1. [scripts/GetLogSummary.py](scripts/GetLogSummary.py): This script can be used to get the summary of the condor jobs. It takes the condor log files as input and gives the summary of the jobs. This summary contains the cut-flow table. It can be used as follows:

   ```bash
   python scripts/GetLogSummary.py <condor_log_file_base_path>
   ```

2. [scripts/check_das_sample.py](scripts/check_das_sample.py): This script can be used to check the status of the DAS samples. It takes the DAS name of the sample as input and gives the status of the sample. It can be used as follows:

   ```bash
   python scripts/check_das_sample.py <DAS_name_of_the_sample>
   ```

3. [scripts/condor_resubmit.py](scripts/condor_resubmit.py): This script can be used to resubmit the failed condor jobs. It takes the condor log files as input and resubmits the failed jobs. It can be used as follows:

   ```bash
   python scripts/condor_resubmit.py <condor_log_file_base_path>
   ```

## Few important points

