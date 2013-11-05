# ./valuesetdefinition_api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:da3b0fe11673b724d4306d23e6651d8beaf84d3a
# Generated 2013-04-18 16:41:20.522612 by PyXB version 1.2.2
# Namespace http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition [xmlns:valuesetdefinition]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:b2e57fe8-a870-11e2-a91a-c82a1438c957')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)

from _nsgroup import ResolvedValueSet # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ResolvedValueSet
from _nsgroup import ValueSetDefinitionMsg # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ValueSetDefinitionMsg
from _nsgroup import ResolvedValueSetMsg # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ResolvedValueSetMsg
from _nsgroup import ValueSetDefinitionEntry # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ValueSetDefinitionEntry
from _nsgroup import ResolvedValueSetSummary # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ResolvedValueSetSummary
from _nsgroup import ValueSetDefinitionDirectory # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ValueSetDefinitionDirectory
from _nsgroup import ValueSetDefinitionList # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ValueSetDefinitionList
from _nsgroup import IteratableResolvedValueSet # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}IteratableResolvedValueSet
from _nsgroup import ResolvedValueSetDirectory # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ResolvedValueSetDirectory
from _nsgroup import ValueSetDefinition # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ValueSetDefinition
from _nsgroup import CompleteCodeSystemReference # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}CompleteCodeSystemReference
from _nsgroup import CompleteValueSetReference # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}CompleteValueSetReference
from _nsgroup import PropertyQueryReference # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}PropertyQueryReference
from _nsgroup import SpecificEntityList # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}SpecificEntityList
from _nsgroup import ResolvedValueSetHeader # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ResolvedValueSetHeader
from _nsgroup import ResolvedValueSet_ # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ResolvedValueSet
from _nsgroup import SetOperator_ as SetOperator # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}SetOperator
from _nsgroup import LeafOrAll # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}LeafOrAll
from _nsgroup import TransitiveClosure # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}TransitiveClosure
from _nsgroup import ExternalValueSetDefinition # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ExternalValueSetDefinition
from _nsgroup import ValueSetDefinitionMsg_ # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ValueSetDefinitionMsg
from _nsgroup import ResolvedValueSetMsg_ # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ResolvedValueSetMsg
from _nsgroup import ValueSetDefinitionEntry_ # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ValueSetDefinitionEntry
from _nsgroup import AssociatedEntitiesReference # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}AssociatedEntitiesReference
from _nsgroup import ResolvedValueSetSummary_ # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ResolvedValueSetSummary
from _nsgroup import ResolvedValueSetDirectoryEntry # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ResolvedValueSetDirectoryEntry
from _nsgroup import ValueSetDefinitionDirectory_ # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ValueSetDefinitionDirectory
from _nsgroup import ValueSetDefinitionList_ # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ValueSetDefinitionList
from _nsgroup import ValueSetDefinitionListEntry # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ValueSetDefinitionListEntry
from _nsgroup import IteratableResolvedValueSet_ # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}IteratableResolvedValueSet
from _nsgroup import ResolvedValueSetDirectory_ # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ResolvedValueSetDirectory
from _nsgroup import ValueSetDefinition_ # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ValueSetDefinition
from _nsgroup import ValueSetDefinitionDirectoryEntry # {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinition}ValueSetDefinitionDirectoryEntry
