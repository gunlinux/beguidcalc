import md5
steamid=76561198057447143
temp = ""
for i in range(8):
	temp +=  chr((steamid & 0xFF))
	steamid >>= 8
m = md5.new("BE"+temp)
print m.hexdigest()
print 'd4d20ab6f6e413c129a2bcbaa17677e5'
