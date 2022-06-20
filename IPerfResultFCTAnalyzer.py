from os import listdir
from os.path import isfile, join
import testAndMeasurement.ResultProcessor as rp
import numpy as np
import matplotlib.pyplot as plt

import ConfigConst

globalPercentileList = [10,20,30,40,50,60,70,80,90,100]

def getAllFilesInDirectory(folderPath):

    # r=root, d=directories, f = files
    onlyfiles = [f for f in listdir(folderPath) if (isfile(join(folderPath, f)))]
    # print("Total files in this directory is ", len(onlyfiles))
    return onlyfiles


# def getAVGFCTByFolderOld(folderName):
#     # files = getAllFilesInDirectory(folderName)
#     flowTypeVsFCTMap = {}
#     flowTypeVsFlowCountMap = {}
#     flowTypeVsSendBytesMap = {}
#     # for flowVolume in ConfigConst.FLOW_TYPE_IDENTIFIER_BY_FLOW_VOLUME_IN_KB:
#     #     # flowTypeVsFCTMap[flowVolume]  = 0
#     #     flowTypeVsFCTMap[flowVolume]  = []
#     #     flowTypeVsFlowCountMap[flowVolume] = 0
#     start, end, iperfResultsAsList = rp.parseIperfResultsFromFolder(folderName)
#     iperfResultsAsList = iperfResultsAsList.iperfResults
#     # print("Result is ", iperfResultsAsList.iperfResultsAsList)
#
#     totalBytesSent = 0
#     for r in iperfResultsAsList:
#         flowSize = r[0].end.sum_received.bytes
#         fct = r[0].end.sum_received.seconds
#         totalBytesSent = totalBytesSent + flowSize
#     totalBytesSent = totalBytesSent/1024
#     print("totalBytesSent (in KB) =",totalBytesSent )
#     print("Total flows "+str(len(iperfResultsAsList)))
#     for r in iperfResultsAsList:
#         flowSize = r[0].end.sum_received.bytes
#         # print(flowSize)
#         fct = r[0].end.sum_received.seconds
#         for flowVolume in ConfigConst.FLOW_TYPE_IDENTIFIER_BY_FLOW_VOLUME_IN_KB:
#             if abs(flowVolume*1024 - flowSize) <= (20*1024):
#                 # flowTypeVsFCTMap[flowVolume] = flowTypeVsFCTMap.get(flowVolume) + fct
#                 if (flowTypeVsFCTMap.get(flowVolume) == None):
#                     flowTypeVsFCTMap[flowVolume] = []
#                     flowTypeVsFlowCountMap[flowVolume] = 0
#                     flowTypeVsSendBytesMap[flowVolume] = []
#                     pass
#                 else:
#                     flowTypeVsFCTMap.get(flowVolume).append(fct)
#                     flowTypeVsFlowCountMap[flowVolume] = flowTypeVsFlowCountMap.get(flowVolume) + 1
#                     flowTypeVsSendBytesMap.get(flowVolume).append(flowSize)
#     totalFlowsize = 0
#     totalOfFlowSizeMultipliedByAvgFct=0
#     for f in flowTypeVsFCTMap:
#         # print(str(f) + " -- ",np.percentile(flowTypeVsFCTMap.get(f), 80))
#         # print(str(f) + " -- ",flowTypeVsFlowCountMap.get(f))
#
#         print(str(f) + " -- ",(flowTypeVsFlowCountMap.get(f)))
#         weightedFct = np.average(flowTypeVsFCTMap.get(f))
#         # weightedFct = np.percentile(flowTypeVsFCTMap.get(f),90)
#         print(str(f) + " -- ",weightedFct)
#         # print(str(f) + " -- ",np.std(flowTypeVsFCTMap.get(f)))
#         # print(flowTypeVsFCTMap.get(f))
#         totalFlowsize= totalFlowsize+ float(f)
#         totalOfFlowSizeMultipliedByAvgFct = totalOfFlowSizeMultipliedByAvgFct + ( float(f) * weightedFct)
#     print("Average FCT  = ", totalOfFlowSizeMultipliedByAvgFct/totalFlowsize)
#     pass
#
# def getAVGFCTByFolderOld(folderName):
#     # files = getAllFilesInDirectory(folderName)
#     flowTypeVsFCTMap = {}
#     flowTypeVsFlowCountMap = {}
#     flowTypeVsSendBytesMap = {}
#     flowTypeVsRetransmissionMap = {}
#     fctList = []
#     retransList = []
#     # for flowVolume in ConfigConst.FLOW_TYPE_IDENTIFIER_BY_FLOW_VOLUME_IN_KB:
#     #     # flowTypeVsFCTMap[flowVolume]  = 0
#     #     flowTypeVsFCTMap[flowVolume]  = []
#     #     flowTypeVsFlowCountMap[flowVolume] = 0
#     start, end, iperfResultsAsList = rp.parseIperfResultsFromFolder(folderName)
#     iperfResultsAsList = iperfResultsAsList.iperfResults
#     # print("Result is ", iperfResultsAsList.iperfResultsAsList)
#
#     totalBytesSent = 0
#     totalTime = 0
#     totalRetransmission= 0
#     for r in iperfResultsAsList:
#         flowSize = r[0].end.sum_received.bytes
#         fct = r[0].end.sum_received.seconds
#         totalTime = totalTime + fct
#         fctList.append(fct)
#         totalBytesSent = totalBytesSent + flowSize
#         retransmits = r[0].end.sum_sent.retransmits
#         retransList.append(retransmits)
#         totalRetransmission = totalRetransmission + retransmits
#     totalBytesSent = totalBytesSent/1024
#
#     print("Total flows "+str(len(iperfResultsAsList)))
#     print("total BytesSent (in KB) =",totalBytesSent )
#     print("Total Time "+str(totalTime))
#     print("Total Retrasmits "+str(totalRetransmission))
#     print("Average throughput "+str(totalBytesSent/totalTime))
#     for r in iperfResultsAsList:
#         flowSize = r[0].end.sum_received.bytes
#         flowVolume = flowSize
#         # print(flowSize)
#         fct = r[0].end.sum_received.seconds
#         # flowTypeVsFCTMap[flowVolume] = flowTypeVsFCTMap.get(flowVolume) + fct
#         if (flowTypeVsFCTMap.get(flowVolume) == None):
#             flowTypeVsFCTMap[flowVolume] = [fct]
#             flowTypeVsFlowCountMap[flowVolume] = 1
#             flowTypeVsSendBytesMap[flowVolume] = [flowVolume]
#             flowTypeVsRetransmissionMap[flowVolume] = [r[0].end.sum_sent.retransmits]
#             pass
#         else:
#             flowTypeVsFCTMap.get(flowVolume).append(fct)
#             flowTypeVsFlowCountMap[flowVolume] = flowTypeVsFlowCountMap.get(flowVolume) + 1
#             flowTypeVsSendBytesMap.get(flowVolume).append(flowSize)
#             flowTypeVsRetransmissionMap.get(flowVolume).append(r[0].end.sum_sent.retransmits)
#     totalFlowsize = 0
#     totalOfFlowSizeMultipliedByAvgFct=0
#     shortFlowTotalBytesSent = 0
#     shortFlowTotalBytesMultipliedByFCT = 0
#     shortFlowTotalBytesMultipledByRetransmission =0
#     largeFlowTotalBytesSent = 0
#     largeFlowTotalBytesMultipliedByFCT = 0
#     largeFlowTotalRetransmission =0
#     shortFlowcount = 0
#     largeFlowcount = 0
#     for f in flowTypeVsFCTMap:
#         j=0
#         for j in range(0,len(flowTypeVsSendBytesMap.get(f))):
#             if (flowTypeVsSendBytesMap.get(f)[j]<1024*1024):
#                 shortFlowTotalBytesSent = shortFlowTotalBytesSent + float(f)
#                 shortFlowTotalBytesMultipliedByFCT = shortFlowTotalBytesMultipliedByFCT + float(f) * flowTypeVsFCTMap.get(f)[j]
#                 shortFlowTotalBytesMultipledByRetransmission = shortFlowTotalBytesMultipledByRetransmission + flowTypeVsRetransmissionMap.get(f)[j]
#                 shortFlowcount =  shortFlowcount  + 1
#             else:
#                 largeFlowTotalBytesSent = largeFlowTotalBytesSent + float(f)
#                 largeFlowTotalBytesMultipliedByFCT = largeFlowTotalBytesMultipliedByFCT + float(f) * flowTypeVsFCTMap.get(f)[j]
#                 largeFlowTotalRetransmission = largeFlowTotalRetransmission + flowTypeVsRetransmissionMap.get(f)[j]
#                 largeFlowcount = largeFlowcount  + 1
#         # weightedFct = np.average(flowTypeVsFCTMap.get(f))
#         #
#         # totalFlowsize= totalFlowsize+ float(f)
#         # totalOfFlowSizeMultipliedByAvgFct = totalOfFlowSizeMultipliedByAvgFct + ( float(f) * weightedFct)
#     if (shortFlowTotalBytesSent > 0):
#         print("shortFlowcount is "+str(shortFlowcount))
#         print("Average FCT for short flow  = ", shortFlowTotalBytesMultipliedByFCT/shortFlowTotalBytesSent)
#     if (largeFlowTotalBytesSent > 0):
#         print("largeFlowcount is "+str(largeFlowcount))
#         print("Average FCT for large flow  = ", largeFlowTotalBytesMultipliedByFCT/largeFlowTotalBytesSent)
#     print("Average retransmissions for short flow  = ", shortFlowTotalBytesMultipledByRetransmission/shortFlowcount)
#     print("Average retransmissions for large flow  = ", largeFlowTotalRetransmission/largeFlowcount)
#
#     # sort the data:
#     fctSorted = np.sort(fctList)
#
#     # calculate the proportional values of samples
#     p = 1. * np.arange(len(fctList)) / (len(fctList) - 1)
#     # plot the sorted data:
#     fig = plt.figure()
#     ax1 = fig.add_subplot(121)
#     ax1.plot(p, fctSorted)
#     ax1.set_xlabel('$p$')
#     ax1.set_ylabel('$x$')
#     plt.savefig("/home/deba/Desktop/P4TE/result/test.pdf")
#
#
#
#     pass


