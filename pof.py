from nltk.sentiment.vader import SentimentIntensityAnalyzer

new_words = {
    'gaming': 7.0,
    'Mental health': 9,
    'new things or ideas': 6,
    'culture': 6,
    'creative': 8,
    'arsty': 5,
    'eclectic': 8,
    'gym': -10,
    'god': -8,
    'cigarettes': -10,
    'I work': 10,
    'workout': -10,
    'Trans': -10,
    'single mother': -5,
    'independent': 2.5,
    'i have kids': -5
}

analyser = SentimentIntensityAnalyzer()

analyser.lexicon.update(new_words)

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return(score)


from Machapi.Engines.POF_com import Session as POFSession

# Create a configuration object from a file.
config = POFSession.Config( './config.ini' )
usersDone = []
POFobject = POFSession( config )
print('pre login')
# start the session by loggin in.
POFobject.login( )
print('logged in')
galleryData = list()
print('list')
import time
while True:

    users = POFobject.searchUsers(config, 100, online_only=True)
    print("Search complete.")

    tomsg = []
    for user in users:
        try:
            #print (user.profile_url)
            #print(user.description.encode("utf-8"))
            if(sentiment_analyzer_scores(user.description.encode("utf-8"))['compound'] > 0.99):
                if user.online == True:
                    if user.profile_url not in usersDone:
                        usersDone.append(user.profile_url)
                        tomsg.append(user)
                
        except Exception as e:
            print (e)
    print("Total Users Found: {0}".format( len(tomsg) ) )
    with open('usersDone.txt', 'w') as f:
        for item in usersDone:
            f.write("%s\n" % item)

    POFobject.broadcastMessage(tomsg, "Hey! This is going to sound terrrrribly awkward but I hacked POF in a very special way that allows me to rank different profiles among the online users to see whose description matches an analysis I'd created that might indicate we'd have a swell chance at a good conversation - so if this isn't terribly scary as well as terribly awkward, do hazard a response back and we'll see if I'm right? I'm legit though here's the code: https://github.com/DunnCreativeSS/POFHacking - in case my account gets auto-shutdown after much of this, I'll drop my American cell # here: 17162268165" )
    time.sleep(60)