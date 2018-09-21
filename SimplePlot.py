# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Jie Lin
# Python 3

#coding=utf-8
"""
@version: 1.1
@author: Jie Lin
@Mail: jlin246@emory.edu
@file: SimplePlot.py
@time: 09/19/2018 10:13pm
@purpose: for learning matplotlib api purpose
@code environment: ubuntu 18.01
"""

import numpy as np
#for data analysis
import pandas as pd 

#plotting library
import matplotlib.pyplot as plt 
from matplotlib import style


def plotLineChart():
	# read files and pd will automatically analyze it
	seqs = pd.read_csv('./csvfiles/GenbankStats.csv');

	#print the Date column
	print(seqs.loc[:,['Date']]);
	#similiar with the following commend. This one has no column name
	print(seqs.Date);

	#format Date column into yyyy-mm-dd
	seqs.Date = pd.to_datetime(seqs.Date, infer_datetime_format=True)
	print(seqs.loc[:,['Date']])

	#replace index with Date
	seqs.set_index('Date', inplace=True)
	print(seqs.index)

	# summed_bases_data=seqs['Bases'].resample('A').sum()
	# print(summed_bases_data)

	summed_sequences_data=seqs['Sequences'].resample('A').sum()
	print(summed_sequences_data)

	#font family ['normal'] not found
	#set up fonts for the text on the plot
	font = {'family' : 'normal',
		    'weight' : 'bold',
		    'size'   : 24};
	plt.rc('font',**font);

	# plot the summed data, also can change color from red to any other colors
	#ax=summed_data.plot(color='r');
	ax=summed_sequences_data.plot(color='b');

	# set scientific notation off on the y axis
	ax.get_yaxis().get_major_formatter().set_scientific(False);

	# set the plot title
	ax.set_title('Genbank Annual Sequence Submissions')

	#some questions at here
		#why it is plt.show(), but not ax.show()
	# set to print the legend and draw
	plt.legend()
	plt.show()



def plotBarChart():
	#show a bar graph
	# Read the data into a dataframe using Pandas
	medData=pd.read_csv('./csvfiles/processed.cleveland.data.csv')
	medDataDf = pd.DataFrame(medData)
	print(medDataDf)

	#Group people into Age-groups using bins. The arange function in numpy takes 
	# the start and end of the range and increment as arguments to create bins
	bins =  np.arange(20,90,10)
	# set the bin labels
	binLabels = ['21-30','31-40', '41-50', '51-60', '61-70', '71-80']
	# the cut function slices the Age column data and assigns them to the 
	# appropriate bins. This is grouped and size of each group is determined and 
	# saved 'patient_count'
	binData=medDataDf.groupby(pd.cut(medDataDf['Age'], bins=bins, labels=binLabels)).size().reset_index(name='patient_count')

	#Set up Fonts for the text on the plot
	font = {'family' : 'normal',
	   'weight' : 'bold',
	    'size'   : 24}
	plt.rc('font', **font)

	# set up the binned data and plot a bar graph
	barPlot = binData.plot.bar(rot=0, color="b", figsize=(12,8))
	barPlot.set_xticklabels(binLabels) # set x tick labels
	barPlot.set_ylabel('Number of Patients', labelpad=15) # set y label

	plt.legend();
	plt.show();

def plotHistogrm():
	# Read in the data into a dataframe
	medData=pd.read_csv('./csvfiles/processed.cleveland.data.csv')
	medDataDf = pd.DataFrame(medData)
	print(medDataDf)

	# show a histogram of certain data
	# Histogram data can be created using the histogram() function in numpy  
	# np.histogram bins the data into 10 equal sized bins
	hist, binEdges = np.histogram(medData['Age'])
	    
	print(hist)
	print(binEdges)    
	    
	# Alternatively, use matplotlib hist function directly to set up the binned
	# data and draw the histogram
	# matplotlib hist function will auto bin the data and present it as
	# a histogram

	n, bins, patches = plt.hist(x=medData['Age'], bins='auto', color='#0504aa',
	                        alpha=0.7, rwidth=0.85)
	print('------------------')
	print(bins)

	#Set up Fonts for the text on the plot
	font = {'family' : 'normal',
	    'weight' : 'bold',
	    'size'   : 24}
	plt.rc('font', **font)

	# the histogram set up by matplotlib can then be plotted
	plt.grid(axis='y', alpha=0.75)
	plt.xlabel('Age')
	plt.ylabel('Frequency')
	plt.title('Distribution of Data set by Age')

	plt.legend();
	plt.show();


if __name__ == '__main__':

	plotLineChart();
	plotBarChart();
	plotHistogrm();

	



	