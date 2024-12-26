import csv

words = []
val = []
valuesoftxt = []
toanalyze = []

def csvthing():
    with open("cleanSentiment.CSV", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            words.append(line[0]) 
            val.append(float(line[1]))

def txttolist(txt):
    with open(txt, "r") as my_file:
        data = my_file.read()
    
    wordstext = data.replace('\n', ' ').split()
    
    return wordstext

def values(txt):
    global valuesoftxt
    wordstext = txttolist(txt)
    word_to_value = dict(zip(words, val))
    
    for word in wordstext:
        if word in word_to_value:
            valuesoftxt.append(word_to_value[word])

def calculate(vals):
    if len(vals) == 0:
        return 0

    sentiment_value = sum(vals)
    
    return sentiment_value

def compute(nameoffile):
    global words, val, toanalyze, valuesoftxt
    csvthing()
    values(nameoffile)
    print(f"\nThe sentiment value of the file '{nameoffile}' is: ")
    sentiment_value = calculate(valuesoftxt)
    print(sentiment_value)

    return sentiment_value

def main():
    num = (int) (input("Please enter the number of files you would like to process (number must be greater than 0): "))
    y = 0.000000

    for i in range(num):
        file = input("\nPlease enter the filename for the text (e.g., positive.txt, negative.txt): ")

        global valuesoftxt, toanalyze
        valuesoftxt = []
        toanalyze = []

        print("\nProcessing sentiment value for the provided text...")
        y = y + compute(file)
    
    print("\n The average sentiment value across all the text files is: "+(str) ((y/(float) (num))))




main()
