# -*- coding: utf-8 -*-
import copy
import sys
from time import time

# Written by Tanzia Haque Tanzi & Mahbub Ul Alam

production_list = []
position_list = []

#we are using bengali charecter as a distinction marker
special_charecter = 'ফ'
special_segment_charecter = 'ব'

#this function makes each line in a printable version.
#it arranges the features as,
#format: words | pos | Name entity value | coreference chain id | sentence number
#example: conscientious Chinese sons and daughters | JJ JJ NNS CC NNS | NORP | 45 | 6
def print_data(data_list):
    
    output_data = []

    for row in data_list:
        c = ['*','*','','']
        for item in row:
            b = item.split(special_segment_charecter)
            b[0]=b[0].replace("*","")
            c[0] = c[0] + " " +b[0]
            c[1] = c[1] + " " +b[1]
            c[2] = c[2] + "" +b[2]
            c[3] = c[3] + " " +b[3]
            #print b
        c[0]=c[0].replace("* ","")
        c[1]=c[1].replace("* ","")
        c[2]=c[2].replace("*","")
        #print c
        if len(c[2])==0 or c[2][0]!='[' or c[2][-1]!=']'or c[2].count("[")>1:
            c[2]='null'
        else:
            c[2]=c[2].replace("[","")
            c[2]=c[2].replace("]","")
        
        c[3]=c[3].replace("|"," ")
    
        #f = c[3]
        q = c[3].split()
    
        if q[0][0]!='[' or q[-1][-1]!=']':
            c[3]='null'
        else:
            q[0]=q[0].replace("[","")
            q[0]=q[0].replace("]","")
            #c[3] = int(q[0])
            c[3] = (q[0])
    
    
        
        output_data.append(c)
        
    return output_data

#this method sends the initial NP phrases(without full pos expansion)
def store_initial_NP_list(tree):
   
    c = copy.deepcopy(tree)

    NP_list = []
    k=-1
    count_new_item=0
    for row_index in range(len(c)):
        if(c[row_index][0]=='NP'):
            k=k+1
            NP_list.append(c[row_index])
            NP_list[k].append(row_index)
            del NP_list[k][0]
   
    c[:] = []
    return NP_list

#this method sends the final NP phrases(with full pos expansion up to it's leaf node)
def store_NP_values(tree, NP_list):
    
    
    b = copy.deepcopy(tree)

    k=0

    while k==0:
        for item_index in range(len(NP_list)-1):
        
        
            selected_item = NP_list[item_index]
            
            if selected_item.count("*")==0:
                
            
                replacable_item = NP_list[item_index]
                
        
                browsing_row_starting_point = int (NP_list[-1])
                browsing_row_starting_point = browsing_row_starting_point + 1
        
                for browsing_row_index in range(browsing_row_starting_point, len(b)):
                    if b[browsing_row_index][0] == replacable_item:
                    
                        NP_list[item_index] = 'bla*'
                        count_new_item=0
                        initial_insert_position_index = item_index
                        for item_index_main in range(1, len(b[browsing_row_index])):
                            
                            count_new_item = count_new_item + 1
                            inserting_position_index = initial_insert_position_index + count_new_item
                            
                            inserting_item = b[browsing_row_index][item_index_main]
                            
                            NP_list.insert(inserting_position_index, inserting_item )
                            
                        b[browsing_row_index][0] = "1969"
                        
                        break
                
                for check_item_index in range(len(NP_list)-1):
                    if NP_list[check_item_index].count("*")== 0:
                        k = 0
                        break
                    else:
                        k = 1
                
    clean_list = []    

    for item_index in range(len(NP_list)-1):
        if NP_list[item_index]!='bla*':
            
            clean_list.append(NP_list[item_index])
   
    b[:] = []
    
    return clean_list

#this method stores all the branches of the tree in a 2d list. the
# first item in each row is the parent of that branch and other items of the
#same row are its child nodes
def print_out(actual_length):
    
    output_list = []
    
    for j in range(actual_length+1):
        
        #if production_list[j].count("NP") == 1:
        individual_line = production_list[j].split(' ')
        #if individual_line[0]=="NP":
        output_list.append(individual_line)
    return output_list

#this method calculates all the branches of the tree and store them in Production_list. It is
#a bit redundant as we need only the NP phrases, but this is helfull if in case we need any other
#branches in future
def calculate_production(s):
    k=0
    c=0
    terminal = ''
    for i in range(len(s)):
        if s[i] == ')':
            c=0
            s[i] = special_charecter #deleting values
            k = i-1
            while True:
                if s[k] != special_charecter and s[k] != '(':
                    terminal = terminal + s[k]
                    s[k] = special_charecter
                    k = k-2
                    
                elif s[k]=='(':
                    append(k,terminal)
                    terminal = ''
                    s[k] = special_charecter
                    break
                    
                elif s[k]==special_charecter:
                    search_range = k
                    while True:
                        if s[k]=='(':
                            break
                        else:
                            k = k-1
                    
                    for g in range(k+2, search_range):
                        if s[g] != special_charecter:
                            if c==0:
                                terminal = terminal + s[g]
                                c=1
                            else:
                                terminal = terminal + ' ' + s[g]
                            s[g] = special_charecter

