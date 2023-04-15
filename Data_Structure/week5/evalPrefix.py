from stackClass import Stack

def evalPrefix( expr ):
    
    s = Stack()		
    expr.reverse()	       
    for token in expr:			
        if token in "+-*/" :	
            val2 = s.pop()		
            val1 = s.pop()		
            if (token == '+'): s.push(val2 + val1)	
            elif (token == '-'): s.push(val2 - val1)
            elif (token == '*'): s.push(val2 * val1)
            elif (token == '/'): s.push(val2 / val1)
        else :				        
            s.push( float(token) )	

    return s.pop()