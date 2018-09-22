style = open('style.css','r')
styles = style.readlines()
countcur = []
counter = 0
for i in styles:
	if '{' in i:
		styles.remove(i)
for i in styles:
	if '}' in i:
		styles.remove(i)

for i in range(len(styles)-1):
	styles[i] = styles[i].replace('\t','')
	styles[i] = styles[i].replace('\n','')
print('всего стилей: '+str(counter))

while True:
	repeat = 0
	count =1
	
	n=len(styles)-1
	if n == 0:
		countcur.append(styles[0])
		break
	i=0
	word=styles[0]
	styles.remove(styles[0])
	while i < len(styles):
		#print(word+' - '+styles[i])
		if word==styles[i]:
			count=count + 1
			styles.remove(styles[i])
		i=i+1
	countcur.append(word+' - '+str(count))
countcur.sort()
for i in countcur:
	print(i)








