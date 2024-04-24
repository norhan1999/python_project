reserved_words=["always","and", "assign", "begin", "buf", "bufif0", "bufif1", "case", "casex", "casez", "cmos", "function", "highz0", "highz1", "if", "initial", "inout", "input", "integer", "join", "large", "macromodule", "medium", "module", "nand", "negedge", "nmos", "nor", "not", "notif0", "notif1", "or", "output", "pmos", "posedge", "primitive", "pull0", "pull1", "pulldown", "pullup", "rcmos", "reg", "release", "repeat", "rnmos", "rpmos", "rtran", "rtranif0", "rtranif1", "scalared", "small", "specify", "specparam", "strong0", "strong1", "supply0", "supply1", "table", "task", "time", "tran", "tranif0", "tranif1", "tri", "tri0", "tri1", "triand", "trior", "vectored", "wait", "wand", "weak0", "weak1", "while", "wire", "xnor","xor"]
special_char=["~","!","@","#","%","^","&","*","(",")","-","=","+","|",":",";","'","?","/",">","<",",",".","[","]","{","}","\\"," "]
#list to store inputs to use them in DUT instantiation also to prevent the user from entering the same name twice
input_list=[]
#list to store outputs to use them in DUT instantiation
output_list=[]
#parameters list
param_list=[]
param_values_list=[]


#ask the user to enter a module name
while True:
    module_name=input("enter module name\n")
    #check it is a valid name
    #1-not a keyword
    if module_name in reserved_words:
        print("invalid module name (key word)\ntry again\n")
    #2-none of these in it 
    elif any(substring in special_char for substring in module_name):
        print("invalid module name (includes a special char)\ntry again\n")
    #3-shoudn't start with a digit or $
    elif module_name[0].isdigit():
        print("invalid module name (it can only start with '_' or an alphabet)\ntry again\n")
    elif module_name[0] == "$":
        print("invalid module name(it can only start with '_' or an alphabet)\ntry again\n")
    else:
        break
               
#asking the user if the design is seq or com or mix
while True:
    try:
         seq_com=int(input("specify whether the design is sequential or combinational or mix (choose 1 or 2 or 3)\n1-sequential\n2-combinational\n3-mix\n"))
    except:
        print("not a valid choice\n(choose 1 or 2 or 3)\n")                             
        continue
    if seq_com ==1 or  seq_com==2 or  seq_com==3 :
        break
    else:
        print("not a valid choice\n(choose 1 or 2 or 3)\n")
        
#create module file and TB_file
F= open(module_name,'w')
F_tb= open(module_name+"_Testbench",'w')
F.write("module "+module_name +"   ")
F_tb.write("module "+module_name+"_TB ();\n")
        
#asking the user if he needs parameters in the design
while True:
    try:
         param=int(input("do you need any parameters in your design (choose 1 or 2)\n1-YES\n2-NO\n"))
    except:
        print("not a valid choice\n(choose 1 or 2)\n")                             
        continue
    if param ==1 or  param==2 :
        break
    else:
        print("not a valid choice\n(choose 1 or 2)\n")
        
if param ==1:
    while True:
        try:
             param_number=int(input("how many parameters do you need\n"))
        except:
            print("not a valid input\ntry again\n")                             
            continue   
        break
else:
    param_number =0
c3=1
while param_number > 0:
    while True: 
        P=input("enter name of parameter"+str(c3)+"\n")
        #check it is a valid name
        #1-not in param list
        if P in param_list:
            print("invalid name(entered that name before)\ntry again\n")
            break
        #2-not a keyword
        if P in reserved_words:
            print("invalid name (keyword)\ntry again\n")
        #3-none of these in it 
        elif any(substring in special_char for substring in P):
            print("invalid name (includes a special char)\ntry again\n")
        #4-shoudn't start with a digit or $
        elif P[0].isdigit():
            print("invalid module name (it can only start with '_' or an alphabet)\ntry again\n")
        elif P[0] == "$":
            print("invalid module name (it can only start with '_' or an alphabet)\ntry again\n")
        else:
                        
            while True:
                try:
                     param_value=int(input("enter value of parameter"+str(c3)+"\n"))
                except:
                    print("not a valid input\ntry again\n")                             
                    continue   
                break
            c3=c3+1      
            param_number=param_number-1
            param_list.append(P)
            param_values_list.append(param_value)
            break
           
