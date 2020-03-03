#讀取聊天紀錄檔案
def read_file(filename):
	chatting = []
	with open(filename, 'r' ) as f:
		for line in f:
			chatting.append(line.strip())
	return chatting

#將聊天紀錄改寫成新的格式

def convert(chatting):
	new = []
	person = None
	for line in chatting:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)

	return new

def write_file(filename, chatting):
	with open(filename, 'w') as f:
		for line in chatting:
			f.write(line + '\n')


def main():
	chatting = read_file('input.txt')
	chatting = convert(chatting)
	write_file('output.txt', chatting)

main()