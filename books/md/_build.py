import pandas as pd
import markdown2
from markdown2 import markdown_path

def build(shortName, title, author, ISBN, yearPublished, yearRead):
    with open('_head.html') as f:
        head = [x.strip('\n,') for x in f]
   
    with open('_foot.html') as f:
        foot = [x.strip('\n,') for x in f]
    
    head = [x.strip() for x in head]    
    foot = [x.strip() for x in foot]

    for line in range(len(head)):
        head[line] = head[line].replace('#SHORTNAME#',shortName)
        head[line] = head[line].replace('#TITLE#',title)
        head[line] = head[line].replace('#AUTHOR#',author)
        head[line] = head[line].replace('#ISBN#',str(ISBN))
        head[line] = head[line].replace('#YEARPUBLISHED#',str(yearPublished))
        head[line] = head[line].replace('#YEARREAD#',str(yearRead))
            
    with open(shortName+'.md') as f:
        md = [x.strip('') for x in f]
    
    mdString = ''.join(md)
    content = markdown2.markdown(mdString, extras=['footnotes','smarty-pants','cuddled-lists','target-blank-links','tables','header-ids','break-on-newline'])
    content = [content]
    doc = head+content+foot

    with open('../'+shortName+'.html', mode='wt', encoding='utf-8') as myfile:
        for lines in doc:
            myfile.write(''.join(lines))
            myfile.write('\n')
    print('\tSaved {}.html'.format(shortName))


df = pd.read_excel('_content.xlsx',
        converters={'shortName':str,'title':str,'author':str,'ISBN':str,'yearPublished':str,'yearRead':str})
for row in range(df.shape[0]):
    shortName       = df.loc[df.index[row],'shortName']
    title           = df.loc[df.index[row],'title']
    author          = df.loc[df.index[row],'author']
    ISBN            = df.loc[df.index[row],'ISBN']
    yearPublished   = df.loc[df.index[row],'yearPublished']
    yearRead        = df.loc[df.index[row],'yearRead']
    build(shortName, title, author, ISBN, yearPublished, yearRead)