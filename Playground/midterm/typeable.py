#create a new global dictionary
#where the keys that share the same row are mapped to the same value
d = {}
d['q'] = 1
d['w'] = 1
d['e'] = 1
d['r'] = 1
d['t'] = 1
d['y'] = 1
d['u'] = 1
d['i'] = 1
d['o'] = 1
d['p'] = 1

d['a'] = 2
d['s'] = 2
d['d'] = 2
d['f'] = 2
d['g'] = 2
d['h'] = 2
d['j'] = 2
d['k'] = 2
d['l'] = 2

d['z'] = 3
d['x'] = 3
d['c'] = 3
d['v'] = 3
d['b'] = 3
d['n'] = 3
d['m'] = 3

def isTypeable(s):
    row = d[s[0]] # extract the first character and check the value, indicating the row
    '''
    run a loop to iterate over the word, and get the value from the dictionary, 
	if it doesn't match the value in row, this indicates it belongs to 
	a different row than the first character. In all such cases return false
    '''
    for ch in s:
        if d[ch]!=row:
            return False
    '''
    if the prgram control reaches this point, this means all
	the hashmap value for every character in the word matcehd row, 
	so return ture.
    '''
    return True



def main():
	#ideally this should be entered from the user, but for now this will do
	words = 'hello world dad alaska peace twerp typewriter gas marine asdasd'.split(' ')	
	print([w for w in words if isTypeable(w)]) #calls isTypeable on each word

main()


