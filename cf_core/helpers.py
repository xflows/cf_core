#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pysimplesoap
from pysimplesoap.client import SoapClient

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

def safeOpen(filename):
    from django.conf import settings

    if filename.startswith(settings.FILES_FOLDER):
        if filename.find("..")==-1:
            return open(filename,'r')
        else:
            raise Exception("Invalid filename")
    else:
        raise Exception("Invalid filename.")



def get_media_root():
    from mothra.settings import MEDIA_ROOT
    return MEDIA_ROOT #"/tmp"

class UnpicklableObject:
    """Methods for object deserialization"""
    def __init__(self, init_string):
        self.init_string = init_string
        self.imports = []

    def addimport(self,import_string):
        self.imports.append(import_string)

    def generate(self):
        for i in self.imports:
            exec(i)
        return eval(self.init_string)

    def __unicode__(self):
        return self.init_string

    def __str__(self):
        return self.init_string

    def __repr__(self):
        return self.init_string


class WebService:
    """WebService methods"""

    def __init__(self, wsdl_url, timeout=60):
        pysimplesoap.client.TIMEOUT = timeout
        self.client = SoapClient(wsdl=wsdl_url,trace=False)
        self.wsdl_url = wsdl_url
        self.name = wsdl_url
        self.methods = []
        for service in list(self.client.services.values()):
            for port in list(service['ports'].values()):
                for op in list(port['operations'].values()):
                    method = {}
                    try:
                        method['documentation']=op['documentation']
                    except:
                        method['documentation']="No documentation provided."
                    method['name']=op['name']
                    method['inputs']=[]
                    method['outputs']=[]
                    try:
                        input_dict = list(op['input'].values())[0]
                    except:
                        input_dict = []
                    for i in input_dict:
                        input = {}
                        input['name']=i
                        input['type']=input_dict[i]
                        method['inputs'].append(input)
                    try:
                        output_dict = list(op['output'].values())[0]
                    except:
                        output_dict = [[]]
                    if type(output_dict)==type([]):
                        output_dict = output_dict[0]
                    for o in output_dict:
                        output = {}
                        output['name']=o
                        method['outputs'].append(output)
                    self.methods.append(method)
    def __unicode__(self):
        return self.wsdl_url
    def __str__(self):
        return self.wsdl_url
