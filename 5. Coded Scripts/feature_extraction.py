import sys

# Written by Tanzia Haque Tanzi & Mahbub Ul Alam

#to check whether the anaphor is nested or not
def nested_anaphor_check(antecedent_words, anaphor_words, antecedent_sentence_number, anaphor_sentence_number):
    
    nested_anaphor_found = False
    
    if anaphor_words in antecedent_words and antecedent_sentence_number == anaphor_sentence_number:
        nested_anaphor_found = True
        
    return nested_anaphor_found
    
    

def distant_feature_extraction(antecedent_sentence_number, anaphor_sentence_number):
    
    value = float ( int(anaphor_sentence_number) - int(antecedent_sentence_number) )
    
    return value

def pronoun_feature_extraction(pos):
    
    noun_list = [ "NN", "NNS", "NNP", "NNPS" ]
    pronoun_list = [ "PRP", "PRP$", "WP", "WP$" ]
    
    noun_found = False
    pronoun_found = 0.0
    pos_list = pos.split(" ")
    
    
    for item in pos_list:
        if item in noun_list:
            noun_found = True
            break
    
    if noun_found == False:
        for item in pos_list:
            if item in pronoun_list:
                pronoun_found = 1.0
                break
    
    return pronoun_found

def string_match_feature_extraction(antecedent_words, anaphor_words):
    
    remove_list = ["a", "an", "the", "this", "these", "that", "those"]
    
    string_match_found = 0.0
    
    antecedent_words = antecedent_words.lower()
    anaphor_words = anaphor_words.lower()
    
    antecedent_words_list = antecedent_words.split(" ")
    anaphor_words_list = anaphor_words.split(" ")
    
    for item in antecedent_words_list:
        if item in remove_list:
            antecedent_words_list.remove(item)
            
    for item in anaphor_words_list:
        if item in remove_list:
            anaphor_words_list.remove(item)
            
    antecedent_words = ' '.join(antecedent_words_list)
    anaphor_words = ' '.join(anaphor_words_list)
    
    
    if(antecedent_words == anaphor_words):
        string_match_found = 1.0
        
    return string_match_found

def definite_noun_phrase_feature_extraction(anaphor_words):
    
    definite_noun_phrase_found = 0.0
    
    anaphor_words = anaphor_words.lower()
    
    anaphor_words_list = anaphor_words.split(" ")
    
    if anaphor_words_list[0]=="the":
        definite_noun_phrase_found = 1.0
    
    return definite_noun_phrase_found

def demonstrative_noun_phrase_feature_extraction(anaphor_words):
    
    starting_word_list = [ "this", "that", "these", "those"]
    
    demonstrative_noun_phrase_found = 0.0
    
    anaphor_words = anaphor_words.lower()
    
    anaphor_words_list = anaphor_words.split(" ")
    
    if anaphor_words_list[0] in starting_word_list:
        demonstrative_noun_phrase_found = 1.0
        
    return demonstrative_noun_phrase_found

def name_entity_match_feature_extraction(antecedent_name_entity, anaphor_name_entity):
    
    name_entity_match_found = 0.0
    
    antecedent_name_entity = antecedent_name_entity.lower()
    anaphor_name_entity = anaphor_name_entity.lower()
    
    if antecedent_name_entity!="null" and antecedent_name_entity == anaphor_name_entity:
        
        name_entity_match_found = 1.0
        
    return name_entity_match_found
            
    
#this method prints all the features values for machine learning. we are considering the following features,

# sentence_distant_feature
# antecedent_pronoun_feature
# anaphor_pronoun_feature
# string_match_feature
# definite_noun_phrase_feature
# demonstrative_noun_phrase_feature
# name_entity_match_feature     

