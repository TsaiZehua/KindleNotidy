__author__ = 'tsaizehua'
# encoding=utf8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import codecs

if __name__ == "__main__":
    read_path = 'C:\\Users\\tsaizehua\\Desktop\\My Clippings.txt'
    read_file = codecs.open(read_path, 'r', encoding='UTF-8')
    write_path = 'C:\\Users\\tsaizehua\\Desktop\\MyKindleNotes.txt'
    write_file = codecs.open(write_path, 'w', encoding='UTF-8')

    # ========== Mark the single-note separator
    is_separator = True
    # Mark the single-note line number
    row_number = 0

    # collect the whole notes: key is the book title, value is a list contains the book's notes
    dict_book_notes = {}
    for line in read_file:
        line = line.strip()
        row_number += 1

        if u"===" in line:
            is_separator = True
            row_number = 0
        else:
            # book title is on top of separator
            if is_separator:
                book_name = line
                is_separator = False

            # filter insignificant lines
            # maybe you need to change the key words according to your language
            if u"- 您在位置" in line or len(line) == 0:
                pass

            # the line 4 is always the note
            if row_number == 4 and len(line) != 0:
                notes = []
                if book_name not in dict_book_notes:
                    dict_book_notes[book_name] = notes
                else:
                    notes = dict_book_notes[book_name]

                notes.append(line)

    # iterate and output the books and its notes
    for book_name, notes in dict_book_notes.items():
        # book name
        write_file.write('='*20 + '\n' + book_name + '\n')

        # note line number, you may delete it
        row_number = 1
        for notes in notes:
            write_file.write(str(row_number) + '. ' + notes + '\n')
            row_number += 1
        write_file.write('\n\n')