def getAVGFCTByFolder(folderName):
    # files = getAllFilesInDirectory(folderName)
    flowTypeVsFCTMap = {}
    flowTypeVsFlowCountMap = {}
    flowTypeVsSendBytesMap = {}
    flowTypeVsRetransmissionMap = {}
    shortFctList = []
    shortRetransList = []
    largeFctList = []
    largeRetransList = []
    # for flowVolume in ConfigConst.FLOW_TYPE_IDENTIFIER_BY_FLOW_VOLUME_IN_KB:
    #     # flowTypeVsFCTMap[flowVolume]  = 0
    #     flowTypeVsFCTMap[flowVolume]  = []
    #     flowTypeVsFlowCountMap[flowVolume] = 0
    start, end, iperfResultsAsList = rp.parseIperfResultsFromFolder(folderName)
    iperfResultsAsList = iperfResultsAsList.iperfResults
    # print("Result is ", iperfResultsAsList.iperfResultsAsList)

    totalBytesSent = 0
    totalTime = 0
    totalRetransmission= 0
    for r in iperfResultsAsList:
        flowSize = r[0].end.sum_received.bytes
        fct = r[0].end.sum_received.seconds
        totalTime = totalTime + fct
        totalBytesSent = totalBytesSent + flowSize
        retransmits = r[0].end.sum_sent.retransmits

        totalRetransmission = totalRetransmission + retransmits
    totalBytesSent = totalBytesSent/1024

    print("Total flows "+str(len(iperfResultsAsList)))
    print("total BytesSent (in KB) =",totalBytesSent )
    print("Total Time "+str(totalTime))
    print("Total Retrasmits "+str(totalRetransmission))
    print("Average throughput "+str(totalBytesSent/totalTime))
    for r in iperfResultsAsList:
        flowSize = r[0].end.sum_received.bytes
        flowVolume = flowSize
        # print(flowSize)
        fct = r[0].end.sum_received.seconds
        # flowTypeVsFCTMap[flowVolume] = flowTypeVsFCTMap.get(flowVolume) + fct
        if (flowTypeVsFCTMap.get(flowVolume) == None):
            flowTypeVsFCTMap[flowVolume] = [fct]
            flowTypeVsFlowCountMap[flowVolume] = 1
            flowTypeVsSendBytesMap[flowVolume] = [flowVolume]
            flowTypeVsRetransmissionMap[flowVolume] = [r[0].end.sum_sent.retransmits]
            pass
        else:
            flowTypeVsFCTMap.get(flowVolume).append(fct)
            flowTypeVsFlowCountMap[flowVolume] = flowTypeVsFlowCountMap.get(flowVolume) + 1
            flowTypeVsSendBytesMap.get(flowVolume).append(flowSize)
            flowTypeVsRetransmissionMap.get(flowVolume).append(r[0].end.sum_sent.retransmits)
    totalFlowsize = 0
    totalOfFlowSizeMultipliedByAvgFct=0
    shortFlowTotalBytesSent = 0
    shortFlowTotalBytesMultipliedByFCT = 0
    shortFlowTotalBytesMultipledByRetransmission =0
    largeFlowTotalBytesSent = 0
    largeFlowTotalBytesMultipliedByFCT = 0
    largeFlowTotalRetransmission =0
    shortFlowcount = 0
    largeFlowcount = 0
    for f in flowTypeVsFCTMap:
        j=0
        for j in range(0,len(flowTypeVsSendBytesMap.get(f))):
            if (flowTypeVsSendBytesMap.get(f)[j]<756*1024):
                shortFlowTotalBytesSent = shortFlowTotalBytesSent + float(f)
                shortFlowTotalBytesMultipliedByFCT = shortFlowTotalBytesMultipliedByFCT + float(f) * flowTypeVsFCTMap.get(f)[j]
                shortFlowTotalBytesMultipledByRetransmission = shortFlowTotalBytesMultipledByRetransmission + flowTypeVsRetransmissionMap.get(f)[j]
                shortFlowcount =  shortFlowcount  + 1
                shortFctList.append(flowTypeVsFCTMap.get(f)[j])
                shortRetransList.append(flowTypeVsRetransmissionMap.get(f)[j])
            else:
                largeFlowTotalBytesSent = largeFlowTotalBytesSent + float(f)
                largeFlowTotalBytesMultipliedByFCT = largeFlowTotalBytesMultipliedByFCT + float(f) * flowTypeVsFCTMap.get(f)[j]
                largeFlowTotalRetransmission = largeFlowTotalRetransmission + flowTypeVsRetransmissionMap.get(f)[j]
                largeFlowcount = largeFlowcount  + 1
                largeFctList.append(flowTypeVsFCTMap.get(f)[j])
                largeRetransList.append(flowTypeVsRetransmissionMap.get(f)[j])
        # weightedFct = np.average(flowTypeVsFCTMap.get(f))
        #
        # totalFlowsize= totalFlowsize+ float(f)
        # totalOfFlowSizeMultipliedByAvgFct = totalOfFlowSizeMultipliedByAvgFct + ( float(f) * weightedFct)
    if (shortFlowTotalBytesSent > 0):
        print("shortFlowcount is "+str(shortFlowcount))
        # print("Average FCT for short flow  = ", shortFlowTotalBytesMultipliedByFCT/shortFlowTotalBytesSent)
        print("Average FCT for short flow  = ", np.average(shortFctList))
    if (largeFlowTotalBytesSent > 0):
        print("largeFlowcount is "+str(largeFlowcount))
        print("Average FCT for large flow  = ", largeFlowTotalBytesMultipliedByFCT/largeFlowTotalBytesSent)
        # print("Average FCT for latge flow  = ", np.average(largeFctList))
    print("Average retransmissions for short flow  = ", shortFlowTotalBytesMultipledByRetransmission/shortFlowcount)
    print("Average retransmissions for large flow  = ", largeFlowTotalRetransmission/largeFlowcount)
    percentileList = [25,70,80,90,100]
    fctCombo=shortFctList+largeFctList
    fctCombo.sort()
    print("Short Flow ")
    if (shortFlowTotalBytesSent > 0):
        for p in percentileList:
            print(np.percentile(shortFctList,p))
    print("Large Flow ")
    if (largeFlowTotalBytesSent > 0):
        for p in percentileList:
            print(np.percentile(largeFctList,p))
    print("Combination")
    for p in percentileList:
        print(np.percentile(fctCombo,p))

    return shortFctList, shortRetransList, largeFctList, largeRetransList, shortFctList+largeFctList, shortRetransList+largeRetransList

