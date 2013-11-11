# ./mapentry_service_api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:d045e739ca7a60c09176ff3b4f34c6c5f55ea812
# Generated 2013-11-09 17:39:50.323322 by PyXB version 1.2.3
# Namespace http://www.omg.org/spec/CTS2/1.1/MapEntryServices

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
import core_api as _ImportedBinding_core_api
import pyxb.binding.datatypes
import core_service_api as _ImportedBinding_core_service_api

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.omg.org/spec/CTS2/1.1/MapEntryServices', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_core = _ImportedBinding_core_api.Namespace
_Namespace_core.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_coreservice = _ImportedBinding_core_service_api.Namespace
_Namespace_coreservice.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}MapTargetRequest with content type ELEMENT_ONLY
class MapTargetRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """A set of parameters that are used to create or
				update a map target"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapTargetRequest')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 54, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}updatedCorrelation uses Python identifier updatedCorrelation
    __updatedCorrelation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedCorrelation'), 'updatedCorrelation', '__httpwww_omg_orgspecCTS21_1MapEntryServices_MapTargetRequest__httpwww_omg_orgspecCTS21_1MapEntryServicesupdatedCorrelation', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 60, 3), )

    
    updatedCorrelation = property(__updatedCorrelation.value, __updatedCorrelation.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}updatedExternalEntryId uses Python identifier updatedExternalEntryId
    __updatedExternalEntryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedExternalEntryId'), 'updatedExternalEntryId', '__httpwww_omg_orgspecCTS21_1MapEntryServices_MapTargetRequest__httpwww_omg_orgspecCTS21_1MapEntryServicesupdatedExternalEntryId', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 73, 3), )

    
    updatedExternalEntryId = property(__updatedExternalEntryId.value, __updatedExternalEntryId.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}updatedMapRule uses Python identifier updatedMapRule
    __updatedMapRule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedMapRule'), 'updatedMapRule', '__httpwww_omg_orgspecCTS21_1MapEntryServices_MapTargetRequest__httpwww_omg_orgspecCTS21_1MapEntryServicesupdatedMapRule', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 86, 3), )

    
    updatedMapRule = property(__updatedMapRule.value, __updatedMapRule.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}updatedMapTo uses Python identifier updatedMapTo
    __updatedMapTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedMapTo'), 'updatedMapTo', '__httpwww_omg_orgspecCTS21_1MapEntryServices_MapTargetRequest__httpwww_omg_orgspecCTS21_1MapEntryServicesupdatedMapTo', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 99, 3), )

    
    updatedMapTo = property(__updatedMapTo.value, __updatedMapTo.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}updatedTargetDescription uses Python identifier updatedTargetDescription
    __updatedTargetDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedTargetDescription'), 'updatedTargetDescription', '__httpwww_omg_orgspecCTS21_1MapEntryServices_MapTargetRequest__httpwww_omg_orgspecCTS21_1MapEntryServicesupdatedTargetDescription', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 112, 3), )

    
    updatedTargetDescription = property(__updatedTargetDescription.value, __updatedTargetDescription.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}updatedTargetExpression uses Python identifier updatedTargetExpression
    __updatedTargetExpression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedTargetExpression'), 'updatedTargetExpression', '__httpwww_omg_orgspecCTS21_1MapEntryServices_MapTargetRequest__httpwww_omg_orgspecCTS21_1MapEntryServicesupdatedTargetExpression', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 125, 3), )

    
    updatedTargetExpression = property(__updatedTargetExpression.value, __updatedTargetExpression.set, None, None)

    _ElementMap.update({
        __updatedCorrelation.name() : __updatedCorrelation,
        __updatedExternalEntryId.name() : __updatedExternalEntryId,
        __updatedMapRule.name() : __updatedMapRule,
        __updatedMapTo.name() : __updatedMapTo,
        __updatedTargetDescription.name() : __updatedTargetDescription,
        __updatedTargetExpression.name() : __updatedTargetExpression
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MapTargetRequest', MapTargetRequest_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 61, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}correlation uses Python identifier correlation
    __correlation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'correlation'), 'correlation', '__httpwww_omg_orgspecCTS21_1MapEntryServices_CTD_ANON_httpwww_omg_orgspecCTS21_1MapEntryServicescorrelation', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 63, 6), )

    
    correlation = property(__correlation.value, __correlation.set, None, u'the name or URI of a correlation factor\n\t\t\t\t\t\t\t\t')

    _ElementMap.update({
        __correlation.name() : __correlation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 74, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}externalEntryId uses Python identifier externalEntryId
    __externalEntryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'externalEntryId'), 'externalEntryId', '__httpwww_omg_orgspecCTS21_1MapEntryServices_CTD_ANON__httpwww_omg_orgspecCTS21_1MapEntryServicesexternalEntryId', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 76, 6), )

    
    externalEntryId = property(__externalEntryId.value, __externalEntryId.set, None, u'an external identifier assigned to this target\n\t\t\t\t\t\t\t\t\tentry by an outside body')

    _ElementMap.update({
        __externalEntryId.name() : __externalEntryId
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 87, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}mapRule uses Python identifier mapRule
    __mapRule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapRule'), 'mapRule', '__httpwww_omg_orgspecCTS21_1MapEntryServices_CTD_ANON_2_httpwww_omg_orgspecCTS21_1MapEntryServicesmapRule', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 89, 6), )

    
    mapRule = property(__mapRule.value, __mapRule.set, None, u'the map rule for the target. If omitted, the rule\n\t\t\t\t\t\t\t\t\talways evaluates to TRUE')

    _ElementMap.update({
        __mapRule.name() : __mapRule
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 100, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}mapTo uses Python identifier mapTo
    __mapTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapTo'), 'mapTo', '__httpwww_omg_orgspecCTS21_1MapEntryServices_CTD_ANON_3_httpwww_omg_orgspecCTS21_1MapEntryServicesmapTo', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 102, 6), )

    
    mapTo = property(__mapTo.value, __mapTo.set, None, u'the entity name or URI to map to\n\t\t\t\t\t\t\t\t')

    _ElementMap.update({
        __mapTo.name() : __mapTo
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 113, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}targetDescription uses Python identifier targetDescription
    __targetDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'targetDescription'), 'targetDescription', '__httpwww_omg_orgspecCTS21_1MapEntryServices_CTD_ANON_4_httpwww_omg_orgspecCTS21_1MapEntryServicestargetDescription', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 115, 6), )

    
    targetDescription = property(__targetDescription.value, __targetDescription.set, None, u'the description of the rule and/or target\n\t\t\t\t\t\t\t\t')

    _ElementMap.update({
        __targetDescription.name() : __targetDescription
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 126, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}targetExpression uses Python identifier targetExpression
    __targetExpression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'targetExpression'), 'targetExpression', '__httpwww_omg_orgspecCTS21_1MapEntryServices_CTD_ANON_5_httpwww_omg_orgspecCTS21_1MapEntryServicestargetExpression', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 128, 6), )

    
    targetExpression = property(__targetExpression.value, __targetExpression.set, None, u'an expression that, when evaluated, produces a\n\t\t\t\t\t\t\t\t\tcomplex target')

    _ElementMap.update({
        __targetExpression.name() : __targetExpression
    })
    _AttributeMap.update({
        
    })



# Complex type {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}UpdateMapEntryRequest with content type ELEMENT_ONLY
class UpdateMapEntryRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """The set of parameters that can be updated in a map
				entry."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UpdateMapEntryRequest')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 142, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}updatedProcessingRule uses Python identifier updatedProcessingRule
    __updatedProcessingRule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedProcessingRule'), 'updatedProcessingRule', '__httpwww_omg_orgspecCTS21_1MapEntryServices_UpdateMapEntryRequest__httpwww_omg_orgspecCTS21_1MapEntryServicesupdatedProcessingRule', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 148, 3), )

    
    updatedProcessingRule = property(__updatedProcessingRule.value, __updatedProcessingRule.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}updatedSource uses Python identifier updatedSource
    __updatedSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedSource'), 'updatedSource', '__httpwww_omg_orgspecCTS21_1MapEntryServices_UpdateMapEntryRequest__httpwww_omg_orgspecCTS21_1MapEntryServicesupdatedSource', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 161, 3), )

    
    updatedSource = property(__updatedSource.value, __updatedSource.set, None, None)

    _ElementMap.update({
        __updatedProcessingRule.name() : __updatedProcessingRule,
        __updatedSource.name() : __updatedSource
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'UpdateMapEntryRequest', UpdateMapEntryRequest_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 149, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}processingRule uses Python identifier processingRule
    __processingRule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'processingRule'), 'processingRule', '__httpwww_omg_orgspecCTS21_1MapEntryServices_CTD_ANON_6_httpwww_omg_orgspecCTS21_1MapEntryServicesprocessingRule', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 151, 6), )

    
    processingRule = property(__processingRule.value, __processingRule.set, None, u'the rule for processing the member sets\n\t\t\t\t\t\t\t\t')

    _ElementMap.update({
        __processingRule.name() : __processingRule
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 162, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'source'), 'source', '__httpwww_omg_orgspecCTS21_1MapEntryServices_CTD_ANON_7_httpwww_omg_orgspecCTS21_1MapEntryServicessource', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 164, 6), )

    
    source = property(__source.value, __source.set, None, u'a source and the role they played in creating the\n\t\t\t\t\t\t\t\t\tentry')

    _ElementMap.update({
        __source.name() : __source
    })
    _AttributeMap.update({
        
    })



# Complex type {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}MapTargetListList with content type ELEMENT_ONLY
class MapTargetListList (pyxb.binding.basis.complexTypeDefinition):
    """A list of map target lists, one per input entity
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapTargetListList')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 206, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpwww_omg_orgspecCTS21_1MapEntryServices_MapTargetListList_httpwww_omg_orgspecCTS21_1MapEntryServicesentry', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 212, 3), )

    
    entry = property(__entry.value, __entry.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MapTargetListList', MapTargetListList)


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}MapTargetList with content type ELEMENT_ONLY
class MapTargetList (pyxb.binding.basis.complexTypeDefinition):
    """An ordered list of map targets """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapTargetList')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 239, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpwww_omg_orgspecCTS21_1MapEntryServices_MapTargetList_httpwww_omg_orgspecCTS21_1MapEntryServicesentry', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 244, 3), )

    
    entry = property(__entry.value, __entry.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MapTargetList', MapTargetList)


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}MapTargetListListMsg with content type ELEMENT_ONLY
class MapTargetListListMsg_ (_ImportedBinding__nsgroup.Message):
    """A list of map target lists, one per input entity
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapTargetListListMsg')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 191, 1)
    _ElementMap = _ImportedBinding__nsgroup.Message._ElementMap.copy()
    _AttributeMap = _ImportedBinding__nsgroup.Message._AttributeMap.copy()
    # Base type is _ImportedBinding__nsgroup.Message
    
    # Element heading ({http://www.omg.org/spec/CTS2/1.1/Core}heading) inherited from {http://www.omg.org/spec/CTS2/1.1/Core}Message
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}mapTargetListList uses Python identifier mapTargetListList
    __mapTargetListList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapTargetListList'), 'mapTargetListList', '__httpwww_omg_orgspecCTS21_1MapEntryServices_MapTargetListListMsg__httpwww_omg_orgspecCTS21_1MapEntryServicesmapTargetListList', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 200, 5), )

    
    mapTargetListList = property(__mapTargetListList.value, __mapTargetListList.set, None, None)

    _ElementMap.update({
        __mapTargetListList.name() : __mapTargetListList
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MapTargetListListMsg', MapTargetListListMsg_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (MapTargetList):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 213, 4)
    _ElementMap = MapTargetList._ElementMap.copy()
    _AttributeMap = MapTargetList._AttributeMap.copy()
    # Base type is MapTargetList
    
    # Element entry ({http://www.omg.org/spec/CTS2/1.1/MapEntryServices}entry) inherited from {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}MapTargetList
    
    # Attribute entryOrder uses Python identifier entryOrder
    __entryOrder = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'entryOrder'), 'entryOrder', '__httpwww_omg_orgspecCTS21_1MapEntryServices_CTD_ANON_8_entryOrder', pyxb.binding.datatypes.positiveInteger, required=True)
    __entryOrder._DeclarationLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/Core.xsd', 2106, 2)
    __entryOrder._UseLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/Core.xsd', 2106, 2)
    
    entryOrder = property(__entryOrder.value, __entryOrder.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __entryOrder.name() : __entryOrder
    })



