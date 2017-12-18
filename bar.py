import pystache 

files=['index_template.html', 'residence_template.html', 'attraction_template.html', 'about_template.html', 'whyus_template.html', 'university_template.html', 'contact_template.html', 'canada_template.html','thanks_template.html', 'tours_template.html', 'professor_template.html', 'signup_template.html']
files_o=['index.html', 'residence.html', 'attraction.html', 'about.html', 'whyus.html', 'university.html', 'contact.html', 'canada.html','thanks.html', 'tours.html', 'professor.html', 'signup.html']

i = 0
file_bar = open('bar.html', 'r', encoding='utf8')
bar = file_bar.read()
file_bar.close()

file_footer = open('footer.html', 'r', encoding='utf8')
footer= file_footer.read()
file_footer.close()

for file_t in files:

	file = open(file_t, 'r', encoding='utf8')
	template = file.read()
	file.close()

	#print(subsititute)
	final = pystache.render(template, {'bar': bar, 'footer': footer})

	f = open(files_o[i], 'w', encoding='utf8')
	f.write(final)  # python will convert \n to os.linesep
	f.close()


	print("Done replace bar in " + files_o[i])
	i += 1