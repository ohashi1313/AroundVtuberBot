#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      t_oha
#
# Created:     15/05/2019
# Copyright:   (c) t_oha 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tweepy, os
import datetime
import random

CK = os.environ.get('consumer_key')
CS = os.environ.get('consumer_secret')
AT = os.environ.get('access_token')
AS = os.environ.get('access_token_secret')
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)
blocked_id = {"uiuiuieros"}

count = 3 #いいねの件数
searchWord = "((vtuber OR バーチャル) (魂 OR 中の人) -雀 (オーディション OR 募集) -放り出された exclude:retweets exclude:replies) OR @eiofkljislnf"
search_result = api.search(q=searchWord, lang='ja', result_type='recent',tweet_mode="extended", count=100)
for i in range(len(search_result)):
    result = random.choice(search_result)
    if result.user.screen_name not in blocked_id:
        try:
            api.create_favorite(result.id)
            print(result.user.name + " status_id:" + str(result.id) + "をいいねしました")
            count -= 1
            if count == 0:
                break
        except Exception as e:
            print(e)


