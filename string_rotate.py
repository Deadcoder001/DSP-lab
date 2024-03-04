# Function to rotate string left and right by d

def rotate_string(s,d): 
   
    Lfirst = s[0 : d] 
    Lsecond = s[d :] 
    Rfirst = s[0 : len(s)-d] 
    Rsecond = s[len(s)-d : ] 
  
    print ("Left Rotation : ", (Lsecond + Lfirst) )
    print ("Right Rotation : ", (Rsecond + Rfirst)) 
  
string = 'Studytonight'
d=4
rotate_string(string,d) 