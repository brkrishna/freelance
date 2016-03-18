#-------------------------------------------------------------------------------
# Name:        process_data
# Purpose:
#
# Author:      Ramakrishna
#
# Created:     17/04/2014
# Copyright:   (c) Ramakrishna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import re
import my_caching
import process_BWH, process_BM, process_BH, process_BL, process_BOS, process_BS
import process_BW, process_BW3, process_BWM, process_DNAI, process_ETC, process_FF
import process_FP, process_FS, process_GS, process_HT, process_IBN, process_IE
import process_IG, process_IN, process_IT, process_KM, process_KR, process_MD
import process_MM, process_MSN, process_MZ, process_NDTV, process_NR, process_OI
import process_PB, process_RE, process_REDIFF, process_RM, process_RMH
import process_SB, process_SH, process_SIFY, process_SULEKHA, process_TOI
import process_YAHOO, process_ZNI

def process(base_url, source_cd, data):
    try:
        record = []

        if source_cd == 'BWH':
            record = process_BWH.process(source_cd, base_url, data)
        if source_cd == 'BH':
            record = process_BH.process(source_cd, base_url, data)
        if source_cd == 'BM':
            record = process_BM.process(source_cd, base_url, data)
        if source_cd == 'BL':
            record = process_BL.process(source_cd, base_url, data)
        if source_cd == 'BOS':
            record = process_BOS.process(source_cd, base_url, data)
        if source_cd == 'BS':
            record = process_BS.process(source_cd, base_url, data)
        if source_cd == 'BW':
            record = process_BW.process(source_cd, base_url, data)
        if source_cd == 'BW3':
            record = process_BW3.process(source_cd, base_url, data)
        if source_cd == 'BWM':
            record = process_BWM.process(source_cd, base_url, data)
        if source_cd == 'DNAI':
            record = process_DNAI.process(source_cd, base_url, data)
        if source_cd == 'ETC':
            record = process_ETC.process(source_cd, base_url, data)
        if source_cd == 'FF':
            record = process_FF.process(source_cd, base_url, data)
        if source_cd == 'FP':
            record = process_FP.process(source_cd, base_url, data)
        if source_cd == 'FS':
            record = process_FS.process(source_cd, base_url, data)
        if source_cd == 'GS':
            record = process_GS.process(source_cd, base_url, data)
        if source_cd == 'HT':
            record = process_HT.process(source_cd, base_url, data)
        if source_cd == 'IBN':
            record = process_IBN.process(source_cd, base_url, data)
        if source_cd == 'IE':
            record = process_IE.process(source_cd, base_url, data)
        if source_cd == 'IG':
            record = process_IG.process(source_cd, base_url, data)
        if source_cd == 'IN':
            record = process_IN.process(source_cd, base_url, data)
        if source_cd == 'IT':
            record = process_IT.process(source_cd, base_url, data)
        if source_cd == 'KM':
            record = process_KM.process(source_cd, base_url, data)
        if source_cd == 'KR':
            record = process_KR.process(source_cd, base_url, data)
        if source_cd == 'MD':
            record = process_MD.process(source_cd, base_url, data)
        if source_cd == 'MM':
            record = process_MM.process(source_cd, base_url, data)
        if source_cd == 'MSN':
            record = process_MSN.process(source_cd, base_url, data)
        if source_cd == 'MZ':
            record = process_MZ.process(source_cd, base_url, data)
        if source_cd == 'NDTV':
            record = process_NDTV.process(source_cd, base_url, data)
        if source_cd == 'NR':
            record = process_NR.process(source_cd, base_url, data)
        if source_cd == 'OI':
            record = process_OI.process(source_cd, base_url, data)
        if source_cd == 'PB':
            record = process_PB.process(source_cd, base_url, data)
        if source_cd == 'RE':
            record = process_RE.process(source_cd, base_url, data)
        if source_cd == 'REDIFF':
            record = process_REDIFF.process(source_cd, base_url, data)
        if source_cd == 'RM':
            record = process_RM.process(source_cd, base_url, data)
        if source_cd == 'RMH':
            record = process_RMH.process(source_cd, base_url, data)
        if source_cd == 'SB':
            record = process_SB.process(source_cd, base_url, data)
        if source_cd == 'SH':
            record = process_SH.process(source_cd, base_url, data)
        if source_cd == 'SIFY':
            record = process_SIFY.process(source_cd, base_url, data)
        if source_cd == 'SULEKHA':
            record = process_SULEKHA.process(source_cd, base_url, data)
        if source_cd == 'TOI':
            record = process_TOI.process(source_cd, base_url, data)
        if source_cd == 'YAHOO':
            record = process_YAHOO.process(source_cd, base_url, data)
        if source_cd == 'ZNI':
            record = process_ZNI.process(source_cd, base_url, data)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)

