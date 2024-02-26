#!/usr/bin/env python
import os
import sys
import argparse

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import createJMECorrector
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import btagSFProducer
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.PrefireCorr import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.muonScaleResProducer import muonScaleResProducer
from PhysicsTools.NanoAODTools.postprocessing.modules.common.LHEScaleWeightProducer import LHEScaleWeightProducer
from ggTemporaryScale import gammaSFProducer

# Custom module imports
from HHWWgg_AnalysisModule import *
from JetSFMaker import *

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--inputFile", default="", type=str, help="Input file name")
    parser.add_argument("-n", "--entriesToRun", default=100, type=int, help="Set  to 0 if need to run over all entries else put number of entries to run")
    parser.add_argument("-d", "--DownloadFileToLocalThenRun", default=True, type=bool, help="Download file to local then run")
    return parser.parse_args()


def getListFromFile(filename):
    """Read file list from a text file."""
    with open(filename, "r") as file:
        return ["root://cms-xrd-global.cern.ch/" + line.strip() for line in file]


def main():
    args = parse_arguments()

    # Initial setup
    testfilelist = []
    modulesToRun = []
    isMC = True
    isFSR = False
    year = None
    cfgFile = None
    jsonFileName = None
    sfFileName = None

    entriesToRun = int(args.entriesToRun)
    DownloadFileToLocalThenRun = args.DownloadFileToLocalThenRun

    # Determine list of files to process
    if args.inputFile.endswith(".txt"):
        testfilelist = getListFromFile(args.inputFile)
    elif args.inputFile.endswith(".root"):
        testfilelist.append(args.inputFile)
    else:
        print("INFO: No input file specified. Using default file list.")
        testfilelist = getListFromFile("ExampleInputFileList.txt")
    print("DEBUG: Input file list: {}".format(testfilelist))
    if len(testfilelist) == 0:
        print("ERROR: No input files found. Exiting.")
        exit(1)

    # Determine the year and type (MC or Data)
    first_file = testfilelist[0]
    # isMC = "UL201" not in first_file
    isMC = "signal" in first_file

    if "UL18" in first_file or "UL2018" in first_file:
        """UL2018 for identification of 2018 UL data and UL18 for identification of 2018 UL MC
        """
        year = 2018
        cfgFile = "Input_2018.yml"
        jsonFileName = "golden_Json/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt"
        sfFileName = "DeepCSV_102XSF_V2.csv"

    if "UL17" in first_file or "UL2017" in first_file:
        year = 2017
        cfgFile = "Input_2017.yml"
        jsonFileName="golden_Json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt"
        sfFileName = "DeepCSV_102XSF_V2.csv"

    if "UL16" in first_file or "UL2016" in first_file:
        year = 2016
        jsonFileName = "golden_Json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt"
        sfFileName = "DeepCSV_102XSF_V2.csv"
    if "UL2016APV" in first_file:
        year = "2016pre"
        jsonFileName = "golden_Json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt"
        sfFileName = "DeepCSV_102XSF_V2.csv"

    # H4LCppModule = lambda: HZZAnalysisCppProducer(year,cfgFile, isMC, isFSR)
    HHWWgg_AnalysisModule = lambda: HHWWgg_AnalysisProducer()
    modulesToRun.extend([HHWWgg_AnalysisModule()])

    print("Input json file: {}".format(jsonFileName))
    print("Input cfg file: {}".format(cfgFile))
    print("isMC: {}".format(isMC))
    print("isFSR: {}".format(isFSR))
    print(year)
    if isMC:
        # btagSF = lambda: btagSFProducer("UL"+str(year), algo="deepjet",selectedWPs=['L','M','T','shape_corr'], sfFileName=sfFileName)
        if year == "2016pre":
            muonScaleRes = lambda: muonScaleResProducer('roccor.Run2.v3', 'RoccoR2016.txt', 2016)
            LHEScaleSF  = lambda : LHEScaleWeightProducer(2016)
        else:
            muonScaleRes = lambda: muonScaleResProducer('roccor.Run2.v3', 'RoccoR'+str(year)+'.txt', year)
            LHEScaleSF  = lambda : LHEScaleWeightProducer(year)
        # Format year string for gammaSFProducer
        if year == 2018: gammaYear = "UL18"
        if year == 2017: gammaYear = "UL17"
        if year == "2016pre": gammaYear = "UL16Pre-VFP" # FIXME: update this
        if year == 2016: gammaYear = "UL16Post-VFP" # FIXME: update this
        if year == 2018: jetYear = "UL2018"
        if year == 2017: jetYear = "UL2017"
        if year == "2016pre": jetYear = "UL2016_preVFP" # FIXME: update this
        if year == 2016: jetYear = "UL2016" # FIXME: update this
        if year == 2018: fixvalue = True
        if year == 2017: fixvalue = False
        if year == "2016pre": fixvalue = False # FIXME: update this
        if year == 2016: fixvalue = False # FIXME: update this
        gammaSF = lambda: gammaSFProducer(gammaYear)
        jetmetCorrector = createJMECorrector(isMC=isMC, dataYear=jetYear, jesUncert="All", jetType = "AK4PFchs",applyHEMfix=fixvalue)
        fatJetCorrector = createJMECorrector(isMC=isMC, dataYear=jetYear, jesUncert="All", jetType = "AK8PFPuppi",applyHEMfix=fixvalue)
        PrefireCorr2016 = lambda : PrefCorr("L1prefiring_jetpt_2016BtoH.root", "L1prefiring_jetpt_2016BtoH", "L1prefiring_photonpt_2016BtoH.root", "L1prefiring_photonpt_2016BtoH")

        PrefireCorr2017 = lambda : PrefCorr('L1prefiring_jetpt_2017BtoF.root', 'L1prefiring_jetpt_2017BtoF', 'L1prefiring_photonpt_2017BtoF.root', 'L1prefiring_photonpt_2017BtoF')

        print("read prefire model")
        btagSF = lambda: btagSFProducer(era = "UL"+str(year), algo = "deepcsv")
        if year == 2018: puyear = 2018
        if year == 2017: puyear = 2017
        if year == "2016pre": puyear = 2016
        if year == 2016: puyear = 2016
        puidSF = lambda: JetSFMaker("%s" % puyear)
        if year == 2016:
            modulesToRun.extend([jetmetCorrector(), fatJetCorrector(), puidSF(), muonScaleRes(), gammaSF(),LHEScaleSF(),PrefireCorr2016()])
        if year == "2016pre":
            modulesToRun.extend([jetmetCorrector(), fatJetCorrector(), puidSF(), muonScaleRes(), gammaSF(),LHEScaleSF(),PrefireCorr2016()])
        if year == 2017:
            modulesToRun.extend([jetmetCorrector(), fatJetCorrector(), puidSF(), muonScaleRes(), gammaSF(),LHEScaleSF(),PrefireCorr2017()])
        if year == 2018:
            print(fixvalue)
            modulesToRun.extend([jetmetCorrector(), fatJetCorrector(), puidSF(), muonScaleRes(), gammaSF(),LHEScaleSF()])
        if year == 2018: modulesToRun.extend([puAutoWeight_UL2018()])
        if year == 2017: modulesToRun.extend([puAutoWeight_UL2017()])
        if year == 2016: modulesToRun.extend([puAutoWeight_UL2016()])
        if year == "2016pre": modulesToRun.extend([puAutoWeight_UL2016()])

        p=PostProcessor(".",testfilelist, None, None,modules = modulesToRun, provenance=True,fwkJobReport=False,haddFileName="skimmed_nano_mc.root", maxEntries=entriesToRun, prefetch=DownloadFileToLocalThenRun, outputbranchsel="keep_and_drop.txt")
    else:
        jetmetCorrector = createJMECorrector(isMC=isMC, dataYear=year, jesUncert="All", jetType = "AK4PFchs")
        fatJetCorrector = createJMECorrector(isMC=isMC, dataYear=year, jesUncert="All", jetType = "AK8PFPuppi")
        muonScaleRes = lambda: muonScaleResProducer('roccor.Run2.v3', 'RoccoR'+str(year)+'.txt', year)
        modulesToRun.extend([jetmetCorrector(), fatJetCorrector()])

        p=PostProcessor(".",testfilelist, None, None, modules = modulesToRun, provenance=True, fwkJobReport=False,haddFileName="skimmed_nano_data.root", jsonInput=jsonFileName, maxEntries=entriesToRun, prefetch=DownloadFileToLocalThenRun, outputbranchsel="keep_and_drop_data.txt")

    p.run()


if __name__ == "__main__":
    main()
