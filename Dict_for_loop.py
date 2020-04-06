import  json

device = "T02-ntsm-ci-ios38"
hostname = "test123-hostname"
banner = "test123-banner"
x={
  "hname-banner-rfs:hname-banner-rfs": [
    {
      "device": "device123",
      "hostname": "hostname123",
      "login-banner": "banner123"
    }
  ]
}

for test in x["hname-banner-rfs:hname-banner-rfs"]:
    print(test)
    print('\n')

for test in x["hname-banner-rfs:hname-banner-rfs"][0]:
    print(test)
    print('\n')

for test in x["hname-banner-rfs:hname-banner-rfs"][0].items():
    print(test)