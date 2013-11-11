# ./entity_service_api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:62803c15fc82f00c6ff1a1fa27f74b4104ea03fb
# Generated 2013-11-09 17:39:50.322065 by PyXB version 1.2.3
# Namespace http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices

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
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices', create_if_missing=True)
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


# Complex type {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}UpdateEntityDescriptionRequest with content type ELEMENT_ONLY
class UpdateEntityDescriptionRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}UpdateEntityDescriptionRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UpdateEntityDescriptionRequest')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 29, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}updatedAlternateEntityIds uses Python identifier updatedAlternateEntityIds
    __updatedAlternateEntityIds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedAlternateEntityIds'), 'updatedAlternateEntityIds', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_UpdateEntityDescriptionRequest__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesupdatedAlternateEntityIds', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 31, 3), )

    
    updatedAlternateEntityIds = property(__updatedAlternateEntityIds.value, __updatedAlternateEntityIds.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}updatedDefinitions uses Python identifier updatedDefinitions
    __updatedDefinitions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedDefinitions'), 'updatedDefinitions', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_UpdateEntityDescriptionRequest__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesupdatedDefinitions', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 38, 3), )

    
    updatedDefinitions = property(__updatedDefinitions.value, __updatedDefinitions.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}updatedDesignations uses Python identifier updatedDesignations
    __updatedDesignations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedDesignations'), 'updatedDesignations', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_UpdateEntityDescriptionRequest__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesupdatedDesignations', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 45, 3), )

    
    updatedDesignations = property(__updatedDesignations.value, __updatedDesignations.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}updatedComments uses Python identifier updatedComments
    __updatedComments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedComments'), 'updatedComments', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_UpdateEntityDescriptionRequest__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesupdatedComments', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 52, 3), )

    
    updatedComments = property(__updatedComments.value, __updatedComments.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}updatedParents uses Python identifier updatedParents
    __updatedParents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedParents'), 'updatedParents', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_UpdateEntityDescriptionRequest__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesupdatedParents', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 59, 3), )

    
    updatedParents = property(__updatedParents.value, __updatedParents.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}updatedProperties uses Python identifier updatedProperties
    __updatedProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedProperties'), 'updatedProperties', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_UpdateEntityDescriptionRequest__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesupdatedProperties', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 66, 3), )

    
    updatedProperties = property(__updatedProperties.value, __updatedProperties.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}updatedResourceTypes uses Python identifier updatedResourceTypes
    __updatedResourceTypes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceTypes'), 'updatedResourceTypes', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_UpdateEntityDescriptionRequest__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesupdatedResourceTypes', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 73, 3), )

    
    updatedResourceTypes = property(__updatedResourceTypes.value, __updatedResourceTypes.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}updatedCodeSystemRole uses Python identifier updatedCodeSystemRole
    __updatedCodeSystemRole = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedCodeSystemRole'), 'updatedCodeSystemRole', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_UpdateEntityDescriptionRequest__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesupdatedCodeSystemRole', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 80, 3), )

    
    updatedCodeSystemRole = property(__updatedCodeSystemRole.value, __updatedCodeSystemRole.set, None, None)

    _ElementMap.update({
        __updatedAlternateEntityIds.name() : __updatedAlternateEntityIds,
        __updatedDefinitions.name() : __updatedDefinitions,
        __updatedDesignations.name() : __updatedDesignations,
        __updatedComments.name() : __updatedComments,
        __updatedParents.name() : __updatedParents,
        __updatedProperties.name() : __updatedProperties,
        __updatedResourceTypes.name() : __updatedResourceTypes,
        __updatedCodeSystemRole.name() : __updatedCodeSystemRole
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'UpdateEntityDescriptionRequest', UpdateEntityDescriptionRequest_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 32, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}alternateEntityId uses Python identifier alternateEntityId
    __alternateEntityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'alternateEntityId'), 'alternateEntityId', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_CTD_ANON_httpwww_omg_orgspecCTS21_1EntityDescriptionServicesalternateEntityId', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 34, 6), )

    
    alternateEntityId = property(__alternateEntityId.value, __alternateEntityId.set, None, None)

    _ElementMap.update({
        __alternateEntityId.name() : __alternateEntityId
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
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 39, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}definition uses Python identifier definition
    __definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'definition'), 'definition', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_CTD_ANON__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesdefinition', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 41, 6), )

    
    definition = property(__definition.value, __definition.set, None, None)

    _ElementMap.update({
        __definition.name() : __definition
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
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 46, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}designation uses Python identifier designation
    __designation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'designation'), 'designation', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_CTD_ANON_2_httpwww_omg_orgspecCTS21_1EntityDescriptionServicesdesignation', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 48, 6), )

    
    designation = property(__designation.value, __designation.set, None, None)

    _ElementMap.update({
        __designation.name() : __designation
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
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 53, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}note uses Python identifier note
    __note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'note'), 'note', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_CTD_ANON_3_httpwww_omg_orgspecCTS21_1EntityDescriptionServicesnote', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 55, 6), )

    
    note = property(__note.value, __note.set, None, None)

    _ElementMap.update({
        __note.name() : __note
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
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 60, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}parent uses Python identifier parent
    __parent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'parent'), 'parent', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_CTD_ANON_4_httpwww_omg_orgspecCTS21_1EntityDescriptionServicesparent', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 62, 6), )

    
    parent = property(__parent.value, __parent.set, None, None)

    _ElementMap.update({
        __parent.name() : __parent
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
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 67, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'property'), 'property_', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_CTD_ANON_5_httpwww_omg_orgspecCTS21_1EntityDescriptionServicesproperty', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 69, 6), )

    
    property_ = property(__property.value, __property.set, None, None)

    _ElementMap.update({
        __property.name() : __property
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 74, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}resourceType uses Python identifier resourceType
    __resourceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'resourceType'), 'resourceType', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_CTD_ANON_6_httpwww_omg_orgspecCTS21_1EntityDescriptionServicesresourceType', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 76, 6), )

    
    resourceType = property(__resourceType.value, __resourceType.set, None, None)

    _ElementMap.update({
        __resourceType.name() : __resourceType
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
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 81, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}codeSystemRole uses Python identifier codeSystemRole
    __codeSystemRole = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'codeSystemRole'), 'codeSystemRole', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_CTD_ANON_7_httpwww_omg_orgspecCTS21_1EntityDescriptionServicescodeSystemRole', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 83, 6), )

    
    codeSystemRole = property(__codeSystemRole.value, __codeSystemRole.set, None, None)

    _ElementMap.update({
        __codeSystemRole.name() : __codeSystemRole
    })
    _AttributeMap.update({
        
    })



# Complex type {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}EntityDescriptionHistoryService with content type ELEMENT_ONLY
class EntityDescriptionHistoryService_ (_ImportedBinding_core_service_api.HistoryService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}EntityDescriptionHistoryService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EntityDescriptionHistoryService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 11, 1)
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
Namespace.addCategoryObject('typeBinding', u'EntityDescriptionHistoryService', EntityDescriptionHistoryService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}EntityDescriptionMaintenanceService with content type ELEMENT_ONLY
class EntityDescriptionMaintenanceService_ (_ImportedBinding_core_service_api.BaseMaintenanceService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}EntityDescriptionMaintenanceService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EntityDescriptionMaintenanceService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 20, 1)
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
Namespace.addCategoryObject('typeBinding', u'EntityDescriptionMaintenanceService', EntityDescriptionMaintenanceService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}EntityDescriptionReadService with content type ELEMENT_ONLY
class EntityDescriptionReadService_ (_ImportedBinding_core_service_api.BaseReadService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}EntityDescriptionReadService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EntityDescriptionReadService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 91, 1)
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
    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}knownCodeSystem uses Python identifier knownCodeSystem
    __knownCodeSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystem'), 'knownCodeSystem', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_EntityDescriptionReadService__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesknownCodeSystem', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 95, 5), )

    
    knownCodeSystem = property(__knownCodeSystem.value, __knownCodeSystem.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}knownCodeSystemVersion uses Python identifier knownCodeSystemVersion
    __knownCodeSystemVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystemVersion'), 'knownCodeSystemVersion', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_EntityDescriptionReadService__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesknownCodeSystemVersion', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 96, 5), )

    
    knownCodeSystemVersion = property(__knownCodeSystemVersion.value, __knownCodeSystemVersion.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}supportedVersionTag uses Python identifier supportedVersionTag
    __supportedVersionTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'supportedVersionTag'), 'supportedVersionTag', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_EntityDescriptionReadService__httpwww_omg_orgspecCTS21_1EntityDescriptionServicessupportedVersionTag', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 97, 5), )

    
    supportedVersionTag = property(__supportedVersionTag.value, __supportedVersionTag.set, None, None)

    _ElementMap.update({
        __knownCodeSystem.name() : __knownCodeSystem,
        __knownCodeSystemVersion.name() : __knownCodeSystemVersion,
        __supportedVersionTag.name() : __supportedVersionTag
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'EntityDescriptionReadService', EntityDescriptionReadService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}EntityDescriptionQueryService with content type ELEMENT_ONLY
class EntityDescriptionQueryService_ (_ImportedBinding_core_service_api.BaseQueryService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}EntityDescriptionQueryService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EntityDescriptionQueryService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 104, 1)
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
    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}knownCodeSystem uses Python identifier knownCodeSystem
    __knownCodeSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystem'), 'knownCodeSystem', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_EntityDescriptionQueryService__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesknownCodeSystem', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 108, 5), )

    
    knownCodeSystem = property(__knownCodeSystem.value, __knownCodeSystem.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}knownCodeSystemVersion uses Python identifier knownCodeSystemVersion
    __knownCodeSystemVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystemVersion'), 'knownCodeSystemVersion', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_EntityDescriptionQueryService__httpwww_omg_orgspecCTS21_1EntityDescriptionServicesknownCodeSystemVersion', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 109, 5), )

    
    knownCodeSystemVersion = property(__knownCodeSystemVersion.value, __knownCodeSystemVersion.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/EntityDescriptionServices}supportedVersionTag uses Python identifier supportedVersionTag
    __supportedVersionTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'supportedVersionTag'), 'supportedVersionTag', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_EntityDescriptionQueryService__httpwww_omg_orgspecCTS21_1EntityDescriptionServicessupportedVersionTag', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 110, 5), )

    
    supportedVersionTag = property(__supportedVersionTag.value, __supportedVersionTag.set, None, None)

    
    # Attribute entities uses Python identifier entities
    __entities = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'entities'), 'entities', '__httpwww_omg_orgspecCTS21_1EntityDescriptionServices_EntityDescriptionQueryService__entities', _ImportedBinding__nsgroup.EntityDirectoryURI, required=True)
    __entities._DeclarationLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 112, 4)
    __entities._UseLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 112, 4)
    
    entities = property(__entities.value, __entities.set, None, None)

    _ElementMap.update({
        __knownCodeSystem.name() : __knownCodeSystem,
        __knownCodeSystemVersion.name() : __knownCodeSystemVersion,
        __supportedVersionTag.name() : __supportedVersionTag
    })
    _AttributeMap.update({
        __entities.name() : __entities
    })
