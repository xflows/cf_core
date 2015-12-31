#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'daleksovski'

from django.shortcuts import render

def object_viewer(request,input_dict,output_dict,widget):
    import pprint
    output_dict = {'object_string':pprint.pformat(input_dict['object'])}
    return render(request, 'visualizations/object_viewer.html',{'widget':widget,'input_dict':input_dict,'output_dict':output_dict})


def display_string(request,input_dict,output_dict,widget):
    return render(request, 'visualizations/display_string.html',{'widget':widget,'input_dict':input_dict,'output_dict':output_dict})

def string_to_file(request,input_dict,output_dict,widget):
    import helpers

    destination = helpers.get_media_root()+'/'+str(request.user.id)+'/'+str(widget.id)+'.txt'
    helpers.ensure_dir(destination)
    f = open(destination,'w')
    f.write(str(input_dict['string']))
    f.close()
    filename = str(request.user.id)+'/'+str(widget.id)+'.txt'
    output_dict['filename'] = filename
    return render(request, 'visualizations/string_to_file.html',{'widget':widget,'input_dict':input_dict,'output_dict':output_dict})
