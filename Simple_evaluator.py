import sys
import math
import ast
x = input("enter a valid arithmatic expression \nCan contain only log(num,base) cos() sec() sin() cosec() tan() cot() () + - . , * ^ / ÷ = \n")


def eval_exp(expr):
    e = expr;
    try:
        d= e.split("=")
    except:
        d[0] = e
    try:
        d[0]=d[0].replace('^', '**')
    except:
        pass
    try:
        d[0]=d[0].replace('÷', '/')
    except:
        pass

    i = "1234567890log/.*-+=sincostanseccot()()  ,"

    for char in d[0]:
            if char not in i:
                print(f"invalid char: '{char}' (ord: {ord(char)}) in \"{d[0]}\"")
                sys.exit() 
            else:
                try:
                    d[0]=d[0].replace('log', 'math.log')
                except:
                    pass
                #try:
                #    d[0]=d[0].replace('ln', 'math.log')
                #except:
                #    pass
                try:
                    d[0]=d[0].replace('sin', 'math.sin')
                except:
                    pass
                try:
                    d[0] = d[0].replace('cosec', '1/math.sin')
                except:
                    pass
                try:
                    d[0]=d[0].replace('cos', 'math.cos')
                except:
                    pass
                try:
                    d[0]=d[0].replace('tan', 'math.tan')
                except:
                    pass
                try:
                    d[0]=d[0].replace('sec', '1/math.cos')
                except:
                    pass
                try:
                    d[0]=d[0].replace('cot', '1/math.tan')
                except:
                    pass
                #print(d[0])

                g = d[0]
                for f in range(len(g)*2):
                        try:
                            #print(f"char:{g[f]}\nindex:{f}")
                            if (f)!= 0:
                                #print(f"here3 {g[f]} dmath.log10igit {g[(f-1)].isdigit()}")
                                
                                if (g[f] == '(') and (g[(f-1)].isdigit()):
                                    
                                    first_part  = g[:f]
                                    second_part = g[f:]
                                    g = first_part + "*" + second_part
                                if (g[f] == '(') and (g[(f-1)] == ')'):
                                    
                                    first_part  = g[:f]
                                    second_part = g[f:]
                                #if (g[f] == '(') and (g[(f-1)].isalpha()):
                                 #   first_part  = g[:f]
                                 #   second_part = g[f:]
                                  #  g = first_part + "*" + second_part
                            if (g[f] == ')') and (g[(f+1)].isdigit()):
                                    first_part  = g[:f+1]
                                    second_part = g[f+1:]
                                    g = first_part + "*" + second_part

                            if (g[f] == ')') and (g[(f+1)]=='('):
                                    first_part  = g[:f+1]
                                    second_part = g[f+1:]
                                    g = first_part + "*" + second_part
                           # if (g[f] == ')') and (g[(f+1)].isalpha()):
                           #         first_part  = g[:f+1]
                           #         second_part = g[f+1:]
                            #        g = first_part + "*" + second_part
                        except: 
                            break
                d[0] = g
                safe_names = {k: getattr(math, k) for k in ["sin", "cos", "tan", "log", "sqrt", "radians"]}
                safe_globals = {"__builtins__": None, "math": math}
                #print(d[0])
                try:
                    #print(eval(f"ast.literal_eval({d[0]})", {"math":math, "ast":ast}))
                    
                    return (eval(d[0], safe_globals, safe_names))  

                except Exception as e:
                    return (f"error: {e}")
                break;    
                    
print(eval_exp(x))