# ./association_api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:969d835031dc569f27b70494e4435b3996dbc7da
# Generated 2013-04-18 16:41:20.524726 by PyXB version 1.2.2
# Namespace http://www.omg.org/spec/CTS2/1.1/Association [xmlns:association]

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
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.omg.org/spec/CTS2/1.1/Association', create_if_missing=True)
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

from _nsgroup import AssociationMsg # {http://www.omg.org/spec/CTS2/1.1/Association}AssociationMsg
from _nsgroup import Association # {http://www.omg.org/spec/CTS2/1.1/Association}Association
from _nsgroup import AssociationDirectory # {http://www.omg.org/spec/CTS2/1.1/Association}AssociationDirectory
from _nsgroup import AssociationList # {http://www.omg.org/spec/CTS2/1.1/Association}AssociationList
from _nsgroup import AssociationGraph # {http://www.omg.org/spec/CTS2/1.1/Association}AssociationGraph
from _nsgroup import AssociationDerivation # {http://www.omg.org/spec/CTS2/1.1/Association}AssociationDerivation
from _nsgroup import AssociationRendering # {http://www.omg.org/spec/CTS2/1.1/Association}AssociationRendering
from _nsgroup import GraphDirection # {http://www.omg.org/spec/CTS2/1.1/Association}GraphDirection
from _nsgroup import GraphFocus # {http://www.omg.org/spec/CTS2/1.1/Association}GraphFocus
from _nsgroup import AssociationMsg_ # {http://www.omg.org/spec/CTS2/1.1/Association}AssociationMsg
from _nsgroup import Association_ # {http://www.omg.org/spec/CTS2/1.1/Association}Association
from _nsgroup import AssociationDirectory_ # {http://www.omg.org/spec/CTS2/1.1/Association}AssociationDirectory
from _nsgroup import AssociationDirectoryEntry # {http://www.omg.org/spec/CTS2/1.1/Association}AssociationDirectoryEntry
from _nsgroup import AssociationList_ # {http://www.omg.org/spec/CTS2/1.1/Association}AssociationList
from _nsgroup import AssociationListEntry # {http://www.omg.org/spec/CTS2/1.1/Association}AssociationListEntry
from _nsgroup import AssociationGraph_ # {http://www.omg.org/spec/CTS2/1.1/Association}AssociationGraph
from _nsgroup import GraphNode # {http://www.omg.org/spec/CTS2/1.1/Association}GraphNode
