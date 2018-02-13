import os
import math

dir = os.getcwd()
#print dir
# Read the percentile that need to be calculated.
fullPath = os.path.join(dir,'..','input','percentile.txt');
#print fullPath
f = open(fullPath);
lines = f.readlines();
percentile = [int(line) for line in lines];
print percentile[0]
#print [int(line) for line in lines];
f.close();

# Read from campain donations.
fullPath = os.path.join(dir,'..','input','itcont.txt');
outputPath = os.path.join(dir,'..','output','repeat_donors.txt');
input = open(fullPath);
output = open(outputPath,'w');
donors = {};
recipients = {};
count = 0;
for line in input:
	print line;
	values = line.split('|');
	#print values;
	# Make sure the name and zip exists for the donor to be unique.
	# Also make sure it is from an individual and amount and cmte_id is not empty. 
	# Also, date length should be 8 digits.
	if (len(values[7]) > 0) and \
	   (len(values[10]) >= 5) and \
	   (len(values[15]) == 0) and \
	   (len(values[14]) > 0) and (len(values[0]) > 0) and (len(values[13]) == 8):
		#print values[7] + values[10][-5:];
		currentKey = values[7] + values[10][0:5]
		if (currentKey not in donors):
			donors[currentKey] = {'CMTE_ID' : values[0],
		                          'Name' : values[7],
								  'Zip': values[10][0:5], 
				                  'date':[values[13][-4:]], 
				                  'amt': [int(values[14])]};
		else:
			currentyear =  values[13][-4:];
			donors[currentKey]['date'].append(currentyear);
			donors[currentKey]['amt'].append(int(values[14]));
			currentrecId = values[0];
			if (currentrecId not in recipients):
				recipients[currentrecId] = {'Zip' : donors[currentKey]['Zip'],
				                                       'date' : currentyear,
                                                       'amt': [int(values[14])],
													   'transactions' : 1}
				pContbn = int(round((percentile[0] / 100) * 1))
				#print str(recipients[currentrecId]['amt'][pContbn])
				#print str(recipients[currentrecId]['amt'][0])
				output.write(currentrecId + '|' + donors[currentKey]['Zip'] + '|' + currentyear + \
				             '|' + str(recipients[currentrecId]['amt'][pContbn]) + '|' + str(recipients[currentrecId]['amt'][0])  +'|1' );	
				output.write('\n');					 
			else:
				if (recipients[currentrecId]['date'] == currentyear):
					recipients[currentrecId]['amt'].append(int(values[14]));
					pContbn = int(round((percentile[0] / 100) * len(recipients[currentrecId]['amt'])))
					#print str(recipients[currentrecId]['amt'][pContbn])
					#print recipients[currentrecId]['amt']
					#print sum(recipients[currentrecId]['amt'])
					output.write(currentrecId + '|' + donors[currentKey]['Zip'] + '|' + currentyear  + \
				             '|' + str(recipients[currentrecId]['amt'][pContbn]) + '|' + str(sum(recipients[currentrecId]['amt']))  +'|' +\
                             str(len(recipients[currentrecId]['amt'])))
					output.write('\n');
			
		
	
print donors;
input.close()
output.close()