Namespace.addCategoryObject('typeBinding', u'EntityDescriptionQueryService', EntityDescriptionQueryService_)


UpdateEntityDescriptionRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UpdateEntityDescriptionRequest'), UpdateEntityDescriptionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 28, 1))
Namespace.addCategoryObject('elementBinding', UpdateEntityDescriptionRequest.name().localName(), UpdateEntityDescriptionRequest)

EntityDescriptionHistoryService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EntityDescriptionHistoryService'), EntityDescriptionHistoryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 10, 1))
Namespace.addCategoryObject('elementBinding', EntityDescriptionHistoryService.name().localName(), EntityDescriptionHistoryService)

EntityDescriptionMaintenanceService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EntityDescriptionMaintenanceService'), EntityDescriptionMaintenanceService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 19, 1))
Namespace.addCategoryObject('elementBinding', EntityDescriptionMaintenanceService.name().localName(), EntityDescriptionMaintenanceService)

EntityDescriptionReadService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EntityDescriptionReadService'), EntityDescriptionReadService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 90, 1))
Namespace.addCategoryObject('elementBinding', EntityDescriptionReadService.name().localName(), EntityDescriptionReadService)

EntityDescriptionQueryService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EntityDescriptionQueryService'), EntityDescriptionQueryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 103, 1))
Namespace.addCategoryObject('elementBinding', EntityDescriptionQueryService.name().localName(), EntityDescriptionQueryService)



UpdateEntityDescriptionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedAlternateEntityIds'), CTD_ANON, scope=UpdateEntityDescriptionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 31, 3)))

UpdateEntityDescriptionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedDefinitions'), CTD_ANON_, scope=UpdateEntityDescriptionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 38, 3)))

UpdateEntityDescriptionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedDesignations'), CTD_ANON_2, scope=UpdateEntityDescriptionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 45, 3)))

UpdateEntityDescriptionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedComments'), CTD_ANON_3, scope=UpdateEntityDescriptionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 52, 3)))

UpdateEntityDescriptionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedParents'), CTD_ANON_4, scope=UpdateEntityDescriptionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 59, 3)))

UpdateEntityDescriptionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedProperties'), CTD_ANON_5, scope=UpdateEntityDescriptionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 66, 3)))

UpdateEntityDescriptionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceTypes'), CTD_ANON_6, scope=UpdateEntityDescriptionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 73, 3)))

UpdateEntityDescriptionRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedCodeSystemRole'), CTD_ANON_7, scope=UpdateEntityDescriptionRequest_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 80, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 31, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 38, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 45, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 52, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 59, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 66, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 73, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 80, 3))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UpdateEntityDescriptionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedAlternateEntityIds')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 31, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UpdateEntityDescriptionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedDefinitions')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 38, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UpdateEntityDescriptionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedDesignations')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 45, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UpdateEntityDescriptionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedComments')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 52, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UpdateEntityDescriptionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedParents')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 59, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(UpdateEntityDescriptionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedProperties')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 66, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(UpdateEntityDescriptionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceTypes')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 73, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(UpdateEntityDescriptionRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedCodeSystemRole')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 80, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UpdateEntityDescriptionRequest_._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alternateEntityId'), _ImportedBinding__nsgroup.ScopedEntityName, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 34, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 34, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'alternateEntityId')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 34, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'definition'), _ImportedBinding__nsgroup.Definition, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 41, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 41, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'definition')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 41, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'designation'), _ImportedBinding__nsgroup.Designation, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 48, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'designation')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 48, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'note'), _ImportedBinding__nsgroup.Comment, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 55, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 55, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'note')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 55, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_4()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'parent'), _ImportedBinding_core_service_api.EntityNameOrURI_, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 62, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 62, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'parent')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 62, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'property'), _ImportedBinding__nsgroup.Property, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 69, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 69, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'property')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 69, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_6()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resourceType'), _ImportedBinding_core_service_api.EntityNameOrURI_, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 76, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resourceType')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 76, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_7()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'codeSystemRole'), _ImportedBinding__nsgroup.CodeSystemRole, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 83, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 83, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'codeSystemRole')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 83, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_8()




