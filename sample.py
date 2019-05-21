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

CK = os.environ.get('consumer_key')
CS = os.environ.get('consumer_secret')
AT = os.environ.get('access_token')
AS = os.environ.get('access_token_secret')
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)
blocked_id = {"uiuiuieros"}

searchWord = "((vtuber OR バーチャル) (魂 OR 中の人) -雀 (オーディション OR 募集) -放り出された exclude:retweets exclude:replies) OR @eiofkljislnf"
for status in api.search(q=searchWord, lang='ja', result_type='recent',tweet_mode="extended", count=5): #qに検索したいワードを指定する。
    if status.user.screen_name not in blocked_id:
        #print("ユーザーID:" + status.user.name) #userIDを表示
        #print("ユーザー名:" + status.user.screen_name) #ユーザー名を表示
        #time = status.created_at + datetime.timedelta(hours=9)
        #print("投稿日時:" + str(status.created_at + datetime.timedelta(hours=9))) #投稿日時を表示
        #print(status.full_text) #ツイートを表示
        #print()
        try:
            api.create_favorite(status.id)
            print(status.user.name + "をいいねしました")
        except Exception as e:
            print(e)


