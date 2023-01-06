"""
Required Packages:
1. google-api-python-client 
2. google-auth-httplib2 
3. google-auth-oauthlib
4. EZgmail

"""

#By default maxLimit is 25

import ezgmail


#keyword = "quora"
def delete_specific_keyword(keyword,maxLimit):
    thread=ezgmail.search(keyword,maxResults=maxLimit)
    print(f"There are {len(thread)} emails with the keyword {keyword}")
    for i in range(len(thread)):
        thread[i].trash()
    print(f"Deleted {len(thread)} emails")


#keywords=["quora","leetcode"]
def delete_keywords(keywords,maxLimit):
   for keyword in keywords:
    delete_specific_keyword(keyword,maxLimit)


def delete_unread(maxLimit):
    t=1
    prev=0
    while(t<=(maxLimit/25)+1):
        unread=ezgmail.unread()
        for i in range(len(unread)):
            print(f"Deleted the mails : {prev+i+1}.........")
            unread[i].trash()
        t=t+1
        prev=prev+25


#sender="Quora" or "the sender email id"
def delete_by_sender(sender,maxLimit):
    thread=ezgmail.search(f"from:{sender}",maxResults=maxLimit)
    print(f"There are {len(thread)} emails from the sender {sender}")
    for i in range(len(thread)):
        thread[i].trash()
    print(f"Deleted {len(thread)} emails")


#sub="Weekly contest"
def delete_by_subject(sub,maxLimit):
    thread=ezgmail.search(f"subject:{sub}",maxResults=maxLimit)
    print(f"There are {len(thread)} emails of the subject {sub}")
    for i in range(len(thread)):
        thread[i].trash()
    print(f"Deleted {len(thread)} emails")


#category="promotions"
# category:primary category:social category:promotions category:updates category:forums category:reservations category:purchases
def delete_by_category(category,maxLimit):
    thread=ezgmail.search(f"category:{category}",maxResults=maxLimit)
    print(f"There are {len(thread)} emails of the category {category}")
    for i in range(len(thread)):
        thread[i].trash()
    print(f"Deleted {len(thread)} emails")

delete_unread(20)