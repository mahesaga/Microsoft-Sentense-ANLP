import random
from collections import Counter

# function calculate the freq of the corse by i+1
# were i is the index of nth words.

def next_word_freq(array, sentence):
	
	sen_len, word_list = len(sentence.split()), []
	
	for i in range(len(array)):

		
		
		if ' '.join(array[i : i + sen_len]).lower() == sentence.lower():

			if i + sen_len < len(array) - 1:

				word_list.append(array[i + sen_len])

	# this function return the count of the word
	
	return dict(Counter(word_list))

# this function return the count of CDF from the counter dictonery


def CDF(d):
	
	prob_sum, sum_vals = 0, sum(d.values())
	
	for k, v in d.items():

		# evaluate the PMF by measuring each 
		# the freq. by total of all frequencies then add
		# all the PMFs till ith word which is the CDF of
		# the ith word.
		
		pmf = v / sum_vals
		prob_sum += pmf
		d[k] = prob_sum

	# Return cdf dictionary
	
	return d

# The main function reads the sentence/word as input
# from user and reads the corpus file. For faster processing,
# we have taken only the first 1000 words.


def main(sent, x, n):

	# it describe the simple text file.
	# anyone can use the text file for executing the code
	# for rading the file from corpus is attached below.

	# corpus = open('AH19334.txt','r').read()

	corpus = ''' is chance of project failure if code not executed properly.
                is described the programming language.
                is a chance of sucess.
                is define as the biggest industry.
                is known as the subsidary of the company.
                is a diversified country.
                is a chance of sucess of project if algorithms are executed properlly.
                is a largest raw mataril supplier company in the world.
    '''
	
	l = corpus.split()

	# "temp_out" will be used to store each partial sentence
	# which will later be stored into "sent". "out" is used to store
	# the final output.
	
	temp_out = ''
	out = sent + ' '
	
	for i in range(n - x):

		# calling the next_word_freq method that returns the frequency of each word next to sent in the whole word carpus
		
		func_out = next_word_freq(l, sent)

		# cdf_dict stores the cdf of each word in the above map that is calculated using method CDF.
		cdf_dict = CDF(func_out)
		
		# We use a random number to predict the next word. The word having its CDF greater than or equal to rand and less than or equal to 1.
		rand = random.uniform(0, 1)

		# If cdf_dict is empty, it means the word.sentence entered by you does not exist in the corpus. Hence, break the loop and just print
		# the word entered by you. To implement this we use try-except block. If an error occurs it implies there aren't enough values to unpack
		# and this can happen only when your input is absent from the corpus.
		try: key, val = zip(*cdf_dict.items())
		except: break

		# Iterate through the cdf values and find the smallest value greater than or equal to the random number. That value is the
		# cdf of your predicted word. Add the key of the value to the output string and update the "sent" variable as "temp_out".
		for j in range(len(val)):
			
			if rand <= val[j]:
				pos = j
				break
					
		temp_out = key[pos]
		out = out + temp_out + ' '
		sent = temp_out
	print(out, end = '\n\n')

if __name__ == '__main__':
	inp_sent = 'is'
	# output have the multipe samples
	main(inp_sent, len(inp_sent), 8)

