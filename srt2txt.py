import pysrt
import os
import sys
import re


def convert_srt_to_text(srt_file):
    text_file = open(os.path.basename(srt_file) + ".txt", 'w')

    subs = pysrt.open(srt_file, encoding='utf-8')

    text_content = ' '.join([sub.text for sub in subs])

    text_file.write(text_content.replace('\n', '').replace('.', '.\n'))
    text_file.close()

    print ('Converted {0}'.format(srt_file))


def convert_all_srt_to_text(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        for srt_file in files:
            filepath = subdir + os.sep + srt_file

            if filepath.endswith('.srt'):
                convert_srt_to_text(filepath)



def main():
    if len(sys.argv) < 1:
        print ('Please include the path to operate on.')
        sys.exit(0)

    fn = sys.argv[1]
    convert_all_srt_to_text(fn)

if __name__ == '__main__':
    main()