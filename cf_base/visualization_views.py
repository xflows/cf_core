import sys, pprint
# from django.shortcuts import render
# from django.http import Http404, HttpResponse

def object_viewer(request,input_dict,output_dict,widget):
    output_dict = {'object_string':pprint.pformat(input_dict['object'])}
    #return render(request, 'visualizations/object_viewer.html',{'widget':widget,'input_dict':input_dict,'output_dict':output_dict})

    print " ------- obj_view_wrong"
    return render(request, 'visualizations/obj_view_wrong.html',{'widget':widget,'input_dict':input_dict,'output_dict':output_dict})

def display_string(request,input_dict,output_dict,widget):
    return render(request, 'visualizations/display_string.html',{'widget':widget,'input_dict':input_dict,'output_dict':output_dict})