#writing paramters in the design file
if param ==1:
     F.write("#(parameter ")      
     for x, y in zip(param_list,param_values_list):
         if param_list[-1] == x:
             F.write(x + "=" +str(y))
         else:
             F.write(x + "=" +str(y)+",  ")
     F.write(")\n\n\n")
         

#if it's sequential or mix there are a clk and rst signals
if seq_com ==1 or seq_com ==3 :
    F.write("\n\n//ports declaration\n\n")
    F.write("(input clk,\ninput rst_n,\n")
    F_tb.write("reg clk_TB;\nreg rst_n_TB;\n")
else:
    F.write("\n\n//ports declaration\n\n")
    F.write("(")
    
while True:
    try:
         inputs=int(input("enter number of inputs \n"))
    except:
        print("not a valid number ,try again\n")
        continue
    if inputs > 0:
        break
    else:
        print("not a valid number ,try again\n")
        
        
while True:
    try:
         outputs=int(input("enter number of outputs\n"))
    except:
        print("not a valid number ,try again\n")
        continue
    if outputs > 0:
        break
    else:
        print("not a valid number ,try again\n")


c1=1
while inputs > 0:
     try:
        in_width=int(input("enter the width of input"+str(c1)+"\n"))
     except:
        print("not a valid input ,try again\n")
        continue
     if not (in_width > 0):
         print("not a valid input ,try again\n")
         continue   
     else:
         
         while True:
             
             IN=input("enter name of input"+str(c1)+"\n")
             #check it is a valid name
             #1-not in input list or param_list
             if IN in input_list: 
                 print("invalid name(entered that name before)\ntry again\n")
                 break              #i don't know why if i entered same input name twice it give me that invalid name message then go to the else condition so i had to put that break
             if IN in param_list: 
                 print("invalid name(entered that name before)\ntry again\n")
                 break
             #2-not a keyword
             if IN in reserved_words:
                 print("invalid name (keyword)\ntry again\n")
             #3-none of these in it 
             elif any(substring in special_char for substring in IN):
                 print("invalid name (includes a special char)\ntry again\n")
             #4-shoudn't start with a digit or $
             elif IN[0].isdigit():
                 print("invalid module name (it can only start with '_' or an alphabet)\ntry again\n")
             elif IN[0] == "$":
                 print("invalid module name (it can only start with '_' or an alphabet)\ntry again\n")
             else:
                 if in_width == 1:
                     F.write("input"+" "+IN+",\n")
                     F_tb.write("reg"+" "+IN+"_TB"+";\n")
                 else:
                     F.write("input"+" "+"["+str((in_width-1))+":0]"+" "+IN+",\n")
                     F_tb.write("reg"+" "+"["+str((in_width-1))+":0]"+" "+IN+"_TB"+";\n")
                 inputs=inputs-1
                 input_list.append(IN)
                 c1=c1+1
                 break
    

    

