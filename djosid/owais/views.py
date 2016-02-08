from django.http import HttpResponse
from django.template.loader import get_template
import oauth2 as oauth
import urllib2 as urllib
from django.shortcuts import render
from vaderSentiment import sentiment as vaderSentiment 
import json

# See assignment1.html instructions or README for how to get these credentials

api_key = "Dw4VBwGoHL0ZxhiD3wRmrNWnk"
api_secret = "yUePLAPTT4yM1mImx8cNKjCWmFxsXtxH3zbcANhj9KzbhhaAwM"
access_token_key = "169851780-zXLOOBa0KcbSghC4118vHBhCvJTb2tvysJqaMZug"
access_token_secret = "gY1W5V2OboX4H5p28ZQDzFXyivNhO30NbdcfdIKY49mCC"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response
def fetchsamples():
  url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=BarackObama"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
	print line.strip()
	
def tapi(request):
  url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=BarackObama"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  return HttpResponse(response)

def twsent(request):
  new = open('C:\\Users\\osiddiqui\\Documents\\venv\\djosid\\owais\\tweets.txt')
  res1 = "\n"
  for line in new:
    vs = vaderSentiment(line) 
    res1 += str(vs)
  return HttpResponse(res1)
				
def sentiment(request):
  res1 = "\n"
  for sentence in open('C:\\Users\\osiddiqui\\Documents\\venv\\djosid\\owais\content.txt'): 
    vs = vaderSentiment(sentence) 
    res1 += str(vs)
  return HttpResponse(res1)
  
def index(request):
    return render(request, "index.html")
