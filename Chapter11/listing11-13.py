# -*-coding:utf-8-*-

import fileinput, re


def process1(line):
    # pat = re.compile('From: (.*) <.*?>$')
    pat = re.compile('(line)')
    pat = re.compile('.*(line).*')
    pat = re.compile(r'.*(line).*')
    m = pat.match(line)
    if m: print m.group(1)
    # print line

def method_1(filename):
    for line in open(filename):
        pat = re.compile('Chapter[1-9]{1,2}.*:(.*)')
        m = re.findall(pat,line)
        for word in m:
            print word

def method_2(filename):
    f=open(filename).read()
    pat = re.compile('Chapter[1-9]{1,2}.*:(.*)')
    m = re.findall(pat,f)
    for word in m:
        print word


def testXML(filename='testxml.html'):
    f=open(filename).read()
    titlePad = re.compile(r'title=\"(.*?)\"')
    linkPad = re.compile(r'href=\"(.*?)\"')
    title = re.findall(titlePad,f)
    for word in title :
        if word.strip() == "":continue
        print word

    title = re.findall(linkPad, f)
    for word in title:
        if word.strip() == "": continue
        print word


# title="3度错失豪门的她，终于嫁给富二代了"
def test():
    filename='../README.txt'
    method_2(filename)

if __name__ == '__main__':
    # test()
    testXML()