def getGlobalPercentileValues(values):
    valueList = []
    values.sort()
    for p in globalPercentileList:
        valueList.append(np.percentile(values,p))
    pList = []
    for p in globalPercentileList:
        pList.append(p/100)
    return valueList, pList

def compareMultipleFCTandDrawCDF(listOfFctLists,nameLists,markerList):
    fctfig = plt.figure()
    ax1 = fctfig.add_subplot(121)
    for i in range (0, len(listOfFctLists)):
        fctList = listOfFctLists[i]
        fctList,p = getGlobalPercentileValues(fctList)
        ax1.plot( fctList,p, label=nameLists[i],marker=markerList[i])
    ax1.set_xlabel('FCT (in sec.)')
    ax1.set_ylabel('CDF of FCT')
    ax1.legend(loc="upper left", ncol=4)
    ax1.legend( ncol=4)
    ax1.legend(fontsize=10)
    plt.savefig("./result/FCT-FlowletColnfiguration.pdf")


def compareThreeFCTAndReTrans(fctList1, fctList2, fctList3, retransList1, retransList2, retransList3, fileName):
    fctList1 = np.sort(fctList1)
    fctList2 = np.sort(fctList2)
    fctList3 = np.sort(fctList3)
    retransList1 = np.sort(retransList1)
    retransList2 = np.sort(retransList2)
    retransList3 = np.sort(retransList3)


    fctfig = plt.figure()
    ax1 = fctfig.add_subplot(121)
    # calculate the proportional values of samples

    p = 1. * np.arange(len(retransList1)) / (len(retransList1) - 1)
    # plot the sorted data:
    # Make p as an np array of percentile values we want to show in graph and make another array with corresponding values.
    retransList1,p = getGlobalPercentileValues(retransList1)
    ax1.plot( retransList1,p, label="ECMP",marker="D")
    p = 1. * np.arange(len(retransList2)) / (len(retransList2) - 1)
    # plot the sorted data:
    retransList2,p = getGlobalPercentileValues(retransList2)
    ax1.plot( retransList2,p, label="HULA",marker="s")
    p = 1. * np.arange(len(retransList3)) / (len(retransList3) - 1)
    # plot the sorted data:
    retransList3,p = getGlobalPercentileValues(retransList3)
    ax1.plot(retransList3, p, label="P4TE",marker="^")

    ax1.set_xlabel('No. of Retransmissions')
    ax1.set_ylabel('CDF of Retransmissions')
    ax1.legend(loc="upper left", ncol=4)
    ax1.legend( ncol=4)
    ax1.legend(fontsize=10)
    plt.savefig("./result/Retrans-"+fileName+".pdf")

    fctfig = plt.figure()
    ax1 = fctfig.add_subplot(121)
    # calculate the proportional values of samples
    p = 1. * np.arange(len(fctList1)) / (len(fctList1) - 1)
    # plot the sorted data:
    fctList1,p = getGlobalPercentileValues(fctList1)
    ax1.plot( fctList1,p, label="ECMP",marker="D")
    p = 1. * np.arange(len(fctList2)) / (len(fctList2) - 1)
    # plot the sorted data:
    fctList2,p = getGlobalPercentileValues(fctList2)
    ax1.plot( fctList2,p, label="HULA",marker="s")
    p = 1. * np.arange(len(fctList3)) / (len(fctList3) - 1)
    # plot the sorted data:
    fctList3,p = getGlobalPercentileValues(fctList3)
    ax1.plot(fctList3, p, label="P4TE",marker="^")

    ax1.set_xlabel('FCT (in sec.)')
    ax1.set_ylabel('CDF of FCT')
    ax1.legend(loc="upper left", ncol=4)
    ax1.legend( ncol=4)
    ax1.legend(fontsize=10)
    plt.savefig("./result/FCT-"+fileName+".pdf")


