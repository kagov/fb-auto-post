# Facebook Auto post

### Create post on your FB page using the Facebook Graph API

This repo contains a sample python project using the facebook-sdk for python

1. Setup the environment

``` sh
my-pc$ virtualenv fb-auto-post
my-pc$ cd fb-auto-post
my-pc$ source bin/activate
my-pc$ pip install requirements.txt
```

If you do not neet a virtualenv or do not have one then just cd into the directory and install the dependencies.

2. Replace the access token

Inside the script.py file replace the access token with your page access token. Find out how to get one [here](https://developers.facebook.com/docs/pages/getting-started)

``` sh
my-pc$ python script.py
my-pc$ Please enter your message : Foo bar baz
```