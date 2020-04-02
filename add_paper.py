#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import argparse


def write_content(file_name, content):
    readme_file = open(file_name, "a+")
    readme_file.write('\n')
    readme_file.write(content)
    readme_file.close()


def create_file(file_name):
    file1 = open(file_name, 'w')
    file1.close()


def add_paper(args):
    tags = args.tags
    notes = args.notes  # "on the difficulty of training rnn"
    author = args.author
    pdf_address = args.pdf_address  # "https://arxiv.org/pdf/1211.5063.pdf"
    years = args.years

    github_address = "https://github.com/ffxz/PaperNotes/blob/master/"
    tags_address = "https://github.com/ffxz/PaperNotes/blob/master/tags/" + args.tags + ".md" #"https://github.com/ffxz/PaperNotes/blob/master/tags/train_method.md"
    notes_address = "https://github.com/ffxz/PaperNotes/blob/master/paper_list/" + args.notes + ".md"#https://github.com/ffxz/PaperNotes/blob/master/paper_list/on_the_difficulty_of_training_rnn.md"
    readme_line = "|[" + tags + "](" + tags_address + ")|[" + notes + "](" + notes_address + ")|" + author + " |[pdf](" + pdf_address +") |"
    write_content("README.md", readme_line)

    tags_line = "|[·]|[" + notes + "](" + notes_address + ")|" + years + "|"
    if not os.path.exists("tags/"+tags+'.md'):
        create_file("tags/"+tags+'.md')
    if os.path.exists("tags/"+tags+'.md'):
        write_content("tags/" + tags + '.md', "| num | paper | years |")
        write_content("tags/" + tags + '.md', "| ------ | ------ | ------ |")
        write_content("tags/"+tags+'.md', tags_line)

    notes_line1 = "|[一级笔记]|[" + notes + "](" + os.path.join(github_address, "level_1", args.notes+".md") + ")|"
    notes_line2 = "|[二级笔记]|[" + notes + "](" + os.path.join(github_address, "level_2", args.notes+".md") + ")|"
    notes_line3 = "|[三级笔记]|[" + notes + "](" + os.path.join(github_address, "level_3", args.notes+".md") + ")|"

    if not os.path.exists("paper_list/" + notes + '.md'):
        create_file("paper_list/" + notes + '.md')

    if os.path.exists("paper_list/" + notes + '.md'):
        write_content("paper_list/" + notes + '.md', "| level | content |")
        write_content("paper_list/" + notes + '.md', "| ------ | ------ |")
        create_file(os.path.join("level_1", args.notes+".md"))
        write_content("paper_list/" + notes + '.md', notes_line1)
        create_file(os.path.join("level_2", args.notes+".md"))
        write_content("paper_list/" + notes + '.md', notes_line2)
        create_file(os.path.join("level_3", args.notes + ".md"))
        write_content("paper_list/" + notes + '.md', notes_line3)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='add notes parser')
    parser.add_argument('--tags', type=str, required=True)
    parser.add_argument('--notes', type=str, required=True)
    parser.add_argument('--author', type=str, required=True)
    parser.add_argument('--pdf_address', type=str, required=True)
    parser.add_argument('--years', type=str, required=True)
    args = parser.parse_args()
    add_paper(args)



