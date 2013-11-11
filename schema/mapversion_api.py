# ./mapversion_api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8502f1b7ba155b4f4b9e4e00bc85e9347e39e88e
# Generated 2013-11-09 17:39:50.318558 by PyXB version 1.2.3
# Namespace http://www.omg.org/spec/CTS2/1.1/MapVersion [xmlns:mapversion]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:364c7059-4998-11e3-bd00-c82a1438c957')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.omg.org/spec/CTS2/1.1/MapVersion', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
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
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)

from _nsgroup import MapVersionMsg # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapVersionMsg
from _nsgroup import MapEntryMsg # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapEntryMsg
from _nsgroup import MapEntry # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapEntry
from _nsgroup import MapVersionDirectory # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapVersionDirectory
from _nsgroup import MapVersionList # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapVersionList
from _nsgroup import MapEntryDirectory # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapEntryDirectory
from _nsgroup import MapEntryList # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapEntryList
from _nsgroup import MapVersion # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapVersion
from _nsgroup import MapVersionMsg_ # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapVersionMsg
from _nsgroup import MapProcessingRule # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapProcessingRule
from _nsgroup import MapTarget # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapTarget
from _nsgroup import MapRule # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapRule
from _nsgroup import MapEntryMsg_ # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapEntryMsg
from _nsgroup import MapSet # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapSet
from _nsgroup import MapEntry_ # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapEntry
from _nsgroup import MapVersionDirectory_ # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapVersionDirectory
from _nsgroup import MapVersionList_ # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapVersionList
from _nsgroup import MapVersionListEntry # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapVersionListEntry
from _nsgroup import MapEntryDirectory_ # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapEntryDirectory
from _nsgroup import MapEntryDirectoryEntry # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapEntryDirectoryEntry
from _nsgroup import MapEntryList_ # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapEntryList
from _nsgroup import MapEntryListEntry # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapEntryListEntry
from _nsgroup import MapVersion_ # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapVersion
from _nsgroup import MapVersionDirectoryEntry # {http://www.omg.org/spec/CTS2/1.1/MapVersion}MapVersionDirectoryEntry
