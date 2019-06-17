import csv
import sys
import random
class TilePool(object):
    """initialize self arguments"""
    def __init__(self):
        self._pool = {}
        self._num_initial_tile=0
        self._num_pop_tile=0
        #read in a tile set from tiles.csv
        self.read_tile()



    def read_tile(self):
        with open('tiles.csv','r') as tiles_csv:
            tilereader = csv.DictReader(tiles_csv)
            #build pool 2D-dictionary {word:{value:count}}
            for row in tilereader:
                self._pool[row['letter']] = {}
                self._pool[row['letter']]['count'] = int(row['count'])
                self._num_initial_tile+=int(row['count'])
                self._pool[row['letter']]['value'] = int(row['value'])


    def __len__(self):
        #keep tracking how many tile left in pool
        return self._num_initial_tile-self._num_pop_tile

    #tile_count set defult to 7
    def pop(self,tile_count=7):
        self._list_letter=[]
        #check the type of tile_count is numberic
        if type(tile_count)==int and tile_count<=7 and tile_count >=1:
            # check if there is enough tiles in the pool can be popped
            if  self.__len__()<tile_count:
                #Tiles left in pool are less than 7
                raise Exception('You cannot pop {} tiles because there are only {} tile(s) left pool'.format(tile_count,self.__len__()))
            else:
                for i in range(tile_count):
                    #random select tile from tile set
                    letter=random.choice(list(self._pool.keys()))
                    self._list_letter.append(letter)
                    self._pool[letter]['count']-=1
                    self._num_pop_tile+=1
                    #remove tile from tile set if its count equal to 0
                    if self._pool[letter]['count']==0:
                        del self._pool[letter]
        #tile_count doesn't take invalid type of argument
        else:
            raise Exception('pop() takes numeric value between 1 and 7 or return 7 random tiles if no argument pass')
        return self._list_letter


class WordFinder(TilePool):
    """docstring for WordFinder."""
    def __init__(self):
        self._wordDict={}
        #read word_dictionary.txt at runtime
        self.read_wordDict()

    def read_wordDict(self):
        TP=TilePool()
        with open('word_dictionary.txt','r') as wd:
            lines=wd.readlines()
            lines=map(str.strip,lines)
            for words in lines:
                score=0
                for word in words:
                    #calculate each word's score
                    score+=TP._pool[word]['value']
                self._wordDict[words]=score

    def list_words(self,letterList,crossletter):
        TP=TilePool()
        results=[]
        words=[]
        for word in self._wordDict.keys():
            temp_letterList=list(letterList)
            temp_letterList.append(crossletter)
            #length of a word cannot be longer than the length of letterlist plus crossletter
            if len(word)<= len(temp_letterList) and crossletter in word:
                count=len(word)
                for letter in word:
                    if letter not in temp_letterList:
                        break
                    else:
                        count-=1
                        temp_letterList.remove(letter)
                    if count==0:
                        words.append(word)
        for i in words:
            #cross tiles do not count towards the word's score and item in tuple
            results.append((i,self._wordDict[i]-TP._pool[crossletter]['value']))
        #results are sorted by score in dedcending order and result can be empty
        results.sort(key=lambda res:res[1],reverse=True)
        print(results)
        return results
