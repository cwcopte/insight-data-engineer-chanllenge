# example of program that calculates the number of tweets cleaned
import json
import unicodedata
import codecs
def create_actors_DB(actor_file):
    '''Create a dictionary keyed on actors from a text file'''
    f = open(actor_file)
    movieInfo = {}
    for line in f:
        line = line.rstrip().lstrip()
        actorAndMovies = line.split(',')
        actor = actorAndMovies[0]
        movies = [x.lstrip().rstrip() for x in actorAndMovies[1:]]
        #movieInfo[actor] = set(movies)
        movieInfo[actor] = movies
    f.close()
    return movieInfo
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def main():
    #actor_DB = create_actors_DB('movies.txt')
    #<contents of "text" field> (timestamp: <contents of "created_at" field>)
    #remove escape characters (e.g. \n, \", \/ ) and unicode 
    json_data=open("tweets.txt").read()
    data = json.loads(json_data)
    time=data['created_at']
    content=data['text']
    print(time)
    print(strip_non_ascii(content))
    print json_data.decode('utf-8').encode('unicode-escape')
    #content.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', content)
    #print(content.decode('ascii'))
    #print(type(data))
    #print content.encode("utf8")
    #print(content.decode('unicode_escape').encode('ascii','ignore'))
'''
    infile = codecs.open('tweets.txt','r',encoding='utf-8',errors='ignore')
    for line in infile.readlines():
        print line;
    infile.close()
    '''
    #output=json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
   # print output

if __name__ == '__main__':
    main()

    
