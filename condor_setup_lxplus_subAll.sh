
voms-proxy-init --rfc --voms cms -valid 192:00
cp /tmp/x509up_u175325 ~/
export X509_USER_PROXY=~/x509up_u175325
cd /afs/cern.ch/work/p/pelai/HZgamma/CMSSW_10_6_20/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/nanoAOD_skim/

condor_submit submit_condor_jobs_HZG_Run2022preEE.jdl
condor_submit submit_condor_jobs_HZG_Run2022postEE.jdl
condor_submit submit_condor_jobs_HZG_Run2023preBPix.jdl
condor_submit submit_condor_jobs_HZG_Run2023postBPix.jdl