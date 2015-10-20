def object_viewer(input_dict):
    """ 
    Displays an arbitrary ClowdFlows object
    """
    return {}


def file_to_string(input_dict):
    """ 
    Reads a file and outputs its textual contents
    """
    from workflows.security import safeOpen

    f = safeOpen(input_dict['file'])
    output_dict = {}
    output_dict['string']=f.read()
    return output_dict

def string_to_file(input_dict):
    return {}


def load_to_string(input_dict):
    '''
    Opens the file and reads its contents into a string.
    '''
    from workflows.security import safeOpen

    f = safeOpen(input_dict['file'])
    output_dict = {}
    output_dict['string']=f.read()
    return output_dict
    
def create_integer(input_dict):
    """ 
    Creates an integer value
    """
    output_dict = {}
    output_dict['integer'] = input_dict['integer']
    return output_dict

def create_string(input_dict):
    """ 
    Creates a textual value
    """
    return input_dict  

def display_string(input_dict):
    """ 
    Displays a textual value
    """
    return {}

def safe_eval_string(input_dict):
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
