import random
import twitter

class MarkovChain(object):
  chain = {}
  hashtags = []
  api = ""

  def __init__(self):
    self.api = twitter.Api(
          consumer_key='skALdxnxoh7iyzKLRTtV7g',
          consumer_secret='NRfKq0AJNTRIwkKg8p92h177yevwjRIQVm0ETz7lWIQ',
          access_token_key='1210230230-NFkRxTc3mMeeyxL465zkzC5YiWRKRgOkjqOTTpE',
          access_token_secret='rnz9ajB5P5RUgCT7AqePNDVCH7mkW1wCDljGklNPw')
    statuses = self.api.GetUserTimeline("bkcmath")
    statuses = reduce(lambda acc,x: acc + [x.text], statuses, [])
    self.hashtags = []

    self.chain = {}
    word1 = "\n"
    word2 = "\n"
    for line in statuses:
      for current_word in line.split():
        if current_word != "":
          if current_word[0] == '#':
            self.hashtags += [current_word]
          else:
            self.chain.setdefault((word1, word2), []).append(current_word)
            word1 = word2
            word2 = current_word

  def chirrrp(self, word_count=20):
    generated_sentence = ""
    word_tuple = random.choice(self.chain.keys())
    w1 = word_tuple[0]
    w2 = word_tuple[1]

    for i in xrange(word_count):
      newword = random.choice(self.chain[(w1, w2)])
      generated_sentence = generated_sentence + " " + newword
      w1 = w2
      w2 = newword

    for i in range(random.randint(1,3)):
      generated_sentence += " %s" % random.choice(self.hashtags)

    self.api.PostUpdate(generated_sentence)
    print "Tweeted: %s" % generated_sentence

chain = MarkovChain()
chain.chirrrp()
