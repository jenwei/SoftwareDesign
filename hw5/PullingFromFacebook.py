# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:28:21 2014

@author: CharlieMouton and JenniferWei

Charlie's fb code: CAAEuAis8fUgBANEcpy6pnuIwr8IZBLFo3MT7N2m2xbgkecbZCps2CTbm3OY
fN9nbLZAS8ZBQaVzqGPMcfP3p4Dma1eH2YRvNGxGLr4xzPuSpZBsYAVi4BMPUp7HTaNkbNddDEZC9Z
Blt5zC3bf9HICmYAJFPZC7mU4zQFHksF1eTRlf9E2RpypFhZBJ3tqkYYCKwZD


"""

from pattern.web import *
import numpy
import re
f = Facebook(license='CAAEuAis8fUgBANEcpy6pnuIwr8IZBLFo3MT7N2m2xbgkecbZCps2CTbm3OYfN9nbLZAS8ZBQaVzqGPMcfP3p4Dma1eH2YRvNGxGLr4xzPuSpZBsYAVi4BMPUp7HTaNkbNddDEZC9ZBlt5zC3bf9HICmYAJFPZC7mU4zQFHksF1eTRlf9E2RpypFhZBJ3tqkYYCKwZD')
me = f.profile()
#print me #prints out information of license (id,name,birthday,gender,country)
listOfFriends = ["Keith Runde Jones","Mia McDonald","Dylan Wagner",
                 "Libby Brudner","Casey Alvarado"] #list of posts to compare
textDict = {} #INSERT COMMENT HERE
wordCounts = {} #Dictionary of words with words as the keys and a list as
                #as the value that stores the wordCounts for each friend 
my_friends = f.search(me[0], type=FRIENDS, count=1000)


def cleanup(friend_name,posts):
    """
    Takes the list of posts taken directly from lFacebook and removes all 
    automatic Facebook posts like "BLANK and BLANK are now friends."
    
    posts: list of newsfeed text
    friend_name = name of newsfeed owner
    
    returns: modPosts = modified list of newsfeed text
    """
    modPosts = []
    for post in posts:
        #post = post.decode("UTF-8")
        if not friend_name in post:
            modPosts.append(str(post))
    return modPosts


def access_newsfeed(frnd):
    """
    access_newsfeed takes in the information of a friend, accesses their 
    newsfeed, and puts all of it into a dictionary, where the key is the 
    name and the value is the newsfeed text list.
    
    frnd: is the newsfeed information for a specified friend
    
    returns: value (list of newsfeed text) from the textDictionary for that
    specific friend
    """
    textList = []
    friend_news = f.search(frnd.id, type=NEWS, count=100)
    for news in friend_news:
        textList.append((news.text).decode("UTF-8"))
    textList = cleanup(frnd.author[1],textList)
    textDict[frnd.author[1]] = textList
    return textDict[frnd.author[1]]
    

    

def facebook_pull(specific_friend):
    """
    facebook_pull pulls the newsfeed information for a specific friend.
    specific_friend: name of specific friend as a string
    
    returns: list of posts from the newsfeed of the specific friend
    """
    
    for friend in my_friends:
        temp_name = friend.author[1]
        
        if (temp_name == specific_friend):
            friendPost = access_newsfeed(friend)
            return friendPost
            
def recursive_flatten(input):
    """
    recursive_flatten takes a list of nested lists (input) and unpacks it to 
    return one, long list

    input: list of nested lists    
    
    returns: single list of all values in all the nested lists
    """
    new_list = []

    for item in input:
        if type(item) != list:
            new_list.append(item)
        elif type(item) == list:
            new_list += recursive_flatten(item)
    return new_list

def histogram():
    """
    histogram takes the list of friends, pulls in their facebook newsfeed, 
    breaks the posts into a list of words, and takes all the lists of words 
    from each post and flattens it into one large list.
    
    listOfFriends: list of strings that contains the names of friends being 
    compared
    
    returns: dictionary of words and their values (values are the word 
    counts for each friend in the comparison)
    """
    #Takes each friend, takes the words on their newsfeed, and puts it into 
    #a larger list
    for friend in listOfFriends:
        wordList = []
        facebook_pull(friend)
        stringList = textDict[friend]
        for strng in stringList:
            strng = strng.lower()
            wordList.append(re.findall("[a-zA-Z']+",strng))
            wordList = recursive_flatten(wordList)
        textDict[friend] = wordList
    
    #Loops through all the words for each person and tallies up the count 
    #in the appropriate location within the value list
    counter = 0
    for c in textDict:
        for d in textDict[c]:
            if d not in wordCounts:
                wordCounts[d] = [0]*len(listOfFriends)
                (wordCounts[d])[counter] = 1
            else:
                (wordCounts[d])[counter] += 1
            
        counter += 1
    #print wordCounts USED TO SEE DICTIONARY OR WORDS AND THE VALUE LIST
    return wordCounts
    
def textSimilarity(wordCounts):
    """
    textSimilarity takes in the wordCounts, creates a vector of its normalized
    value list, creates a second vector that stores the values after computing 
    the cosine similarity between the words
    
    wordCounts: dictionary of words and their values (values are the word 
    counts for each friend in the comparison)
    
    returns: name (type: string) of least similar friend out of listOfFriends
    """
     
   #Creates a vector of normalized the normalized value list 
    vectors = [[]]*len(wordCounts[wordCounts.keys()[0]])
    for i in xrange(len(vectors)):
        vectors[i]=[]
    for w in wordCounts:
        counter = 0
        for vals in wordCounts[w]: #vals = list of values for each friend i.e. 3
            vectors[counter].append(float(vals)/float(len(textDict[listOfFriends[counter]])))
            counter += 1
            
    #Creates a vector after computing the cosine similarity
    sim = [[]]*len(vectors)
    for i in xrange(len(sim)):
        sim[i] = []
    counter = 0
    for v in vectors:
        for n in range(len(vectors)):
            sim[counter].append(numpy.dot(v,vectors[n])/(numpy.linalg.norm(v)*numpy.linalg.norm(vectors[n])))
        counter += 1

    print "Table of (Dis)Similarities: \n", sim
    
    for n in range(len(sim)):
        sim[n] = sum(sim[n])
    print "Sum of Similarities for Each Friend: \n", sim
    oddOne = sim.index(min(sim)) #Index of "odd" friend
    return listOfFriends[oddOne]
            
#TEST FOR textSimilarity
print "\n WHO IS THE ODD ONE OUT?\n"
odd = textSimilarity(histogram())
print "\nTHE ODD ONE OUT IS: \n",odd