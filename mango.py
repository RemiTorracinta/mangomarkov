import random
import twitter

class MarkovChain(object):
  chain = {}
  api = ""

  def __init__(self):
    self.api = twitter.Api(
          consumer_key='RkQqA84KN38hydz2eMboomHCd',
          consumer_secret='placeholder',
          access_token_key='3450870856-FVeOp4H1OPiT1NNS2MrgAnzMQVlrjWBG7eUQgf7',
          access_token_secret='placeholder')
    statuses = self.api.GetUserTimeline("C9Mang0")
    statuses = reduce(lambda acc,x: acc + [x.text], statuses, [])

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
	word_count = random.randint(1,12)
    generated_sentence = ""
    word_tuple = random.choice(self.chain.keys())
    w1 = word_tuple[0]
    w2 = word_tuple[1]

    for i in xrange(word_count):
      newword = random.choice(self.chain[(w1, w2)])
      generated_sentence = generated_sentence + " " + newword
      w1 = w2
      w2 = newword

    #.api.PostUpdate(generated_sentence)
    print "Tweeted: %s" % generated_sentence

chain = MarkovChain()
chain.chirrrp()
