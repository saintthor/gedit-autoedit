# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 2016

@author: thor
"""
import re

def ReplaceSymbols( text ):
    ""
    for symbols in (( ',', '，' ), ( '.', '。' ), ( ';', '；' ), ( ':', '：' ), 
                    ( '?', '？' ), ( '!', '！' ), ( '(', '（' ), ( ')', '）' )):
        text = text.replace( *symbols )
        
    for OldSymb, ( LeftSymb, RightSymb ) in (( "'", ( "“", "”" )), ( '"', ( "‘", "’" ))):
        if OldSymb in text:
            text = text.replace( OldSymb, LeftSymb, 1 ).replace( OldSymb, RightSymb, 1 )
    
    return text

def AutoFormat( window, JoinLines = True ):
    ""
    doc = window.get_active_document()
    start, end = doc.get_bounds()
    Text = doc.get_text( start, end, True )
    
    Text = ReplaceSymbols( Text )
    if JoinLines:
        Text = re.sub( r'(?<!\n)\n(?!\n)', '', Text )
    
    doc.set_text( Text )
    

def AutoNote( window, noteLines = (), labelPttn = r'\[(\d+)\]' ):
    ""
    if isinstance( noteLines, str ):
        noteLines = list( filter( None, noteLines.split( '\n' )))
        
    doc = window.get_active_document()
    start, end = doc.get_bounds()
    Text = doc.get_text( start, end, True )
    
    Labels = map( int, re.findall( labelPttn, Text ))
    
    for i, lb in enumerate( Labels ):
        if i + 1 != lb:
            raise Exception( 'labels order error: %s' % lb )
        note = u'[toggle=off][title][sup][注%d][/sup][/title]\n[content]%s[/content][/toggle]' % ( lb, noteLines[i] )
        Text = re.sub( labelPttn, note, Text, 1 )
        
    Text = ReplaceSymbols( Text )
    doc.set_text( Text )


def AutoReplace( window, replaceFunc ):
    ""
    doc = window.get_active_document()
    start, end = doc.get_bounds()
    Text = doc.get_text( start, end, True )
    doc.set_text( replaceFunc( Text ))
