def count_words(text):
    count_list = text.split()
    return len(count_list)

def count_characters(text):
    converted = text.lower()

    dict = {}

    for char in converted:
        if char in dict:
            dict[char]+=1
        else:
            dict[char]=1
    
    return dict

def sort_dict(dict):

    dict_list = []

    for key in dict:
            curr_dict={}
            curr_dict["name"] = key
            curr_dict["num"] = dict[key]
            dict_list.append(curr_dict)

    
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    
def sort_on(dict):
    return dict["num"]
