# ./entity_api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:903d49345115f87025c95594612025a02821ffad
# Generated 2013-04-18 16:41:20.525808 by PyXB version 1.2.2
# Namespace http://www.omg.org/spec/CTS2/1.1/Entity [xmlns:entity]

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
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.omg.org/spec/CTS2/1.1/Entity', create_if_missing=True)
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

from _nsgroup import EntityDescription # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityDescription
from _nsgroup import EntityDescriptionMsg # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityDescriptionMsg
from _nsgroup import EntityReferenceMsg # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityReferenceMsg
from _nsgroup import EntityDirectory # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityDirectory
from _nsgroup import EntityList # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityList
from _nsgroup import EntityDescription_ # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityDescription
from _nsgroup import DesignationRole # {http://www.omg.org/spec/CTS2/1.1/Entity}DesignationRole
from _nsgroup import ClassDescriptionType # {http://www.omg.org/spec/CTS2/1.1/Entity}ClassDescriptionType
from _nsgroup import ClassDescriptionState # {http://www.omg.org/spec/CTS2/1.1/Entity}ClassDescriptionState
from _nsgroup import Transitivity # {http://www.omg.org/spec/CTS2/1.1/Entity}Transitivity
from _nsgroup import ObjectPropertyDirectionality # {http://www.omg.org/spec/CTS2/1.1/Entity}ObjectPropertyDirectionality
from _nsgroup import EntityDescriptionBase # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityDescriptionBase
from _nsgroup import EntityDescriptionMsg_ # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityDescriptionMsg
from _nsgroup import EntityReferenceMsg_ # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityReferenceMsg
from _nsgroup import NamedEntityDescription # {http://www.omg.org/spec/CTS2/1.1/Entity}NamedEntityDescription
from _nsgroup import AnonymousEntityDescription # {http://www.omg.org/spec/CTS2/1.1/Entity}AnonymousEntityDescription
from _nsgroup import Designation # {http://www.omg.org/spec/CTS2/1.1/Entity}Designation
from _nsgroup import ClassDescription # {http://www.omg.org/spec/CTS2/1.1/Entity}ClassDescription
from _nsgroup import NamedIndividualDescription # {http://www.omg.org/spec/CTS2/1.1/Entity}NamedIndividualDescription
from _nsgroup import AnonymousIndividualDescription # {http://www.omg.org/spec/CTS2/1.1/Entity}AnonymousIndividualDescription
from _nsgroup import DataTypeDescription # {http://www.omg.org/spec/CTS2/1.1/Entity}DataTypeDescription
from _nsgroup import PredicateDescription # {http://www.omg.org/spec/CTS2/1.1/Entity}PredicateDescription
from _nsgroup import EntityDirectoryEntry # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityDirectoryEntry
from _nsgroup import AnnotationPropertyDescription # {http://www.omg.org/spec/CTS2/1.1/Entity}AnnotationPropertyDescription
from _nsgroup import DataPropertyDescription # {http://www.omg.org/spec/CTS2/1.1/Entity}DataPropertyDescription
from _nsgroup import ObjectPropertyDescription # {http://www.omg.org/spec/CTS2/1.1/Entity}ObjectPropertyDescription
from _nsgroup import EntityDirectory_ # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityDirectory
from _nsgroup import EntityList_ # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityList
from _nsgroup import EntityListEntry # {http://www.omg.org/spec/CTS2/1.1/Entity}EntityListEntry
