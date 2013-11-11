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

import unittest
from utils.prettyxml import prettyxml

from utils.xmldiff import diff
from schema.entity_api import ClassDescription, EntityDescription
from schema.core_api import ScopedEntityName, CodeSystemVersionReference, URIAndEntityName, NameAndMeaningReference, \
                            CodeSystemReference
from model.Designation import Designation

class testEntity(unittest.TestCase):
    def test1(self):
        e = ClassDescription()
        e.about = "http://snomed.info/id/74400008"
        e.entityID = ScopedEntityName()
        e.entityID.namespace='sctid'
        e.entityID.name='74400008'
        e.describingCodeSystemVersion = CodeSystemVersionReference()
        e.describingCodeSystemVersion.version = NameAndMeaningReference('SNOMED_CT_20130731')
        e.describingCodeSystemVersion.version.uri="http://snomed.info/sct/900000000000207008/version/20130731"
        e.describingCodeSystemVersion.codeSystem = CodeSystemReference('SNOMED_CT')
        e.describingCodeSystemVersion.codeSystem.uri="http://snomed.info/sct/900000000000207008"
        e.designation.append(Designation('Appendicitis &< (Finding)'))
        e.designation.append(Designation('This is <b>bold</b> statement', isPreferred=False, xmlns="http://www.w3.org/1999/xhtml"))
        #e.designation.append(Designation('This is <b>bold</b> statement', isPreferred=False))


        et = URIAndEntityName()
        et.uri = 'http://www.w3.org/2002/07/owl#Class'
        et.nameSpace = 'owl'
        et.name = 'Class'
        e.entityType.append(et)
        c = EntityDescription()
        c.classDescription = e

        #print prettyxml(c.toxml())
        self.assertTrue(diff(c.toxml(),"""<?xml version="1.0" encoding="UTF-8"?>
<entity:EntityDescription xmlns:entity="http://www.omg.org/spec/CTS2/1.1/Entity" xmlns:core="http://www.omg.org/spec/CTS2/1.1/Core">
    <entity:classDescription about="http://snomed.info/id/74400008">
        <entity:entityID>
            <core:namespace>sctid</core:namespace>
            <core:name>74400008</core:name>
        </entity:entityID>
        <entity:describingCodeSystemVersion>
            <core:version uri="http://snomed.info/sct/900000000000207008/version/20130731">SNOMED_CT_20130731</core:version>
            <core:codeSystem uri="http://snomed.info/sct/900000000000207008">SNOMED_CT</core:codeSystem>
        </entity:describingCodeSystemVersion>
        <entity:designation designationRole="PREFERRED">
            <value>Appendicitis &amp;amp;&amp;lt; (Finding)</value>
        </entity:designation>
        <entity:designation designationRole="ALTERNATIVE">
            <core:value>This is <core:b>bold</core:b> statement</core:value>
        </entity:designation>
        <entity:entityType uri="http://www.w3.org/2002/07/owl#Class">
            <core:name>Class</core:name>
        </entity:entityType>
    </entity:classDescription>
</entity:EntityDescription>"""))



if __name__ == '__main__':
    unittest.main()