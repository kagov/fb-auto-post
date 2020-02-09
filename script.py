import facebook

'''
the page access token
Please look here on how to get one
https://developers.facebook.com/docs/pages/getting-started
'''
access_token = "your-page-access-token-here"

# initialize the graph object with the page access token
graph = facebook.GraphAPI(access_token=access_token)


text = input('Please enter your message : ')
graph.put_object(parent_object='me', connection_name='feed',message=text)

