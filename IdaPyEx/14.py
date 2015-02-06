import idaapi
import idautils
import sys

##def rename_functions_ida():
##  #Get number of segments
##  seg=idaapi.getnseg(0)
##  if seg:
##  #Get list of functions in that segment
##    funcs=idautils.Functions(seg.startEA, seg.endEA)
##    for funcaddress in funcs:
##      f_name= GetFunctionName(funcaddress)
##      if f_name == 'giant_keyloggercase_structure':
##        for address in Heads(funcaddress, FindFuncEnd(funcaddress)):
##          if GetMnem(address) == 'call':
##            t1= GetOpnd(address, 0)
##            if t1.startswith('sub_'):
##              t2= t1.split('_')
##              MakeNameEx(int(t2[1], 16),"keylog_charbychar_"+t2[1],SN_NOWARN)

#Wait for analysis to complete
idaapi.autoWait()

def idautils_strings():
  """
  Examples for all the APIs that idautils contains. I will follow the exact order that the IDA documentation follows.
  """

  """
  Get existing Strings from a program from IDA.
  IDA GUI: View - Open SubViews - Strings
  """
  s = idautils.Strings()
  for i in s:
    #These options are part of the StringItem class which is a Nested Class of the String class
    print "%x: len=%d type=%d -> '%s'" % (i.ea, i.length, i.type, str(i))

  """
  How to call some other instance methods of the String class.

  IDA GUI: View - Open SubViews - Strings - Right click - Setup
  """
  
  s.setup(strtypes=1, minlen=5, only_7bit=True, ignore_instructions=False, ea1=None, ea2=None, display_only_existing_strings=False)
  s.clear_cache()
  s.refresh()

  print "Iterate over and print out a list of all the strings"
  for j in s.__iter__():
    print j

  print "Get only the 2nd string from the entire list"
  print s.__getitem__(1)

def idautils_peutils():
  """
  Get PE header from a Windows file. Using this you should be able to view every single field inside the header. Only it isn't clear via the documentation - on how these
  fields are to be accessed. There doesn't seem to be any code in idautils that does this either. Need to dig into this some more.

  Some properties though...are exposed. These can be obtained by calling them.

  IDA GUI: Manually load the file at the start and then go to View - Open Subviews - Segments and look at the HEADER segment.
  """
  p = idautils.peutils_t()
  print "Imagebase of the loaded binary: " + hex(p.imagebase)

  #Its unclear what use this is or how to use it. This should have returned an entire header, which we could then iterate through. That didn't work though :(
  print "Peheader instance of the entire PE header: "
  print p.header()

def idautils_getXrefs_to():
  """
  IDA GUI: Right click on any address and click List Cross-references to. This is a list of all those locations in all segments that refer to this address.
           While this code will work, it makes more sense to iterate over an entire function and check every location for Cross references.
  """
  
  print "Getting all cross references to a specific address"
  xrefs= idautils.XrefsTo(0x000000004A6811E0, 0)
  for ref in xrefs:
    print hex(ref.frm)

def idautils_getXrefs_from():
  """
  IDA GUI: Right click on any address and click List Cross-references from. This is just a list of all those locations in all segments that this address refers to.
           While this code will work, it makes more sense to iterate over an entire function and check every location for Cross references.
  """
  
  print "Getting all cross references from a specific address"
  xrefs= idautils.XrefsFrom(0x000000004A6811E0, 0)
  for ref in xrefs:
    print hex(ref.to)

def idautils_getcoderefs_to():
  """
  IDA GUI: Right click on any address and click List Cross-references to. This is a list of all those locations in all segments that refer to this address.
           The only ones that matter for this API are the ones in the .text segment.
           While this code will work, it makes more sense to iterate over an entire function and check every location for Cross references.
  """
  
  print "Getting all code references to a specific address"
  coderefs= idautils.CodeRefsTo(0x000000004A6811E0, 1)
  for ref in coderefs:
    print str(ref) + ':' + str(hex(ref))

def idautils_getcoderefs_from():
  """
  IDA GUI: Right click on any address and click List Cross-references from. This is just a list of all those locations in all segments that this address refers to.
           The only ones that matter for this API are the ones in the .text segment.
           While this code will work, it makes more sense to iterate over an entire function and check every location for Cross references.
  """
  
  print "Getting all code references from a specific address"
  coderefs= idautils.CodeRefsFrom(0x000000004A6811E0, 1)
  for ref in coderefs:
    print str(ref) + ':' + str(hex(ref))

def idautils_getdatarefs_to():
  """
  IDA GUI: Right click on any address and click List Cross-references to. This is just a list of all those locations in all segments that refer to this address.
           The only ones that matter for this API are the ones NOT in the .text segment.
           While this code will work, it makes more sense to iterate over an entire function and check every location for Cross references.
  """
  
  print "Getting all data references to a specific address"
  datarefs= idautils.DataRefsTo(0x000000004A6811E0)
  for ref in datarefs:
    print str(ref) + ':' + str(hex(ref))

def idautils_getdatarefs_from():
  """
  IDA GUI: Right click on any address and click List Cross-references to. This is just a list of all those locations in all segments that this address refers to.
           The only ones that matter for this API are the ones NOT in the .text segment.
           While this code will work, it makes more sense to iterate over an entire function and check every location for Cross references.
  """
  
  print "Getting all data references from a specific address"
  datarefs= idautils.DataRefsFrom(0x000000004A6811E0)
  for ref in datarefs:
    print str(ref) + ':' + str(hex(ref))
    
#idautils_strings()
#idautils_peutils()
#idautils_getcoderefs_to()
#idautils_getcoderefs_from()
#idautils_getdatarefs_to()
#idautils_getdatarefs_from()
idautils_getXrefs_to()
idautils_getXrefs_from()

#Exit IDA
idc.Exit(0)
