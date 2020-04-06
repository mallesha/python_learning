import  json

####################Basic examples ###########################
mylist = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in mylist:
    #print(list_sum)
    list_sum = list_sum + num
print(list_sum)
print('\n')

my_list = [(1,2), (3,4), (5,6), (7,8)]
for item in my_list:
    print(item)
print('\n')

#############################################################

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

print( "real time example \n ")
for test in x["hname-banner-rfs:hname-banner-rfs"]:
    print(test)
    print('\n')

for test in x["hname-banner-rfs:hname-banner-rfs"][0]:
    print(test)
    print('\n')

for test in x["hname-banner-rfs:hname-banner-rfs"][0].items():
    print(test)