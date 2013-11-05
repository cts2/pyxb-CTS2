# ./conceptdomainbinding_service_api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:83e64866a204e8d1e100442da32a2137fb714ac7
# Generated 2013-04-18 16:41:20.530074 by PyXB version 1.2.2
# Namespace http://www.omg.org/spec/CTS2/1.1/ConceptDomainBindingServices

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
import core_service_api as _ImportedBinding_core_service_api
import pyxb.binding.datatypes
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.omg.org/spec/CTS2/1.1/ConceptDomainBindingServices', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_coreservice = _ImportedBinding_core_service_api.Namespace
_Namespace_coreservice.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/ConceptDomainBindingServices}updatedBoundValueSetDefinition uses Python identifier updatedBoundValueSetDefinition
    __updatedBoundValueSetDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedBoundValueSetDefinition'), 'updatedBoundValueSetDefinition', '__httpwww_omg_orgspecCTS21_1ConceptDomainBindingServices_CTD_ANON_httpwww_omg_orgspecCTS21_1ConceptDomainBindingServicesupdatedBoundValueSetDefinition', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 14, 4), )

    
    updatedBoundValueSetDefinition = property(__updatedBoundValueSetDefinition.value, __updatedBoundValueSetDefinition.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/ConceptDomainBindingServices}updatedUseCodeSystemVersion uses Python identifier updatedUseCodeSystemVersion
    __updatedUseCodeSystemVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedUseCodeSystemVersion'), 'updatedUseCodeSystemVersion', '__httpwww_omg_orgspecCTS21_1ConceptDomainBindingServices_CTD_ANON_httpwww_omg_orgspecCTS21_1ConceptDomainBindingServicesupdatedUseCodeSystemVersion', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 26, 4), )

    
    updatedUseCodeSystemVersion = property(__updatedUseCodeSystemVersion.value, __updatedUseCodeSystemVersion.set, None, None)

    _ElementMap.update({
        __updatedBoundValueSetDefinition.name() : __updatedBoundValueSetDefinition,
        __updatedUseCodeSystemVersion.name() : __updatedUseCodeSystemVersion
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
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 15, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/ConceptDomainBindingServices}boundValueSetDefinition uses Python identifier boundValueSetDefinition
    __boundValueSetDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'boundValueSetDefinition'), 'boundValueSetDefinition', '__httpwww_omg_orgspecCTS21_1ConceptDomainBindingServices_CTD_ANON__httpwww_omg_orgspecCTS21_1ConceptDomainBindingServicesboundValueSetDefinition', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 17, 7), )

    
    boundValueSetDefinition = property(__boundValueSetDefinition.value, __boundValueSetDefinition.set, None, u'the specific value set definition to be used in\n\t\t\t\t\t\t\t\t\t\tthis binding')

    _ElementMap.update({
        __boundValueSetDefinition.name() : __boundValueSetDefinition
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
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 27, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/ConceptDomainBindingServices}useCodeSystemVersion uses Python identifier useCodeSystemVersion
    __useCodeSystemVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'useCodeSystemVersion'), 'useCodeSystemVersion', '__httpwww_omg_orgspecCTS21_1ConceptDomainBindingServices_CTD_ANON_2_httpwww_omg_orgspecCTS21_1ConceptDomainBindingServicesuseCodeSystemVersion', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 29, 7), )

    
    useCodeSystemVersion = property(__useCodeSystemVersion.value, __useCodeSystemVersion.set, None, u'the local identifiers for or URIs of a set of\n\t\t\t\t\t\t\t\t\t\tcode system versions to be used in the binding')

    _ElementMap.update({
        __useCodeSystemVersion.name() : __useCodeSystemVersion
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (_ImportedBinding_core_service_api.BaseMaintenanceService_):
    """A service that allows the creation, update and
					deletion of concept domain bindings"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 43, 2)
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (_ImportedBinding_core_service_api.BaseQueryService_):
    """A service that allows the enumeration, query and
					filtering of the concept domain bindings known to the system
				"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 57, 2)
    _ElementMap = _ImportedBinding_core_service_api.BaseQueryService_._ElementMap.copy()
    _AttributeMap = _ImportedBinding_core_service_api.BaseQueryService_._AttributeMap.copy()
    # Base type is _ImportedBinding_core_service_api.BaseQueryService_
    
    # Element {http://www.omg.org/spec/CTS2/1.1/ConceptDomainBindingServices}conceptDomainBindings uses Python identifier conceptDomainBindings
    __conceptDomainBindings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'conceptDomainBindings'), 'conceptDomainBindings', '__httpwww_omg_orgspecCTS21_1ConceptDomainBindingServices_CTD_ANON_4_httpwww_omg_orgspecCTS21_1ConceptDomainBindingServicesconceptDomainBindings', False, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 66, 6), )

    
    conceptDomainBindings = property(__conceptDomainBindings.value, __conceptDomainBindings.set, None, u'a DirectoryURI that resolves to the set of all\n\t\t\t\t\t\t\t\t\tconcept domain bindings known to the service')

    
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
        __conceptDomainBindings.name() : __conceptDomainBindings
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (_ImportedBinding_core_service_api.BaseReadService_):
    """A service that provides direct read access to
					bindings that are asserted between concept domains and value sets.
				"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 81, 2)
    _ElementMap = _ImportedBinding_core_service_api.BaseReadService_._ElementMap.copy()
    _AttributeMap = _ImportedBinding_core_service_api.BaseReadService_._AttributeMap.copy()
    # Base type is _ImportedBinding_core_service_api.BaseReadService_
    
    # Element {http://www.omg.org/spec/CTS2/1.1/ConceptDomainBindingServices}supportedTag uses Python identifier supportedTag
    __supportedTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'supportedTag'), 'supportedTag', '__httpwww_omg_orgspecCTS21_1ConceptDomainBindingServices_CTD_ANON_5_httpwww_omg_orgspecCTS21_1ConceptDomainBindingServicessupportedTag', True, pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 90, 6), )

    
    supportedTag = property(__supportedTag.value, __supportedTag.set, None, u'the set of version tags known to the service.\n\t\t\t\t\t\t\t\t\tAll services must recognize the tag, CURRENT, the\n\t\t\t\t\t\t\t\t\tinterpretation of which is service specific.')

    
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
        __supportedTag.name() : __supportedTag
    })
    _AttributeMap.update({
        
    })



UpdateConceptDomainBindingRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UpdateConceptDomainBindingRequest'), CTD_ANON, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 11, 1))
Namespace.addCategoryObject('elementBinding', UpdateConceptDomainBindingRequest.name().localName(), UpdateConceptDomainBindingRequest)

ConceptDomainBindingMaintenanceService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConceptDomainBindingMaintenanceService'), CTD_ANON_3, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 42, 1))
Namespace.addCategoryObject('elementBinding', ConceptDomainBindingMaintenanceService.name().localName(), ConceptDomainBindingMaintenanceService)

ConceptDomainBindingQueryService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConceptDomainBindingQueryService'), CTD_ANON_4, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 56, 1))
Namespace.addCategoryObject('elementBinding', ConceptDomainBindingQueryService.name().localName(), ConceptDomainBindingQueryService)

ConceptDomainBindingReadService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConceptDomainBindingReadService'), CTD_ANON_5, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 80, 1))
Namespace.addCategoryObject('elementBinding', ConceptDomainBindingReadService.name().localName(), ConceptDomainBindingReadService)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedBoundValueSetDefinition'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 14, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedUseCodeSystemVersion'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 26, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 14, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 26, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedBoundValueSetDefinition')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 14, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedUseCodeSystemVersion')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 26, 4))
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
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'boundValueSetDefinition'), _ImportedBinding__nsgroup.DocumentURI, scope=CTD_ANON_, documentation=u'the specific value set definition to be used in\n\t\t\t\t\t\t\t\t\t\tthis binding', location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 17, 7)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 17, 7))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'boundValueSetDefinition')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 17, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'useCodeSystemVersion'), _ImportedBinding_core_service_api.NameOrURIList_, scope=CTD_ANON_2, documentation=u'the local identifiers for or URIs of a set of\n\t\t\t\t\t\t\t\t\t\tcode system versions to be used in the binding', location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 29, 7)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 29, 7))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'useCodeSystemVersion')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 29, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
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
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'conceptDomainBindings'), _ImportedBinding__nsgroup.ConceptDomainBindingDirectoryURI, scope=CTD_ANON_4, documentation=u'a DirectoryURI that resolves to the set of all\n\t\t\t\t\t\t\t\t\tconcept domain bindings known to the service', location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 66, 6)))

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
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownProperty')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedMatchAlgorithm')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 754, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedModelAttribute')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 759, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'conceptDomainBindings')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 66, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
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
    st_11._set_transitionSet(transitions)
    transitions = []
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'supportedTag'), _ImportedBinding__nsgroup.VersionTagReference, scope=CTD_ANON_5, documentation=u'the set of version tags known to the service.\n\t\t\t\t\t\t\t\t\tAll services must recognize the tag, CURRENT, the\n\t\t\t\t\t\t\t\t\tinterpretation of which is service specific.', location=pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 90, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_coreservice, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedTag')), pyxb.utils.utility.Location('http://informatics.mayo.edu/cts2/spec/CTS2/1.1/conceptdomainbinding/ConceptDomainBindingServices.xsd', 90, 6))
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
         ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()

