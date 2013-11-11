# ./mapversion_service_api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a43fc8f48071b530d2c3840083cbdd30e59c3bd0
# Generated 2013-11-09 17:39:50.325034 by PyXB version 1.2.3
# Namespace http://www.omg.org/spec/CTS2/1.1/MapVersionServices

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
import pyxb.binding.datatypes
import core_service_api as _ImportedBinding_core_service_api

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.omg.org/spec/CTS2/1.1/MapVersionServices', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
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


# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}MapRole
class MapRole_ (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """An indicator that determines whether the "from", the "to" or both components of a Map or MapVersion are being queried."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapRole')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 13, 1)
    _Documentation = u'An indicator that determines whether the "from", the "to" or both components of a Map or MapVersion are being queried.'
MapRole_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MapRole_, enum_prefix=None)
MapRole_.MAP_FROM_ROLE = MapRole_._CF_enumeration.addEnumeration(unicode_value=u'MAP_FROM_ROLE', tag=u'MAP_FROM_ROLE')
MapRole_.MAP_TO_ROLE = MapRole_._CF_enumeration.addEnumeration(unicode_value=u'MAP_TO_ROLE', tag=u'MAP_TO_ROLE')
MapRole_.BOTH_MAP_ROLES = MapRole_._CF_enumeration.addEnumeration(unicode_value=u'BOTH_MAP_ROLES', tag=u'BOTH_MAP_ROLES')
MapRole_._InitializeFacetMap(MapRole_._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MapRole', MapRole_)

# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}MapStatus
class MapStatus_ (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """An indicator that determines whether all referencs..."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 37, 1)
    _Documentation = u'An indicator that determines whether all referencs...'
MapStatus_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MapStatus_, enum_prefix=None)
MapStatus_.UNMAPPED = MapStatus_._CF_enumeration.addEnumeration(unicode_value=u'UNMAPPED', tag=u'UNMAPPED')
MapStatus_.NOMAP = MapStatus_._CF_enumeration.addEnumeration(unicode_value=u'NOMAP', tag=u'NOMAP')
MapStatus_.MAPPED = MapStatus_._CF_enumeration.addEnumeration(unicode_value=u'MAPPED', tag=u'MAPPED')
MapStatus_.ALLMAPENTRIES = MapStatus_._CF_enumeration.addEnumeration(unicode_value=u'ALLMAPENTRIES', tag=u'ALLMAPENTRIES')
MapStatus_._InitializeFacetMap(MapStatus_._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MapStatus', MapStatus_)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 84, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}useCodeSystemVersions uses Python identifier useCodeSystemVersions
    __useCodeSystemVersions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'useCodeSystemVersions'), 'useCodeSystemVersions', '__httpwww_omg_orgspecCTS21_1MapVersionServices_CTD_ANON_httpwww_omg_orgspecCTS21_1MapVersionServicesuseCodeSystemVersions', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 86, 8), )

    
    useCodeSystemVersions = property(__useCodeSystemVersions.value, __useCodeSystemVersions.set, None, None)

    _ElementMap.update({
        __useCodeSystemVersions.name() : __useCodeSystemVersions
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
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 91, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}applicableContexts uses Python identifier applicableContexts
    __applicableContexts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'applicableContexts'), 'applicableContexts', '__httpwww_omg_orgspecCTS21_1MapVersionServices_CTD_ANON__httpwww_omg_orgspecCTS21_1MapVersionServicesapplicableContexts', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 93, 8), )

    
    applicableContexts = property(__applicableContexts.value, __applicableContexts.set, None, None)

    _ElementMap.update({
        __applicableContexts.name() : __applicableContexts
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (_ImportedBinding_core_service_api.BaseService_):
    """A service that interprets and resolves maps
				"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 146, 2)
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



# Complex type {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}MapVersionHistoryService with content type ELEMENT_ONLY
class MapVersionHistoryService_ (_ImportedBinding_core_service_api.HistoryService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}MapVersionHistoryService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapVersionHistoryService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 103, 1)
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
Namespace.addCategoryObject('typeBinding', u'MapVersionHistoryService', MapVersionHistoryService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}MapVersionMaintenanceService with content type ELEMENT_ONLY
class MapVersionMaintenanceService_ (_ImportedBinding_core_service_api.BaseMaintenanceService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}MapVersionMaintenanceService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapVersionMaintenanceService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 112, 1)
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
Namespace.addCategoryObject('typeBinding', u'MapVersionMaintenanceService', MapVersionMaintenanceService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}MapVersionReadService with content type ELEMENT_ONLY
class MapVersionReadService_ (_ImportedBinding_core_service_api.BaseReadService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}MapVersionReadService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapVersionReadService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 137, 1)
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
Namespace.addCategoryObject('typeBinding', u'MapVersionReadService', MapVersionReadService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}CreateMapVersionRequest with content type ELEMENT_ONLY
class CreateMapVersionRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}CreateMapVersionRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CreateMapVersionRequest')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 66, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}fromCodeSystemVersion uses Python identifier fromCodeSystemVersion
    __fromCodeSystemVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fromCodeSystemVersion'), 'fromCodeSystemVersion', '__httpwww_omg_orgspecCTS21_1MapVersionServices_CreateMapVersionRequest__httpwww_omg_orgspecCTS21_1MapVersionServicesfromCodeSystemVersion', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 68, 3), )

    
    fromCodeSystemVersion = property(__fromCodeSystemVersion.value, __fromCodeSystemVersion.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}fromValueSetDefinition uses Python identifier fromValueSetDefinition
    __fromValueSetDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fromValueSetDefinition'), 'fromValueSetDefinition', '__httpwww_omg_orgspecCTS21_1MapVersionServices_CreateMapVersionRequest__httpwww_omg_orgspecCTS21_1MapVersionServicesfromValueSetDefinition', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 69, 3), )

    
    fromValueSetDefinition = property(__fromValueSetDefinition.value, __fromValueSetDefinition.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}toCodeSystemVersion uses Python identifier toCodeSystemVersion
    __toCodeSystemVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'toCodeSystemVersion'), 'toCodeSystemVersion', '__httpwww_omg_orgspecCTS21_1MapVersionServices_CreateMapVersionRequest__httpwww_omg_orgspecCTS21_1MapVersionServicestoCodeSystemVersion', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 70, 3), )

    
    toCodeSystemVersion = property(__toCodeSystemVersion.value, __toCodeSystemVersion.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}toValueSetDefinition uses Python identifier toValueSetDefinition
    __toValueSetDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'toValueSetDefinition'), 'toValueSetDefinition', '__httpwww_omg_orgspecCTS21_1MapVersionServices_CreateMapVersionRequest__httpwww_omg_orgspecCTS21_1MapVersionServicestoValueSetDefinition', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 71, 3), )

    
    toValueSetDefinition = property(__toValueSetDefinition.value, __toValueSetDefinition.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}useCodeSystemVersions uses Python identifier useCodeSystemVersions
    __useCodeSystemVersions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'useCodeSystemVersions'), 'useCodeSystemVersions', '__httpwww_omg_orgspecCTS21_1MapVersionServices_CreateMapVersionRequest__httpwww_omg_orgspecCTS21_1MapVersionServicesuseCodeSystemVersions', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 72, 3), )

    
    useCodeSystemVersions = property(__useCodeSystemVersions.value, __useCodeSystemVersions.set, None, None)

    
    # Attribute documentURI uses Python identifier documentURI
    __documentURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'documentURI'), 'documentURI', '__httpwww_omg_orgspecCTS21_1MapVersionServices_CreateMapVersionRequest__documentURI', _ImportedBinding__nsgroup.DocumentURI, required=True)
    __documentURI._DeclarationLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 74, 2)
    __documentURI._UseLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 74, 2)
    
    documentURI = property(__documentURI.value, __documentURI.set, None, None)

    
    # Attribute mapVersionName uses Python identifier mapVersionName
    __mapVersionName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mapVersionName'), 'mapVersionName', '__httpwww_omg_orgspecCTS21_1MapVersionServices_CreateMapVersionRequest__mapVersionName', _ImportedBinding__nsgroup.MapVersionName, required=True)
    __mapVersionName._DeclarationLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 75, 2)
    __mapVersionName._UseLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 75, 2)
    
    mapVersionName = property(__mapVersionName.value, __mapVersionName.set, None, None)

    _ElementMap.update({
        __fromCodeSystemVersion.name() : __fromCodeSystemVersion,
        __fromValueSetDefinition.name() : __fromValueSetDefinition,
        __toCodeSystemVersion.name() : __toCodeSystemVersion,
        __toValueSetDefinition.name() : __toValueSetDefinition,
        __useCodeSystemVersions.name() : __useCodeSystemVersions
    })
    _AttributeMap.update({
        __documentURI.name() : __documentURI,
        __mapVersionName.name() : __mapVersionName
    })
Namespace.addCategoryObject('typeBinding', u'CreateMapVersionRequest', CreateMapVersionRequest_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}UpdateMapVersionRequest with content type ELEMENT_ONLY
class UpdateMapVersionRequest_ (_ImportedBinding_core_service_api.UpdateResourceVersionDescription_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}UpdateMapVersionRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UpdateMapVersionRequest')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 79, 1)
    _ElementMap = _ImportedBinding_core_service_api.UpdateResourceVersionDescription_._ElementMap.copy()
    _AttributeMap = _ImportedBinding_core_service_api.UpdateResourceVersionDescription_._AttributeMap.copy()
    # Base type is _ImportedBinding_core_service_api.UpdateResourceVersionDescription_
    
    # Element updatedAdditionalDocumentation ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedAdditionalDocumentation) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedKeywords ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedKeywords) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedSources ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedSources) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedNotes ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedNotes) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedProperties ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedProperties) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedResourceSynopsis ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedResourceSynopsis) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedResourceTypes ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedResourceTypes) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedRights ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedRights) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedPredecessor ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedPredecessor) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceVersionDescription
    
    # Element updatedSourceAndNotation ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedSourceAndNotation) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceVersionDescription
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}updatedUseCodeSystemVersions uses Python identifier updatedUseCodeSystemVersions
    __updatedUseCodeSystemVersions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedUseCodeSystemVersions'), 'updatedUseCodeSystemVersions', '__httpwww_omg_orgspecCTS21_1MapVersionServices_UpdateMapVersionRequest__httpwww_omg_orgspecCTS21_1MapVersionServicesupdatedUseCodeSystemVersions', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 83, 5), )

    
    updatedUseCodeSystemVersions = property(__updatedUseCodeSystemVersions.value, __updatedUseCodeSystemVersions.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}updatedApplicableContexts uses Python identifier updatedApplicableContexts
    __updatedApplicableContexts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedApplicableContexts'), 'updatedApplicableContexts', '__httpwww_omg_orgspecCTS21_1MapVersionServices_UpdateMapVersionRequest__httpwww_omg_orgspecCTS21_1MapVersionServicesupdatedApplicableContexts', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 90, 5), )

    
    updatedApplicableContexts = property(__updatedApplicableContexts.value, __updatedApplicableContexts.set, None, None)

    
    # Attribute updatedFormalName inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Attribute updatedState inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceVersionDescription
    
    # Attribute updatedOfficialActivationDate inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceVersionDescription
    
    # Attribute updatedOfficialReleaseDate inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceVersionDescription
    
    # Attribute updatedOfficialResourceVersionId inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceVersionDescription
    _ElementMap.update({
        __updatedUseCodeSystemVersions.name() : __updatedUseCodeSystemVersions,
        __updatedApplicableContexts.name() : __updatedApplicableContexts
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'UpdateMapVersionRequest', UpdateMapVersionRequest_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}MapVersionQueryService with content type ELEMENT_ONLY
class MapVersionQueryService_ (_ImportedBinding_core_service_api.BaseQueryService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}MapVersionQueryService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MapVersionQueryService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 121, 1)
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
    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}knownCodeSystem uses Python identifier knownCodeSystem
    __knownCodeSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystem'), 'knownCodeSystem', '__httpwww_omg_orgspecCTS21_1MapVersionServices_MapVersionQueryService__httpwww_omg_orgspecCTS21_1MapVersionServicesknownCodeSystem', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 125, 5), )

    
    knownCodeSystem = property(__knownCodeSystem.value, __knownCodeSystem.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}knownCodeSystemVersion uses Python identifier knownCodeSystemVersion
    __knownCodeSystemVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystemVersion'), 'knownCodeSystemVersion', '__httpwww_omg_orgspecCTS21_1MapVersionServices_MapVersionQueryService__httpwww_omg_orgspecCTS21_1MapVersionServicesknownCodeSystemVersion', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 126, 5), )

    
    knownCodeSystemVersion = property(__knownCodeSystemVersion.value, __knownCodeSystemVersion.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}knownValueSet uses Python identifier knownValueSet
    __knownValueSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'knownValueSet'), 'knownValueSet', '__httpwww_omg_orgspecCTS21_1MapVersionServices_MapVersionQueryService__httpwww_omg_orgspecCTS21_1MapVersionServicesknownValueSet', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 127, 5), )

    
    knownValueSet = property(__knownValueSet.value, __knownValueSet.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}knownValueSetDefinition uses Python identifier knownValueSetDefinition
    __knownValueSetDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'knownValueSetDefinition'), 'knownValueSetDefinition', '__httpwww_omg_orgspecCTS21_1MapVersionServices_MapVersionQueryService__httpwww_omg_orgspecCTS21_1MapVersionServicesknownValueSetDefinition', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 128, 5), )

    
    knownValueSetDefinition = property(__knownValueSetDefinition.value, __knownValueSetDefinition.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/MapVersionServices}supportedTag uses Python identifier supportedTag
    __supportedTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'supportedTag'), 'supportedTag', '__httpwww_omg_orgspecCTS21_1MapVersionServices_MapVersionQueryService__httpwww_omg_orgspecCTS21_1MapVersionServicessupportedTag', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 129, 5), )

    
    supportedTag = property(__supportedTag.value, __supportedTag.set, None, None)

    
    # Attribute mapVersions uses Python identifier mapVersions
    __mapVersions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mapVersions'), 'mapVersions', '__httpwww_omg_orgspecCTS21_1MapVersionServices_MapVersionQueryService__mapVersions', _ImportedBinding__nsgroup.MapVersionDirectoryURI, required=True)
    __mapVersions._DeclarationLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 131, 4)
    __mapVersions._UseLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 131, 4)
    
    mapVersions = property(__mapVersions.value, __mapVersions.set, None, None)

    _ElementMap.update({
        __knownCodeSystem.name() : __knownCodeSystem,
        __knownCodeSystemVersion.name() : __knownCodeSystemVersion,
        __knownValueSet.name() : __knownValueSet,
        __knownValueSetDefinition.name() : __knownValueSetDefinition,
        __supportedTag.name() : __supportedTag
    })
    _AttributeMap.update({
        __mapVersions.name() : __mapVersions
    })
Namespace.addCategoryObject('typeBinding', u'MapVersionQueryService', MapVersionQueryService_)


MapRole = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapRole'), MapRole_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 12, 1))
Namespace.addCategoryObject('elementBinding', MapRole.name().localName(), MapRole)

MapStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapStatus'), MapStatus_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 36, 1))
Namespace.addCategoryObject('elementBinding', MapStatus.name().localName(), MapStatus)

MapResolutionService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapResolutionService'), CTD_ANON_2, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 145, 1))
Namespace.addCategoryObject('elementBinding', MapResolutionService.name().localName(), MapResolutionService)

MapVersionHistoryService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapVersionHistoryService'), MapVersionHistoryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 102, 1))
Namespace.addCategoryObject('elementBinding', MapVersionHistoryService.name().localName(), MapVersionHistoryService)

MapVersionMaintenanceService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapVersionMaintenanceService'), MapVersionMaintenanceService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 111, 1))
Namespace.addCategoryObject('elementBinding', MapVersionMaintenanceService.name().localName(), MapVersionMaintenanceService)

MapVersionReadService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapVersionReadService'), MapVersionReadService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 136, 1))
Namespace.addCategoryObject('elementBinding', MapVersionReadService.name().localName(), MapVersionReadService)

CreateMapVersionRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CreateMapVersionRequest'), CreateMapVersionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 65, 1))
Namespace.addCategoryObject('elementBinding', CreateMapVersionRequest.name().localName(), CreateMapVersionRequest)

UpdateMapVersionRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UpdateMapVersionRequest'), UpdateMapVersionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 78, 1))
Namespace.addCategoryObject('elementBinding', UpdateMapVersionRequest.name().localName(), UpdateMapVersionRequest)

MapVersionQueryService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MapVersionQueryService'), MapVersionQueryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 120, 1))
Namespace.addCategoryObject('elementBinding', MapVersionQueryService.name().localName(), MapVersionQueryService)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'useCodeSystemVersions'), _ImportedBinding_core_service_api.NameOrURIList_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 86, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 86, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'useCodeSystemVersions')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 86, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'applicableContexts'), _ImportedBinding_core_service_api.NameOrURIList_, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 93, 8)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 93, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'applicableContexts')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 93, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
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
CTD_ANON_2._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapVersionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'changeHistory')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 453, 5))
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
MapVersionHistoryService_._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapVersionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
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
MapVersionMaintenanceService_._Automaton = _BuildAutomaton_4()




def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapVersionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
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
MapVersionReadService_._Automaton = _BuildAutomaton_5()




CreateMapVersionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fromCodeSystemVersion'), _ImportedBinding_core_service_api.NameOrURI_, scope=CreateMapVersionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 68, 3)))

CreateMapVersionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fromValueSetDefinition'), _ImportedBinding_core_service_api.NameOrURI_, scope=CreateMapVersionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 69, 3)))

CreateMapVersionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'toCodeSystemVersion'), _ImportedBinding_core_service_api.NameOrURI_, scope=CreateMapVersionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 70, 3)))

CreateMapVersionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'toValueSetDefinition'), _ImportedBinding_core_service_api.NameOrURI_, scope=CreateMapVersionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 71, 3)))

CreateMapVersionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'useCodeSystemVersions'), _ImportedBinding_core_service_api.NameOrURIList_, scope=CreateMapVersionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 72, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 68, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 69, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 70, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 71, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 72, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CreateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fromCodeSystemVersion')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 68, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CreateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fromValueSetDefinition')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 69, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CreateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'toCodeSystemVersion')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 70, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CreateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'toValueSetDefinition')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 71, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CreateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'useCodeSystemVersions')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 72, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CreateMapVersionRequest_._Automaton = _BuildAutomaton_6()




UpdateMapVersionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedUseCodeSystemVersions'), CTD_ANON, scope=UpdateMapVersionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 83, 5)))

UpdateMapVersionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedApplicableContexts'), CTD_ANON_, scope=UpdateMapVersionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 90, 5)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 351, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 358, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 365, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 372, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 379, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 386, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 393, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 400, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 420, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 427, 5))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 83, 5))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 90, 5))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'updatedAdditionalDocumentation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 351, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'updatedKeywords')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 358, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'updatedSources')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 365, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'updatedNotes')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 372, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'updatedProperties')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 379, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'updatedResourceSynopsis')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 386, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'updatedResourceTypes')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 393, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'updatedRights')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 400, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'updatedPredecessor')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 420, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'updatedSourceAndNotation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 427, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedUseCodeSystemVersions')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 83, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(UpdateMapVersionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedApplicableContexts')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 90, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UpdateMapVersionRequest_._Automaton = _BuildAutomaton_7()




MapVersionQueryService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystem'), _ImportedBinding__nsgroup.CodeSystemReference, scope=MapVersionQueryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 125, 5)))

MapVersionQueryService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystemVersion'), _ImportedBinding__nsgroup.CodeSystemVersionReference, scope=MapVersionQueryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 126, 5)))

MapVersionQueryService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'knownValueSet'), _ImportedBinding__nsgroup.ValueSetReference, scope=MapVersionQueryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 127, 5)))

MapVersionQueryService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'knownValueSetDefinition'), _ImportedBinding__nsgroup.ValueSetDefinitionReference, scope=MapVersionQueryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 128, 5)))

MapVersionQueryService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'supportedTag'), _ImportedBinding__nsgroup.VersionTagReference, scope=MapVersionQueryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 129, 5)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 125, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 126, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 127, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 128, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 129, 5))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownProperty')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedMatchAlgorithm')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 754, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedModelAttribute')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 759, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystem')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 125, 5))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystemVersion')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 126, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownValueSet')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 127, 5))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownValueSetDefinition')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 128, 5))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MapVersionQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedTag')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/mapversion/MapVersionServices.xsd', 129, 5))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
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
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MapVersionQueryService_._Automaton = _BuildAutomaton_8()

