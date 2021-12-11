import requests
import tokens
import json


def postInstagramQuote(image_location, caption):
    creds = tokens.get_instagram_creds()
    # Post the Image
    # imagelocation strictly web based with https
    post_url = 'https://graph.facebook.com/v10.0/{}/media'.format(
        creds['ig_user_id'])
    payload = {
        'image_url': image_location,
        'caption': caption,
        'access_token': creds['ig_user_access_token']
    }
    r = requests.post(post_url, data=payload)
    print(r.text)
    result = json.loads(r.text)
    if 'id' in result:
        creation_id = result['id']
        second_url = 'https://graph.facebook.com/v10.0/{}/media_publish'.format(
            creds['ig_user_id'])
        second_payload = {
            'creation_id': creation_id,
            'access_token': creds['ig_user_access_token']
        }
        r = requests.post(second_url, data=second_payload)
        print('--------Just posted to instagram--------')
        print(r.text)
    else:
        print('HOUSTON we have a problem')


postInstagramQuote(
    'https://i.postimg.cc/B6wcJJvw/viciousprofile.jpg', 'This is a post from API')
