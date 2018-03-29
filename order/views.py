from django.http import HttpResponse
import xml.etree.ElementTree as ET
import operator
import json

namespaces = {'g': 'http://base.google.com/ns/1.0'}


def orderpricedesc(request):
    tree = ET.parse('test.xml')
    root = tree.getroot()
    items = root.findall('./channel/item')
    data = {}
    for a in items:
        title_item = a.find('g:id', namespaces).text
        price_item = a.find('g:price', namespaces)
        price_value = price_item.text
        price_value = price_value.replace('DKK', '')
        data[title_item] = float(price_value)

    sorted_data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    final_data = dict(sorted_data[0:20])
    return HttpResponse(json.dumps(final_data))


def orderdiscountdesc(request):
    tree = ET.parse('test.xml')
    root = tree.getroot()
    items = root.findall('./channel/item')
    data = {}
    for a in items:
        title_item = a.find('g:id', namespaces).text
        price_item = a.find('g:price', namespaces)
        discount_item = a.find('g:custom_label_0', namespaces)
        price_value = price_item.text
        price_value = price_value.replace('DKK', '')
        try:
            discount_value = discount_item.text
        except:
            discount_value = price_value
        discount_percent = float(price_value) - float(discount_value)
        data[title_item] = float(discount_percent)

    sorted_data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    final_data = dict(sorted_data[0:20])
    return HttpResponse(json.dumps(final_data))


def getcomedy(request):
    tree = ET.parse('test.xml')
    root = tree.getroot()
    items = root.findall('./channel/item')
    data = {}
    for a in items:
        title_item = a.find('g:id', namespaces).text
        product_type_item = a.find('g:product_type', namespaces)
        product_type = product_type_item.text
        if "Comedy" in product_type:
            data[title_item] = product_type

    return HttpResponse(json.dumps(data))