def feature_extraction_main(potential_antecedent, potential_anaphor, coreferent_value, test_data_check):
    
    potential_antecedent_values = potential_antecedent.split(" | ")
    potential_anaphor_values = potential_anaphor.split(" | ")
    
    final_output_list = []
    
    nested_anaphor_found = False
    
    if coreferent_value == True:
        coreferent_target_value = 1.0
    else:
        coreferent_target_value = 0.0
    
    
    if test_data_check == True:
        nested_anaphor_found = nested_anaphor_check(potential_antecedent_values[0], potential_anaphor_values[0],potential_antecedent_values[4], potential_anaphor_values[4])     
            
    if test_data_check == False or nested_anaphor_found == False:
        
        distant_feature = distant_feature_extraction(potential_antecedent_values[4], potential_anaphor_values[4])
        antecedent_pronoun_feature = pronoun_feature_extraction(potential_antecedent_values[1])
        anaphor_pronoun_feature = pronoun_feature_extraction(potential_anaphor_values[1])
        string_match_feature = string_match_feature_extraction(potential_antecedent_values[0], potential_anaphor_values[0])
        definite_noun_phrase_feature = definite_noun_phrase_feature_extraction(potential_anaphor_values[0])
        demonstrative_noun_phrase_feature = demonstrative_noun_phrase_feature_extraction(potential_anaphor_values[0])
        name_entity_match_feature = name_entity_match_feature_extraction(potential_antecedent_values[2], potential_anaphor_values[2])
    
        final_output_list.append(str(coreferent_target_value))
        final_output_list.append(str(distant_feature))
        final_output_list.append(str(antecedent_pronoun_feature))
        final_output_list.append(str(anaphor_pronoun_feature))
        final_output_list.append(str(string_match_feature))
        final_output_list.append(str(definite_noun_phrase_feature))
        final_output_list.append(str(demonstrative_noun_phrase_feature))
        final_output_list.append(str(name_entity_match_feature))

        final_output = ','.join((final_output_list))
    
        
        if test_data_check == True:
            #sys.stdout = open("output/test_features", 'a')
            file1 = open("output/test_features", "a")
            file1.write(final_output + "\n")
            file1.close()
        elif test_data_check == False:
            #sys.stdout = open("output/training_features", 'a')
            file1 = open("output/training_features", "a")
            file1.write(final_output + "\n")
            file1.close()
        #print final_output
        
        
        if test_data_check == False and coreferent_value == False:
            #sys.stdout = open("output/training_data_Negative_chain_lines", 'a') 
            #print potential_antecedent+ " |**| "+potential_anaphor
            file1 = open("output/training_data_Negative_chain_lines", "a")
            file1.write(potential_antecedent+ " |**| "+potential_anaphor + "\n")
            file1.close()
        elif test_data_check == False and coreferent_value == True:
            #sys.stdout = open("output/training_data_Positive_chain_lines", 'a')
            #print potential_antecedent+ " |**| "+potential_anaphor
            file1 = open("output/training_data_Positive_chain_lines", "a")
            file1.write(potential_antecedent+ " |**| "+potential_anaphor + "\n")
            file1.close()
        elif test_data_check == True and coreferent_value == True:
            #sys.stdout = open("output/test_data_Positive_chain_lines", 'a')
            #print potential_antecedent+ " |**| "+potential_anaphor
            file1 = open("output/test_data_Positive_chain_lines", "a")
            file1.write(potential_antecedent+ " |**| "+potential_anaphor + "\n")
            file1.close()
        elif test_data_check == True and coreferent_value == False and nested_anaphor_found == False:
            #sys.stdout = open("output/test_data_Negaitive_chain_lines", 'a')
            #print potential_antecedent+ " |**| "+potential_anaphor
            file1 = open("output/test_data_Negaitive_chain_lines", "a")
            file1.write(potential_antecedent+ " |**| "+potential_anaphor + "\n")
            file1.close()
    

    
#this method creates all the negative pairs of coreferents    
def creating_negaitive_chains(coreference_chain_number_list, file_data, test_data_check):
      
    for row_index in range(len(coreference_chain_number_list)):
        
        for item_index in range(len(coreference_chain_number_list[row_index]) -1 ):
            
            antecedent_item_line_number = coreference_chain_number_list[row_index][item_index]
            
            anaphor_item_line_number = coreference_chain_number_list[row_index][item_index+1] 
            
            if anaphor_item_line_number - antecedent_item_line_number > 1:
                
                anaphor_line = file_data[anaphor_item_line_number]
                
                
                for line_index in range(antecedent_item_line_number + 1, anaphor_item_line_number ):
                    
                    antecedent_line = file_data[line_index]
                    
                    feature_extraction_main(antecedent_line, anaphor_line, False, test_data_check)


