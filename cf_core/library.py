#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'daleksovski'

def core_object_viewer(input_dict):
    """ 
    Displays an arbitrary ClowdFlows object
    """
    return {}


def core_file_to_string(input_dict):
    """ 
    Reads a file and outputs its textual contents
    """
    from workflows.security import safeOpen

    f = safeOpen(input_dict['file'])
    output_dict = {}
    output_dict['string']=f.read()
    return output_dict

def core_string_to_file(input_dict):
    return {}


def core_load_to_string(input_dict):
    '''
    Opens the file and reads its contents into a string.
    '''
    from workflows.security import safeOpen

    f = safeOpen(input_dict['file'])
    output_dict = {}
    output_dict['string']=f.read()
    return output_dict
    
def core_create_integer(input_dict):
    """ 
    Creates an integer value
    """
    output_dict = {}
    output_dict['integer'] = input_dict['integer']
    return output_dict

def core_create_string(input_dict):
    """ 
    Creates a textual value
    """
    return input_dict  

def core_display_string(input_dict):
    """ 
    Displays a textual value
    """
    return {}

def core_safe_eval_string(input_dict):
    """Safe evaluation of a string as a Python command
    Only literal structures can be evaluated: strings, numbers, tuples, lists, dicts, booleans, and None
    """

    import ast
    sdata = str(input_dict['data'])
    try:
        result = ast.literal_eval(sdata)
    except ValueError:
        raise Exception('Cannot evaluate string (remember, for safety reasons only literal structures can be evaluated: strings, numbers, tuples, lists, dicts, booleans, and None)')
    except SyntaxError:
        raise Exception('Invalid string! Please check all quotes, commas, ...')
    else:
        return {'evaluation_result': result}

def core_object_viewer(input_dict):
    return {}


def core_concatenate_lists(input_dict):
    lists = input_dict['lists']
    new_list = []
    for every_list in lists:
        new_list = new_list+every_list
    output_dict = {}
    output_dict['list']=new_list
    return output_dict

def core_merge_dictionaries(input_dict):
    dict1 = input_dict['dict1']
    dict2 = input_dict['dict2']
    items = list(dict1.items())+list(dict2.items())
    output_dict = {}
    output_dict['dict']=dict(items)
    return output_dict

def core_create_list(input_dict):
    return input_dict

def core_create_tuple(input_dict):
    lists = input_dict['elements']
    output_dict = {}
    output_dict['tuple'] = tuple(lists)
    return output_dict

def core_create_dictionary(input_dict):
    keys = input_dict['keys']
    values = input_dict['values']
    dic = {}
    for idx in range(0,min(len(keys),len(values))):
        dic[keys[idx]] = values[idx]
    output_dict = {'dict': dic}
    return output_dict

def core_create_range(input_dict):
    output_dict = {}
    output_dict['rangeout'] = list(range(int(input_dict['n_range'])))
    return output_dict

def core_delay(input_dict,widget):
    widget.progress=0
    widget.save()
    timeleft = int(input_dict['time'])
    i = 0
    import time
    import math
    while i<timeleft:
        time.sleep(1)
        i=i+1
        widget.progress = math.floor(((i*1.0)/timeleft)*100)
        widget.save()
    widget.progress=100
    widget.save()
    output_dict = {}
    output_dict['data'] = input_dict['data']
    return output_dict


def core_ensemble(input_dict):
    import math
    ens = {}
    data_inds = input_dict['data_inds']
    ens_type = input_dict['ens_type']
    # TODO ens_level = input_dict['ens_level']
    for item in data_inds:
        #det_by = item['detected_by']
        for i in item['inds']:
            if i not in ens:
                ens[i] = 1
            else:
                ens[i] += 1

    ens_out = {}
    ens_out['name'] = input_dict['ens_name']
    ens_out['inds'] = []
    n_algs = len(data_inds)
    print(ens_type)
    if ens_type == "consensus":
        ens_out['inds'] = sorted([x[0] for x in list(ens.items()) if x[1] == n_algs])
    else: # majority
        ens_out['inds'] = sorted([x[0] for x in list(ens.items()) if x[1] >= math.floor(n_algs/2+1)])

    output_dict = {}
    output_dict['ens_out'] = ens_out
    return output_dict