# Complex type {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}MapTargetListMsg with content type ELEMENT_ONLY
class MapTargetListMsg_ (_ImportedBinding__nsgroup.Message):
    """An ordered list of map targets """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapTargetListMsg')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 225, 1)
    _ElementMap = _ImportedBinding__nsgroup.Message._ElementMap.copy()
    _AttributeMap = _ImportedBinding__nsgroup.Message._AttributeMap.copy()
    # Base type is _ImportedBinding__nsgroup.Message
    
    # Element heading ({http://www.omg.org/spec/CTS2/1.1/Core}heading) inherited from {http://www.omg.org/spec/CTS2/1.1/Core}Message
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}mapTargetList uses Python identifier mapTargetList
    __mapTargetList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapTargetList'), 'mapTargetList', '__httpwww_omg_orgspecCTS21_1MapEntryServices_MapTargetListMsg__httpwww_omg_orgspecCTS21_1MapEntryServicesmapTargetList', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 233, 5), )

    
    mapTargetList = property(__mapTargetList.value, __mapTargetList.set, None, None)

    _ElementMap.update({
        __mapTargetList.name() : __mapTargetList
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MapTargetListMsg', MapTargetListMsg_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}MapResolutionService with content type ELEMENT_ONLY
class MapResolutionService_ (_ImportedBinding_core_service_api.BaseService_):
    """A service that interprets and resolves maps
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapResolutionService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 250, 1)
    _ElementMap = _ImportedBinding_core_service_api.BaseService_._ElementMap.copy()
    _AttributeMap = _ImportedBinding_core_service_api.BaseService_._AttributeMap.copy()
    # Base type is _ImportedBinding_core_service_api.BaseService_
    
    # Element serviceName ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceName) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceDescription ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceDescription) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceVersion ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceVersion) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceProvider ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceProvider) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element defaultFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}defaultFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedProfile ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedProfile) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element implementationType ({http://www.omg.org/spec/CTS2/1.1/CoreService}implementationType) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element knownNamespace ({http://www.omg.org/spec/CTS2/1.1/CoreService}knownNamespace) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MapResolutionService', MapResolutionService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}MapEntryReadService with content type ELEMENT_ONLY
class MapEntryReadService_ (_ImportedBinding_core_service_api.BaseReadService_):
    """A service providing direct access to entries in map
				versions."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapEntryReadService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 14, 1)
    _ElementMap = _ImportedBinding_core_service_api.BaseReadService_._ElementMap.copy()
    _AttributeMap = _ImportedBinding_core_service_api.BaseReadService_._AttributeMap.copy()
    # Base type is _ImportedBinding_core_service_api.BaseReadService_
    
    # Element serviceName ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceName) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceDescription ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceDescription) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceVersion ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceVersion) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceProvider ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceProvider) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element defaultFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}defaultFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedProfile ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedProfile) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element implementationType ({http://www.omg.org/spec/CTS2/1.1/CoreService}implementationType) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element knownNamespace ({http://www.omg.org/spec/CTS2/1.1/CoreService}knownNamespace) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MapEntryReadService', MapEntryReadService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}MapEntryQueryService with content type ELEMENT_ONLY
class MapEntryQueryService_ (_ImportedBinding_core_service_api.BaseQueryService_):
    """Services that allow the filtering and query of
				entries in a MapVersion. These services allow the filtering of
				entries by rule and target content."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapEntryQueryService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 27, 1)
    _ElementMap = _ImportedBinding_core_service_api.BaseQueryService_._ElementMap.copy()
    _AttributeMap = _ImportedBinding_core_service_api.BaseQueryService_._AttributeMap.copy()
    # Base type is _ImportedBinding_core_service_api.BaseQueryService_
    
    # Element serviceName ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceName) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceDescription ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceDescription) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceVersion ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceVersion) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceProvider ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceProvider) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element defaultFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}defaultFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedProfile ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedProfile) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element implementationType ({http://www.omg.org/spec/CTS2/1.1/CoreService}implementationType) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element knownNamespace ({http://www.omg.org/spec/CTS2/1.1/CoreService}knownNamespace) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element knownProperty ({http://www.omg.org/spec/CTS2/1.1/CoreService}knownProperty) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseQueryService
    
    # Element supportedMatchAlgorithm ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedMatchAlgorithm) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseQueryService
    
    # Element supportedModelAttribute ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedModelAttribute) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseQueryService
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MapEntryQueryService', MapEntryQueryService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}MapEntryHistoryService with content type ELEMENT_ONLY
class MapEntryHistoryService_ (_ImportedBinding_core_service_api.HistoryService_):
    """A service that allows the evolution of a map entry
				to be retrieved and viewed."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapEntryHistoryService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 41, 1)
    _ElementMap = _ImportedBinding_core_service_api.HistoryService_._ElementMap.copy()
    _AttributeMap = _ImportedBinding_core_service_api.HistoryService_._AttributeMap.copy()
    # Base type is _ImportedBinding_core_service_api.HistoryService_
    
    # Element serviceName ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceName) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceDescription ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceDescription) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceVersion ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceVersion) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceProvider ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceProvider) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element defaultFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}defaultFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedProfile ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedProfile) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element implementationType ({http://www.omg.org/spec/CTS2/1.1/CoreService}implementationType) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element knownNamespace ({http://www.omg.org/spec/CTS2/1.1/CoreService}knownNamespace) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element changeHistory ({http://www.omg.org/spec/CTS2/1.1/CoreService}changeHistory) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}HistoryService
    
    # Attribute earliestChange inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}HistoryService
    
    # Attribute latestChange inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}HistoryService
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MapEntryHistoryService', MapEntryHistoryService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapEntryServices}MapEntryMaintenanceService with content type ELEMENT_ONLY
class MapEntryMaintenanceService_ (_ImportedBinding_core_service_api.BaseMaintenanceService_):
    """A service that allows the creation, update and
				deletion of MapEntries within a MapVersion"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapEntryMaintenanceService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 178, 1)
    _ElementMap = _ImportedBinding_core_service_api.BaseMaintenanceService_._ElementMap.copy()
    _AttributeMap = _ImportedBinding_core_service_api.BaseMaintenanceService_._AttributeMap.copy()
    # Base type is _ImportedBinding_core_service_api.BaseMaintenanceService_
    
    # Element serviceName ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceName) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceDescription ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceDescription) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceVersion ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceVersion) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceProvider ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceProvider) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element defaultFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}defaultFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedProfile ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedProfile) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element implementationType ({http://www.omg.org/spec/CTS2/1.1/CoreService}implementationType) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element knownNamespace ({http://www.omg.org/spec/CTS2/1.1/CoreService}knownNamespace) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MapEntryMaintenanceService', MapEntryMaintenanceService_)


MapTargetRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapTargetRequest'), MapTargetRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 53, 1))
Namespace.addCategoryObject('elementBinding', MapTargetRequest.name().localName(), MapTargetRequest)

UpdateMapEntryRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UpdateMapEntryRequest'), UpdateMapEntryRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 141, 1))
Namespace.addCategoryObject('elementBinding', UpdateMapEntryRequest.name().localName(), UpdateMapEntryRequest)

MapTargetListListMsg = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapTargetListListMsg'), MapTargetListListMsg_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 190, 1))
Namespace.addCategoryObject('elementBinding', MapTargetListListMsg.name().localName(), MapTargetListListMsg)

MapTargetListMsg = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapTargetListMsg'), MapTargetListMsg_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 224, 1))
Namespace.addCategoryObject('elementBinding', MapTargetListMsg.name().localName(), MapTargetListMsg)

MapResolutionService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapResolutionService'), MapResolutionService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 249, 1))
Namespace.addCategoryObject('elementBinding', MapResolutionService.name().localName(), MapResolutionService)

MapEntryReadService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapEntryReadService'), MapEntryReadService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 13, 1))
Namespace.addCategoryObject('elementBinding', MapEntryReadService.name().localName(), MapEntryReadService)

MapEntryQueryService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapEntryQueryService'), MapEntryQueryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 26, 1))
Namespace.addCategoryObject('elementBinding', MapEntryQueryService.name().localName(), MapEntryQueryService)

MapEntryHistoryService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapEntryHistoryService'), MapEntryHistoryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 40, 1))
Namespace.addCategoryObject('elementBinding', MapEntryHistoryService.name().localName(), MapEntryHistoryService)

MapEntryMaintenanceService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapEntryMaintenanceService'), MapEntryMaintenanceService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 177, 1))
Namespace.addCategoryObject('elementBinding', MapEntryMaintenanceService.name().localName(), MapEntryMaintenanceService)



MapTargetRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedCorrelation'), CTD_ANON, scope=MapTargetRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 60, 3)))

MapTargetRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedExternalEntryId'), CTD_ANON_, scope=MapTargetRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 73, 3)))

MapTargetRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedMapRule'), CTD_ANON_2, scope=MapTargetRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 86, 3)))

MapTargetRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedMapTo'), CTD_ANON_3, scope=MapTargetRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 99, 3)))

MapTargetRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedTargetDescription'), CTD_ANON_4, scope=MapTargetRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 112, 3)))

MapTargetRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedTargetExpression'), CTD_ANON_5, scope=MapTargetRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 125, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 60, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 73, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 86, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 99, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 112, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 125, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MapTargetRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedCorrelation')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 60, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MapTargetRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedExternalEntryId')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 73, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MapTargetRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedMapRule')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 86, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MapTargetRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedMapTo')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 99, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MapTargetRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedTargetDescription')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 112, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MapTargetRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedTargetExpression')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 125, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MapTargetRequest_._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'correlation'), _ImportedBinding__nsgroup.MapCorrelationReference, scope=CTD_ANON, documentation=u'the name or URI of a correlation factor\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 63, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 63, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'correlation')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 63, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'externalEntryId'), _ImportedBinding__nsgroup.String, scope=CTD_ANON_, documentation=u'an external identifier assigned to this target\n\t\t\t\t\t\t\t\t\tentry by an outside body', location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 76, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 76, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'externalEntryId')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 76, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapRule'), _ImportedBinding__nsgroup.MapRule, scope=CTD_ANON_2, documentation=u'the map rule for the target. If omitted, the rule\n\t\t\t\t\t\t\t\t\talways evaluates to TRUE', location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 89, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 89, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapRule')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 89, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapTo'), _ImportedBinding_core_service_api.EntityNameOrURI_, scope=CTD_ANON_3, documentation=u'the entity name or URI to map to\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 102, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 102, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapTo')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 102, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_4()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'targetDescription'), _ImportedBinding__nsgroup.OpaqueData, scope=CTD_ANON_4, documentation=u'the description of the rule and/or target\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 115, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 115, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'targetDescription')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 115, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'targetExpression'), _ImportedBinding__nsgroup.EntityExpression_, scope=CTD_ANON_5, documentation=u'an expression that, when evaluated, produces a\n\t\t\t\t\t\t\t\t\tcomplex target', location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 128, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 128, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'targetExpression')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 128, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_6()




UpdateMapEntryRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedProcessingRule'), CTD_ANON_6, scope=UpdateMapEntryRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 148, 3)))

UpdateMapEntryRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedSource'), CTD_ANON_7, scope=UpdateMapEntryRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 161, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 148, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 161, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapEntryRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedProcessingRule')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 148, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapEntryRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedSource')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 161, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UpdateMapEntryRequest_._Automaton = _BuildAutomaton_7()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'processingRule'), _ImportedBinding__nsgroup.MapProcessingRule, scope=CTD_ANON_6, documentation=u'the rule for processing the member sets\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 151, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'processingRule')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 151, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_8()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'source'), _ImportedBinding__nsgroup.SourceAndRoleReference, scope=CTD_ANON_7, documentation=u'a source and the role they played in creating the\n\t\t\t\t\t\t\t\t\tentry', location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 164, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 164, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'source')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 164, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_9()




MapTargetListList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), CTD_ANON_8, scope=MapTargetListList, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 212, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapTargetListList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 212, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MapTargetListList._Automaton = _BuildAutomaton_10()




MapTargetList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), _ImportedBinding__nsgroup.MapTarget, scope=MapTargetList, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 244, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 244, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MapTargetList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 244, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MapTargetList._Automaton = _BuildAutomaton_11()




MapTargetListListMsg_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapTargetListList'), MapTargetListList, scope=MapTargetListListMsg_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 200, 5)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapTargetListListMsg_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, u'heading')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/Core.xsd', 2101, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapTargetListListMsg_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapTargetListList')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 200, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MapTargetListListMsg_._Automaton = _BuildAutomaton_12()




def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 244, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 244, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_13()




MapTargetListMsg_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapTargetList'), MapTargetList, scope=MapTargetListMsg_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 233, 5)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapTargetListMsg_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, u'heading')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/Core.xsd', 2101, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapTargetListMsg_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapTargetList')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapEntryServices.xsd', 233, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MapTargetListMsg_._Automaton = _BuildAutomaton_14()




def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapResolutionService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapResolutionService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapResolutionService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapResolutionService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapResolutionService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapResolutionService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapResolutionService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapResolutionService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapResolutionService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MapResolutionService_._Automaton = _BuildAutomaton_15()




def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapEntryReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MapEntryReadService_._Automaton = _BuildAutomaton_16()




def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownProperty')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedMatchAlgorithm')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 754, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapEntryQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedModelAttribute')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 759, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MapEntryQueryService_._Automaton = _BuildAutomaton_17()




def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapEntryHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'changeHistory')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 453, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MapEntryHistoryService_._Automaton = _BuildAutomaton_18()




def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapEntryMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapEntryMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MapEntryMaintenanceService_._Automaton = _BuildAutomaton_19()

