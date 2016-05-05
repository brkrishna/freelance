# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         ps
# Purpose:      Power Supply, sample aggregation
#
# Author:       Ramakrishna
#
# Dated:        07/Apr/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import pandas as pd

#Assuming that the csv file is residing in the same folder, read the columns we need to reduce mem usage
df = pd.read_csv("keywords_elog.csv", usecols=['campaign_id','campaign_name', 'money_in_the_bank_paid_to_us', 'cost'])

result = df.groupby('campaign_name').agg({'money_in_the_bank_paid_to_us':sum, 'cost':sum})

result.to_csv("output.csv")


