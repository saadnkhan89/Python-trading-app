#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas_datareader as pdr
import datetime
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt 
import statsmodels.api as sm
from dateutil.parser import parse


# In[4]:


def TRADE(stk,mtd,st_dte,end_dte,short_avg,long_avg):
        #strt=parse(st_dte)
        #strt=strt.strftime('%Y/%m/%d')
        #if end_dte=='now':
        #    end=datetime.datetime.now()
        #else:
        #    end=parse(end_dte)
        #    end=end.strftime('%Y/%m/%d')
        end=datetime.datetime.now()
        st_dte="2016-01-01"
        strt=parse(st_dte)
        strt=strt.strftime('%Y/%m/%d')
        df=pdr.get_data_yahoo(stk, strt, end)
        sig_df=pd.DataFrame(index=df.index)
        sig_df['Close']=df.Close
        sig_df['signal']=0
        sig_df['short_moving_average']=df.Close.rolling(window=short_avg,min_periods=1, center=False).mean()
        sig_df['long_moving_average']=df.Close.rolling(window=long_avg,min_periods=1, center=False).mean()
        r_sma,c_sma=np.shape(sig_df)
        idx=list(range(0,r_sma))
        if mtd=='Mean Reversion Strategy':
            sig_df['signal'][short_avg:]=np.where(sig_df['short_moving_average'][short_avg:]<
                                          sig_df['long_moving_average'][short_avg:],1,0)
            sig_df['position']=sig_df['signal'].diff()
        elif mtd=='Crossover Strategy':
            sig_df['signal'][short_avg:]=np.where(sig_df['short_moving_average'][short_avg:]>
                                          sig_df['long_moving_average'][short_avg:],1,0)
            sig_df['position']=sig_df['signal'].diff()
        fig=plt.figure()
        axis_font = {'fontname':'Arial', 'size':'24'}
        if mtd=='Mean Reversion Strategy':
            ax1=fig.add_subplot(111)
            ax1.plot(idx,df['Close'], color='r', lw=1)
            ax1.plot(idx,sig_df['short_moving_average'], color='b', lw=2)
            ax1.plot(idx,sig_df['long_moving_average'], color='y', lw=2)
            #ax1.plot(sig_df.loc[sig_df.position==1].index,sig_df.short_moving_average[sig_df.position==1],
            # '^', markersize=10, color='m')
            #ax1.plot(sig_df.loc[sig_df.position==-1].index,sig_df.short_moving_average[sig_df.position==-1],
            # 'v', markersize=10, color='k')
            #plt.title('Mean Reversion Strategy',fontsize=40)
            #plt.gca().legend(('Closing Price','Short Moving Avg','Long Moving Avg','Buy','Sell'),fontsize=16)
            #plt.xlabel("Date", **axis_font)
            #plt.ylabel("Price", **axis_font)
        elif mtd=='Crossover Strategy':
            ax1=fig.add_subplot(111)
            ax1.plot(idx,df['Close'], color='r', lw=1)
            ax1.plot(idx,sig_df['short_moving_average'], color='b', lw=2)
            ax1.plot(idx,sig_df['long_moving_average'], color='y', lw=2)
            #ax1.plot(sig_df.loc[sig_df.position==1].index,sig_df.short_moving_average[sig_df.position==1],
            # '^', markersize=10, color='m')
            #ax1.plot(sig_df.loc[sig_df.position==-1].index,sig_df.short_moving_average[sig_df.position==-1],
            # 'v', markersize=10, color='k')
            #plt.title('Crossover Trading Strategy',fontsize=40)
            #plt.gca().legend(('Closing Price','Short Moving Avg','Long Moving Avg','Buy','Sell'),fontsize=16)
            #plt.xlabel("Date", **axis_font)
            #plt.ylabel("Price", **axis_font)
        #plt.grid(True)
        #fig.set_size_inches(18.5, 10.5)
        #plt.rcParams.update({'font.size': 10})
        return idx


# In[ ]:





# In[ ]:




