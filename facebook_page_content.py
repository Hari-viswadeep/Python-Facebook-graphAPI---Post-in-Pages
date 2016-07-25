from bs4 import BeautifulSoup
import json
import urllib2
import pickle
import os.path

opener = urllib2.build_opener()
file_name = 'fb_page_content.p'

page_list = ['page_name1'] #add page names here coma separated

def main():
    app_secret = 'APP_SECRET'
    app_id     = 'APP_ID'
    
    graph_url = "https://graph.facebook.com/"
    for each_page in page_list:
        current_page = graph_url + each_page
        url = current_page + "/posts/?access_token=%s|%s"%(app_secret,app_id)
    fb_json = get_json_fb(url)
    fb_data = fb_json['data']
    data = {}
    content = False
    if os.path.isfile(file_name):
        content = pickle.load(open(file_name,"rb"))
    for each in fb_data:
        try:
            value = str(each['id'])
            value = value.split('_')
            post_id = int(value[1])     # taking only second portion after underscore
            details = ''
            if ('message' in each):
                details = each['message'] 
            if content:
                if post_id in content.keys():
                    continue
                else:
                    content[post_id] = details
            else:
                content[post_id] = details
        except Exception as e:
            print e
            continue
    pickle.dump(content,open(file_name,"wb"))

def get_json_fb(url):
    f = opener.open(url)
    soup = BeautifulSoup(f.read(),'html.parser')
    results  = json.loads(str(soup))   
    return results

if __name__ == "__main__":
    main()
