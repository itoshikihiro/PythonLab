# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Jie Lin
# Python 3

#coding=utf-8
"""
@version: 1.1
@author: Jie Lin
@Mail: jlin246@emory.edu
@file: PandasLearning.py
@time: 09/19/2018 9:42pm
@purpose: for learning Pandas api purpose
@code environment: ubuntu 18.01
"""

#import padas library
import pandas as pd

if __name__ == '__main__':
    seqs = pd.read_csv('./csvfiles/GenbankStats.csv');
    #surpress scientific notation
    pd.set_option('display.float_format', lambda x: '%.3f' % x);
    #print what seqs is
    print(seqs);

    #just print the Release column
    print(seqs.Release);

    #print the Bases column, which is not shown in print(seqs)
    print(seqs.Bases);

    #print each number column's mean
    print(seqs.mean());

    #print the original Date column
    print(seqs.Date);
    #change the original Date to certain format yyyy-mm-dd
    seqs.Date = pd.to_datetime(seqs.Date, infer_datetime_format=True);
    #print the changed Date
    print("changed Date:");
    print(seqs.Date);

    #print certain row of certain column
    #print from tenth row to fifteenth row in Sequences column
    print(seqs.loc[10:15,['Sequences']]);

    #set index to Date column and print
    seqs.set_index('Date', inplace=True);
    print(seqs.Sequences);True


    #group by year and sum Sequences in that year
    summed_date = seqs['Sequences'].resample('A').sum();
    print(summed_date);
