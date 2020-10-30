import pytumblr
# pip install pytumblr -- if not already installed
import re, string
# regex to exclude html tag
import datetime as dt


# Authenticate via OAuth
# We only need the consumer key to call "posts" function
client = pytumblr.TumblrRestClient('nAvaCgNT6dVls4dxKYnWyM1as57L0aSAkSXAayRCPEtNxJSQjr')

# exclude html tags, punctuation, and extra whitespaces

def reformat_text(data):
    html = re.compile(r'<.*?>')
    temp = html.sub(' ', data)
    special = re.compile(r'[%s\s]+' % re.escape(string.punctuation))
    temp2 = special.sub(' ', temp)
    wspace = re.compile('\s{2,}')
    return wspace.sub(' ', temp2)

def make_json(blogname):
    print(blogname)
    # Make the request
    # Use minkim25.tumblr.com for test
    data = client.posts(blogname + '.tumblr.com')
    
    #To be modified later
    #Filters out all blogs without 'blog' or 'posts' elements
    try:
        website = data['blog']['url']
        last_update = data['posts'][0]['date'][:19]
    except:
        print('Warning: blog or posts or date or url is null')
        return {}
    
    last_update = dt.datetime.strptime(last_update, '%Y-%m-%d %H:%M:%S').strftime("%Y-%m-%d %H:%M:%S")
    trail_flag = 0
    
    # Initialization
    title_text = ""
    body_text = ""
    title_font = ""
    body_font = ""
    back_color = ""
    text_color = ""
    link_color = ""   
    
    for post in data['posts']:
        if post['type'] == 'text':
            if trail_flag == 0 and post['trail'] != []:
                theme = post['trail'][0]['blog']['theme']
                title_font = theme['title_font']
                body_font = theme['body_font']
                back_color = theme['background_color']
                text_color = theme['title_color']
                link_color = theme['link_color']
                trail_flag = 1
            if post['title'] != None:
                title_text = title_text + ' ' + post['title']
                title_text = reformat_text(title_text)
            if post['reblog']['comment'] != '':
                body_text = body_text + ' ' + post['reblog']['comment']
                body_text = reformat_text(body_text)
        elif post['type'] == 'photo':
            if trail_flag == 0 and post['trail'] != []:
                theme = post['trail'][0]['blog']['theme']
                title_font = theme['title_font']
                body_font = theme['body_font']
                back_color = theme['background_color']
                text_color = theme['title_color']
                link_color = theme['link_color']
                trail_flag = 1
            title_text = ''
            if post['reblog']['comment'] != '':
                body_text = body_text + ' ' + post['reblog']['comment']
                body_text = reformat_text(body_text)
            
    result = {'website': website, 'last_update': last_update, 'title_font': title_font, 'body_font': body_font, \
              'back_color': back_color, 'text_color': text_color, 'link_color': link_color, \
              'title_text': title_text, 'body_text': body_text}
    return result