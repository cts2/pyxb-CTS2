# ./valuesetdefinition_service_api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b93baa80244cec75f3f6da5e7414c44c62f97bed
# Generated 2013-11-09 17:39:50.325698 by PyXB version 1.2.3
# Namespace http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices

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
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices', create_if_missing=True)
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


# Complex type {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}ResolvedValueSetLoader with content type ELEMENT_ONLY
class ResolvedValueSetLoader_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}ResolvedValueSetLoader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ResolvedValueSetLoader')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 51, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}knownValueSet uses Python identifier knownValueSet
    __knownValueSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'knownValueSet'), 'knownValueSet', '__httpwww_omg_orgspecCTS21_1ValueSetDefinitionServices_ResolvedValueSetLoader__httpwww_omg_orgspecCTS21_1ValueSetDefinitionServicesknownValueSet', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 53, 3), )

    
    knownValueSet = property(__knownValueSet.value, __knownValueSet.set, None, None)

    _ElementMap.update({
        __knownValueSet.name() : __knownValueSet
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ResolvedValueSetLoader', ResolvedValueSetLoader_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}ValueSetDefinitionResolution with content type ELEMENT_ONLY
class ValueSetDefinitionResolution_ (_ImportedBinding_core_service_api.BaseService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}ValueSetDefinitionResolution with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValueSetDefinitionResolution')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 58, 1)
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
Namespace.addCategoryObject('typeBinding', u'ValueSetDefinitionResolution', ValueSetDefinitionResolution_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}ValueSetDefinitionHistoryService with content type ELEMENT_ONLY
class ValueSetDefinitionHistoryService_ (_ImportedBinding_core_service_api.HistoryService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}ValueSetDefinitionHistoryService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValueSetDefinitionHistoryService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 13, 1)
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
Namespace.addCategoryObject('typeBinding', u'ValueSetDefinitionHistoryService', ValueSetDefinitionHistoryService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}ValueSetDefinitionMaintenanceService with content type ELEMENT_ONLY
class ValueSetDefinitionMaintenanceService_ (_ImportedBinding_core_service_api.BaseMaintenanceService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}ValueSetDefinitionMaintenanceService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValueSetDefinitionMaintenanceService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 22, 1)
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
Namespace.addCategoryObject('typeBinding', u'ValueSetDefinitionMaintenanceService', ValueSetDefinitionMaintenanceService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}ValueSetDefinitionQueryService with content type ELEMENT_ONLY
class ValueSetDefinitionQueryService_ (_ImportedBinding_core_service_api.BaseQueryService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}ValueSetDefinitionQueryService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValueSetDefinitionQueryService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 31, 1)
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
Namespace.addCategoryObject('typeBinding', u'ValueSetDefinitionQueryService', ValueSetDefinitionQueryService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}ValueSetDefinitionReadService with content type ELEMENT_ONLY
class ValueSetDefinitionReadService_ (_ImportedBinding_core_service_api.BaseReadService_):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}ValueSetDefinitionReadService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValueSetDefinitionReadService')
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 40, 1)
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
    
    # Element {http://www.omg.org/spec/CTS2/1.1/ValueSetDefinitionServices}knownTag uses Python identifier knownTag
    __knownTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'knownTag'), 'knownTag', '__httpwww_omg_orgspecCTS21_1ValueSetDefinitionServices_ValueSetDefinitionReadService__httpwww_omg_orgspecCTS21_1ValueSetDefinitionServicesknownTag', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 44, 5), )

    
    knownTag = property(__knownTag.value, __knownTag.set, None, None)

    _ElementMap.update({
        __knownTag.name() : __knownTag
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ValueSetDefinitionReadService', ValueSetDefinitionReadService_)


ResolvedValueSetLoader = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ResolvedValueSetLoader'), ResolvedValueSetLoader_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 50, 1))
Namespace.addCategoryObject('elementBinding', ResolvedValueSetLoader.name().localName(), ResolvedValueSetLoader)

ValueSetDefinitionResolution = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueSetDefinitionResolution'), ValueSetDefinitionResolution_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 57, 1))
Namespace.addCategoryObject('elementBinding', ValueSetDefinitionResolution.name().localName(), ValueSetDefinitionResolution)

ValueSetDefinitionHistoryService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueSetDefinitionHistoryService'), ValueSetDefinitionHistoryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 12, 1))
Namespace.addCategoryObject('elementBinding', ValueSetDefinitionHistoryService.name().localName(), ValueSetDefinitionHistoryService)

ValueSetDefinitionMaintenanceService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueSetDefinitionMaintenanceService'), ValueSetDefinitionMaintenanceService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 21, 1))
Namespace.addCategoryObject('elementBinding', ValueSetDefinitionMaintenanceService.name().localName(), ValueSetDefinitionMaintenanceService)

ValueSetDefinitionQueryService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueSetDefinitionQueryService'), ValueSetDefinitionQueryService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 30, 1))
Namespace.addCategoryObject('elementBinding', ValueSetDefinitionQueryService.name().localName(), ValueSetDefinitionQueryService)

ValueSetDefinitionReadService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueSetDefinitionReadService'), ValueSetDefinitionReadService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 39, 1))
Namespace.addCategoryObject('elementBinding', ValueSetDefinitionReadService.name().localName(), ValueSetDefinitionReadService)



ResolvedValueSetLoader_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'knownValueSet'), _ImportedBinding__nsgroup.ResolvedValueSetSummary_, scope=ResolvedValueSetLoader_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 53, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 53, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ResolvedValueSetLoader_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownValueSet')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 53, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ResolvedValueSetLoader_._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionResolution_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionResolution_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionResolution_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionResolution_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionResolution_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionResolution_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionResolution_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionResolution_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionResolution_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
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
ValueSetDefinitionResolution_._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionHistoryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'changeHistory')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 453, 5))
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
ValueSetDefinitionHistoryService_._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
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
ValueSetDefinitionMaintenanceService_._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownProperty')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedMatchAlgorithm')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 754, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionQueryService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedModelAttribute')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 759, 5))
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
ValueSetDefinitionQueryService_._Automaton = _BuildAutomaton_4()




ValueSetDefinitionReadService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'knownTag'), _ImportedBinding__nsgroup.VersionTagReference, scope=ValueSetDefinitionReadService_, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 44, 5)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 44, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionReadService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ValueSetDefinitionReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownTag')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/valuesetdefinition/ValueSetDefinitionServices.xsd', 44, 5))
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
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ValueSetDefinitionReadService_._Automaton = _BuildAutomaton_5()

