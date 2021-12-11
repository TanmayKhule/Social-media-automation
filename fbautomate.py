import requests
import tokens
import json
import os

creds = tokens.get_facebook_creds()


""" def postImage(group_id, img):
    url = f"https://graph.facebook.com/{group_id}/photos?access_token=" + \
        creds['fb_page_access_token']

    files = {
        'file': open(img, 'rb'),
    }
    data = {
        "published": False
    }
    r = requests.post(url, files=files, data=data).json()
    return r """


def multiPostImage(folder_path, caption, group_id):

    group_id = creds['fb_user_id']
    imgs_id = []
    img_list = []
    for filename in os.listdir(folder_path):
        img_list.append(folder_path+filename)
    for img in img_list:
        url = f"https://graph.facebook.com/{group_id}/photos?access_token=" + \
            creds['fb_page_access_token']

        files = {
            'file': open(img, 'rb'),
        }
        data = {
            "published": False
        }
        r = requests.post(url, files=files, data=data).json()

        post_id = r

        imgs_id.append(post_id['id'])

    args = dict()
    args["message"] = caption
    for img_id in imgs_id:
        key = "attached_media["+str(imgs_id.index(img_id))+"]"
        args[key] = "{'media_fbid': '"+img_id+"'}"
    url = f"https://graph.facebook.com/{group_id}/feed?access_token=" + \
        creds['fb_page_access_token']
    requests.post(url, data=args)


multiPostImage('D:/Rotract/Trial/', "Aadanjafaof",
               group_id=creds['fb_user_id'])
