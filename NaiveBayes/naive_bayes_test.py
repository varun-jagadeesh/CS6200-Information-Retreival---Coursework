import math
import glob

# Initialization
total = 0

pos_top = dict()  # dictionary for top positive
neg_top = dict()  # dictionary for top negative

pos_temp_top_20 = dict()  # dictionary for top 20 positive
neg_temp_top_20 = dict()  # dictionary for top 20 negative

pos_temp_dict = dict()  # positive temporary dictionary
neg_temp_dict = dict()  # negative temporary dictionary


def open_file():
    open_file_1 = open('model_file.txt', 'r')
    read_open_file_1 = open_file_1.readlines()
    for lines in read_open_file_1:
        if int(lines.split()[1]) != 0:
            pos_temp_dict[lines.split()[0]] = int(lines.split()[1])
        if int(lines.split()[2]) != 0:
            neg_temp_dict[lines.split()[0]] = int(lines.split()[2])


def find_prob(file_name, new_file):
    pos = 0
    neg = 0
    text_file = glob.glob(file_name)
    for files in range(len(text_file)):

        open_text_file = open(text_file[files], 'r')
        read_file = open_text_file.read()
        split_text = read_file.split()
        rank = 0

        temp_new = dict()

        for i in split_text:
            if i not in pos_temp_dict:
                rank = rank + 1
                temp_new[i] = 0

        pos_prob = dict()
        temp = 0
        pos_prob_temp = 0
        if rank == 0:
            for j in pos_temp_dict:
                pos_prob[j] = pos_temp_dict[j] / sum(pos_temp_dict.values())
            for k in split_text:
                pos_prob_temp = pos_prob_temp + math.log(pos_prob[k])
        else:

            for l in split_text:
                if l in pos_temp_dict:
                    pos_prob_temp = pos_prob_temp + math.log(
                        (pos_temp_dict[l] + 1) / (len(pos_temp_dict) + sum(pos_temp_dict.values()) + len(temp_new)))
                    temp = temp + 1
                else:
                    pos_prob_temp = pos_prob_temp + math.log(
                        1 / (len(pos_temp_dict) + sum(pos_temp_dict.values()) + len(temp_new)))
                    temp = temp + 1

        neg_prob_temp = 0
        neg_rank = 0
        temp_new_neg = dict()
        for a in split_text:
            if a not in neg_temp_dict:
                neg_rank = neg_rank + 1
                temp_new_neg[a] = 0

        neg_prob = dict()

        if neg_rank == 0:
            for d in neg_temp_dict:
                neg_prob[d] = neg_temp_dict[d] / sum(neg_temp_dict.values())

            for d in split_text:
                neg_prob_temp = neg_prob_temp + math.log(neg_prob[d])
        else:
            for d in split_text:
                if d not in neg_temp_dict:
                    neg_prob_temp = neg_prob_temp + math.log(
                        1 / (len(neg_temp_dict) + len(temp_new_neg) + sum(neg_temp_dict.values())))
                else:
                    neg_prob_temp = neg_prob_temp + math.log((neg_temp_dict[d] + 1) / (
                            len(neg_temp_dict) + sum(neg_temp_dict.values()) + len(temp_new_neg)))
            print(text_file[files])

            print('Positive Prob:', pos_prob_temp)
            print('Negative Prob: ', neg_prob_temp)

            out_text_files = open(new_file, "a")

            out_text_files.write("\n")
            out_text_files.write("File: " + str(text_file[files]) + "\n")
            out_text_files.write("Positive Prob" + str(pos_prob_temp) + "\n")
            out_text_files.write("Negative Prob" + str(neg_prob_temp) + "\n")

            if pos_prob_temp > neg_prob_temp:
                print('Positive File')
                out_text_files.write("Positive Review" + "\n" + "\n")

            else:
                print('Negative File')
                out_text_files.write("Negative Review" + "\n" + "\n")

            print('\n')
            out_text_files.close()

        if pos_prob_temp > neg_prob_temp:
            pos = pos + 1

        else:
            neg = neg + 1

    out_no_pos_neg_prob = open(new_file, "a")

    out_no_pos_neg_prob.write("No of Positive" + str(pos) + "\n")
    out_no_pos_neg_prob.write("No of Negative" + str(neg) + "\n")

    out_no_pos_neg_prob.close()

    print('No of Positive ', pos)
    print('No of Negative ', neg)


def top_pos_neg():
    for k in pos_temp_dict:
        pos_top[k] = pos_temp_dict[k] / sum(pos_temp_dict.values())
    for k in neg_temp_dict:
        neg_top[k] = neg_temp_dict[k] / sum(neg_temp_dict.values())

    # Top Positive
    for k in pos_top:
        if k in neg_top:
            pos_temp_top_20[k] = math.log(pos_top[k] / neg_top[k])
    # Top Negative
    for k in neg_top:
        if k in pos_top:
            neg_temp_top_20[k] = math.log(neg_top[k] / pos_top[k])
    # Top 20 pos neg ratio

    print('TOP 20 pos neg ratio')
    print(sorted(pos_temp_top_20.items(), key=lambda x: x[1], reverse=True)[0:20])
    print('\n')

    # Writing in a file
    top_20_pos_neg_ratio = open("top_20_pos_neg_ratio.txt", "w")
    top_20_pos_neg_ratio.write("TOP 20 pos neg ratio" + '\n')
    top_20_pos_neg_ratio.write(str(sorted(pos_temp_top_20.items(), key=lambda x: x[1], reverse=True)[0:20]))
    top_20_pos_neg_ratio.close()

    # Top 20 neg pos ratio

    print('TOP 20 neg pos ratio')
    print(sorted(neg_temp_top_20.items(), key=lambda x: x[1], reverse=True)[0:20])

    # Writing in a file
    op_20_neg_pos_ratio = open("top_20_neg_pos_ratio.txt", "w")
    op_20_neg_pos_ratio.write("TOP 20 neg pos ratio" + '\n')
    op_20_neg_pos_ratio.write(str(sorted(neg_temp_top_20.items(), key=lambda x: x[1], reverse=True)[0:20]))
    op_20_neg_pos_ratio.close()


# Main function
def main():
    open_file()
    # passing path and the file name for creating a new file for dev positive
    find_prob('/Users/varun/PycharmProjects/Hw-4/textcat/dev/pos/*.txt', 'dev_pos.txt')
    # passing path and the file name for creating a new file for dev negative
    find_prob('/Users/varun/PycharmProjects/Hw-4/textcat/dev/neg/*.txt', 'dev_neg.txt')
    # passing path and the file name for creating a new file for test
    find_prob('/Users/varun/PycharmProjects/Hw-4/textcat/test/*.txt', 'test.txt')
    top_pos_neg()


if __name__ == '__main__':
    main()
