import pefile

def get_sections(filename):
    sections= {}
    pe= pefile.PE(filename)
    sections= {section.Name+'_'+str(section.SizeOfRawData): section.get_data() for section in pe.sections}
    return sections

# This file is a malicious file that I copied for demo purposes from another repo. Be careful while running it :)
sections= get_sections('03.exe')
print "These are the names of the sections in this file"
print sections.keys()
