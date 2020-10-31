# -*- coding: utf-8 -*-

"""
pyaction.beautifulsoup_.objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main objects of the beautifulsoup field.

"""

__all__ = ['get_xpath']

#-----------------------------------------------------------------------------

def get_xpath(element):

    def get_index(el):
        prev_sibs = [tag for tag in el.previous_siblings if tag.name == el.name]
        next_sibs = [tag for tag in el.next_siblings if tag.name == el.name]

        if (len(prev_sibs) != 0) and (len(next_sibs) != 0):
            result = '[' + str(len(prev_sibs) + 1) + ']'
        elif (len(prev_sibs) == 0) and (len(next_sibs) != 0):
            result = '[1]'
        elif (len(prev_sibs) != 0) and (len(next_sibs) == 0):
            result = '[' + str(len(prev_sibs) + 1) + ']'
        elif (len(prev_sibs) == 0) and (len(next_sibs) == 0):
            result = ''
        else:
            result = ''

        return result

    xpath = ''
    current_element = element
    while current_element.name != 'html':
        xpath = '/' + current_element.name + get_index(current_element) + xpath
        current_element = current_element.parent

    return '/html' + xpath

#-----------------------------------------------------------------------------
