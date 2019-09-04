import flickrapi as fa
import urllib
import os
import argparse

my_api_key = 'dd3d37bdbe27efaf9e3bfa87ce551484'
my_secret = 'b94f7320cf655805'

f = fa.FlickrAPI(my_api_key, my_secret, format='parsed-json')

parser = argparse.ArgumentParser(description='Enter keyword and number of images')
parser.add_argument('keyword', type=str, nargs='+',
                    help='keyword to seach')
parser.add_argument('number', type=int,
                    help='number of photos')

args = parser.parse_args()

keyword = 'panda'
img_num = 1 
    
keyword = args.keyword
img_num = args.number

def flickr_search(keyword, how_many):
    obj = f.photos.search(text=keyword,
                           tags=keyword,
                           extras='url_c',
                           per_page=how_many)
    for photo in obj['photos']['photo']:
        u=photo['url_c']
        try:
            name = u[-25:]
            pwd = os.getcwd()
            path = os.path.join(pwd, name + '.jpg')
            print(path)
            urllib.request.urlretrieve(u,  path)
        except Exception as e:
            print('failed to download image')

flickr_search(keyword, img_num)

