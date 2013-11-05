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
import re
from schema import core_api


# Understanding how to get information into a mixed namespace item is a bit of a challenge.
# We've circumvented this by letting the CreateFromDocument build it for us

xmlTemplate = """<?xml version="1.0"  encoding="UTF-8"?>
<EntityExpression xmlns="http://www.omg.org/spec/CTS2/1.1/Core"
    xmlns:core="http://www.omg.org/spec/CTS2/1.1/Core"
    xmlns:xhtml="http://www.w3.org/1999/xhtml">
    <ontologyLanguageAndSyntax>
        <ontologyLanguage>lang</ontologyLanguage>
        <ontologySyntax>syntax</ontologySyntax>
    </ontologyLanguageAndSyntax>
    <expression>
        <core:value>%s</core:value>
    </expression>
</EntityExpression>
"""

xhtmlURI    = "http://www.w3.org/1999/xhtml"

class OpaqueData(core_api.OpaqueData, object):

    def __init__(self, value):
        """ Constructor

        @param value: Value of the opaque data element. Can be any ascii text.
        @type value: String

        """
        core_api.OpaqueData.__init__(self)
        xml = xmlTemplate % value
        xml = xml.encode('utf-8')
        self.value_ = core_api.CreateFromDocument(xml).expression.value_


    def setValue(self, val):
        self.content().append(val)

    @property
    def text(self):
        return reduce(lambda a,b: a + b if isinstance(b, basestring) else b.toxml(), self.value_.content(), '')





