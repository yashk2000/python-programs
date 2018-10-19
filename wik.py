import wikipedia

s=input("enter search parameter:")
res=wikipedia.page(s)
print(res.summary)
for link in res.links:
    print(link)