c2=1  
while outputs > 0:
     try:
        out_width=int(input("enter the width of output"+str(c2)+"\n"))
     except:
        print("not a valid input\ntry again\n")
        continue
     if not (out_width > 0):
         print("not a valid input\ntry again\n")
         continue
     else:
         while True:
             OUT=input("enter name of output"+str(c2)+"\n")
             #check it is a valid name
             #1-not in output list or input list or param_list
             if OUT in output_list:
                 print("invalid name(entered that name before)\ntry again\n")
                 break
             if OUT in input_list:
                 print("invalid name(entered that name before)\ntry again\n")
                 break
             if OUT in param_list:
                 print("invalid name(entered that name before)\ntry again\n")
                 break
             #2-not a keyword
             if OUT in reserved_words:
                 print("invalid name (keyword)\ntry again\n")
             #3-none of these in it 
             elif any(substring in special_char for substring in OUT):
                 print("invalid name (includes a special char)\ntry again\n")
             #3-shoudn't start with a digit or $
             elif OUT[0].isdigit():
                 print("invalid module name (it can only start with '_' or an alphabet)\ntry again\n")
             elif OUT[0] == "$":
                 print("invalid module name (it can only start with '_' or an alphabet)\ntry again\n")
             else:
                 while True:
                     try:
                        output_type=int(input("what type is the output (choose 1 or 2)\n1-wire\n2-reg\n"))
                     except:
                        print("not a valid choice \n(choose 1 or 2)\n")
                        continue
                     if not (output_type == 1 or output_type == 2):
                         print("not a valid choice \n(choose 1 or 2)\n")
                         continue
                     else:
                         if out_width == 1:
                             if outputs==1:
                                 if output_type == 1:
                                     F.write("output"+" "+OUT+");\n")
                                     F_tb.write("wire"+" "+OUT+"_TB"+";\n")
                                 else:
                                     F.write("output reg"+" "+OUT+");\n")
                                     F_tb.write("wire"+" "+OUT+"_TB"+";\n")                                  
                             else:
                                 if output_type == 1:
                                     F.write("output"+" "+OUT+",\n")
                                     F_tb.write("wire"+" "+OUT+"_TB"+";\n")
                                 else:
                                     F.write("output reg"+" "+OUT+",\n")
                                     F_tb.write("wire"+" "+OUT+"_TB"+";\n")               
                         else:
                             if outputs == 1:
                                 if output_type == 1:
                                     F.write("output"+" "+"["+str((out_width-1))+":0]"+" "+OUT+");\n")
                                     F_tb.write("wire"+" "+"["+str((out_width-1))+":0]"+" "+OUT+"_TB"+";\n")  
                                 else:
                                     F.write("output reg"+" "+"["+str((out_width-1))+":0]"+" "+OUT+");\n")
                                     F_tb.write("wire"+" "+"["+str((out_width-1))+":0]"+" "+OUT+"_TB"+";\n")  
                             else:
                                 if output_type == 1:
                                     F.write("output"+" "+"["+str((out_width-1))+":0]"+" "+OUT+",\n")
                                     F_tb.write("wire"+" "+"["+str((out_width-1))+":0]"+" "+OUT+"_TB"+";\n")
                                 else:
                                     F.write("output reg"+" "+"["+str((out_width-1))+":0]"+" "+OUT+",\n")
                                     F_tb.write("wire"+" "+"["+str((out_width-1))+":0]"+" "+OUT+"_TB"+";\n")
                                     
                     outputs=outputs-1
                     c2=c2+1
                     output_list.append(OUT)
                     print(output_list)
                     break
                 break
  
while True:
    if seq_com ==2:
        break
    else:
    
        try:
             syn_asy=int(input("specify whether the design is synchronous or asynchronous (choose 1 or 2)\n1-synchronous\n2-asynchronous\n"))
        except:
            print("not a valid choice\n(choose 1 or 2)\n")
            continue
        if syn_asy ==1 or syn_asy==2:
            break
        else:
            print("not a valid choice\n(choose 1 or 2)\n")

#sequential and combinational blocks
#only seq blocks
F.write("\n\n\n\n")
if seq_com ==1:
    F.write("//sequential blocks\n")
    if syn_asy == 1:
        F.write("\n\nalways @(posedge clk)\nbegin\nif (!rst_n)\nbegin\n// Reset condition\nend\nelse\nbegin\n// Non-reset condition\nend\nend\n")
    else:
        F.write("\n\nalways @(posedge clk or negedge rst_n)\nbegin\nif (!rst_n)\nbegin\n// Reset condition\nend\nelse\nbegin\n// Non-reset condition\nend\nend\n")
