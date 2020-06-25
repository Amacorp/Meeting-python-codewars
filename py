def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))
    
    
 OR
 
 
 def meeting(s):
  s = s.upper()
  s = s.split(';')
  array = []
  string = ""
  for i in s:
    i = i.split(':')
    string = '('+i[1]+', '+i[0]+')'
    array.append(string)
  array.sort()
  output = ""
  for j in array:
    output += j
  return output
  
  
  OR
  
  
def meeting(s):
    s = s.split(';')
    s.sort()
    res= []
    for i in s:
        first = i.split(':')[0]
        last = i.split(':')[1]
        res.append(str("(" + last.upper() + "," + first.upper() + ")"))
    res.sort()
    return ''.join(res)

print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"))
