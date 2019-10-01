>>> def main():
	sentence = input("Please Enter Your Sentence: ")
	num_characters= len(sentence)
	print ("Number of characters:" , num_characters)
	num_words=len(sentence.split())
	print ("Number of words:", num_words)
	avg_word_length= float(num_characters/num_words)
	print("Average word length:", avg_word_length)

>>> main()
