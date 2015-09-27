# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:28:31 2015

@author: tyin
"""

import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
import os
os.chdir('D:\Nanodegree\MongoDB')

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons"]

mapping = { 'Ave': "Avenue",
            'Dr': "Drive",
            'Dr.': "Drive",
            'Ln': "Lane",
            'Rd': "Road",
            'St': "Street",
            'st': "Street",
            'street': "Street"
            }

def update_name(name, mapping):
    name_list = name.split(' ')
    street_abbreviation = name_list[-1]
    if street_abbreviation in ['Ave', 'Dr', 'Dr.', 'Ln', 'Rd', 'St', 'st', 'street']:
        new_name = ' '.join(name_list[:-1]) 
        name = new_name + ' ' + mapping[street_abbreviation]
    return name


def shape_element(element):
    node = {}
    node['created']={}
    node['pos']=[]
    if element.tag == "node" or element.tag == "way" :
        node['id'] = element.attrib['id']
        node['type'] =  element.tag
        if 'visible' in element.attrib: 
            node['visible'] = element.attrib['visible']
        node['created'] = {'version':element.attrib['version'], 
                           'changeset':element.attrib['changeset'], 
                           'timestamp':element.attrib['timestamp'], 
                           'user':element.attrib['user'], 
                           'uid':element.attrib['uid']}
        if 'lat' in element.attrib: 
            node['pos'] = [float(element.attrib['lat']), 
                           float(element.attrib['lon'])]
        for tag in element.iter('tag'):
            if tag.attrib['k'] == "addr:street":
                tag.attrib['v'] = update_name(tag.attrib['v'], mapping)
                # print tag.attrib['v']
        address = {}
        flag = False
        for tag in element.iter('tag'):
            if re.search(problemchars, tag.attrib['k']):
                pass
            elif len(tag.attrib['k'].split(':')) == 3:
                pass
            elif "addr:" in tag.attrib['k']:                 
                address[tag.attrib['k'].split(':')[1]] = tag.attrib['v']
                flag = True
            elif "addr:" not in tag.attrib['k'] and len(tag.attrib['k'].split(':')) == 1:
                node[tag.attrib['k']] = tag.attrib['v']
                #print node[tag.attrib['k']]
            elif "addr:" not in tag.attrib['k'] and len(tag.attrib['k'].split(':')) >= 2 :  
                pass
        if flag: 
            node['address'] = address
        node_refs = []
        for tag in element.iter("nd"):
            node_refs.append(tag.attrib["ref"])
            node["node_refs"] = node_refs
        return node
    else:
        return None


def process_map(file_in, pretty = False):
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

# This modified process_map function is for when I don't want to write the JSON file again
def process_map(file_in, pretty = False):
    data = []
    for _, element in ET.iterparse(file_in):
        el = shape_element(element)
        if el:
            data.append(el)
    return data


data = process_map('lincoln_nebraska.osm', False)






