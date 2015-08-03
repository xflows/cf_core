from workflows.security import safeOpen


def object_viewer(input_dict):
    """ 
    Displays an arbitrary ClowdFlows object
    """
    return {}


def file_to_string(input_dict):
    """ 
    Reads a file and outputs its textual contents
    """
    f = safeOpen(input_dict['file'])
    output_dict = {}
    output_dict['string']=f.read()
    return output_dict

def load_to_string(input_dict):
    '''
    Opens the file and reads its contents into a string.
    '''
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