# print(" Analyzing average FCT and total retransmissions for data mining workload ")
#
# print("Load factor 0.8")
# print("ECMP")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1, combinedFCTList1, combinedRetransList1= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP/DataMining_Workload_load_factor_0.8/client-logs-0")
# print("\n\n")
#
# print("HULA")
# shortFctList2, shortRetransList2, largeFctList2, largeRetransList2, combinedFCTList2, combinedRetransList2 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/HULA/DataMining_Workload_load_factor_0.8/client-logs-0")
# print("\n\n")
#
# print("P4TE")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 , combinedFCTList3, combinedRetransList3= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/DataMining_Workload_load_factor_0.8/client-logs-0")
# print("\n\n")
#
# compareThreeFCTAndReTrans(shortFctList1, shortFctList2, shortFctList3, shortRetransList1, shortRetransList2, shortRetransList3, "datamining_0.8-short-flow")
# compareThreeFCTAndReTrans(largeFctList1, largeFctList2, largeFctList3, largeRetransList1, largeRetransList2, largeRetransList3, "datamining_0.8-large-flow")
# compareThreeFCTAndReTrans(combinedFCTList1, combinedFCTList2, combinedFCTList3, combinedRetransList1, combinedRetransList2, combinedRetransList2, "datamining_0.8-combined")
#
# # print("-----------------------------------------------")
# #
# # #
# # # #-----------------------------------------------
# #
# print("Load factor 0.6")
# print("ECMP")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1, combinedFCTList1, combinedRetransList1= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP/DataMining_Workload_load_factor_0.6/client-logs-0")
# print("\n\n")
#
# print("HULA")
# shortFctList2, shortRetransList2, largeFctList2, largeRetransList2,combinedFCTList2, combinedRetransList2  = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/HULA/DataMining_Workload_load_factor_0.6/client-logs-0")
# print("\n\n")
#
# print("P4TE")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3,combinedFCTList3, combinedRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/DataMining_Workload_load_factor_0.6/client-logs-0")
# print("\n\n")
# compareThreeFCTAndReTrans(shortFctList1, shortFctList2, shortFctList3, shortRetransList1, shortRetransList2, shortRetransList3, "datamining_0.6-short-flow")
# compareThreeFCTAndReTrans(largeFctList1, largeFctList2, largeFctList3, largeRetransList1, largeRetransList2, largeRetransList3, "datamining_0.6-large-flow")
# compareThreeFCTAndReTrans(combinedFCTList1, combinedFCTList2, combinedFCTList3, combinedRetransList1, combinedRetransList2, combinedRetransList2, "datamining_0.6-combined")
# #
# # print("-----------------------------------------------")
# #
# # #-----------------------------------------------
# print("Load factor 0.4")
# print("ECMP")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1, combinedFCTList1, combinedRetransList1= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP/DataMining_Workload_load_factor_0.4/client-logs-0")
# print("\n\n")
#
# print("HULA")
# shortFctList2, shortRetransList2, largeFctList2, largeRetransList2,combinedFCTList2, combinedRetransList2  = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/HULA/DataMining_Workload_load_factor_0.4/client-logs-0")
# print("\n\n")
#
# print("P4TE")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 ,combinedFCTList3, combinedRetransList3= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/DataMining_Workload_load_factor_0.4/client-logs-0")
# print("\n\n")
# compareThreeFCTAndReTrans(shortFctList1, shortFctList2, shortFctList3, shortRetransList1, shortRetransList2, shortRetransList3, "datamining_0.4-short-flow")
# compareThreeFCTAndReTrans(largeFctList1, largeFctList2, largeFctList3, largeRetransList1, largeRetransList2, largeRetransList3, "datamining_0.4-large-flow")
# compareThreeFCTAndReTrans(combinedFCTList1, combinedFCTList2, combinedFCTList3, combinedRetransList1, combinedRetransList2, combinedRetransList2, "datamining_0.4-combined")
# #
# print("-----------------------------------------------")
# # # #-----------------------------------------------
# #
# print("Load factor 0.2")
# print("ECMP")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1, combinedFCTList1, combinedRetransList1= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP/DataMining_Workload_load_factor_0.2/client-logs-0")
# print("\n\n")
#
# print("HULA")
# shortFctList2, shortRetransList2, largeFctList2, largeRetransList2 ,combinedFCTList2, combinedRetransList2 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/HULA/DataMining_Workload_load_factor_0.2/client-logs-0")
# print("\n\n")
#
# print("P4TE")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3,combinedFCTList3, combinedRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/DataMining_Workload_load_factor_0.2/client-logs-0")
# print("\n\n")
# compareThreeFCTAndReTrans(shortFctList1, shortFctList2, shortFctList3, shortRetransList1, shortRetransList2, shortRetransList3, "datamining_0.2-short-flow")
# compareThreeFCTAndReTrans(largeFctList1, largeFctList2, largeFctList3, largeRetransList1, largeRetransList2, largeRetransList3, "datamining_0.2-large-flow")
# compareThreeFCTAndReTrans(combinedFCTList1, combinedFCTList2, combinedFCTList3, combinedRetransList1, combinedRetransList2, combinedRetransList2, "datamining_0.2-combined")
# #
# print("-----------------------------------------------")
# # # #
#
# print("===================================================================================================================================================")
# print(" Analyzing average FCT and total retransmissions for web search workload ")
#
# print("Load factor 0.8")
# print("ECMP")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1, combinedFCTList1, combinedRetransList1= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP/WebSearchWorkLoad_load_factor_0.8/client-logs-0")
# print("\n\n")
#
# print("HULA")
# shortFctList2, shortRetransList2, largeFctList2, largeRetransList2,combinedFCTList2, combinedRetransList2  = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/HULA/WebSearchWorkLoad_load_factor_0.8/client-logs-0")
# print("\n\n")
#
# print("P4TE")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3,combinedFCTList3, combinedRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/WebSearchWorkLoad_load_factor_0.8/client-logs-0")
# print("\n\n")
# compareThreeFCTAndReTrans(shortFctList1, shortFctList2, shortFctList3, shortRetransList1, shortRetransList2, shortRetransList3, "websearch_0.8-short-flow")
# compareThreeFCTAndReTrans(largeFctList1, largeFctList2, largeFctList3, largeRetransList1, largeRetransList2, largeRetransList3, "websearch_0.8-large-flow")
# compareThreeFCTAndReTrans(combinedFCTList1, combinedFCTList2, combinedFCTList3, combinedRetransList1, combinedRetransList2, combinedRetransList2, "websearch_0.8-combined")
#
#
#
#
# # compareThreeFCTAndReTrans(shortFctList1, shortFctList2, shortFctList3, shortRetransList1, shortRetransList2, shortRetransList3, "webSearch_0.8")
# # print("-----------------------------------------------")
# #
# # #
# # # #-----------------------------------------------
# #
# print("Load factor 0.6")
# print("ECMP")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1, combinedFCTList1, combinedRetransList1= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP/WebSearchWorkLoad_load_factor_0.6/client-logs-0")
# print("\n\n")
#
# print("HULA")
# shortFctList2, shortRetransList2, largeFctList2, largeRetransList2,combinedFCTList2, combinedRetransList2  = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/HULA/WebSearchWorkLoad_load_factor_0.6/client-logs-0")
# print("\n\n")
#
# print("P4TE")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 ,combinedFCTList3, combinedRetransList3= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/WebSearchWorkLoad_load_factor_0.6/client-logs-0")
# print("\n\n")
# compareThreeFCTAndReTrans(shortFctList1, shortFctList2, shortFctList3, shortRetransList1, shortRetransList2, shortRetransList3, "websearch_0.6-short-flow")
# compareThreeFCTAndReTrans(largeFctList1, largeFctList2, largeFctList3, shortRetransList1, shortRetransList2, shortRetransList3, "websearch_0.6-large-flow")
# compareThreeFCTAndReTrans(combinedFCTList1, combinedFCTList2, combinedFCTList3, combinedRetransList1, combinedRetransList2, combinedRetransList2, "websearch_0.6-combined")
# #
# # print("-----------------------------------------------")
# #
# # #-----------------------------------------------
# print("Load factor 0.4")
# print("ECMP")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1, combinedFCTList1, combinedRetransList1= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP/WebSearchWorkLoad_load_factor_0.4/client-logs-0")
# print("\n\n")
#
# print("HULA")
# shortFctList2, shortRetransList2, largeFctList2, largeRetransList2 ,combinedFCTList2, combinedRetransList2 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/HULA/WebSearchWorkLoad_load_factor_0.4/client-logs-0")
# print("\n\n")
#
# print("P4TE")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3,combinedFCTList3, combinedRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/WebSearchWorkLoad_load_factor_0.4/client-logs-0")
# print("\n\n")
# compareThreeFCTAndReTrans(shortFctList1, shortFctList2, shortFctList3, shortRetransList1, shortRetransList2, shortRetransList3, "websearch_0.4-short-flow")
# compareThreeFCTAndReTrans(largeFctList1, largeFctList2, largeFctList3, shortRetransList1, shortRetransList2, shortRetransList3, "websearch_0.4-large-flow")
# compareThreeFCTAndReTrans(combinedFCTList1, combinedFCTList2, combinedFCTList3, combinedRetransList1, combinedRetransList2, combinedRetransList2, "websearch_0.4-combined")
# #
# print("-----------------------------------------------")
# # # #-----------------------------------------------
# #
# print("Load factor 0.2")
# print("ECMP")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1, combinedFCTList1, combinedRetransList1= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP/WebSearchWorkLoad_load_factor_0.2/client-logs-0")
# print("\n\n")
#
# print("HULA")
# shortFctList2, shortRetransList2, largeFctList2, largeRetransList2 ,combinedFCTList2, combinedRetransList2 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/HULA/WebSearchWorkLoad_load_factor_0.2/client-logs-0")
# print("\n\n")
#
# print("P4TE")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3,combinedFCTList3, combinedRetransList3  = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/WebSearchWorkLoad_load_factor_0.2/client-logs-0")
# print("\n\n")
# compareThreeFCTAndReTrans(shortFctList1, shortFctList2, shortFctList3, shortRetransList1, shortRetransList2, shortRetransList3, "websearch_0.2-short-flow")
# compareThreeFCTAndReTrans(largeFctList1, largeFctList2, largeFctList3, shortRetransList1, shortRetransList2, shortRetransList3, "websearch_0.2-large-flow")
# compareThreeFCTAndReTrans(combinedFCTList1, combinedFCTList2, combinedFCTList3, combinedRetransList1, combinedRetransList2, combinedRetransList2, "websearch_0.2-combined")
# #



