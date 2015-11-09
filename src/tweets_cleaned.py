# example of program that calculates the number of tweets cleaned
import json
import unicodedata
import codecs
import re
import time
import math

def safe_open(fileName):
    '''test if file exist and catch error'''
    try:
        f = open(fileName)
    except IOError, e:
        return 'file does not exist'
    else:
        print('file exists and opened successfully')
        return f
    
def clean_tweets(tweets_file,output):
    '''extract and clean the relevant data for the Twitter JSON messages'''
    f = open(tweets_file)
    i=0
    #tweetsInfo = {}
    length=0
    for line in f:
        line = line.rstrip().lstrip()
        data = json.loads(line)
        length=length+1
        if ('created_at' in data and 'text' in data):
            time=data['created_at']
            content=data['text']
            non_content=strip_non_ascii(content)
            clean_text=re.sub(r'[\x00-\x1f\x7f-\xff]',' ', non_content)
            tweets=clean_text+' (timestamp: '+time+')\n'
            output.write(tweets)
##            print str(len(time))
            if(non_content!=content):
                i=i+1
    #<number of tweets that had unicode> tweets contained unicode.
    f.close()                
    print "file length"+str(length)
    return i
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def update_hashtag(tweets_file,output):
    '''continually update the Twitter hashtag graph and hence, the average degree of the graph.'''
    f = open(tweets_file)
    for line in f:
        if(line=='\n'):
            break
        else:
            line = line.rstrip().lstrip()
            #should find all hashtag
            hashtag_position=[m.start() for m in re.finditer('#', line)]
            #[hashtag_position.start() for hashtag_position in re.finditer('#', line)]
            #hashtag_position=line.find('#')
            if(len(hashtag_position)>1):
                #print hashtag_position
                #tag_end=[m.start()  line.find(' ', hashtag_position[m])]
                for m in range(0,len(hashtag_position)):
                    tag_end=line.find(' ', hashtag_position[m])
                    tag=line[hashtag_position[m]+1:tag_end]
                    print(tag.lower())
                    #output.write(tag.lower()+'\n')
                #output.write(line[-31:-1]+'\n')
                print(line[-31:-1])
##            for(n in range(0,len(hashtag_postion))):
##            [hashtag_position.start() for hashtag_position in re.finditer('#', line)]
##            tag_end=line.find(' ', hashtag_position)
##            tag=line[hashtag_position:tag_end]
##            if(tag!=''):

            
def bio_distribution(n,m):
    n1=math.factorial(n)
    n2=math.factorial(m)
    n3=math.factorial(n-m)   
    return n1/(n2*n3*1.0)

def main():
    '''feature 1'''
##    output=open("ft1.txt",'w')
##    m=clean_tweets("tweets-full.txt",output)
##    output.write('\n'+ str(m)+' tweets contained unicode.')
##    output.close()
    '''feature2'''
    
    #f=open("ft1.txt",'r')
    #f=open('tweets-feature2.txt','r')
    
    output=open("ft2.txt",'w')
    update_hashtag('tweets-feature2.txt',output)
    output.close()


#tweets_DB


if __name__ == '__main__':
    start_time = time.time()
    #main()
    print bio_distribution(5,2)
    print("--- %s seconds ---" % (time.time() - start_time))


    
