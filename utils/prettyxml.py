# -*- coding: utf-8 -*-
# Copyright (c) 2013, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the <ORGANIZATION> nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
import pyxb
import xml.parsers.expat
from xml.sax.saxutils import escape,unescape
from schema import  core_api, association_api, codesystem_api, codesystemversion_api, \
                    conceptdomain_api, conceptdomainbinding_api, entity_api, \
                    map_api, mapversion_api, statement_api, valueset_api,  \
                    valuesetdefinition_api, updates_api, core_service_api, entity_service_api


core_api.Namespace.setPrefix('core')
association_api.Namespace.setPrefix('assoc')
codesystem_api.Namespace.setPrefix('cs')
codesystemversion_api.Namespace.setPrefix('csv')
conceptdomain_api.Namespace.setPrefix('cd')
conceptdomainbinding_api.Namespace.setPrefix('cdb')
entity_api.Namespace.setPrefix('entity')
map_api.Namespace.setPrefix('map')
mapversion_api.Namespace.setPrefix('mapversion')
statement_api.Namespace.setPrefix('stmt')
valueset_api.Namespace.setPrefix('vs')
valuesetdefinition_api.Namespace.setPrefix('vsd')
updates_api.Namespace.setPrefix('upd')


core_service_api.Namespace.setPrefix('svc')
entity_service_api.Namespace.setPrefix('entitysvc')

defaultNS = core_api.Namespace

def prettyxml(pyxb_xml, validate=True, ns=None, xslt=None):
    """ XML pretty printer.  Surprising as it may seem, there doesn't seem to be a really decent
        Python based pretty printer for XML, so we rolled this one ourselves.
        Note: Sometimes setting RequireValidWhenGenerating to false results in errors.

        @param pyxb_xml: XML to be prettified
        @type pyxb_xml: either a string containing xml or a pyxb node
        @param validate: Indicator on whether the XML should be validated.  Only applies if the input is of type pyxb node
        @type validate: C{bool}
        @param ns: default namespace
        @type ns: C{pyxb.Namespace}
        @param xslt: URI of an XSLT transform if needed
        @type xslt: String
        @return: Pretty xml
    """

    def indent(depth, prev):
        return ('\n' + (' ' * 4 * depth)) if prev != 'd' else ""
        
    def args(alist):
        if len(alist):
            return ' ' + ' '.join([k+'="'+v+'"' for (k,v) in alist.items()])
        return ''

    pyxb.defaultNamespace = ns
    pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(ns if ns else defaultNS)
    pyxb.RequireValidWhenGenerating(validate)
    rawxml = pyxb_xml if isinstance(pyxb_xml, basestring) else pyxb_xml.toxml()

    seq = []
    p = xml.parsers.expat.ParserCreate('UTF-8')
    p.StartElementHandler  = lambda name, attrs: seq.append( ('s', name, attrs))
    p.EndElementHandler    = lambda name:        seq.append( ('e', name ))
    p.CharacterDataHandler = lambda data:        seq.append( ('d', data ))
    p.Parse(rawxml.encode('UTF-8'),1)

    depth, prev, rval = (0, 'e', '<?xml version="1.0" encoding="UTF-8"?>' + (xslt if xslt else ""))
    dataText = ''
    while len(seq):
        e = seq.pop(0)
        if e[0] == 's':
            # shortcut the simple start end tag
            if seq[0][0] == 'e':
                assert e[1] == seq[0][1]
                seq.pop(0)
                rval += indent(depth, prev)
                rval += '<' + e[1] + args(e[2]) + '/>'
                depth -= 1
            else:
                if prev != 'e':
                    depth += 1
                if dataText:
                    rval += dataText
                    dataText = ''
                rval += indent(depth, prev)
                rval += '<' + e[1] + args(e[2]) + '>'
        elif e[0] == 'e':
            if prev != 'd':
                depth -= 1
            else:
                rval += escape(unescape(dataText))
                dataText = ''
            rval += indent(depth, prev)
            rval += '</' + e[1] + '>'
        else:
            if prev != 'e' or e[0] <> 'd' or e[1].strip():
                dataText += e[1]
        if prev != 'e' or e[0] <> 'd' or e[1].strip():
            prev = e[0]
    return rval 


def cleanxml(txt):
    if txt:
        return uncleanxml(txt).replace('&','&amp;').replace('<', '&lt;')
    return None

def uncleanxml(txt):
    if txt:
        return txt.replace('&amp;','&').replace('&lt;', '<')