# print("===================================================================================================================================================")
# listOfFctLists = []
# nameLists = []
# markerList = []
# print(" Analyzing average FCT and total retransmissions for Flowlet Interval determination")
#
# print("ECMP-10")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1,combinedFCTList1,_= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP-FLOWLET-IPG/ECMP-10/WebSearchWorkLoad_load_factor_0.8/client-logs-0")
# print("\n\n")
# listOfFctLists.append(combinedFCTList1)
# nameLists.append("Int. 10ms")
# markerList.append(".")
#
# print("ECMP-20")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1,combinedFCTList2,_= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP-FLOWLET-IPG/ECMP-20/WebSearchWorkLoad_load_factor_0.8/client-logs-0")
# print("\n\n")
# listOfFctLists.append(combinedFCTList2)
# nameLists.append("Int. 20ms")
# markerList.append("o")
#
# print("ECMP-30")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1,combinedFCTList3,_= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP-FLOWLET-IPG/ECMP-30/WebSearchWorkLoad_load_factor_0.8/client-logs-0")
# print("\n\n")
# listOfFctLists.append(combinedFCTList3)
# nameLists.append("Int. 30ms")
# markerList.append("v")
#
# print("ECMP-40")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1,combinedFCTList3,_= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP-FLOWLET-IPG/ECMP-40/WebSearchWorkLoad_load_factor_0.8/client-logs-0")
# print("\n\n")
# listOfFctLists.append(combinedFCTList3)
# nameLists.append("Int. 40ms")
# markerList.append("s")
#
# print("ECMP-50")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1,combinedFCTList4,_= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP-FLOWLET-IPG/ECMP-50/WebSearchWorkLoad_load_factor_0.8/client-logs-0")
# print("\n\n")
# listOfFctLists.append(combinedFCTList4)
# nameLists.append("Int. 50ms")
# markerList.append("+")
#
# print("ECMP-60")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1,combinedFCTList5,_= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP-FLOWLET-IPG/ECMP-60/WebSearchWorkLoad_load_factor_0.8/client-logs-0")
# print("\n\n")
# listOfFctLists.append(combinedFCTList5)
# nameLists.append("Int. 60ms")
# markerList.append("D")
#
# print("ECMP-70")
# shortFctList1, shortRetransList1, largeFctList1, largeRetransList1,combinedFCTList6,_= getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP-FLOWLET-IPG/ECMP-70/WebSearchWorkLoad_load_factor_0.8/client-logs-0")
# print("\n\n")
# listOfFctLists.append(combinedFCTList6)
# nameLists.append("Int. 70ms")
# markerList.append("<")
#
# compareMultipleFCTandDrawCDF(listOfFctLists,nameLists,markerList)