def core_pickle_object(input_dict):
    '''
    Serializes the input object.
    '''
    pkl_obj = cPickle.dumps(input_dict['object'])
    output_dict = {}
    output_dict['pickled_object'] = pkl_obj
    return output_dict

def core_unpickle_object(input_dict):
    '''
    Serializes the input object.
    '''
    obj = cPickle.loads(str(input_dict['pickled_object']))
    output_dict = {}
    output_dict['object'] = obj
    return output_dict

def core_stopwatch(input_dict):
    import time
    inputTime = input_dict['time_in']
    now = time.time()
    if (isinstance(inputTime, float)):
        elapsedTime = now - inputTime
    else:
        elapsedTime = None
    output_dict = {}
    output_dict['signal_out'] = input_dict['signal']
    output_dict['time_out'] = now
    output_dict['time_span'] = elapsedTime

    return output_dict


def core_safe_eval_string(input_dict):
    import ast
    sdata = str(input_dict['data'])
    try:
        result = ast.literal_eval(sdata)
    except ValueError:
        raise Exception('Cannot evaluate string (remember, for safety reasons only literal structures can be evaluated: strings, numbers, tuples, lists, dicts, booleans, and None)')
    except SyntaxError:
        raise Exception('Invalid string! Please check all quotes, commas, ...')
    else:
        return {'evaluation_result': result}
#end


def core_ravel_list(input_dict):
    def core_ravel(data, result):
        for x in data:
            if not isinstance(x, list):
                result.append(x)
            else:
                if x:
                    ravel(x, result)
    #end

    ilist = input_dict['input_list']
    result = []
    ravel(ilist, result)
    return {'clean_list': result}
#end

def core_split_documents(input_dict):
    output_dict = {}
    documents = input_dict['string'].splitlines()
    query = input_dict['class']
    new_documents = []
    for doc in documents:
        if doc.split(' ',1)[0]==input_dict['class']:
            new_documents.append(doc.split(" ",1)[1])
    output_dict['string']="\n".join(new_documents)
    return output_dict

def core_extract_results(input_dict):
    fbeta = 1
    fscore = input_dict['fscore']
    precision = input_dict['precision']
    recall = input_dict['recall']
    auc = input_dict['auc']
    accuracy = input_dict['accuracy'] * 100 # ViperCharts expects percentages
    runtime = input_dict['runtime']
    name = input_dict['name']
    results = {'fbeta':1,'fscore':fscore,'name': name,'precision': precision,'recall': recall,'auc': auc,'accuracy': accuracy,'runtime': runtime}
    output_dict = {}
    output_dict['results']=results
    return output_dict

def core_unzip_list(input_dict):
    '''
    Unzips a list of tuples for the given index.

    Example inputs:

        index = 0
        input_list = [(a, 1), (b, 2), (c, 3)]

        result: [a, b, c]

    or

        index = 1
        input_list = [(a, 1), (b, 2), (c, 3)]

        result: [1, 2, 3]
    '''
    idx = int(input_dict.get('index', 0))
    input_list = input_dict['input_list']
    unzipped_list = [el[idx] for el in input_list]

    return {'unzipped_list': unzipped_list}

def core_average_list(input_dict):
    '''
    Computes the average of the given input list.
    '''
    input_list = input_dict['input_list']

    if input_list:
        average = sum(input_list)/float(len(input_list))
    else:
        average = None

    return {'average': average}

def core_js_snippet(input_dict):
    return {'out': None}

def core_js_snippet_finished(postdata, input_dict, output_dict):
    try:
        out_list = json.loads(postdata['out'][0])
        out = out_list[0]
    except:
        raise Exception("Problem de-serializing the output.")
    return {'out': out}
