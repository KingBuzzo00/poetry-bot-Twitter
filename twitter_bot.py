import tweepy
import random

consumer_key = 'ZTSXjsOU2q7ZgfKLwTjankGiZ'

consumer_secret = 'oVS8zIdU93fUqLQkkQnq2eAXPUbn0ll6dQ1kGZHINhNmUBIKWG'

access_token = '397804926-yrpinjvI4hEdtBHdrPqPEhGqgk3MqA9ngTtRNoVG'

access_token_secret = 'RDr2DBUqeAZGwrk8bPbk3pOXfY2yPD9ZlKn0HJmbtQiCS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



# the open keyword opens a file in read-only mode by default
f = open(r"C:\Users\jmac\Desktop\Nouns.txt")
v = open(r"C:\Users\jmac\Desktop\verbs.txt")
adj = open(r"C:\Users\jmac\Desktop\adjectives.txt")
av = open(r"C:\Users\jmac\Desktop\adverbs.txt")




nouns = f.readlines()
stripped_nouns = [s.rstrip("\n") for s in nouns]
r_noun = random.choice(stripped_nouns)

r_noun2 = random.choice(stripped_nouns)
if len(r_noun2) > 3:
  if r_noun2[-1:] == "y":
    r_noun2 = r_noun2[:-1] + "ie"
if r_noun2[-2:] == "ss":
    r_noun2 = r_noun2 + "e"




verbs = v.readlines()
stripped_verbs = [s.rstrip("\n") for s in verbs]
r_verb = random.choice(stripped_verbs)
if r_verb[-1] == "e":
    r_verb = r_verb + "d"
else:
    r_verb = r_verb + "ed"

adjectives = adj.readlines()
stripped_adjectives = [s.rstrip(" \n") for s in adjectives]
r_adjective = random.choice(stripped_adjectives)

adverbs = av.readlines()
stripped_adverbs = [s.rstrip("\n") for s in adverbs]
r_adverb = random.choice(stripped_adverbs)


predicates = ["in", 'at', 'is']
definite_article = ['the', 'a']
r_definarticle = random.choice(definite_article)


r_sentence = (r_definarticle.capitalize() + " " + r_noun + " " + r_adverb
          + " " + r_verb + " " + r_adjective + " " +
          r_noun2 + "s.")






f.close()
v.close()
adj.close()
av.close()



api.update_status(status=r_sentence)