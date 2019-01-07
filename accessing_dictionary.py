x = {
	"foo":1,
	"bar":999,
	"lorem":{
		"ipsum":[20, 30, 40],
		"sit":"dolor",
		"amet":{
			"foo":1,
			"bar":2
		}
	}
}

print (x['foo'])
print (x['bar'])
print (x['lorem'])
print (x['lorem']['ipsum'])
print (x['lorem']['amet'])
print (x['lorem']['amet']['foo'])

for key in x:
	print (key)

for key in x:
	print (x[key])