#
# print("===================================================================================================================================================")
# print(" Analyzing average FCT and total retransmissions for Impact of Rate control determination Using Web Search Workload ")
#
# print("Load factor 0.8")
#
# print("P4TE-Without-Rate-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE-NRC/WebSearchWorkLoad_load_factor_0.8/client-logs-0")
# print("\n\n")
# #
#
# print("P4TE-With-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/WebSearchWorkLoad_load_factor_0.8/client-logs-0")
# print("\n\n")
#
#
# print("Load factor 0.6")
#
# print("P4TE-Without-Rate-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE-NRC/WebSearchWorkLoad_load_factor_0.6/client-logs-0")
# print("\n\n")
# #
#
# print("P4TE-With-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/WebSearchWorkLoad_load_factor_0.6/client-logs-0")
# print("\n\n")
#
#
# print("Load factor 0.4")
#
# print("P4TE-Without-Rate-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE-NRC/WebSearchWorkLoad_load_factor_0.4/client-logs-0")
# print("\n\n")
# #
#
# print("P4TE-With-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/WebSearchWorkLoad_load_factor_0.4/client-logs-0")
# print("\n\n")
#
#
# print("Load factor 0.2")
#
# print("P4TE-Without-Rate-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE-NRC/WebSearchWorkLoad_load_factor_0.2/client-logs-0")
# print("\n\n")
# #
#
# print("P4TE-With-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/WebSearchWorkLoad_load_factor_0.2/client-logs-0")
# print("\n\n")
#
#
# print("===================================================================================================================================================")
# print(" Analyzing average FCT and total retransmissions for Impact of Rate control determination Using Data Mining Workload ")
#
# print("Load factor 0.8")
#
# print("P4TE-Without-Rate-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE-NRC/DataMining_Workload_load_factor_0.8/client-logs-0")
# print("\n\n")
# #
#
# print("P4TE-With-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/DataMining_Workload_load_factor_0.8/client-logs-0")
# print("\n\n")
#
#
# print("Load factor 0.6")
#
# print("P4TE-Without-Rate-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE-NRC/DataMining_Workload_load_factor_0.6/client-logs-0")
# print("\n\n")
# #
#
# print("P4TE-With-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/DataMining_Workload_load_factor_0.6/client-logs-0")
# print("\n\n")
#
# print("Load factor 0.4")
#
# print("P4TE-Without-Rate-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE-NRC/DataMining_Workload_load_factor_0.4/client-logs-0")
# print("\n\n")
# #
#
# print("P4TE-With-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/DataMining_Workload_load_factor_0.4/client-logs-0")
# print("\n\n")
#
#
#
# print("Load factor 0.2")
#
# print("P4TE-Without-Rate-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE-NRC/DataMining_Workload_load_factor_0.2/client-logs-0")
# print("\n\n")
# #
#
# print("P4TE-With-Control")
# shortFctList3, shortRetransList3, largeFctList3, largeRetransList3 = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/DataMining_Workload_load_factor_0.2/client-logs-0")
# print("\n\n")

print("Incast")

print("P4TE")
shortFctList3, shortRetransList3, largeFctList3, largeRetransList3, _, _ = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/P4TE/l2-incast/client-logs-0")
print("\n\n")
#

print("ECMP")
shortFctList3, shortRetransList3, largeFctList3, largeRetransList3, _, _ = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/ECMP/l2-incast/client-logs-0")
print("\n\n")

print("HULA")
shortFctList3, shortRetransList3, largeFctList3, largeRetransList3, _, _ = getAVGFCTByFolder(folderName= "/home/deba/Desktop/P4TE/testAndMeasurement/TEST_RESULTS/HULA/l2-incast/client-logs-0")
print("\n\n")