# KindleNotidy
Sort out Kindle 'My Clippings.txt' and classify the notes according to the book.

It is a simple Script by Python, so just set the read_path (the 'My Clippings.txt' path) and write_path ( the output file path) and RUN it. You will get tidy notes soon :)

    read_path = 'path/My Clippings.txt'
    read_file = codecs.open(read_path, 'r', encoding='UTF-8')
    write_path = 'path/MyKindleNotes.txt'
    write_file = codecs.open(write_path, 'w', encoding='UTF-8')

这是一个整理Kindle笔记（My Clippings.txt）的小脚本，能够把Kindle中按时间记录混杂在一起的笔记按照书籍名称分门别类。

运行前请先设置下read_path跟write_path，你懂的~