#this method creates all the positive co-reference chain pairs
def creating_positive_chains(coreference_chain_value_list, test_data_check):
    
    #print "creating_positive_chains: "
    
    for row_index in range(len(coreference_chain_value_list)):
        for item_index in range(len(coreference_chain_value_list[row_index]) -1 ):
            
            antecedent_line = coreference_chain_value_list[row_index][item_index]
            anaphor_line = coreference_chain_value_list[row_index][item_index+1]
            
            feature_extraction_main(antecedent_line, anaphor_line, True, test_data_check)


#this is a preprocessing function for storing the coreference ids. for our help we are re-mapping the
#ids here
def change_corefrence_id_in_file_data(file_data, segment_begin_line_number, segment_end_line_number):
    
    coreference_mapping = {}
    coreference_number_list = []
    
    for line_index in range(segment_begin_line_number, segment_end_line_number):
        line = file_data[line_index]
        markable_items = line.split(" | ")
        if len(markable_items)==5 and markable_items[3]!="null" and markable_items[3].isdigit()==True:
            coreference_id = int(markable_items[3])
            coreference_number_list.append(coreference_id)
    
    coreference_number_list = list (set ( coreference_number_list ))
    
    
    for line_index in range (len(coreference_number_list)):
        mapping_key = coreference_number_list[line_index]
        mapping_value = line_index
        coreference_mapping[mapping_key] = mapping_value
        
    return coreference_mapping
            
    
#this method stores corefrence chain values in a list
def corefrence_chain_calculation(file_data, segment_begin_line_number, segment_end_line_number,test_data_check):
    
    
    coreference_mapping = change_corefrence_id_in_file_data(file_data, segment_begin_line_number, segment_end_line_number)
    coreferent_count = len(coreference_mapping)
    
    line_count = segment_begin_line_number - 1
    
    coreference_chain_number_list = [[]for j in range(coreferent_count)]
    coreference_chain_value_list = [[]for j in range(coreferent_count)]
    
    

    for line_index in range(segment_begin_line_number, segment_end_line_number):
        line_count = line_count + 1
        line = file_data[line_index]
        markable_items = line.split(" | ")
        
        if len(markable_items)==5 and markable_items[3]!="null" and markable_items[3].isdigit()==True:
            
            coreference_id = int(markable_items[3])
            new_coreference_id = coreference_mapping[coreference_id]
            coreference_chain_number_list[new_coreference_id].append(line_count)
            coreference_chain_value_list[new_coreference_id].append(line)
    
    #now sending the value lists for calculating the pairs
    creating_positive_chains(coreference_chain_value_list, test_data_check)
    creating_negaitive_chains(coreference_chain_number_list, file_data, test_data_check)
    
    coreference_chain_number_list[:] = []
    coreference_chain_number_list[:] = []

#this method calculate the boundary of each segment in markable file
def markable_data_manipulation(markable_file_name, test_data_check):
    
    
    segment_count_list = []
    
    raw_data = open(markable_file_name)
    
    file_data = raw_data.read().split('\n')
    raw_data.close()
    
    for line_index in range (len (file_data)):
        if "#begin" in file_data[line_index]:
            segment_count_list.append(line_index)
    
    for line_index in range (len (segment_count_list)-1):
        
        segment_begin_line_number = int ( segment_count_list[line_index] ) + 1
        segment_end_line_number = int ( segment_count_list[line_index + 1] ) - 1
        
        #now the boundary information and the data are sent for future calculation 
        corefrence_chain_calculation(file_data, segment_begin_line_number, segment_end_line_number,test_data_check)
        

markable_data_manipulation("output/test_markables", True)#False=training data, True=test data
markable_data_manipulation("output/training_markables", False)#False=training data, True=test data


