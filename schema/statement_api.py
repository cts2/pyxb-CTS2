# ./statement_api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:df6f8caeb426fd99db1bac108f156434e14c5647
# Generated 2013-11-05 15:25:28.321268 by PyXB version 1.2.3
# Namespace http://www.omg.org/spec/CTS2/1.1/Statement [xmlns:stmt]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:c74202c2-4660-11e3-9c81-c82a1438c957')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.omg.org/spec/CTS2/1.1/Statement', create_if_missing=True)
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

from _nsgroup import StatementMsg # {http://www.omg.org/spec/CTS2/1.1/Statement}StatementMsg
from _nsgroup import Statement # {http://www.omg.org/spec/CTS2/1.1/Statement}Statement
from _nsgroup import StatementDirectory # {http://www.omg.org/spec/CTS2/1.1/Statement}StatementDirectory
from _nsgroup import StatementList # {http://www.omg.org/spec/CTS2/1.1/Statement}StatementList
from _nsgroup import StatementSubject # {http://www.omg.org/spec/CTS2/1.1/Statement}StatementSubject
from _nsgroup import StatementQualifier # {http://www.omg.org/spec/CTS2/1.1/Statement}StatementQualifier
from _nsgroup import StatementMsg_ # {http://www.omg.org/spec/CTS2/1.1/Statement}StatementMsg
from _nsgroup import Statement_ # {http://www.omg.org/spec/CTS2/1.1/Statement}Statement
from _nsgroup import StatementDirectory_ # {http://www.omg.org/spec/CTS2/1.1/Statement}StatementDirectory
from _nsgroup import StatementDirectoryEntry # {http://www.omg.org/spec/CTS2/1.1/Statement}StatementDirectoryEntry
from _nsgroup import StatementList_ # {http://www.omg.org/spec/CTS2/1.1/Statement}StatementList
from _nsgroup import StatementListEntry # {http://www.omg.org/spec/CTS2/1.1/Statement}StatementListEntry
