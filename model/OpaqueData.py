# -*- coding: latin-1 -*-
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

from schema import core_api
from schema.core_api import tsAnyType

import pyxb
from xml.sax import SAXParseException
from utils.prettyxml import cleanxml


class OpaqueData(core_api.OpaqueData, object):
    """ C{core_api.OpaqueData} wrapper.  OpaqueData may include:
            1. value (tsAnyType) (req)
            2. format (FormatReference) (opt)
            3. language (LanguageReference) (opt)
            4. schema (DocumentURI) (opt)

    """

    def __init__(self, value=None, valueNamespace=None):
        """ Constructor

        @param value: Value of the opaque data element. Can be any ascii text.
        @type value: C{String}

        @param valueNamespace: namespace URI for the value. If omitted, the value is
            assumed to have no embedded XML
        @type valueNamespace: C{uri}
        """
        core_api.OpaqueData.__init__(self)
        self.value_ = tsAnyType(value)
        if valueNamespace:
            assert False, "value namespace not implemented"


    @property
    def text(self):
        return reduce(lambda a,b: a + b if isinstance(b, basestring) else b.toxml(), self.value_.orderedContent(), '')


class tsAnyType(core_api.tsAnyType, object):
    """ C{core_api.tsAnyType} wrapper.  The schema is::

            <xs:complexType mixed="true" name="tsAnyType">
                <xs:sequence>
                    <xs:any maxOccurs="unbounded" minOccurs="0" namespace="##any" processContents="lax"/>
                </xs:sequence>
            </xs:complexType>

        The value(s) can either be plain text, xml or a mixture thereof.

    """
    def __init__(self, value=None):
        """ Construct a new instance.
        @param value: text or xml value
        """
        core_api.tsAnyType.__init__(self)
        if value:
            self.append(value)

    def append(self, value):
        if '<' in value:
            try:
                for e in pyxb.utils.domutils.StringToDOM('<v>%s</v>' % value).firstChild.childNodes:
                    core_api.tsAnyType.append(self, e)
            except SAXParseException, e:
                core_api.tsAnyType.append(self, cleanxml(value), _maybe_element=False)
        else:
            core_api.tsAnyType.append(self, unicode(value,errors='ignore'), _maybe_element=False)