#only com blocks
if seq_com ==2:
    F.write("//combinational blocks\n")
    F.write("\n\nalways @(*)\nbegin\n\n\n<combinational statements>\n\n\nend\n")
#both 
if seq_com ==3:
    F.write("//sequential and combinational blocks\n")
    if syn_asy == 1:
        F.write("\n\nalways @(posedge clk)\nbegin\nif (!rst_n)\nbegin\n// Reset condition\nend\nelse\nbegin\n// Non-reset condition\nend\nend\n")
        F.write("\n\nalways @(*)\nbegin\n\n\n<combinational statements>\n\n\nend\n")
    else:
        F.write("\n\nalways @(posedge clk or negedge rst_n)\nbegin\nif (!rst_n)\nbegin\n// Reset condition\nend\nelse\nbegin\n// Non-reset condition\nend\nend\n")
        F.write("\n\nalways @(*)\nbegin\n\n\n<combinational statements>\n\n\nend\n")
    
    
    
F.write("\n\nendmodule\n")

# dut instantiation in TB
F_tb.write("\n\n//DUT instantiation\n")
# 1- if there are parameters
if param ==1:
     F_tb.write(module_name + " #(")
     for x, y in zip(param_list,param_values_list):
         if param_list[-1] == x:
             F_tb.write(x + "=" +str(y))
         else:
             F_tb.write(x + "=" +str(y)+",")
     F_tb.write(")")
else:
    F_tb.write(module_name)
    

if seq_com ==2:
    F_tb.write(" DUT"+"(")
    for i in input_list:
        F_tb.write("."+i+"("+i+"_TB),\n")
    for j in output_list:
        if j==output_list[-1]:
            F_tb.write("."+j+"("+j+"_TB)\n")
        else:
            F_tb.write("."+j+"("+j+"_TB),\n")
    F_tb.write(");\n")
    
else:
    F_tb.write(" DUT"+"(.clk(clk_TB),\n.rst_n(rst_n_TB),\n")
    for i in input_list:
        F_tb.write("."+i+"("+i+"_TB),\n")
    for j in output_list:
        if j==output_list[-1]:
            F_tb.write("."+j+"("+j+"_TB)\n")
        else:
            F_tb.write("."+j+"("+j+"_TB),\n")
             
    F_tb.write(");\n")
    
    #clock generation in TB
    F_tb.write("\n\n//clock generation\n")
    F_tb.write("initial begin\n clk_TB = 0;\n forever\n #1 clk_TB = ~clk_TB;\nend")

#generating testcases
if seq_com ==2:
    F_tb.write("\n\ninitial begin\n //initial values for inputs\n\n")
    #test case 1
    F_tb.write("test case 1\n")
    for i in input_list:
        F_tb.write(i+"_TB = ;\n")
    F_tb.write("#10\n\n")
    #test case 2
    F_tb.write("test case 2\n")
    for i in input_list:
        F_tb.write(i+"_TB = ;\n")
    F_tb.write("#10\n\n\n")
    F_tb.write("$stop\nend\nendmodule")

else:
    F_tb.write("\n\ninitial begin\n //reset and initial values for inputs\nrst_n_TB = 0;\n#10\nrst_n_TB = 1;\n")
    #test case 1
    F_tb.write("\n\n\n//test case 1\n")
    for i in input_list:
        F_tb.write(i+"_TB = ;\n")
    F_tb.write("#10\n\n")
    #test case 2
    F_tb.write("\n//test case 2\n")
    F_tb.write("rst_n_TB = 0;\n#2\nrst_n_TB = 1;\n")
    for i in input_list:
        F_tb.write(i+"_TB = ;\n")
    F_tb.write("#10\n\n\n")
    F_tb.write("$stop\nend\nendmodule")

#closing files
F.close()
F_tb.close()






    


    
    
    
    
    
    