import os.path
import glob
import time
import matplotlib.pyplot as plt
import argparse
import sys as sys


def main(source_dir,target_dir):
    if not os.path.isdir(source_dir):
        print('Error: "%s" must be a directory' % source_dir, file=sys.stderr)
        return
    
    if target_dir is None:
        dirname = os.path.dirname(source_dir)
        out_path = dirname + "/Uppercase_converted_textfiles"

    if not os.path.exists(target_dir):
        print('Creating directory', target_dir)
        os.mkdir(target_dir)
        
    # This specifies that we want to look for all the files in a directory called "multiple_random_textfiles1"
    # that end in “.txt”.
    file_location = os.path.join(source_dir, '*.txt')
    # The output of the function glob is a list of all the filenames that fit the pattern specified in the input.
    # The input is the file location.
    filenames = glob.glob(file_location)
    x = []
    y = []
    i = 0
    start_time = time.time()
    x.append(i)
    end_time = time.time()
    y.append(end_time - start_time)
    for f in filenames:
        outfile = open(f, 'r')
        # filenames has a list with names in this format -'multiple_random_textfiles1\\file_0.txt'
        # therefore split name and add to path
        path = os.path.join(target_dir, f.split("\\")[1])
        fh = open(path, 'w')
        for line in outfile:
            line = line.upper()
            # for making the text bold
            # line = "\033[1m" + line #+ "\033[0m"
            # for underlining
            # line  ='\033[4m' + line + '\033[0m'
            fh.write(line)
        outfile.close()
        fh.close()
        if i in [99, 199, 299, 399, 499]:
            x.append(i)
            end_time = time.time()
            y.append(end_time - start_time)
        i += 1

    plt.plot(x, y, 'go-')
    plt.xlabel('Number of files(1mb each) -> ')
    plt.ylabel('Time taken (s) ->')
    plt.title(label="Time taken to convert 5k files to uppercase", fontsize=20, color="violet")
    plt.show()

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir")
    parser.add_argument("target_dir")
    args = parser.parse_args()
    main(args.source_dir, args.target_dir )
