import random
from twython import Twython
import time
import nltk
import enchant

class MarkovChain(object):
  d = enchant.Dict("en_US")
  chain = {}
  twitter = ""
  CONSUMER_KEY = 'RkQqA84KN38hydz2eMboomHCd'
  CONSUMER_SECRET = 'placeholder'
  ACCESS_KEY = '3450870856-FVeOp4H1OPiT1NNS2MrgAnzMQVlrjWBG7eUQgf7'
  ACCESS_SECRET = 'placeholder'
  def __init__(self):
    self.twitter = Twython(self.CONSUMER_KEY,
						   self.CONSUMER_SECRET,
						   self.ACCESS_KEY,
						   self.ACCESS_SECRET)
    statuses = self.twitter.get_user_timeline(screen_name="@C9Mang0",count=1)
    lis = [statuses[0]['id']]
    for i in range(0, 16): #16 ## iterate through all tweets
        newStatuses = self.twitter.get_user_timeline(screen_name="@C9Mang0",
        count = 200, include_retweets=False, max_id=lis[-1])
        time.sleep(0.5) ##300 # 5 minute rest between api calls
        for tweet in newStatuses:
            lis.append(tweet['id']) ## append tweet id's
        statuses += newStatuses[1:]
    #print [s['text'] for s in statuses]
    statuses = reduce(lambda acc,x: acc + [x['text']], statuses, [])
    
    self.chain = {}
    word1 = "\n"
    word2 = "\n"
    for line in statuses:
      for current_word in line.split():
        if current_word != "":
          self.chain.setdefault((word1, word2), []).append(current_word)
          word1 = word2
          word2 = current_word
  def chirrrp(self):

    word_count = random.randint(1,13)
    #word_count = 10
    generated_sentence = ""
    word_tuple = random.choice(self.chain.keys())
    w1 = word_tuple[0]
    w2 = word_tuple[1]

    for i in xrange(word_count):
      newword = random.choice(self.chain[(w1, w2)])
      generated_sentence = generated_sentence + " " + newword
      w1 = w2
      w2 = newword
    while self.d.check(newword):
      newword = random.choice(self.chain[(w1, w2)])
      generated_sentence = generated_sentence + " " + newword
      w1 = w2
      w2 = newword
    print "Tweeted: %s" % generated_sentence
    self.twitter.update_status(status=generated_sentence)
    
    

chain = MarkovChain()
chain.chirrrp()
