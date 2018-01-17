from pycorenlp import StanfordCoreNLP



nlp = StanfordCoreNLP('http://localhost:9000')
res = nlp.annotate("I love you. I hate him. You are nice. He is dumb",
                   properties={
                       'outputFormat': 'json',
                       'timeout': 1000,
                   })
