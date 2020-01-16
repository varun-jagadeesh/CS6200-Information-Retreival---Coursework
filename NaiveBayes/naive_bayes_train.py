import glob

# Initialization
total = 0

pos_word = dict()  # Pos word dictionary
neg_word = dict()  # Neg word dictionary

neg_docs = []  # negative documents
pos_docs = []  # positive documents

pos_word_count = dict()  # count of positive words
neg_word_count = dict()  # counts of negative words

pos_temp_list = []  # temporary positive list
neg_temp_list = []  # temporary negative list

temp_comb = dict() # combination of positive and negative

pos_top = dict() # dictionary for top positive
neg_top = dict() # dictionary for top negative

pos_temp_top_20 = dict()  # dictionary for top 20 positive
neg_temp_top_20 = dict() # dictionary for top 20 negative

pos_temp_dict = dict() # positive temporary dictionary
neg_temp_dict = dict() # negative temporary dictionary


def train_pos_neg_words():
    for files in glob.glob('/Users/varun/PycharmProjects/Hw-4/textcat/train/pos/*.txt'):
        # Opening all the files
        open_all_file = open(files, 'r')
        # reading all the text files
        read_text_file = open_all_file.read()
        # appending - positive
        pos_docs.append(read_text_file.split())
        for word in read_text_file.split():
            if word not in pos_word:
                pos_word[word] = 1

    for files in glob.glob('/Users/varun/PycharmProjects/Hw-4/textcat/train/neg/*.txt'):
        # Opening all the files
        open_all_file = open(files, 'r')
        # reading all the text files
        read_text_file = open_all_file.read()
        # appending - negative
        neg_docs.append(read_text_file.split())
        for word in read_text_file.split():
            neg_word[word] = 1


def pos_neg_words_count_dict():
    for files in glob.glob('/Users/varun/PycharmProjects/Hw-4/textcat/train/pos/*.txt'):
        # Opening all the files
        open_all_file = open(files, 'r')
        # reading all the text files
        read_text_file = open_all_file.read()
        for word in read_text_file.split():

            if word in pos_word_count:
                pos_word_count[word] = pos_word_count[word] + 1
            else:
                pos_word_count[word] = 1

    for files in glob.glob('/Users/varun/PycharmProjects/Hw-4/textcat/train/neg/*.txt'):
        # Opening all the files
        open_all_file = open(files, 'r')
        # reading all the text files
        read_text_file = open_all_file.read()
        for word in read_text_file.split():
            if word in neg_word_count:
                neg_word_count[word] = neg_word_count[word] + 1
            else:
                neg_word_count[word] = 1

    for i in pos_word.keys():
        pos_temp_list.append(i)

    for word in pos_temp_list:

        if word not in neg_word_count:
            if pos_word_count[word] < 5:
                del pos_word_count[word]
        else:
            if pos_word_count[word] + neg_word_count[word] < 5:
                del pos_word_count[word]
                del neg_word_count[word]

    for i in neg_word_count.keys():
        neg_temp_list.append(i)
    for word in neg_temp_list:
        if word not in pos_word_count:
            if neg_word_count[word] < 5:
                del neg_word_count[word]

    for i in pos_word_count:
        temp_comb[i] = []
    for i in neg_word_count:
        temp_comb[i] = []

    for i in pos_word_count:
        if i in neg_word_count:
            temp_comb[i].append(pos_word_count[i])
            temp_comb[i].append(neg_word_count[i])
        else:
            temp_comb[i].append(pos_word_count[i])
            temp_comb[i].append(0)
    for i in neg_word_count:
        if i not in pos_word_count:
            temp_comb[i].append(0)
            temp_comb[i].append(neg_word_count[i])


def create_file():
    f = open('model_file.txt', 'a')
    for key, value in temp_comb.items():
        print(key)
        f.write(key + ' ' + str(value[0]) + ' ' + str(value[1]))
        f.write('\n')
    f.close()


# Main function
def main():
    train_pos_neg_words()
    pos_neg_words_count_dict()
    create_file()

if __name__ == '__main__':
    main()