#this method helps to dishtinguish between terminal and non-terminal
def append(position, terminal):
    for i in range(len(position_list)):
        if position_list[i] == position:
            non_terminal = production_list[i]
            non_terminal_position = i
            break
    non_terminal = non_terminal + ' ' + terminal
    production_list[non_terminal_position] = non_terminal

#this method returns the length of the longest branch of the tree
#this is needed for extracting the NP branches from the tree
def store_non_terminal_pos(s):
    actual_length = -1
    length = len(production_list)
    k=0
    for i in range(len(s)):
        if s[i]=='(':
            actual_length = actual_length+1
            m = s[i+1]
            if(length==0 or k>length-1):
                production_list.append(m)
                position_list.append(i)
            else:
                production_list[k] = m
                position_list[k] = i
                k = k + 1 
                
    return(actual_length)

#parse tree or othe 'unclear' data is formatted here for processing purposes
def parse_tree_formating(line):
    
    temp_data = list(line)
    temp_data[0]=''
    temp_data[1]=''
    temp_data[len(temp_data)-1]=''
    temp_data[len(temp_data)-2]=''
    temp_data = [w.replace('(', '('+special_charecter) for w in temp_data]
    temp_data = [w.replace(')', special_charecter+')') for w in temp_data]
    temp_data = [w.replace(' ', special_charecter) for w in temp_data]
    s = ''.join(temp_data)
    
    temp_data[:] = []
    
    list_data = s.split(special_charecter)
    
    return list_data
    
#this fucntion acts as a controller and communicates with other helper functions    
def parsing_line(line, sentence_count):
    

     
    sentence_list =[]
    data = []
    printable_version = []
   
    list_data = parse_tree_formating(line)
        
    actual_length = store_non_terminal_pos(list_data)
            
    calculate_production(list_data)
    
    individual_output = print_out(actual_length)
    
    #clearing list
    production_list[:] = []
    position_list[:] = []
    
    #here only the NP branches are collected with their initial values
    #ex. NP --> NP NNP
    initial_NP_list = store_initial_NP_list(individual_output)
    
    for row in initial_NP_list:
        
        #here the final version of NP is collected
        #ex. NP --> DET NNP NNP 
        final_NP_list = store_NP_values(individual_output, row)
        data.append(final_NP_list)
        
    #clearing list
    initial_NP_list[:] = []
    
    individual_output[:] = []
    
    printable_version = print_data(data)
    
    data[:] = []
    
    #No we have the printable lines with the following feeatures,
    #1. words, 2. POS, 3. Name entity value, 4. coreference chain id and 5. sentence number
    for row in printable_version:
        row.append(str(sentence_count))
        each_line = ' | '.join(row)
        sentence_list.append(each_line)
        
    
    printable_version[:] = []
    
    #finally we are printing the lines in a file
    for row in sentence_list:
        print row
        
    
    
#in this function we are generating one sentence at a time with annotation features
#(parse tree, pos, name entity, sentence number and coreference section) and sending the mixed data to
#parsing_line() function for clearing and markable creating.
def main_calculation(file_location):
    raw_data = open(file_location)
    
    file_data = raw_data.read().split('\n')
    raw_data.close()

    sentence_count = 1

    full_tree=''
    
    for line in file_data:
        
        temp_data = line.split()

        if(len(temp_data)!=0):
            
            initial_check = temp_data[0]
            
            if initial_check == "#begin":
                print line
            
            elif initial_check!="#end":
                
                
                parse_bit = temp_data[5]
        
                parse_bit=parse_bit.replace("(", " (")
        
                if temp_data[2] == '0':
                    parse_bit=parse_bit.replace(" (TOP","(")
        
                extra_bit = special_segment_charecter+temp_data[4]+special_segment_charecter+temp_data[10]+special_segment_charecter+temp_data[-1]
                extra_bit= extra_bit.replace("(", "[")
                extra_bit= extra_bit.replace(")", "]")
                
                parse_bit = parse_bit.replace("*", " ("+temp_data[4]+" "+temp_data[3]+"*"+extra_bit+")")
                
                full_tree = full_tree + parse_bit   
        
        else:
            
            full_tree=full_tree[:-1] + ' ' + full_tree[-1:]
            #print full_tree
            if len(full_tree)!=1:
                parsing_line(full_tree, sentence_count)
                full_tree=''
                sentence_count = sentence_count + 1
            else:
                full_tree=''


#training_data = raw_input("Enter the name of training data file [with full address if it is in other location]:\n")
#test_data = raw_input("Enter the name of test data file [with full address if it is in other location]:\n")			
				
sys.stdout = open("output/training_markables", 'w')
main_calculation("ontonotes-train.conll")

print "#begin added for final padding between file segments"
sys.stdout = open("output/test_markables", 'w')
main_calculation("ontonotes-test.conll")
print "#begin added for final padding between file segments"

