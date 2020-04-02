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


def insert_notes(path, content, line=0):
    lines = []
    with open(path) as r:
        for l in r:
            lines.append(l)
    if line == 0:
        lines.insert(0, '{}\n'.format(content))
    else:
        lines.insert(line-1, '{}\n'.format(content))
    s = ''.join(lines)
    with open(path, 'w') as m:
        m.write(s)


def add_paper(args):
    tags = args.tags
    notes = args.notes
    notes = notes.replace(' ', '_')
    author = args.author
    pdf_address = args.pdf_address
    years = args.years

    github_address = "https://github.com/ffxz/PaperNotes/blob/master/"
    tags_address = github_address + "tags/" + args.tags + ".md"
    notes_address = github_address + "paper_list/" + notes + ".md"
    readme_line = "|[" + tags + "](" + tags_address + ")|[" + notes.replace('_', ' ') + "](" + notes_address + ")|" + author + " |[pdf](" + pdf_address +")|" + years + "|"
    #write_content("README.md", readme_line)
    insert_notes("README.md", readme_line, 3)

    if os.path.exists("tags/"+tags+'.md'):
        #read first num
        tags_file = open("tags/"+tags+'.md', 'r')
        lines = tags_file.readlines()
        num = str(int(lines[3][2])+1)
        tags_line = "|[" + num + "]|[" + notes.replace('_', ' ') + "](" + notes_address + ")|" + years + "|"
        #write_content("tags/" + tags + '.md', tags_line)
        insert_notes("tags/" + tags + '.md', tags_line, 4)
    if not os.path.exists("tags/"+tags+'.md'):
        create_file("tags/"+tags+'.md')
        write_content("tags/" + tags + '.md', "| num | paper | years |")
        write_content("tags/" + tags + '.md', "| ------ | ------ | ------ |")
        tags_line = "|[1]|[" + notes.replace('_', ' ') + "](" + notes_address + ")|" + years + "|"
        write_content("tags/" + tags + '.md', tags_line)

    notes_line1 = "|[一级笔记]|[" + notes.replace('_', ' ') + "](" + os.path.join(github_address, "level_1", notes+".md") + ")|"
    notes_line2 = "|[二级笔记]|[" + notes.replace('_', ' ') + "](" + os.path.join(github_address, "level_2", notes+".md") + ")|"
    notes_line3 = "|[三级笔记]|[" + notes.replace('_', ' ') + "](" + os.path.join(github_address, "level_3", notes+".md") + ")|"

    if not os.path.exists("paper_list/" + notes + '.md'):
        create_file("paper_list/" + notes + '.md')
        write_content("paper_list/" + notes + '.md', "| level | content |")
        write_content("paper_list/" + notes + '.md', "| ------ | ------ |")

    if os.path.exists("paper_list/" + notes + '.md'):
        create_file(os.path.join("level_1", notes+".md"))
        write_content("paper_list/" + notes + '.md', notes_line1)
        create_file(os.path.join("level_2", notes+".md"))
        write_content("paper_list/" + notes + '.md', notes_line2)
        create_file(os.path.join("level_3", notes + ".md"))
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



