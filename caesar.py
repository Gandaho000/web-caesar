def rotate_string(text, rot):

	alphabet_position_caps = {
	"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
	alphabet_position_lower = { 
	"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
	new_text=[]


	for char in text:
		if char.isalpha() and char.isupper():
			char_value = ((alphabet_position_caps[char]) + rot)
			new_value = char_value % 26
			encrypted_char = (list(alphabet_position_caps.keys())[list(alphabet_position_caps.values()).index(new_value)])
			new_text.append(encrypted_char)

		elif char.isalpha() and char.islower():
			char_value = ((alphabet_position_lower[char]) + rot)
			new_value = char_value % 26
			encrypted_char = (list(alphabet_position_lower.keys())[list(alphabet_position_lower.values()).index(new_value)])
			new_text.append(encrypted_char)

		else:
			new_text.append(char)
			

	new_text=''.join(new_text)
	print(new_text)
	return(new_text)

def main():
	text = input("Type a message:")
	text = str(text)
	rot = input("Rotate by:")
	rot = int(rot)
	rotate_string(text, rot)

if __name__ == '__main__':
	main()