def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'changeHistory')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 453, 5))
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
EntityDescriptionHistoryService_._Automaton = _BuildAutomaton_9()




def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
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
EntityDescriptionMaintenanceService_._Automaton = _BuildAutomaton_10()




EntityDescriptionReadService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystem'), _ImportedBinding__nsgroup.CodeSystemReference, scope=EntityDescriptionReadService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 95, 5)))

EntityDescriptionReadService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystemVersion'), _ImportedBinding__nsgroup.CodeSystemVersionReference, scope=EntityDescriptionReadService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 96, 5)))

EntityDescriptionReadService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'supportedVersionTag'), _ImportedBinding__nsgroup.VersionTagReference, scope=EntityDescriptionReadService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 97, 5)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 95, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 96, 5))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystem')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 95, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystemVersion')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 96, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedVersionTag')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 97, 5))
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
    transitions.append(fac.Transition(st_11, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EntityDescriptionReadService_._Automaton = _BuildAutomaton_11()




EntityDescriptionQueryService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystem'), _ImportedBinding__nsgroup.CodeSystemReference, scope=EntityDescriptionQueryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 108, 5)))

EntityDescriptionQueryService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystemVersion'), _ImportedBinding__nsgroup.CodeSystemVersionReference, scope=EntityDescriptionQueryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 109, 5)))

EntityDescriptionQueryService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'supportedVersionTag'), _ImportedBinding__nsgroup.VersionTagReference, scope=EntityDescriptionQueryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 110, 5)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 108, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 109, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownProperty')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedMatchAlgorithm')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 754, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedModelAttribute')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 759, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystem')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 108, 5))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownCodeSystemVersion')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 109, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EntityDescriptionQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedVersionTag')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/entity/EntityDescriptionServices.xsd', 110, 5))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
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
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EntityDescriptionQueryService_._Automaton = _BuildAutomaton_12()

