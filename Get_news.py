import feedparser
import webbrowser

def main():
    print("*****  Security News Website List ******")
    print("[0] => TheHacker News")
    print("[1] => TheHacker News")
    print("[2] => TheHacker News")


    Website_List = ("https://feeds.feedburner.com/TheHackersNews", "https://threatpost.com/feed", "https://nakedsecurity.sophos.com/feed")

    Chosen_Website = (int(input("Enter the  Website Number  0 - 2  ")))

    NewsFeed = feedparser.parse(Website_List[Chosen_Website])

    Article_List = []2
    Article_Linq = []

    for i in range(5):
        article = NewsFeed.entries[i]
        titles = article.title
        link = article.link
        Article_Linq.append(link)
        Article_List.append(titles)

    article_num = 1
    for article in Article_List:
        print('[{}] {}'.format(str(article_num), article))
        article_num += 1
    
    article_link_status = False
    while not article_link_status:
        Click_Event = int(input("Enter the Link To Open 1 - 5 "))
        webbrowser.open(Article_Linq[Click_Event-1])
        article_link_status = True
main()








