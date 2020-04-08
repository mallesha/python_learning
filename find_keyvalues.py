test = {'key1':'value1', 'key2':'value2'}
print('value2' in test.values())


test = {'key1':'value1', 'key2':'value2'}
print('value3' in test.values())

test = {'key1':'value1', 'key2':'value2'}
print('key2' in test.keys())

########################################
##### Practical examples #####
# we can find the required values in available in the dictionary by just going through the ibuilt in .keys() or values()
# if the value is found it will print True or False
x={
  "hname-banner-rfs:hname-banner-rfs": [
    {
      "device": "device123",
      "hostname": "hostname123",
      "login-banner": "banner123"
    }
  ]
}

print ('hostname123' in x["hname-banner-rfs:hname-banner-rfs"][0].values())

###########
# we can take a decision based on return value True or flase for example below
x={
  "hname-banner-rfs:hname-banner-rfs": [
    {
      "device": "device123",
      "hostname": "hostname123",
      "login-banner": "banner123"
    }
  ]
}


while ('hostname123' in x["hname-banner-rfs:hname-banner-rfs"][0].values()):  # if the value hostname123 found result is True

    x["hname-banner-rfs:hname-banner-rfs"][0]['hostname'] = 'hostname321' # reassigning the value to hostname321

    print(x["hname-banner-rfs:hname-banner-rfs"][0]['hostname'])

    print(x["hname-banner-rfs:hname-banner-rfs"])
