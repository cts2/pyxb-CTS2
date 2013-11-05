# ./core_service_api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:766b87429f1e7a189b9fb1b81a7fcaeef51dc3cf
# Generated 2013-11-05 15:25:28.323155 by PyXB version 1.2.3
# Namespace http://www.omg.org/spec/CTS2/1.1/CoreService [xmlns:coreservice]

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
import pyxb.binding.datatypes
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.omg.org/spec/CTS2/1.1/CoreService', create_if_missing=True)
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


# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/CoreService}StructuralProfile
class StructuralProfile (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The CTS specification defines eleven distinct structural profiles. CTS compliant implementations may elect to implement any combination of these profiles to meet their individual requirements and use cases."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StructuralProfile')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 93, 1)
    _Documentation = u'The CTS specification defines eleven distinct structural profiles. CTS compliant implementations may elect to implement any combination of these profiles to meet their individual requirements and use cases.'
StructuralProfile._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StructuralProfile, enum_prefix=None)
StructuralProfile.SP_CODE_SYSTEM = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_CODE_SYSTEM', tag=u'SP_CODE_SYSTEM')
StructuralProfile.SP_CODE_SYSTEM_VERSION = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_CODE_SYSTEM_VERSION', tag=u'SP_CODE_SYSTEM_VERSION')
StructuralProfile.SP_ENTITY_DESCRIPTION = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_ENTITY_DESCRIPTION', tag=u'SP_ENTITY_DESCRIPTION')
StructuralProfile.SP_ASSOCIATION = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_ASSOCIATION', tag=u'SP_ASSOCIATION')
StructuralProfile.SP_VALUE_SET = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_VALUE_SET', tag=u'SP_VALUE_SET')
StructuralProfile.SP_VALUE_SET_DEFINITION = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_VALUE_SET_DEFINITION', tag=u'SP_VALUE_SET_DEFINITION')
StructuralProfile.SP_VALUE_SET_RESOLUTION = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_VALUE_SET_RESOLUTION', tag=u'SP_VALUE_SET_RESOLUTION')
StructuralProfile.SP_CONCEPT_DOMAIN = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_CONCEPT_DOMAIN', tag=u'SP_CONCEPT_DOMAIN')
StructuralProfile.SP_CONCEPT_DOMAIN_BINDING = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_CONCEPT_DOMAIN_BINDING', tag=u'SP_CONCEPT_DOMAIN_BINDING')
StructuralProfile.SP_MAP = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_MAP', tag=u'SP_MAP')
StructuralProfile.SP_MAP_VERSION = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_MAP_VERSION', tag=u'SP_MAP_VERSION')
StructuralProfile.SP_MAP_ENTRY = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_MAP_ENTRY', tag=u'SP_MAP_ENTRY')
StructuralProfile.SP_STATEMENT = StructuralProfile._CF_enumeration.addEnumeration(unicode_value=u'SP_STATEMENT', tag=u'SP_STATEMENT')
StructuralProfile._InitializeFacetMap(StructuralProfile._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'StructuralProfile', StructuralProfile)

# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/CoreService}FunctionalProfile
class FunctionalProfile (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """An enumeration of the possible functional profiles, some or all of which can be implemented by a conformant CTS service"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FunctionalProfile')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 167, 1)
    _Documentation = u'An enumeration of the possible functional profiles, some or all of which can be implemented by a conformant CTS service'
FunctionalProfile._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FunctionalProfile, enum_prefix=None)
FunctionalProfile.FP_READ = FunctionalProfile._CF_enumeration.addEnumeration(unicode_value=u'FP_READ', tag=u'FP_READ')
FunctionalProfile.FP_QUERY = FunctionalProfile._CF_enumeration.addEnumeration(unicode_value=u'FP_QUERY', tag=u'FP_QUERY')
FunctionalProfile.FP_IMPORT = FunctionalProfile._CF_enumeration.addEnumeration(unicode_value=u'FP_IMPORT', tag=u'FP_IMPORT')
FunctionalProfile.FP_EXPORT = FunctionalProfile._CF_enumeration.addEnumeration(unicode_value=u'FP_EXPORT', tag=u'FP_EXPORT')
FunctionalProfile.FP_UPDATE = FunctionalProfile._CF_enumeration.addEnumeration(unicode_value=u'FP_UPDATE', tag=u'FP_UPDATE')
FunctionalProfile.FP_MAINTENANCE = FunctionalProfile._CF_enumeration.addEnumeration(unicode_value=u'FP_MAINTENANCE', tag=u'FP_MAINTENANCE')
FunctionalProfile.FP_TEMPORAL = FunctionalProfile._CF_enumeration.addEnumeration(unicode_value=u'FP_TEMPORAL', tag=u'FP_TEMPORAL')
FunctionalProfile._InitializeFacetMap(FunctionalProfile._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'FunctionalProfile', FunctionalProfile)

# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/CoreService}ImplementationProfile
class ImplementationProfile (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """Indicates what PSM(s) are supported by the given service implementation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ImplementationProfile')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 182, 1)
    _Documentation = u'Indicates what PSM(s) are supported by the given service implementation.'
ImplementationProfile._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ImplementationProfile, enum_prefix=None)
ImplementationProfile.IP_REST = ImplementationProfile._CF_enumeration.addEnumeration(unicode_value=u'IP_REST', tag=u'IP_REST')
ImplementationProfile.IP_SOAP = ImplementationProfile._CF_enumeration.addEnumeration(unicode_value=u'IP_SOAP', tag=u'IP_SOAP')
ImplementationProfile.IP_CRDF = ImplementationProfile._CF_enumeration.addEnumeration(unicode_value=u'IP_CRDF', tag=u'IP_CRDF')
ImplementationProfile._InitializeFacetMap(ImplementationProfile._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ImplementationProfile', ImplementationProfile)

# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/CoreService}OverwriteRule
class OverwriteRule (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OverwriteRule')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 501, 1)
    _Documentation = ''
OverwriteRule._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OverwriteRule, enum_prefix=None)
OverwriteRule.OVERWRITE_IF_EXISTS = OverwriteRule._CF_enumeration.addEnumeration(unicode_value=u'OVERWRITE_IF_EXISTS', tag=u'OVERWRITE_IF_EXISTS')
OverwriteRule.FAIL_IF_EXISTS = OverwriteRule._CF_enumeration.addEnumeration(unicode_value=u'FAIL_IF_EXISTS', tag=u'FAIL_IF_EXISTS')
OverwriteRule._InitializeFacetMap(OverwriteRule._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'OverwriteRule', OverwriteRule)

# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/CoreService}ErrorResponse
class ErrorResponse (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ErrorResponse')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 511, 1)
    _Documentation = ''
ErrorResponse._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ErrorResponse, enum_prefix=None)
ErrorResponse.CONTINUE_ON_ERROR = ErrorResponse._CF_enumeration.addEnumeration(unicode_value=u'CONTINUE_ON_ERROR', tag=u'CONTINUE_ON_ERROR')
ErrorResponse.STOP_ON_ERROR = ErrorResponse._CF_enumeration.addEnumeration(unicode_value=u'STOP_ON_ERROR', tag=u'STOP_ON_ERROR')
ErrorResponse.STOP_ON_WARNING = ErrorResponse._CF_enumeration.addEnumeration(unicode_value=u'STOP_ON_WARNING', tag=u'STOP_ON_WARNING')
ErrorResponse._InitializeFacetMap(ErrorResponse._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ErrorResponse', ErrorResponse)

# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/CoreService}SyncOrAsync
class SyncOrAsync (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SyncOrAsync')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 534, 1)
    _Documentation = ''
SyncOrAsync._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SyncOrAsync, enum_prefix=None)
SyncOrAsync.SYNCHRONOUS = SyncOrAsync._CF_enumeration.addEnumeration(unicode_value=u'SYNCHRONOUS', tag=u'SYNCHRONOUS')
SyncOrAsync.ASYNCHRONOUS = SyncOrAsync._CF_enumeration.addEnumeration(unicode_value=u'ASYNCHRONOUS', tag=u'ASYNCHRONOUS')
SyncOrAsync._InitializeFacetMap(SyncOrAsync._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SyncOrAsync', SyncOrAsync)

# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/CoreService}ValidationLevel
class ValidationLevel (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValidationLevel')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 543, 1)
    _Documentation = ''
ValidationLevel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ValidationLevel, enum_prefix=None)
ValidationLevel.VL_WARN = ValidationLevel._CF_enumeration.addEnumeration(unicode_value=u'VL_WARN', tag=u'VL_WARN')
ValidationLevel.VL_ERROR = ValidationLevel._CF_enumeration.addEnumeration(unicode_value=u'VL_ERROR', tag=u'VL_ERROR')
ValidationLevel._InitializeFacetMap(ValidationLevel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ValidationLevel', ValidationLevel)

# Atomic simple type: [anonymous]
class STD_ANON (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 559, 4)
    _Documentation = ''
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.VALID = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'VALID', tag=u'VALID')
STD_ANON.INVALID = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'INVALID', tag=u'INVALID')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 578, 4)
    _Documentation = ''
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.SUCCESS = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'SUCCESS', tag=u'SUCCESS')
STD_ANON_.FAILURE = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'FAILURE', tag=u'FAILURE')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/CoreService}LoggingLevel
class LoggingLevel (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """The  entries are modeled after the corresponding levels in the log4j package, each level includes the entries in the lower level. In particular, levels are ordered. For the standard levels, we have DEBUG &lt; INFO &lt; WARN &lt; ERROR &lt; FATAL."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LoggingLevel')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 667, 1)
    _Documentation = u'The  entries are modeled after the corresponding levels in the log4j package, each level includes the entries in the lower level. In particular, levels are ordered. For the standard levels, we have DEBUG &lt; INFO &lt; WARN &lt; ERROR &lt; FATAL.'
LoggingLevel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LoggingLevel, enum_prefix=None)
LoggingLevel.DEBUG = LoggingLevel._CF_enumeration.addEnumeration(unicode_value=u'DEBUG', tag=u'DEBUG')
LoggingLevel.INFO = LoggingLevel._CF_enumeration.addEnumeration(unicode_value=u'INFO', tag=u'INFO')
LoggingLevel.WARN = LoggingLevel._CF_enumeration.addEnumeration(unicode_value=u'WARN', tag=u'WARN')
LoggingLevel.ERROR = LoggingLevel._CF_enumeration.addEnumeration(unicode_value=u'ERROR', tag=u'ERROR')
LoggingLevel.FATAL = LoggingLevel._CF_enumeration.addEnumeration(unicode_value=u'FATAL', tag=u'FATAL')
LoggingLevel._InitializeFacetMap(LoggingLevel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LoggingLevel', LoggingLevel)

# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/CoreService}RestrictionType
class RestrictionType (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """A parameter used in queries where multiple elements are provided. It determines whether a candidate element must satisfy all restrictions or just one or more restriction in order to be considered as satisfying the restriction composite"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RestrictionType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 880, 1)
    _Documentation = u'A parameter used in queries where multiple elements are provided. It determines whether a candidate element must satisfy all restrictions or just one or more restriction in order to be considered as satisfying the restriction composite'
RestrictionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RestrictionType, enum_prefix=None)
RestrictionType.ALL = RestrictionType._CF_enumeration.addEnumeration(unicode_value=u'ALL', tag=u'ALL')
RestrictionType.AT_LEAST_ONE = RestrictionType._CF_enumeration.addEnumeration(unicode_value=u'AT_LEAST_ONE', tag=u'AT_LEAST_ONE')
RestrictionType._InitializeFacetMap(RestrictionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'RestrictionType', RestrictionType)

# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/CoreService}ActiveOrAll
class ActiveOrAll (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """An indicator that determines whether the given service access request applies only to elements that are currently marked as  in the context of the particular query or to both  and  entries."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ActiveOrAll')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 929, 1)
    _Documentation = u'An indicator that determines whether the given service access request applies only to elements that are currently marked as  in the context of the particular query or to both  and  entries.'
ActiveOrAll._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ActiveOrAll, enum_prefix=None)
ActiveOrAll.ACTIVE_ONLY = ActiveOrAll._CF_enumeration.addEnumeration(unicode_value=u'ACTIVE_ONLY', tag=u'ACTIVE_ONLY')
ActiveOrAll.ACTIVE_AND_INACTIVE = ActiveOrAll._CF_enumeration.addEnumeration(unicode_value=u'ACTIVE_AND_INACTIVE', tag=u'ACTIVE_AND_INACTIVE')
ActiveOrAll._InitializeFacetMap(ActiveOrAll._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ActiveOrAll', ActiveOrAll)

# Atomic simple type: {http://www.omg.org/spec/CTS2/1.1/CoreService}SortDirection
class SortDirection (_ImportedBinding__nsgroup.Enumeration, pyxb.binding.basis.enumeration_mixin):

    """The collating order of a sort."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SortDirection')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1007, 1)
    _Documentation = u'The collating order of a sort.'
SortDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SortDirection, enum_prefix=None)
SortDirection.ASCENDING = SortDirection._CF_enumeration.addEnumeration(unicode_value=u'ASCENDING', tag=u'ASCENDING')
SortDirection.DESCENDING = SortDirection._CF_enumeration.addEnumeration(unicode_value=u'DESCENDING', tag=u'DESCENDING')
SortDirection._InitializeFacetMap(SortDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SortDirection', SortDirection)

# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}Query with content type ELEMENT_ONLY
class Query_ (pyxb.binding.basis.complexTypeDefinition):
    """
			Message structure for packaging and sending complex queries.
			
			A Query may contain a Filter, a Set Operation, or Both.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Query')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 6, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}matchAlgorithm uses Python identifier matchAlgorithm
    __matchAlgorithm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'matchAlgorithm'), 'matchAlgorithm', '__httpwww_omg_orgspecCTS21_1CoreService_Query__httpwww_omg_orgspecCTS21_1CoreServicematchAlgorithm', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 16, 3), )

    
    matchAlgorithm = property(__matchAlgorithm.value, __matchAlgorithm.set, None, u"\n\t\t\t\t\tThe match algorithm of the filter to be applied. If a 'setOperation' is specified, \n\t\t\t\t\tthe filter will apply to the resulting aggregate.\n\t\t\t\t\t")

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}matchValue uses Python identifier matchValue
    __matchValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'matchValue'), 'matchValue', '__httpwww_omg_orgspecCTS21_1CoreService_Query__httpwww_omg_orgspecCTS21_1CoreServicematchValue', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 24, 3), )

    
    matchValue = property(__matchValue.value, __matchValue.set, None, u"\n\t\t\t\t\tThe match value of the filter to be applied. If a 'setOperation' is specified, \n\t\t\t\t\tthe filter will apply to the resulting aggregate.\n\t\t\t\t\t")

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}filterComponent uses Python identifier filterComponent
    __filterComponent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'filterComponent'), 'filterComponent', '__httpwww_omg_orgspecCTS21_1CoreService_Query__httpwww_omg_orgspecCTS21_1CoreServicefilterComponent', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 32, 3), )

    
    filterComponent = property(__filterComponent.value, __filterComponent.set, None, u"\n\t\t\t\t\tThe target components of the filter to be applied. If a 'setOperation' is specified, \n\t\t\t\t\tthe filter will apply to the resulting aggregate.\n\t\t\t\t\t")

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}setOperation uses Python identifier setOperation
    __setOperation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'setOperation'), 'setOperation', '__httpwww_omg_orgspecCTS21_1CoreService_Query__httpwww_omg_orgspecCTS21_1CoreServicesetOperation', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 40, 3), )

    
    setOperation = property(__setOperation.value, __setOperation.set, None, u'\n\t\t\t\t\tThe Set Operation to be applied to the two DirectoryURIs.\n\t\t\t\t\t')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}query1 uses Python identifier query1
    __query1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'query1'), 'query1', '__httpwww_omg_orgspecCTS21_1CoreService_Query__httpwww_omg_orgspecCTS21_1CoreServicequery1', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 53, 4), )

    
    query1 = property(__query1.value, __query1.set, None, u'\n\t\t\t\t\t\tThe left-hand side of the Set Operation.\n\t\t\t\t\t\t')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}directoryUri1 uses Python identifier directoryUri1
    __directoryUri1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'directoryUri1'), 'directoryUri1', '__httpwww_omg_orgspecCTS21_1CoreService_Query__httpwww_omg_orgspecCTS21_1CoreServicedirectoryUri1', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 60, 4), )

    
    directoryUri1 = property(__directoryUri1.value, __directoryUri1.set, None, u'\n\t\t\t\t\t\tThe left-hand side of the Set Operation.\n\t\t\t\t\t\t')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}query2 uses Python identifier query2
    __query2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'query2'), 'query2', '__httpwww_omg_orgspecCTS21_1CoreService_Query__httpwww_omg_orgspecCTS21_1CoreServicequery2', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 74, 4), )

    
    query2 = property(__query2.value, __query2.set, None, u'\n\t\t\t\t\t\tThe right-hand side of the Set Operation.\n\t\t\t\t\t\t')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}directoryUri2 uses Python identifier directoryUri2
    __directoryUri2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'directoryUri2'), 'directoryUri2', '__httpwww_omg_orgspecCTS21_1CoreService_Query__httpwww_omg_orgspecCTS21_1CoreServicedirectoryUri2', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 81, 4), )

    
    directoryUri2 = property(__directoryUri2.value, __directoryUri2.set, None, u'\n\t\t\t\t\t\tThe right-hand side of the Set Operation.\n\t\t\t\t\t\t')

    _ElementMap.update({
        __matchAlgorithm.name() : __matchAlgorithm,
        __matchValue.name() : __matchValue,
        __filterComponent.name() : __filterComponent,
        __setOperation.name() : __setOperation,
        __query1.name() : __query1,
        __directoryUri1.name() : __directoryUri1,
        __query2.name() : __query2,
        __directoryUri2.name() : __directoryUri2
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Query', Query_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}ProfileElement with content type ELEMENT_ONLY
class ProfileElement (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}ProfileElement with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ProfileElement')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 210, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}structuralProfile uses Python identifier structuralProfile
    __structuralProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'structuralProfile'), 'structuralProfile', '__httpwww_omg_orgspecCTS21_1CoreService_ProfileElement_httpwww_omg_orgspecCTS21_1CoreServicestructuralProfile', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 212, 3), )

    
    structuralProfile = property(__structuralProfile.value, __structuralProfile.set, None, u'A resource that is implemented by a service instance')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}functionalProfile uses Python identifier functionalProfile
    __functionalProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'functionalProfile'), 'functionalProfile', '__httpwww_omg_orgspecCTS21_1CoreService_ProfileElement_httpwww_omg_orgspecCTS21_1CoreServicefunctionalProfile', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 217, 3), )

    
    functionalProfile = property(__functionalProfile.value, __functionalProfile.set, None, u'A functional profile that the service instance supports for the corresponding structure')

    _ElementMap.update({
        __structuralProfile.name() : __structuralProfile,
        __functionalProfile.name() : __functionalProfile
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ProfileElement', ProfileElement)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService with content type ELEMENT_ONLY
class BaseService_ (pyxb.binding.basis.complexTypeDefinition):
    """ contains the components that are common to any CTS service implementation. It includes information about the service itself, the namespaces and formats that are known to the service and the structural, functional and representation profiles that are supported by the service instance."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BaseService')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 248, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}serviceName uses Python identifier serviceName
    __serviceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'serviceName'), 'serviceName', '__httpwww_omg_orgspecCTS21_1CoreService_BaseService__httpwww_omg_orgspecCTS21_1CoreServiceserviceName', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3), )

    
    serviceName = property(__serviceName.value, __serviceName.set, None, u'A short name that identifies the particular service and implementation.')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}serviceDescription uses Python identifier serviceDescription
    __serviceDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'serviceDescription'), 'serviceDescription', '__httpwww_omg_orgspecCTS21_1CoreService_BaseService__httpwww_omg_orgspecCTS21_1CoreServiceserviceDescription', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3), )

    
    serviceDescription = property(__serviceDescription.value, __serviceDescription.set, None, u'A description of the service, its use, etc.')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}serviceVersion uses Python identifier serviceVersion
    __serviceVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'serviceVersion'), 'serviceVersion', '__httpwww_omg_orgspecCTS21_1CoreService_BaseService__httpwww_omg_orgspecCTS21_1CoreServiceserviceVersion', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3), )

    
    serviceVersion = property(__serviceVersion.value, __serviceVersion.set, None, u'The version or release identifier of the service.')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}serviceProvider uses Python identifier serviceProvider
    __serviceProvider = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'serviceProvider'), 'serviceProvider', '__httpwww_omg_orgspecCTS21_1CoreService_BaseService__httpwww_omg_orgspecCTS21_1CoreServiceserviceProvider', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3), )

    
    serviceProvider = property(__serviceProvider.value, __serviceProvider.set, None, u'A reference to the individual or organization that provides the service.')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}supportedFormat uses Python identifier supportedFormat
    __supportedFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'supportedFormat'), 'supportedFormat', '__httpwww_omg_orgspecCTS21_1CoreService_BaseService__httpwww_omg_orgspecCTS21_1CoreServicesupportedFormat', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3), )

    
    supportedFormat = property(__supportedFormat.value, __supportedFormat.set, None, u'A list of the representation formats supported by the service. Example: text/html, text/xml, application/json')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}defaultFormat uses Python identifier defaultFormat
    __defaultFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'defaultFormat'), 'defaultFormat', '__httpwww_omg_orgspecCTS21_1CoreService_BaseService__httpwww_omg_orgspecCTS21_1CoreServicedefaultFormat', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3), )

    
    defaultFormat = property(__defaultFormat.value, __defaultFormat.set, None, u'The default format used by the service unless otherwise specified.')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}supportedProfile uses Python identifier supportedProfile
    __supportedProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'supportedProfile'), 'supportedProfile', '__httpwww_omg_orgspecCTS21_1CoreService_BaseService__httpwww_omg_orgspecCTS21_1CoreServicesupportedProfile', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3), )

    
    supportedProfile = property(__supportedProfile.value, __supportedProfile.set, None, u'The set of service profiles that are supported by this service implementation')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}implementationType uses Python identifier implementationType
    __implementationType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'implementationType'), 'implementationType', '__httpwww_omg_orgspecCTS21_1CoreService_BaseService__httpwww_omg_orgspecCTS21_1CoreServiceimplementationType', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3), )

    
    implementationType = property(__implementationType.value, __implementationType.set, None, u'The particular implementation type(s) supported by this profile')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}knownNamespace uses Python identifier knownNamespace
    __knownNamespace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'knownNamespace'), 'knownNamespace', '__httpwww_omg_orgspecCTS21_1CoreService_BaseService__httpwww_omg_orgspecCTS21_1CoreServiceknownNamespace', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3), )

    
    knownNamespace = property(__knownNamespace.value, __knownNamespace.set, None, u"The set of namespaces recognized by this service. Because many namespace identifiers tend to be cryptic (i.e. HL7 OIDs, BioPortal URL's, etc.),  includes the namespace name, an optional URI \\emph{and} a place to provide textual detail describing what the namespace references. Note that namespace names must be unique across an entire CTS implementation - the same namespace name cannot represent one namespace in code system A\n\t\t\t\t\t\tand a second in code system B. Note also that namespace names are \\emph{local} to a service instance. Information that is communicated between service instances, recorded in data tables or client software \\emph{must} use full URIs.")

    _ElementMap.update({
        __serviceName.name() : __serviceName,
        __serviceDescription.name() : __serviceDescription,
        __serviceVersion.name() : __serviceVersion,
        __serviceProvider.name() : __serviceProvider,
        __supportedFormat.name() : __supportedFormat,
        __defaultFormat.name() : __defaultFormat,
        __supportedProfile.name() : __supportedProfile,
        __implementationType.name() : __implementationType,
        __knownNamespace.name() : __knownNamespace
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'BaseService', BaseService_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 326, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}releaseDocumentation uses Python identifier releaseDocumentation
    __releaseDocumentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'releaseDocumentation'), 'releaseDocumentation', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_httpwww_omg_orgspecCTS21_1CoreServicereleaseDocumentation', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 328, 8), )

    
    releaseDocumentation = property(__releaseDocumentation.value, __releaseDocumentation.set, None, None)

    _ElementMap.update({
        __releaseDocumentation.name() : __releaseDocumentation
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
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 333, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}releaseFormat uses Python identifier releaseFormat
    __releaseFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'releaseFormat'), 'releaseFormat', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON__httpwww_omg_orgspecCTS21_1CoreServicereleaseFormat', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 335, 8), )

    
    releaseFormat = property(__releaseFormat.value, __releaseFormat.set, None, None)

    _ElementMap.update({
        __releaseFormat.name() : __releaseFormat
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
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 352, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'uri'), 'uri', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_2_httpwww_omg_orgspecCTS21_1CoreServiceuri', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 354, 6), )

    
    uri = property(__uri.value, __uri.set, None, None)

    _ElementMap.update({
        __uri.name() : __uri
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
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 359, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}keyword uses Python identifier keyword
    __keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'keyword'), 'keyword', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_3_httpwww_omg_orgspecCTS21_1CoreServicekeyword', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 361, 6), )

    
    keyword = property(__keyword.value, __keyword.set, None, None)

    _ElementMap.update({
        __keyword.name() : __keyword
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
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 366, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'source'), 'source', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_4_httpwww_omg_orgspecCTS21_1CoreServicesource', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 368, 6), )

    
    source = property(__source.value, __source.set, None, None)

    _ElementMap.update({
        __source.name() : __source
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
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 373, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}note uses Python identifier note
    __note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'note'), 'note', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_5_httpwww_omg_orgspecCTS21_1CoreServicenote', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 375, 6), )

    
    note = property(__note.value, __note.set, None, None)

    _ElementMap.update({
        __note.name() : __note
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
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 380, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'property'), 'property_', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_6_httpwww_omg_orgspecCTS21_1CoreServiceproperty', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 382, 6), )

    
    property_ = property(__property.value, __property.set, None, None)

    _ElementMap.update({
        __property.name() : __property
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
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 387, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}resourceSynopsis uses Python identifier resourceSynopsis
    __resourceSynopsis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'resourceSynopsis'), 'resourceSynopsis', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_7_httpwww_omg_orgspecCTS21_1CoreServiceresourceSynopsis', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 389, 6), )

    
    resourceSynopsis = property(__resourceSynopsis.value, __resourceSynopsis.set, None, None)

    _ElementMap.update({
        __resourceSynopsis.name() : __resourceSynopsis
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 394, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}resourceType uses Python identifier resourceType
    __resourceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'resourceType'), 'resourceType', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_8_httpwww_omg_orgspecCTS21_1CoreServiceresourceType', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 396, 6), )

    
    resourceType = property(__resourceType.value, __resourceType.set, None, None)

    _ElementMap.update({
        __resourceType.name() : __resourceType
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 401, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}rights uses Python identifier rights
    __rights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'rights'), 'rights', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_9_httpwww_omg_orgspecCTS21_1CoreServicerights', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 403, 6), )

    
    rights = property(__rights.value, __rights.set, None, None)

    _ElementMap.update({
        __rights.name() : __rights
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 421, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}predecessor uses Python identifier predecessor
    __predecessor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'predecessor'), 'predecessor', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_10_httpwww_omg_orgspecCTS21_1CoreServicepredecessor', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 423, 8), )

    
    predecessor = property(__predecessor.value, __predecessor.set, None, None)

    _ElementMap.update({
        __predecessor.name() : __predecessor
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 428, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}sourceAndNotation uses Python identifier sourceAndNotation
    __sourceAndNotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sourceAndNotation'), 'sourceAndNotation', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_11_httpwww_omg_orgspecCTS21_1CoreServicesourceAndNotation', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 430, 8), )

    
    sourceAndNotation = property(__sourceAndNotation.value, __sourceAndNotation.set, None, None)

    _ElementMap.update({
        __sourceAndNotation.name() : __sourceAndNotation
    })
    _AttributeMap.update({
        
    })



# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}ValidationResponse with content type ELEMENT_ONLY
class ValidationResponse (pyxb.binding.basis.complexTypeDefinition):
    """The result of a change set validation call"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValidationResponse')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 552, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_omg_orgspecCTS21_1CoreService_ValidationResponse_httpwww_omg_orgspecCTS21_1CoreServicemessage', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 557, 3), )

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}validationResponse uses Python identifier validationResponse
    __validationResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'validationResponse'), 'validationResponse', '__httpwww_omg_orgspecCTS21_1CoreService_ValidationResponse_httpwww_omg_orgspecCTS21_1CoreServicevalidationResponse', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 558, 3), )

    
    validationResponse = property(__validationResponse.value, __validationResponse.set, None, None)

    _ElementMap.update({
        __message.name() : __message,
        __validationResponse.name() : __validationResponse
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ValidationResponse', ValidationResponse)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}SuccessIndicator with content type ELEMENT_ONLY
class SuccessIndicator (pyxb.binding.basis.complexTypeDefinition):
    """An indicator that determines whether a change set was successfully added or not."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SuccessIndicator')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 571, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_omg_orgspecCTS21_1CoreService_SuccessIndicator_httpwww_omg_orgspecCTS21_1CoreServicemessage', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 576, 3), )

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}successIndicator uses Python identifier successIndicator
    __successIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'successIndicator'), 'successIndicator', '__httpwww_omg_orgspecCTS21_1CoreService_SuccessIndicator_httpwww_omg_orgspecCTS21_1CoreServicesuccessIndicator', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 577, 3), )

    
    successIndicator = property(__successIndicator.value, __successIndicator.set, None, None)

    _ElementMap.update({
        __message.name() : __message,
        __successIndicator.name() : __successIndicator
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SuccessIndicator', SuccessIndicator)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}LogEntries with content type ELEMENT_ONLY
class LogEntries_ (pyxb.binding.basis.complexTypeDefinition):
    """A ordered sequence of log entries. The order of the entries is determined by the specific CTS service implementation and should not be assumed by client applications."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogEntries')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 626, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpwww_omg_orgspecCTS21_1CoreService_LogEntries__httpwww_omg_orgspecCTS21_1CoreServiceentry', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 631, 3), )

    
    entry = property(__entry.value, __entry.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'LogEntries', LogEntries_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}ChangeSetEntryList with content type ELEMENT_ONLY
class ChangeSetEntryList (pyxb.binding.basis.complexTypeDefinition):
    """An ordered list of The order of the list reflects the order in which the change sets were applied to the service instance"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ChangeSetEntryList')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 799, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpwww_omg_orgspecCTS21_1CoreService_ChangeSetEntryList_httpwww_omg_orgspecCTS21_1CoreServiceentry', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 804, 3), )

    
    entry = property(__entry.value, __entry.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ChangeSetEntryList', ChangeSetEntryList)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}EntityNameOrURI with content type ELEMENT_ONLY
class EntityNameOrURI_ (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a class, property or individual that is described in some Code System.  may either reference an entity that is known locally to the service or an entity that is described elsewhere. If the entity is known to the service, it is possible to use the  variant, but note that  nor the  are guaranteed to be the same in different CTS implementations. The
					 variant is intended for use in human/browser interactions and should not be hard-coded into data tables or applications."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EntityNameOrURI')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 823, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}entityName uses Python identifier entityName
    __entityName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entityName'), 'entityName', '__httpwww_omg_orgspecCTS21_1CoreService_EntityNameOrURI__httpwww_omg_orgspecCTS21_1CoreServiceentityName', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 829, 3), )

    
    entityName = property(__entityName.value, __entityName.set, None, u'A combination of a namespace identifier and a local name that, together, uniquely references an entity known to the service')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'uri'), 'uri', '__httpwww_omg_orgspecCTS21_1CoreService_EntityNameOrURI__httpwww_omg_orgspecCTS21_1CoreServiceuri', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 834, 3), )

    
    uri = property(__uri.value, __uri.set, None, u'An  that references a class, property or individual')

    _ElementMap.update({
        __entityName.name() : __entityName,
        __uri.name() : __uri
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'EntityNameOrURI', EntityNameOrURI_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}EntityNameOrURIList with content type ELEMENT_ONLY
class EntityNameOrURIList_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EntityNameOrURIList')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 843, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpwww_omg_orgspecCTS21_1CoreService_EntityNameOrURIList__httpwww_omg_orgspecCTS21_1CoreServiceentry', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 848, 3), )

    
    entry = property(__entry.value, __entry.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'EntityNameOrURIList', EntityNameOrURIList_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}NameOrURIList with content type ELEMENT_ONLY
class NameOrURIList_ (pyxb.binding.basis.complexTypeDefinition):
    """A set of zero or more  elements"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NameOrURIList')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 871, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpwww_omg_orgspecCTS21_1CoreService_NameOrURIList__httpwww_omg_orgspecCTS21_1CoreServiceentry', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 876, 3), )

    
    entry = property(__entry.value, __entry.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'NameOrURIList', NameOrURIList_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}QueryControl with content type ELEMENT_ONLY
class QueryControl_ (pyxb.binding.basis.complexTypeDefinition):
    """Parameters that control the return format, number of elements and amount of time that can be taken for a query to complete."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'QueryControl')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 900, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}maxToReturn uses Python identifier maxToReturn
    __maxToReturn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'maxToReturn'), 'maxToReturn', '__httpwww_omg_orgspecCTS21_1CoreService_QueryControl__httpwww_omg_orgspecCTS21_1CoreServicemaxToReturn', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 905, 3), )

    
    maxToReturn = property(__maxToReturn.value, __maxToReturn.set, None, u'The maximum number of  that may be present in a return . Note that a service may choose to return less than  entries - this is simply an upper limit. If  is not supplied, the service may use whatever return block size it determines to be most appropriate.')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}timeLimit uses Python identifier timeLimit
    __timeLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'timeLimit'), 'timeLimit', '__httpwww_omg_orgspecCTS21_1CoreService_QueryControl__httpwww_omg_orgspecCTS21_1CoreServicetimeLimit', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 910, 3), )

    
    timeLimit = property(__timeLimit.value, __timeLimit.set, None, u'The maximum amount of time that may be taken to process a query before a time out exception occurs. If not present, the service determines the maximum query time out.')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}format uses Python identifier format
    __format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'format'), 'format', '__httpwww_omg_orgspecCTS21_1CoreService_QueryControl__httpwww_omg_orgspecCTS21_1CoreServiceformat', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 915, 3), )

    
    format = property(__format.value, __format.set, None, u'The local identifier or URI of the return format for query results.')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}sortCriteria uses Python identifier sortCriteria
    __sortCriteria = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sortCriteria'), 'sortCriteria', '__httpwww_omg_orgspecCTS21_1CoreService_QueryControl__httpwww_omg_orgspecCTS21_1CoreServicesortCriteria', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 920, 3), )

    
    sortCriteria = property(__sortCriteria.value, __sortCriteria.set, None, u'The local identifier or URI of the sort criteria for query results.')

    _ElementMap.update({
        __maxToReturn.name() : __maxToReturn,
        __timeLimit.name() : __timeLimit,
        __format.name() : __format,
        __sortCriteria.name() : __sortCriteria
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'QueryControl', QueryControl_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}ReadContext with content type ELEMENT_ONLY
class ReadContext_ (pyxb.binding.basis.complexTypeDefinition):
    """The context that controls the behavior of a read or query. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReadContext')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 949, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'active'), 'active', '__httpwww_omg_orgspecCTS21_1CoreService_ReadContext__httpwww_omg_orgspecCTS21_1CoreServiceactive', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 954, 3), )

    
    active = property(__active.value, __active.set, None, u'Determines whether the query only applies to only active or all entries. ')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}referenceLanguage uses Python identifier referenceLanguage
    __referenceLanguage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'referenceLanguage'), 'referenceLanguage', '__httpwww_omg_orgspecCTS21_1CoreService_ReadContext__httpwww_omg_orgspecCTS21_1CoreServicereferenceLanguage', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 959, 3), )

    
    referenceLanguage = property(__referenceLanguage.value, __referenceLanguage.set, None, u'The spoken or written language that should be used for the results of the inquiry, where appropriate.')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}changeSetContext uses Python identifier changeSetContext
    __changeSetContext = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'changeSetContext'), 'changeSetContext', '__httpwww_omg_orgspecCTS21_1CoreService_ReadContext__httpwww_omg_orgspecCTS21_1CoreServicechangeSetContext', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 964, 3), )

    
    changeSetContext = property(__changeSetContext.value, __changeSetContext.set, None, u'The URI of an open change set whose contents should be included in the results of the access request.  is only applicable in services that support the  profile')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}referenceTime uses Python identifier referenceTime
    __referenceTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'referenceTime'), 'referenceTime', '__httpwww_omg_orgspecCTS21_1CoreService_ReadContext__httpwww_omg_orgspecCTS21_1CoreServicereferenceTime', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 969, 3), )

    
    referenceTime = property(__referenceTime.value, __referenceTime.set, None, u'The contextual date and time of the query.  is may only be present in services that support the  profile.')

    _ElementMap.update({
        __active.name() : __active,
        __referenceLanguage.name() : __referenceLanguage,
        __changeSetContext.name() : __changeSetContext,
        __referenceTime.name() : __referenceTime
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ReadContext', ReadContext_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}SortCriteria with content type ELEMENT_ONLY
class SortCriteria_ (pyxb.binding.basis.complexTypeDefinition):
    """An ordered list of sort criterion. The first entry in the list identifies the primary sort order, the second entry the sub sort order, etc. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SortCriteria')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 979, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpwww_omg_orgspecCTS21_1CoreService_SortCriteria__httpwww_omg_orgspecCTS21_1CoreServiceentry', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 984, 3), )

    
    entry = property(__entry.value, __entry.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SortCriteria', SortCriteria_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}SortCriterion with content type ELEMENT_ONLY
class SortCriterion_ (pyxb.binding.basis.complexTypeDefinition):
    """The particular attribute, property or special element to be sorted along with the sort direction"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SortCriterion')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 989, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}sortDirection uses Python identifier sortDirection
    __sortDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sortDirection'), 'sortDirection', '__httpwww_omg_orgspecCTS21_1CoreService_SortCriterion__httpwww_omg_orgspecCTS21_1CoreServicesortDirection', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 994, 3), )

    
    sortDirection = property(__sortDirection.value, __sortDirection.set, None, u'The sort order to be applied to the element.')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}sortElement uses Python identifier sortElement
    __sortElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sortElement'), 'sortElement', '__httpwww_omg_orgspecCTS21_1CoreService_SortCriterion__httpwww_omg_orgspecCTS21_1CoreServicesortElement', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 999, 3), )

    
    sortElement = property(__sortElement.value, __sortElement.set, None, u'The type and name of the attribute, property or special element to be sorted')

    _ElementMap.update({
        __sortDirection.name() : __sortDirection,
        __sortElement.name() : __sortElement
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SortCriterion', SortCriterion_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}VersionResolutionService with content type EMPTY
class VersionResolutionService_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VersionResolutionService')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1035, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'VersionResolutionService', VersionResolutionService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}URIList with content type ELEMENT_ONLY
class URIList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}URIList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'URIList')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1041, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}member uses Python identifier member
    __member = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'member'), 'member', '__httpwww_omg_orgspecCTS21_1CoreService_URIList_httpwww_omg_orgspecCTS21_1CoreServicemember', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1043, 3), )

    
    member = property(__member.value, __member.set, None, None)

    _ElementMap.update({
        __member.name() : __member
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'URIList', URIList)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateChangeableMetadataRequest with content type ELEMENT_ONLY
class UpdateChangeableMetadataRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateChangeableMetadataRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UpdateChangeableMetadataRequest')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1048, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedStatus uses Python identifier updatedStatus
    __updatedStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedStatus'), 'updatedStatus', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateChangeableMetadataRequest__httpwww_omg_orgspecCTS21_1CoreServiceupdatedStatus', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1050, 3), )

    
    updatedStatus = property(__updatedStatus.value, __updatedStatus.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedEntryState uses Python identifier updatedEntryState
    __updatedEntryState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedEntryState'), 'updatedEntryState', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateChangeableMetadataRequest__httpwww_omg_orgspecCTS21_1CoreServiceupdatedEntryState', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1057, 3), )

    
    updatedEntryState = property(__updatedEntryState.value, __updatedEntryState.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedEffectiveDate uses Python identifier updatedEffectiveDate
    __updatedEffectiveDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedEffectiveDate'), 'updatedEffectiveDate', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateChangeableMetadataRequest__httpwww_omg_orgspecCTS21_1CoreServiceupdatedEffectiveDate', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1064, 3), )

    
    updatedEffectiveDate = property(__updatedEffectiveDate.value, __updatedEffectiveDate.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedChangeNotes uses Python identifier updatedChangeNotes
    __updatedChangeNotes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedChangeNotes'), 'updatedChangeNotes', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateChangeableMetadataRequest__httpwww_omg_orgspecCTS21_1CoreServiceupdatedChangeNotes', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1071, 3), )

    
    updatedChangeNotes = property(__updatedChangeNotes.value, __updatedChangeNotes.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedChangeSource uses Python identifier updatedChangeSource
    __updatedChangeSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedChangeSource'), 'updatedChangeSource', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateChangeableMetadataRequest__httpwww_omg_orgspecCTS21_1CoreServiceupdatedChangeSource', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1078, 3), )

    
    updatedChangeSource = property(__updatedChangeSource.value, __updatedChangeSource.set, None, None)

    _ElementMap.update({
        __updatedStatus.name() : __updatedStatus,
        __updatedEntryState.name() : __updatedEntryState,
        __updatedEffectiveDate.name() : __updatedEffectiveDate,
        __updatedChangeNotes.name() : __updatedChangeNotes,
        __updatedChangeSource.name() : __updatedChangeSource
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'UpdateChangeableMetadataRequest', UpdateChangeableMetadataRequest_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1051, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'status'), 'status', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_12_httpwww_omg_orgspecCTS21_1CoreServicestatus', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1053, 6), )

    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __status.name() : __status
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1058, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}entryState uses Python identifier entryState
    __entryState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entryState'), 'entryState', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_13_httpwww_omg_orgspecCTS21_1CoreServiceentryState', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1060, 6), )

    
    entryState = property(__entryState.value, __entryState.set, None, None)

    _ElementMap.update({
        __entryState.name() : __entryState
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1065, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}effectiveDate uses Python identifier effectiveDate
    __effectiveDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'effectiveDate'), 'effectiveDate', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_14_httpwww_omg_orgspecCTS21_1CoreServiceeffectiveDate', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1067, 6), )

    
    effectiveDate = property(__effectiveDate.value, __effectiveDate.set, None, None)

    _ElementMap.update({
        __effectiveDate.name() : __effectiveDate
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1072, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}changeNotes uses Python identifier changeNotes
    __changeNotes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'changeNotes'), 'changeNotes', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_15_httpwww_omg_orgspecCTS21_1CoreServicechangeNotes', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1074, 6), )

    
    changeNotes = property(__changeNotes.value, __changeNotes.set, None, None)

    _ElementMap.update({
        __changeNotes.name() : __changeNotes
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1079, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}changeSource uses Python identifier changeSource
    __changeSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'changeSource'), 'changeSource', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_16_httpwww_omg_orgspecCTS21_1CoreServicechangeSource', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1081, 6), )

    
    changeSource = property(__changeSource.value, __changeSource.set, None, None)

    _ElementMap.update({
        __changeSource.name() : __changeSource
    })
    _AttributeMap.update({
        
    })



# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateChangeSetMetadataRequest with content type ELEMENT_ONLY
class UpdateChangeSetMetadataRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateChangeSetMetadataRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UpdateChangeSetMetadataRequest')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1089, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedState uses Python identifier updatedState
    __updatedState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedState'), 'updatedState', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateChangeSetMetadataRequest__httpwww_omg_orgspecCTS21_1CoreServiceupdatedState', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1091, 3), )

    
    updatedState = property(__updatedState.value, __updatedState.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedCreator uses Python identifier updatedCreator
    __updatedCreator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedCreator'), 'updatedCreator', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateChangeSetMetadataRequest__httpwww_omg_orgspecCTS21_1CoreServiceupdatedCreator', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1098, 3), )

    
    updatedCreator = property(__updatedCreator.value, __updatedCreator.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedChangeInstructions uses Python identifier updatedChangeInstructions
    __updatedChangeInstructions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedChangeInstructions'), 'updatedChangeInstructions', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateChangeSetMetadataRequest__httpwww_omg_orgspecCTS21_1CoreServiceupdatedChangeInstructions', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1105, 3), )

    
    updatedChangeInstructions = property(__updatedChangeInstructions.value, __updatedChangeInstructions.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedOfficialEffectiveDate uses Python identifier updatedOfficialEffectiveDate
    __updatedOfficialEffectiveDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedOfficialEffectiveDate'), 'updatedOfficialEffectiveDate', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateChangeSetMetadataRequest__httpwww_omg_orgspecCTS21_1CoreServiceupdatedOfficialEffectiveDate', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1112, 3), )

    
    updatedOfficialEffectiveDate = property(__updatedOfficialEffectiveDate.value, __updatedOfficialEffectiveDate.set, None, None)

    _ElementMap.update({
        __updatedState.name() : __updatedState,
        __updatedCreator.name() : __updatedCreator,
        __updatedChangeInstructions.name() : __updatedChangeInstructions,
        __updatedOfficialEffectiveDate.name() : __updatedOfficialEffectiveDate
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'UpdateChangeSetMetadataRequest', UpdateChangeSetMetadataRequest_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1092, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'state'), 'state', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_17_httpwww_omg_orgspecCTS21_1CoreServicestate', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1094, 6), )

    
    state = property(__state.value, __state.set, None, None)

    _ElementMap.update({
        __state.name() : __state
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1099, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}creator uses Python identifier creator
    __creator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'creator'), 'creator', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_18_httpwww_omg_orgspecCTS21_1CoreServicecreator', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1101, 6), )

    
    creator = property(__creator.value, __creator.set, None, None)

    _ElementMap.update({
        __creator.name() : __creator
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1106, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}changeInstructions uses Python identifier changeInstructions
    __changeInstructions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'changeInstructions'), 'changeInstructions', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_19_httpwww_omg_orgspecCTS21_1CoreServicechangeInstructions', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1108, 6), )

    
    changeInstructions = property(__changeInstructions.value, __changeInstructions.set, None, None)

    _ElementMap.update({
        __changeInstructions.name() : __changeInstructions
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1113, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}officialEffectiveDate uses Python identifier officialEffectiveDate
    __officialEffectiveDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'officialEffectiveDate'), 'officialEffectiveDate', '__httpwww_omg_orgspecCTS21_1CoreService_CTD_ANON_20_httpwww_omg_orgspecCTS21_1CoreServiceofficialEffectiveDate', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1115, 6), )

    
    officialEffectiveDate = property(__officialEffectiveDate.value, __officialEffectiveDate.set, None, None)

    _ElementMap.update({
        __officialEffectiveDate.name() : __officialEffectiveDate
    })
    _AttributeMap.update({
        
    })



# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseMaintenanceService with content type ELEMENT_ONLY
class BaseMaintenanceService_ (BaseService_):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BaseMaintenanceService')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 304, 1)
    _ElementMap = BaseService_._ElementMap.copy()
    _AttributeMap = BaseService_._AttributeMap.copy()
    # Base type is BaseService_
    
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
Namespace.addCategoryObject('typeBinding', u'BaseMaintenanceService', BaseMaintenanceService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription with content type ELEMENT_ONLY
class UpdateResourceDescription_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UpdateResourceDescription')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 346, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedAdditionalDocumentation uses Python identifier updatedAdditionalDocumentation
    __updatedAdditionalDocumentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedAdditionalDocumentation'), 'updatedAdditionalDocumentation', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceDescription__httpwww_omg_orgspecCTS21_1CoreServiceupdatedAdditionalDocumentation', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 351, 3), )

    
    updatedAdditionalDocumentation = property(__updatedAdditionalDocumentation.value, __updatedAdditionalDocumentation.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedKeywords uses Python identifier updatedKeywords
    __updatedKeywords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedKeywords'), 'updatedKeywords', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceDescription__httpwww_omg_orgspecCTS21_1CoreServiceupdatedKeywords', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 358, 3), )

    
    updatedKeywords = property(__updatedKeywords.value, __updatedKeywords.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedSources uses Python identifier updatedSources
    __updatedSources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedSources'), 'updatedSources', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceDescription__httpwww_omg_orgspecCTS21_1CoreServiceupdatedSources', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 365, 3), )

    
    updatedSources = property(__updatedSources.value, __updatedSources.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedNotes uses Python identifier updatedNotes
    __updatedNotes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedNotes'), 'updatedNotes', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceDescription__httpwww_omg_orgspecCTS21_1CoreServiceupdatedNotes', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 372, 3), )

    
    updatedNotes = property(__updatedNotes.value, __updatedNotes.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedProperties uses Python identifier updatedProperties
    __updatedProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedProperties'), 'updatedProperties', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceDescription__httpwww_omg_orgspecCTS21_1CoreServiceupdatedProperties', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 379, 3), )

    
    updatedProperties = property(__updatedProperties.value, __updatedProperties.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedResourceSynopsis uses Python identifier updatedResourceSynopsis
    __updatedResourceSynopsis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceSynopsis'), 'updatedResourceSynopsis', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceDescription__httpwww_omg_orgspecCTS21_1CoreServiceupdatedResourceSynopsis', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 386, 3), )

    
    updatedResourceSynopsis = property(__updatedResourceSynopsis.value, __updatedResourceSynopsis.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedResourceTypes uses Python identifier updatedResourceTypes
    __updatedResourceTypes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceTypes'), 'updatedResourceTypes', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceDescription__httpwww_omg_orgspecCTS21_1CoreServiceupdatedResourceTypes', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 393, 3), )

    
    updatedResourceTypes = property(__updatedResourceTypes.value, __updatedResourceTypes.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedRights uses Python identifier updatedRights
    __updatedRights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedRights'), 'updatedRights', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceDescription__httpwww_omg_orgspecCTS21_1CoreServiceupdatedRights', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 400, 3), )

    
    updatedRights = property(__updatedRights.value, __updatedRights.set, None, None)

    
    # Attribute updatedFormalName uses Python identifier updatedFormalName
    __updatedFormalName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'updatedFormalName'), 'updatedFormalName', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceDescription__updatedFormalName', _ImportedBinding__nsgroup.String)
    __updatedFormalName._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 408, 2)
    __updatedFormalName._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 408, 2)
    
    updatedFormalName = property(__updatedFormalName.value, __updatedFormalName.set, None, None)

    _ElementMap.update({
        __updatedAdditionalDocumentation.name() : __updatedAdditionalDocumentation,
        __updatedKeywords.name() : __updatedKeywords,
        __updatedSources.name() : __updatedSources,
        __updatedNotes.name() : __updatedNotes,
        __updatedProperties.name() : __updatedProperties,
        __updatedResourceSynopsis.name() : __updatedResourceSynopsis,
        __updatedResourceTypes.name() : __updatedResourceTypes,
        __updatedRights.name() : __updatedRights
    })
    _AttributeMap.update({
        __updatedFormalName.name() : __updatedFormalName
    })
Namespace.addCategoryObject('typeBinding', u'UpdateResourceDescription', UpdateResourceDescription_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}HistoryService with content type ELEMENT_ONLY
class HistoryService_ (BaseService_):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HistoryService')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 446, 1)
    _ElementMap = BaseService_._ElementMap.copy()
    _AttributeMap = BaseService_._AttributeMap.copy()
    # Base type is BaseService_
    
    # Element serviceName ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceName) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceDescription ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceDescription) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceVersion ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceVersion) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceProvider ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceProvider) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element defaultFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}defaultFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedProfile ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedProfile) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element implementationType ({http://www.omg.org/spec/CTS2/1.1/CoreService}implementationType) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element knownNamespace ({http://www.omg.org/spec/CTS2/1.1/CoreService}knownNamespace) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}changeHistory uses Python identifier changeHistory
    __changeHistory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'changeHistory'), 'changeHistory', '__httpwww_omg_orgspecCTS21_1CoreService_HistoryService__httpwww_omg_orgspecCTS21_1CoreServicechangeHistory', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 453, 5), )

    
    changeHistory = property(__changeHistory.value, __changeHistory.set, None, None)

    
    # Attribute earliestChange uses Python identifier earliestChange
    __earliestChange = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'earliestChange'), 'earliestChange', '__httpwww_omg_orgspecCTS21_1CoreService_HistoryService__earliestChange', _ImportedBinding__nsgroup.DateAndTime, required=True)
    __earliestChange._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 455, 4)
    __earliestChange._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 455, 4)
    
    earliestChange = property(__earliestChange.value, __earliestChange.set, None, None)

    
    # Attribute latestChange uses Python identifier latestChange
    __latestChange = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'latestChange'), 'latestChange', '__httpwww_omg_orgspecCTS21_1CoreService_HistoryService__latestChange', _ImportedBinding__nsgroup.DateAndTime, required=True)
    __latestChange._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 456, 4)
    __latestChange._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 456, 4)
    
    latestChange = property(__latestChange.value, __latestChange.set, None, None)

    _ElementMap.update({
        __changeHistory.name() : __changeHistory
    })
    _AttributeMap.update({
        __earliestChange.name() : __earliestChange,
        __latestChange.name() : __latestChange
    })
Namespace.addCategoryObject('typeBinding', u'HistoryService', HistoryService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}ImportExportBase with content type ELEMENT_ONLY
class ImportExportBase_ (BaseService_):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ImportExportBase')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 522, 1)
    _ElementMap = BaseService_._ElementMap.copy()
    _AttributeMap = BaseService_._AttributeMap.copy()
    # Base type is BaseService_
    
    # Element serviceName ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceName) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceDescription ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceDescription) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceVersion ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceVersion) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceProvider ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceProvider) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element defaultFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}defaultFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedProfile ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedProfile) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element implementationType ({http://www.omg.org/spec/CTS2/1.1/CoreService}implementationType) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element knownNamespace ({http://www.omg.org/spec/CTS2/1.1/CoreService}knownNamespace) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}supportedSourceAndNotation uses Python identifier supportedSourceAndNotation
    __supportedSourceAndNotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'supportedSourceAndNotation'), 'supportedSourceAndNotation', '__httpwww_omg_orgspecCTS21_1CoreService_ImportExportBase__httpwww_omg_orgspecCTS21_1CoreServicesupportedSourceAndNotation', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 529, 5), )

    
    supportedSourceAndNotation = property(__supportedSourceAndNotation.value, __supportedSourceAndNotation.set, None, None)

    _ElementMap.update({
        __supportedSourceAndNotation.name() : __supportedSourceAndNotation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ImportExportBase', ImportExportBase_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}LogEntry with content type ELEMENT_ONLY
class LogEntry_ (pyxb.binding.basis.complexTypeDefinition):
    """An entry in sequence of messages related to a process or task"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogEntry')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 635, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}logLevel uses Python identifier logLevel
    __logLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'logLevel'), 'logLevel', '__httpwww_omg_orgspecCTS21_1CoreService_LogEntry__httpwww_omg_orgspecCTS21_1CoreServicelogLevel', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 641, 3), )

    
    logLevel = property(__logLevel.value, __logLevel.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}messageID uses Python identifier messageID
    __messageID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'messageID'), 'messageID', '__httpwww_omg_orgspecCTS21_1CoreService_LogEntry__httpwww_omg_orgspecCTS21_1CoreServicemessageID', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 643, 3), )

    
    messageID = property(__messageID.value, __messageID.set, None, u'An external identifier that uniquely names the message.  is present to enable automated processing of log entries where appropriate. The significance and use of  is not addressed within the context of the CTS specification')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}processUID uses Python identifier processUID
    __processUID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'processUID'), 'processUID', '__httpwww_omg_orgspecCTS21_1CoreService_LogEntry__httpwww_omg_orgspecCTS21_1CoreServiceprocessUID', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 648, 3), )

    
    processUID = property(__processUID.value, __processUID.set, None, None)

    
    # Attribute entryTime uses Python identifier entryTime
    __entryTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'entryTime'), 'entryTime', '__httpwww_omg_orgspecCTS21_1CoreService_LogEntry__entryTime', _ImportedBinding__nsgroup.DateAndTime, required=True)
    __entryTime._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 651, 2)
    __entryTime._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 651, 2)
    
    entryTime = property(__entryTime.value, __entryTime.set, None, u'The time the entry was made')

    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpwww_omg_orgspecCTS21_1CoreService_LogEntry__message', _ImportedBinding__nsgroup.String, required=True)
    __message._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 656, 2)
    __message._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 656, 2)
    
    message = property(__message.value, __message.set, None, u'The text of the message')

    
    # Attribute programName uses Python identifier programName
    __programName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'programName'), 'programName', '__httpwww_omg_orgspecCTS21_1CoreService_LogEntry__programName', _ImportedBinding__nsgroup.String)
    __programName._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 661, 2)
    __programName._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 661, 2)
    
    programName = property(__programName.value, __programName.set, None, u'The name of the program or application that created the entry')

    _ElementMap.update({
        __logLevel.name() : __logLevel,
        __messageID.name() : __messageID,
        __processUID.name() : __processUID
    })
    _AttributeMap.update({
        __entryTime.name() : __entryTime,
        __message.name() : __message,
        __programName.name() : __programName
    })
Namespace.addCategoryObject('typeBinding', u'LogEntry', LogEntry_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus with content type ELEMENT_ONLY
class ProcessStatus_ (pyxb.binding.basis.complexTypeDefinition):
    """The state of a running or completed load or export process."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ProcessStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 701, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}log uses Python identifier log
    __log = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'log'), 'log', '__httpwww_omg_orgspecCTS21_1CoreService_ProcessStatus__httpwww_omg_orgspecCTS21_1CoreServicelog', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 707, 3), )

    
    log = property(__log.value, __log.set, None, u'The set of log records created by the process')

    
    # Attribute completionMessage uses Python identifier completionMessage
    __completionMessage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'completionMessage'), 'completionMessage', '__httpwww_omg_orgspecCTS21_1CoreService_ProcessStatus__completionMessage', _ImportedBinding__nsgroup.String)
    __completionMessage._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 714, 2)
    __completionMessage._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 714, 2)
    
    completionMessage = property(__completionMessage.value, __completionMessage.set, None, u'A message summarizing the final results of the process')

    
    # Attribute endTime uses Python identifier endTime
    __endTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'endTime'), 'endTime', '__httpwww_omg_orgspecCTS21_1CoreService_ProcessStatus__endTime', _ImportedBinding__nsgroup.DateAndTime)
    __endTime._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 719, 2)
    __endTime._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 719, 2)
    
    endTime = property(__endTime.value, __endTime.set, None, u"The date and time that the process finished execution if it isn't still running")

    
    # Attribute numErrors uses Python identifier numErrors
    __numErrors = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numErrors'), 'numErrors', '__httpwww_omg_orgspecCTS21_1CoreService_ProcessStatus__numErrors', _ImportedBinding__nsgroup.NaturalNumber, required=True)
    __numErrors._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 724, 2)
    __numErrors._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 724, 2)
    
    numErrors = property(__numErrors.value, __numErrors.set, None, u'The number of errors ( =  or ) encountered by the process so far')

    
    # Attribute numWarnings uses Python identifier numWarnings
    __numWarnings = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numWarnings'), 'numWarnings', '__httpwww_omg_orgspecCTS21_1CoreService_ProcessStatus__numWarnings', _ImportedBinding__nsgroup.NaturalNumber, required=True)
    __numWarnings._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 729, 2)
    __numWarnings._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 729, 2)
    
    numWarnings = property(__numWarnings.value, __numWarnings.set, None, u'The number of warnings () encountered by the process so far')

    
    # Attribute startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'startTime'), 'startTime', '__httpwww_omg_orgspecCTS21_1CoreService_ProcessStatus__startTime', _ImportedBinding__nsgroup.DateAndTime, required=True)
    __startTime._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 734, 2)
    __startTime._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 734, 2)
    
    startTime = property(__startTime.value, __startTime.set, None, u'The date and time that the process began execution')

    _ElementMap.update({
        __log.name() : __log
    })
    _AttributeMap.update({
        __completionMessage.name() : __completionMessage,
        __endTime.name() : __endTime,
        __numErrors.name() : __numErrors,
        __numWarnings.name() : __numWarnings,
        __startTime.name() : __startTime
    })
Namespace.addCategoryObject('typeBinding', u'ProcessStatus', ProcessStatus_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseQueryService with content type ELEMENT_ONLY
class BaseQueryService_ (BaseService_):
    """ represents the set of attributes and operations that are common across all query service implementations. It includes generic directory manipulation functions as well as enumerations of the permissible values for query parameters in the given service context."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BaseQueryService')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 742, 1)
    _ElementMap = BaseService_._ElementMap.copy()
    _AttributeMap = BaseService_._AttributeMap.copy()
    # Base type is BaseService_
    
    # Element serviceName ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceName) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceDescription ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceDescription) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceVersion ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceVersion) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceProvider ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceProvider) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element defaultFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}defaultFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedProfile ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedProfile) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element implementationType ({http://www.omg.org/spec/CTS2/1.1/CoreService}implementationType) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element knownNamespace ({http://www.omg.org/spec/CTS2/1.1/CoreService}knownNamespace) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}knownProperty uses Python identifier knownProperty
    __knownProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'knownProperty'), 'knownProperty', '__httpwww_omg_orgspecCTS21_1CoreService_BaseQueryService__httpwww_omg_orgspecCTS21_1CoreServiceknownProperty', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5), )

    
    knownProperty = property(__knownProperty.value, __knownProperty.set, None, u'The set of properties that are used in one or more instances of the resource represented by this service. This list includes all properties that are can be used in queries in this service, independent of the entryState or temporal state of the resource(s) being searched. ')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}supportedMatchAlgorithm uses Python identifier supportedMatchAlgorithm
    __supportedMatchAlgorithm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'supportedMatchAlgorithm'), 'supportedMatchAlgorithm', '__httpwww_omg_orgspecCTS21_1CoreService_BaseQueryService__httpwww_omg_orgspecCTS21_1CoreServicesupportedMatchAlgorithm', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 754, 5), )

    
    supportedMatchAlgorithm = property(__supportedMatchAlgorithm.value, __supportedMatchAlgorithm.set, None, u'The match algorithms that can be used in filters for this service instance.')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}supportedModelAttribute uses Python identifier supportedModelAttribute
    __supportedModelAttribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'supportedModelAttribute'), 'supportedModelAttribute', '__httpwww_omg_orgspecCTS21_1CoreService_BaseQueryService__httpwww_omg_orgspecCTS21_1CoreServicesupportedModelAttribute', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 759, 5), )

    
    supportedModelAttribute = property(__supportedModelAttribute.value, __supportedModelAttribute.set, None, u'The set of model attributes that can be referenced in filter instances for the given service implementation.')

    _ElementMap.update({
        __knownProperty.name() : __knownProperty,
        __supportedMatchAlgorithm.name() : __supportedMatchAlgorithm,
        __supportedModelAttribute.name() : __supportedModelAttribute
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'BaseQueryService', BaseQueryService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseReadService with content type ELEMENT_ONLY
class BaseReadService_ (BaseService_):
    """The common metadata about a CTS service instance that is shared among all service instances."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BaseReadService')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 770, 1)
    _ElementMap = BaseService_._ElementMap.copy()
    _AttributeMap = BaseService_._AttributeMap.copy()
    # Base type is BaseService_
    
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
Namespace.addCategoryObject('typeBinding', u'BaseReadService', BaseReadService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}ChangeSetEntry with content type ELEMENT_ONLY
class ChangeSetEntry (pyxb.binding.basis.complexTypeDefinition):
    """A change set URI along with the date and time it was applied to a particular service implementation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ChangeSetEntry')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 781, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}applicationDate uses Python identifier applicationDate
    __applicationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'applicationDate'), 'applicationDate', '__httpwww_omg_orgspecCTS21_1CoreService_ChangeSetEntry_httpwww_omg_orgspecCTS21_1CoreServiceapplicationDate', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 786, 3), )

    
    applicationDate = property(__applicationDate.value, __applicationDate.set, None, u'The date and time that a change set was applied to a given service instance')

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}changeSetURI uses Python identifier changeSetURI
    __changeSetURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'changeSetURI'), 'changeSetURI', '__httpwww_omg_orgspecCTS21_1CoreService_ChangeSetEntry_httpwww_omg_orgspecCTS21_1CoreServicechangeSetURI', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 791, 3), )

    
    changeSetURI = property(__changeSetURI.value, __changeSetURI.set, None, u'The URI of the change set that was applied')

    
    # Attribute entryOrder uses Python identifier entryOrder
    __entryOrder = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'entryOrder'), 'entryOrder', '__httpwww_omg_orgspecCTS21_1CoreService_ChangeSetEntry_entryOrder', _ImportedBinding__nsgroup.NaturalNumber, required=True)
    __entryOrder._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 797, 2)
    __entryOrder._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 797, 2)
    
    entryOrder = property(__entryOrder.value, __entryOrder.set, None, None)

    _ElementMap.update({
        __applicationDate.name() : __applicationDate,
        __changeSetURI.name() : __changeSetURI
    })
    _AttributeMap.update({
        __entryOrder.name() : __entryOrder
    })
Namespace.addCategoryObject('typeBinding', u'ChangeSetEntry', ChangeSetEntry)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseUpdateService with content type ELEMENT_ONLY
class BaseUpdateService_ (BaseService_):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BaseUpdateService')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 808, 1)
    _ElementMap = BaseService_._ElementMap.copy()
    _AttributeMap = BaseService_._AttributeMap.copy()
    # Base type is BaseService_
    
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
Namespace.addCategoryObject('typeBinding', u'BaseUpdateService', BaseUpdateService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}NameOrURI with content type EMPTY
class NameOrURI_ (pyxb.binding.basis.complexTypeDefinition):
    """Carries either a local identifier () or a URI () that references a resource in the service.  is only used as an input parameter and its type is always defined by the usage context. Note that service calls that use the  option may not be portable across implementations, as there is no guarantee that any two CTS service implementations will use the same local identifiers for the same
				resources."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NameOrURI')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 853, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_omg_orgspecCTS21_1CoreService_NameOrURI__name', _ImportedBinding__nsgroup.String)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 858, 2)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 858, 2)
    
    name = property(__name.value, __name.set, None, u'a  that references a unique resource within the context of the service implementation and type of resource being accessed')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpwww_omg_orgspecCTS21_1CoreService_NameOrURI__uri', _ImportedBinding__nsgroup.String)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 863, 2)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 863, 2)
    
    uri = property(__uri.value, __uri.set, None, u'an  that references a unique resource within the context of the resource type')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'NameOrURI', NameOrURI_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}URIResolutionService with content type EMPTY
class URIResolutionService_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'URIResolutionService')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1027, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute lastUpdated uses Python identifier lastUpdated
    __lastUpdated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lastUpdated'), 'lastUpdated', '__httpwww_omg_orgspecCTS21_1CoreService_URIResolutionService__lastUpdated', _ImportedBinding__nsgroup.DateAndTime, required=True)
    __lastUpdated._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1031, 2)
    __lastUpdated._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1031, 2)
    
    lastUpdated = property(__lastUpdated.value, __lastUpdated.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lastUpdated.name() : __lastUpdated
    })
Namespace.addCategoryObject('typeBinding', u'URIResolutionService', URIResolutionService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateAbstractResourceDescription with content type ELEMENT_ONLY
class UpdateAbstractResourceDescription_ (UpdateResourceDescription_):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UpdateAbstractResourceDescription')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 318, 1)
    _ElementMap = UpdateResourceDescription_._ElementMap.copy()
    _AttributeMap = UpdateResourceDescription_._AttributeMap.copy()
    # Base type is UpdateResourceDescription_
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedReleaseDocumentation uses Python identifier updatedReleaseDocumentation
    __updatedReleaseDocumentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedReleaseDocumentation'), 'updatedReleaseDocumentation', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateAbstractResourceDescription__httpwww_omg_orgspecCTS21_1CoreServiceupdatedReleaseDocumentation', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 325, 5), )

    
    updatedReleaseDocumentation = property(__updatedReleaseDocumentation.value, __updatedReleaseDocumentation.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedReleaseFormats uses Python identifier updatedReleaseFormats
    __updatedReleaseFormats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedReleaseFormats'), 'updatedReleaseFormats', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateAbstractResourceDescription__httpwww_omg_orgspecCTS21_1CoreServiceupdatedReleaseFormats', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 332, 5), )

    
    updatedReleaseFormats = property(__updatedReleaseFormats.value, __updatedReleaseFormats.set, None, None)

    
    # Element updatedAdditionalDocumentation ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedAdditionalDocumentation) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedKeywords ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedKeywords) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedSources ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedSources) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedNotes ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedNotes) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedProperties ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedProperties) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedResourceSynopsis ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedResourceSynopsis) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedResourceTypes ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedResourceTypes) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedRights ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedRights) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Attribute updatedFormalName inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    _ElementMap.update({
        __updatedReleaseDocumentation.name() : __updatedReleaseDocumentation,
        __updatedReleaseFormats.name() : __updatedReleaseFormats
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'UpdateAbstractResourceDescription', UpdateAbstractResourceDescription_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceVersionDescription with content type ELEMENT_ONLY
class UpdateResourceVersionDescription_ (UpdateResourceDescription_):
    """The set of attributes that can be changed whenever an instance of a  is updated."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UpdateResourceVersionDescription')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 413, 1)
    _ElementMap = UpdateResourceDescription_._ElementMap.copy()
    _AttributeMap = UpdateResourceDescription_._AttributeMap.copy()
    # Base type is UpdateResourceDescription_
    
    # Element updatedAdditionalDocumentation ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedAdditionalDocumentation) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedKeywords ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedKeywords) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedSources ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedSources) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedNotes ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedNotes) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedProperties ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedProperties) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedResourceSynopsis ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedResourceSynopsis) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedResourceTypes ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedResourceTypes) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element updatedRights ({http://www.omg.org/spec/CTS2/1.1/CoreService}updatedRights) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedPredecessor uses Python identifier updatedPredecessor
    __updatedPredecessor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedPredecessor'), 'updatedPredecessor', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceVersionDescription__httpwww_omg_orgspecCTS21_1CoreServiceupdatedPredecessor', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 420, 5), )

    
    updatedPredecessor = property(__updatedPredecessor.value, __updatedPredecessor.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}updatedSourceAndNotation uses Python identifier updatedSourceAndNotation
    __updatedSourceAndNotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'updatedSourceAndNotation'), 'updatedSourceAndNotation', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceVersionDescription__httpwww_omg_orgspecCTS21_1CoreServiceupdatedSourceAndNotation', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 427, 5), )

    
    updatedSourceAndNotation = property(__updatedSourceAndNotation.value, __updatedSourceAndNotation.set, None, None)

    
    # Attribute updatedFormalName inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}UpdateResourceDescription
    
    # Attribute updatedState uses Python identifier updatedState
    __updatedState = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'updatedState'), 'updatedState', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceVersionDescription__updatedState', _ImportedBinding__nsgroup.FinalizableState)
    __updatedState._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 435, 4)
    __updatedState._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 435, 4)
    
    updatedState = property(__updatedState.value, __updatedState.set, None, None)

    
    # Attribute updatedOfficialActivationDate uses Python identifier updatedOfficialActivationDate
    __updatedOfficialActivationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'updatedOfficialActivationDate'), 'updatedOfficialActivationDate', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceVersionDescription__updatedOfficialActivationDate', _ImportedBinding__nsgroup.DateAndTime)
    __updatedOfficialActivationDate._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 436, 4)
    __updatedOfficialActivationDate._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 436, 4)
    
    updatedOfficialActivationDate = property(__updatedOfficialActivationDate.value, __updatedOfficialActivationDate.set, None, None)

    
    # Attribute updatedOfficialReleaseDate uses Python identifier updatedOfficialReleaseDate
    __updatedOfficialReleaseDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'updatedOfficialReleaseDate'), 'updatedOfficialReleaseDate', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceVersionDescription__updatedOfficialReleaseDate', _ImportedBinding__nsgroup.DateAndTime)
    __updatedOfficialReleaseDate._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 437, 4)
    __updatedOfficialReleaseDate._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 437, 4)
    
    updatedOfficialReleaseDate = property(__updatedOfficialReleaseDate.value, __updatedOfficialReleaseDate.set, None, None)

    
    # Attribute updatedOfficialResourceVersionId uses Python identifier updatedOfficialResourceVersionId
    __updatedOfficialResourceVersionId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'updatedOfficialResourceVersionId'), 'updatedOfficialResourceVersionId', '__httpwww_omg_orgspecCTS21_1CoreService_UpdateResourceVersionDescription__updatedOfficialResourceVersionId', _ImportedBinding__nsgroup.DateAndTime)
    __updatedOfficialResourceVersionId._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 438, 4)
    __updatedOfficialResourceVersionId._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 438, 4)
    
    updatedOfficialResourceVersionId = property(__updatedOfficialResourceVersionId.value, __updatedOfficialResourceVersionId.set, None, None)

    _ElementMap.update({
        __updatedPredecessor.name() : __updatedPredecessor,
        __updatedSourceAndNotation.name() : __updatedSourceAndNotation
    })
    _AttributeMap.update({
        __updatedState.name() : __updatedState,
        __updatedOfficialActivationDate.name() : __updatedOfficialActivationDate,
        __updatedOfficialReleaseDate.name() : __updatedOfficialReleaseDate,
        __updatedOfficialResourceVersionId.name() : __updatedOfficialResourceVersionId
    })
Namespace.addCategoryObject('typeBinding', u'UpdateResourceVersionDescription', UpdateResourceVersionDescription_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseExportService with content type ELEMENT_ONLY
class BaseExportService_ (ImportExportBase_):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BaseExportService')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 463, 1)
    _ElementMap = ImportExportBase_._ElementMap.copy()
    _AttributeMap = ImportExportBase_._AttributeMap.copy()
    # Base type is ImportExportBase_
    
    # Element serviceName ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceName) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceDescription ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceDescription) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceVersion ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceVersion) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceProvider ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceProvider) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element defaultFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}defaultFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedProfile ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedProfile) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element implementationType ({http://www.omg.org/spec/CTS2/1.1/CoreService}implementationType) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element knownNamespace ({http://www.omg.org/spec/CTS2/1.1/CoreService}knownNamespace) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedSourceAndNotation ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedSourceAndNotation) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ImportExportBase
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'BaseExportService', BaseExportService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}ExportStatus with content type ELEMENT_ONLY
class ExportStatus_ (ProcessStatus_):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExportStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 474, 1)
    _ElementMap = ProcessStatus_._ElementMap.copy()
    _AttributeMap = ProcessStatus_._AttributeMap.copy()
    # Base type is ProcessStatus_
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}errorHandling uses Python identifier errorHandling
    __errorHandling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'errorHandling'), 'errorHandling', '__httpwww_omg_orgspecCTS21_1CoreService_ExportStatus__httpwww_omg_orgspecCTS21_1CoreServiceerrorHandling', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 482, 5), )

    
    errorHandling = property(__errorHandling.value, __errorHandling.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}exportedIRIs uses Python identifier exportedIRIs
    __exportedIRIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'exportedIRIs'), 'exportedIRIs', '__httpwww_omg_orgspecCTS21_1CoreService_ExportStatus__httpwww_omg_orgspecCTS21_1CoreServiceexportedIRIs', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 483, 5), )

    
    exportedIRIs = property(__exportedIRIs.value, __exportedIRIs.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}overwriteRule uses Python identifier overwriteRule
    __overwriteRule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'overwriteRule'), 'overwriteRule', '__httpwww_omg_orgspecCTS21_1CoreService_ExportStatus__httpwww_omg_orgspecCTS21_1CoreServiceoverwriteRule', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 484, 5), )

    
    overwriteRule = property(__overwriteRule.value, __overwriteRule.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}resourcesToExport uses Python identifier resourcesToExport
    __resourcesToExport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'resourcesToExport'), 'resourcesToExport', '__httpwww_omg_orgspecCTS21_1CoreService_ExportStatus__httpwww_omg_orgspecCTS21_1CoreServiceresourcesToExport', True, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 485, 5), )

    
    resourcesToExport = property(__resourcesToExport.value, __resourcesToExport.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}synchronicity uses Python identifier synchronicity
    __synchronicity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'synchronicity'), 'synchronicity', '__httpwww_omg_orgspecCTS21_1CoreService_ExportStatus__httpwww_omg_orgspecCTS21_1CoreServicesynchronicity', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 486, 5), )

    
    synchronicity = property(__synchronicity.value, __synchronicity.set, None, None)

    
    # Element log ({http://www.omg.org/spec/CTS2/1.1/CoreService}log) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus
    
    # Attribute destination uses Python identifier destination
    __destination = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'destination'), 'destination', '__httpwww_omg_orgspecCTS21_1CoreService_ExportStatus__destination', _ImportedBinding__nsgroup.URI, required=True)
    __destination._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 488, 4)
    __destination._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 488, 4)
    
    destination = property(__destination.value, __destination.set, None, u'The export destination')

    
    # Attribute numElementsExported uses Python identifier numElementsExported
    __numElementsExported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numElementsExported'), 'numElementsExported', '__httpwww_omg_orgspecCTS21_1CoreService_ExportStatus__numElementsExported', _ImportedBinding__nsgroup.NaturalNumber, required=True)
    __numElementsExported._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 493, 4)
    __numElementsExported._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 493, 4)
    
    numElementsExported = property(__numElementsExported.value, __numElementsExported.set, None, u'The number of elements that have been exported so far')

    
    # Attribute completionMessage inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus
    
    # Attribute endTime inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus
    
    # Attribute numErrors inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus
    
    # Attribute numWarnings inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus
    
    # Attribute startTime inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus
    _ElementMap.update({
        __errorHandling.name() : __errorHandling,
        __exportedIRIs.name() : __exportedIRIs,
        __overwriteRule.name() : __overwriteRule,
        __resourcesToExport.name() : __resourcesToExport,
        __synchronicity.name() : __synchronicity
    })
    _AttributeMap.update({
        __destination.name() : __destination,
        __numElementsExported.name() : __numElementsExported
    })
Namespace.addCategoryObject('typeBinding', u'ExportStatus', ExportStatus_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseImportService with content type ELEMENT_ONLY
class BaseImportService_ (ImportExportBase_):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BaseImportService')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 591, 1)
    _ElementMap = ImportExportBase_._ElementMap.copy()
    _AttributeMap = ImportExportBase_._AttributeMap.copy()
    # Base type is ImportExportBase_
    
    # Element serviceName ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceName) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceDescription ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceDescription) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceVersion ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceVersion) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element serviceProvider ({http://www.omg.org/spec/CTS2/1.1/CoreService}serviceProvider) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element defaultFormat ({http://www.omg.org/spec/CTS2/1.1/CoreService}defaultFormat) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedProfile ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedProfile) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element implementationType ({http://www.omg.org/spec/CTS2/1.1/CoreService}implementationType) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element knownNamespace ({http://www.omg.org/spec/CTS2/1.1/CoreService}knownNamespace) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}BaseService
    
    # Element supportedSourceAndNotation ({http://www.omg.org/spec/CTS2/1.1/CoreService}supportedSourceAndNotation) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ImportExportBase
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'BaseImportService', BaseImportService_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}FunctionalProfileEntry with content type SIMPLE
class FunctionalProfileEntry (pyxb.binding.basis.complexTypeDefinition):
    """The combination of a  and a link to the service description that describes the function/structure"""
    _TypeDefinition = FunctionalProfile
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FunctionalProfileEntry')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 193, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is FunctionalProfile
    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'href'), 'href', '__httpwww_omg_orgspecCTS21_1CoreService_FunctionalProfileEntry_href', _ImportedBinding__nsgroup.ServiceURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 200, 4)
    __href._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 200, 4)
    
    href = property(__href.value, __href.set, None, u'A link to the service description for this particular function. The href must reference an instance of ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href
    })
Namespace.addCategoryObject('typeBinding', u'FunctionalProfileEntry', FunctionalProfileEntry)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}ImportStatus with content type ELEMENT_ONLY
class ImportStatus_ (ProcessStatus_):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ImportStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 602, 1)
    _ElementMap = ProcessStatus_._ElementMap.copy()
    _AttributeMap = ProcessStatus_._AttributeMap.copy()
    # Base type is ProcessStatus_
    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}languageAndSyntax uses Python identifier languageAndSyntax
    __languageAndSyntax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'languageAndSyntax'), 'languageAndSyntax', '__httpwww_omg_orgspecCTS21_1CoreService_ImportStatus__httpwww_omg_orgspecCTS21_1CoreServicelanguageAndSyntax', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 609, 5), )

    
    languageAndSyntax = property(__languageAndSyntax.value, __languageAndSyntax.set, None, None)

    
    # Element {http://www.omg.org/spec/CTS2/1.1/CoreService}validation uses Python identifier validation
    __validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'validation'), 'validation', '__httpwww_omg_orgspecCTS21_1CoreService_ImportStatus__httpwww_omg_orgspecCTS21_1CoreServicevalidation', False, pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 610, 5), )

    
    validation = property(__validation.value, __validation.set, None, None)

    
    # Element log ({http://www.omg.org/spec/CTS2/1.1/CoreService}log) inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus
    
    # Attribute metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'metadata'), 'metadata', '__httpwww_omg_orgspecCTS21_1CoreService_ImportStatus__metadata', _ImportedBinding__nsgroup.URI)
    __metadata._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 612, 4)
    __metadata._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 612, 4)
    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Attribute source uses Python identifier source
    __source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'source'), 'source', '__httpwww_omg_orgspecCTS21_1CoreService_ImportStatus__source', _ImportedBinding__nsgroup.URI, required=True)
    __source._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 613, 4)
    __source._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 613, 4)
    
    source = property(__source.value, __source.set, None, None)

    
    # Attribute loadedURI uses Python identifier loadedURI
    __loadedURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadedURI'), 'loadedURI', '__httpwww_omg_orgspecCTS21_1CoreService_ImportStatus__loadedURI', _ImportedBinding__nsgroup.RenderingURI)
    __loadedURI._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 614, 4)
    __loadedURI._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 614, 4)
    
    loadedURI = property(__loadedURI.value, __loadedURI.set, None, None)

    
    # Attribute synchronicity uses Python identifier synchronicity
    __synchronicity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'synchronicity'), 'synchronicity', '__httpwww_omg_orgspecCTS21_1CoreService_ImportStatus__synchronicity', SyncOrAsync, required=True)
    __synchronicity._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 615, 4)
    __synchronicity._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 615, 4)
    
    synchronicity = property(__synchronicity.value, __synchronicity.set, None, u'The CTS2 URI(s) of the resulting resources')

    
    # Attribute numElementsImported uses Python identifier numElementsImported
    __numElementsImported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numElementsImported'), 'numElementsImported', '__httpwww_omg_orgspecCTS21_1CoreService_ImportStatus__numElementsImported', pyxb.binding.datatypes.string, required=True)
    __numElementsImported._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 620, 4)
    __numElementsImported._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 620, 4)
    
    numElementsImported = property(__numElementsImported.value, __numElementsImported.set, None, None)

    
    # Attribute completionMessage inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus
    
    # Attribute endTime inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus
    
    # Attribute numErrors inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus
    
    # Attribute numWarnings inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus
    
    # Attribute startTime inherited from {http://www.omg.org/spec/CTS2/1.1/CoreService}ProcessStatus
    _ElementMap.update({
        __languageAndSyntax.name() : __languageAndSyntax,
        __validation.name() : __validation
    })
    _AttributeMap.update({
        __metadata.name() : __metadata,
        __source.name() : __source,
        __loadedURI.name() : __loadedURI,
        __synchronicity.name() : __synchronicity,
        __numElementsImported.name() : __numElementsImported
    })
Namespace.addCategoryObject('typeBinding', u'ImportStatus', ImportStatus_)


# Complex type {http://www.omg.org/spec/CTS2/1.1/CoreService}DocumentedNamespaceReference with content type SIMPLE
class DocumentedNamespaceReference (_ImportedBinding__nsgroup.NamespaceReference):
    """
			A namespace reference that may include additional documentation about the scope of the namespace.
			"""
    _TypeDefinition = _ImportedBinding__nsgroup.String
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DocumentedNamespaceReference')
    _XSDLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 228, 1)
    _ElementMap = _ImportedBinding__nsgroup.NamespaceReference._ElementMap.copy()
    _AttributeMap = _ImportedBinding__nsgroup.NamespaceReference._AttributeMap.copy()
    # Base type is _ImportedBinding__nsgroup.NamespaceReference
    
    # Attribute uri inherited from {http://www.omg.org/spec/CTS2/1.1/Core}NameAndMeaningReference
    
    # Attribute href inherited from {http://www.omg.org/spec/CTS2/1.1/Core}NameAndMeaningReference
    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpwww_omg_orgspecCTS21_1CoreService_DocumentedNamespaceReference_description', _ImportedBinding__nsgroup.String)
    __description._DeclarationLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 236, 4)
    __description._UseLocation = pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 236, 4)
    
    description = property(__description.value, __description.set, None, u'\n\t\t\t\t\t\tDocumentation about the scope and origin of the namespace.\n\t\t\t\t\t\t')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __description.name() : __description
    })
Namespace.addCategoryObject('typeBinding', u'DocumentedNamespaceReference', DocumentedNamespaceReference)


Query = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Query'), Query_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 5, 1))
Namespace.addCategoryObject('elementBinding', Query.name().localName(), Query)

BaseService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BaseService'), BaseService_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 247, 1))
Namespace.addCategoryObject('elementBinding', BaseService.name().localName(), BaseService)

LogEntries = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LogEntries'), LogEntries_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 625, 1))
Namespace.addCategoryObject('elementBinding', LogEntries.name().localName(), LogEntries)

EntityNameOrURI = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EntityNameOrURI'), EntityNameOrURI_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 822, 1))
Namespace.addCategoryObject('elementBinding', EntityNameOrURI.name().localName(), EntityNameOrURI)

EntityNameOrURIList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EntityNameOrURIList'), EntityNameOrURIList_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 842, 1))
Namespace.addCategoryObject('elementBinding', EntityNameOrURIList.name().localName(), EntityNameOrURIList)

NameOrURIList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NameOrURIList'), NameOrURIList_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 870, 1))
Namespace.addCategoryObject('elementBinding', NameOrURIList.name().localName(), NameOrURIList)

QueryControl = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QueryControl'), QueryControl_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 899, 1))
Namespace.addCategoryObject('elementBinding', QueryControl.name().localName(), QueryControl)

ReadContext = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReadContext'), ReadContext_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 948, 1))
Namespace.addCategoryObject('elementBinding', ReadContext.name().localName(), ReadContext)

SortCriteria = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SortCriteria'), SortCriteria_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 978, 1))
Namespace.addCategoryObject('elementBinding', SortCriteria.name().localName(), SortCriteria)

SortCriterion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SortCriterion'), SortCriterion_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 988, 1))
Namespace.addCategoryObject('elementBinding', SortCriterion.name().localName(), SortCriterion)

VersionResolutionService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VersionResolutionService'), VersionResolutionService_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1034, 1))
Namespace.addCategoryObject('elementBinding', VersionResolutionService.name().localName(), VersionResolutionService)

UpdateChangeableMetadataRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UpdateChangeableMetadataRequest'), UpdateChangeableMetadataRequest_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1047, 1))
Namespace.addCategoryObject('elementBinding', UpdateChangeableMetadataRequest.name().localName(), UpdateChangeableMetadataRequest)

UpdateChangeSetMetadataRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UpdateChangeSetMetadataRequest'), UpdateChangeSetMetadataRequest_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1088, 1))
Namespace.addCategoryObject('elementBinding', UpdateChangeSetMetadataRequest.name().localName(), UpdateChangeSetMetadataRequest)

BaseMaintenanceService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BaseMaintenanceService'), BaseMaintenanceService_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 303, 1))
Namespace.addCategoryObject('elementBinding', BaseMaintenanceService.name().localName(), BaseMaintenanceService)

UpdateResourceDescription = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UpdateResourceDescription'), UpdateResourceDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 345, 1))
Namespace.addCategoryObject('elementBinding', UpdateResourceDescription.name().localName(), UpdateResourceDescription)

HistoryService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HistoryService'), HistoryService_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 445, 1))
Namespace.addCategoryObject('elementBinding', HistoryService.name().localName(), HistoryService)

ImportExportBase = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImportExportBase'), ImportExportBase_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 521, 1))
Namespace.addCategoryObject('elementBinding', ImportExportBase.name().localName(), ImportExportBase)

LogEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LogEntry'), LogEntry_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 634, 1))
Namespace.addCategoryObject('elementBinding', LogEntry.name().localName(), LogEntry)

ProcessStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessStatus'), ProcessStatus_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 700, 1))
Namespace.addCategoryObject('elementBinding', ProcessStatus.name().localName(), ProcessStatus)

BaseQueryService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BaseQueryService'), BaseQueryService_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 741, 1))
Namespace.addCategoryObject('elementBinding', BaseQueryService.name().localName(), BaseQueryService)

BaseReadService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BaseReadService'), BaseReadService_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 769, 1))
Namespace.addCategoryObject('elementBinding', BaseReadService.name().localName(), BaseReadService)

BaseUpdateService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BaseUpdateService'), BaseUpdateService_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 807, 1))
Namespace.addCategoryObject('elementBinding', BaseUpdateService.name().localName(), BaseUpdateService)

NameOrURI = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NameOrURI'), NameOrURI_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 852, 1))
Namespace.addCategoryObject('elementBinding', NameOrURI.name().localName(), NameOrURI)

URIResolutionService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URIResolutionService'), URIResolutionService_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1026, 1))
Namespace.addCategoryObject('elementBinding', URIResolutionService.name().localName(), URIResolutionService)

UpdateAbstractResourceDescription = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UpdateAbstractResourceDescription'), UpdateAbstractResourceDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 317, 1))
Namespace.addCategoryObject('elementBinding', UpdateAbstractResourceDescription.name().localName(), UpdateAbstractResourceDescription)

UpdateResourceVersionDescription = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UpdateResourceVersionDescription'), UpdateResourceVersionDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 412, 1))
Namespace.addCategoryObject('elementBinding', UpdateResourceVersionDescription.name().localName(), UpdateResourceVersionDescription)

BaseExportService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BaseExportService'), BaseExportService_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 462, 1))
Namespace.addCategoryObject('elementBinding', BaseExportService.name().localName(), BaseExportService)

ExportStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExportStatus'), ExportStatus_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 473, 1))
Namespace.addCategoryObject('elementBinding', ExportStatus.name().localName(), ExportStatus)

BaseImportService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BaseImportService'), BaseImportService_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 590, 1))
Namespace.addCategoryObject('elementBinding', BaseImportService.name().localName(), BaseImportService)

ImportStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImportStatus'), ImportStatus_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 601, 1))
Namespace.addCategoryObject('elementBinding', ImportStatus.name().localName(), ImportStatus)



Query_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'matchAlgorithm'), NameOrURI_, scope=Query_, documentation=u"\n\t\t\t\t\tThe match algorithm of the filter to be applied. If a 'setOperation' is specified, \n\t\t\t\t\tthe filter will apply to the resulting aggregate.\n\t\t\t\t\t", location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 16, 3)))

Query_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'matchValue'), _ImportedBinding__nsgroup.String, scope=Query_, documentation=u"\n\t\t\t\t\tThe match value of the filter to be applied. If a 'setOperation' is specified, \n\t\t\t\t\tthe filter will apply to the resulting aggregate.\n\t\t\t\t\t", location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 24, 3)))

Query_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'filterComponent'), NameOrURIList_, scope=Query_, documentation=u"\n\t\t\t\t\tThe target components of the filter to be applied. If a 'setOperation' is specified, \n\t\t\t\t\tthe filter will apply to the resulting aggregate.\n\t\t\t\t\t", location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 32, 3)))

Query_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'setOperation'), _ImportedBinding__nsgroup.SetOperator, scope=Query_, documentation=u'\n\t\t\t\t\tThe Set Operation to be applied to the two DirectoryURIs.\n\t\t\t\t\t', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 40, 3)))

Query_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'query1'), Query_, scope=Query_, documentation=u'\n\t\t\t\t\t\tThe left-hand side of the Set Operation.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 53, 4)))

Query_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'directoryUri1'), _ImportedBinding__nsgroup.DirectoryURI, scope=Query_, documentation=u'\n\t\t\t\t\t\tThe left-hand side of the Set Operation.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 60, 4)))

Query_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'query2'), Query_, scope=Query_, documentation=u'\n\t\t\t\t\t\tThe right-hand side of the Set Operation.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 74, 4)))

Query_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'directoryUri2'), _ImportedBinding__nsgroup.DirectoryURI, scope=Query_, documentation=u'\n\t\t\t\t\t\tThe right-hand side of the Set Operation.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 81, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 16, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 24, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 32, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 40, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 47, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 53, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 60, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 68, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 74, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 81, 4))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Query_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'matchAlgorithm')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 16, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Query_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'matchValue')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 24, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Query_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'filterComponent')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 32, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Query_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'setOperation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 40, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Query_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'query1')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 53, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Query_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'directoryUri1')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 60, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Query_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'query2')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 74, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Query_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'directoryUri2')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 81, 4))
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
        fac.UpdateInstruction(cc_4, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_5, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_6, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True),
        fac.UpdateInstruction(cc_8, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Query_._Automaton = _BuildAutomaton()




ProfileElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'structuralProfile'), StructuralProfile, scope=ProfileElement, documentation=u'A resource that is implemented by a service instance', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 212, 3)))

ProfileElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'functionalProfile'), FunctionalProfileEntry, scope=ProfileElement, documentation=u'A functional profile that the service instance supports for the corresponding structure', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 217, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProfileElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'structuralProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 212, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProfileElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'functionalProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 217, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProfileElement._Automaton = _BuildAutomaton_()




BaseService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'serviceName'), _ImportedBinding__nsgroup.String, scope=BaseService_, documentation=u'A short name that identifies the particular service and implementation.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3)))

BaseService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'serviceDescription'), _ImportedBinding__nsgroup.OpaqueData, scope=BaseService_, documentation=u'A description of the service, its use, etc.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3)))

BaseService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'serviceVersion'), _ImportedBinding__nsgroup.String, scope=BaseService_, documentation=u'The version or release identifier of the service.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3)))

BaseService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'serviceProvider'), _ImportedBinding__nsgroup.SourceReference, scope=BaseService_, documentation=u'A reference to the individual or organization that provides the service.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3)))

BaseService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'supportedFormat'), _ImportedBinding__nsgroup.FormatReference, scope=BaseService_, documentation=u'A list of the representation formats supported by the service. Example: text/html, text/xml, application/json', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3)))

BaseService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'defaultFormat'), _ImportedBinding__nsgroup.FormatReference, scope=BaseService_, documentation=u'The default format used by the service unless otherwise specified.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3)))

BaseService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'supportedProfile'), ProfileElement, scope=BaseService_, documentation=u'The set of service profiles that are supported by this service implementation', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3)))

BaseService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'implementationType'), ImplementationProfile, scope=BaseService_, documentation=u'The particular implementation type(s) supported by this profile', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3)))

BaseService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'knownNamespace'), DocumentedNamespaceReference, scope=BaseService_, documentation=u"The set of namespaces recognized by this service. Because many namespace identifiers tend to be cryptic (i.e. HL7 OIDs, BioPortal URL's, etc.),  includes the namespace name, an optional URI \\emph{and} a place to provide textual detail describing what the namespace references. Note that namespace names must be unique across an entire CTS implementation - the same namespace name cannot represent one namespace in code system A\n\t\t\t\t\t\tand a second in code system B. Note also that namespace names are \\emph{local} to a service instance. Information that is communicated between service instances, recorded in data tables or client software \\emph{must} use full URIs.", location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BaseService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
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
BaseService_._Automaton = _BuildAutomaton_2()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'releaseDocumentation'), _ImportedBinding__nsgroup.OpaqueData, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 328, 8)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 328, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'releaseDocumentation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 328, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_3()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'releaseFormat'), _ImportedBinding__nsgroup.SourceAndNotation, scope=CTD_ANON_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 335, 8)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 335, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'releaseFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 335, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_4()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'uri'), _ImportedBinding__nsgroup.URI, scope=CTD_ANON_2, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 354, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 354, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'uri')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 354, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_5()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'keyword'), _ImportedBinding__nsgroup.String, scope=CTD_ANON_3, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 361, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 361, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'keyword')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 361, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_6()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'source'), _ImportedBinding__nsgroup.SourceAndRoleReference, scope=CTD_ANON_4, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 368, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 368, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'source')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 368, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_7()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'note'), _ImportedBinding__nsgroup.Comment, scope=CTD_ANON_5, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 375, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 375, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'note')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 375, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_8()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'property'), _ImportedBinding__nsgroup.Property, scope=CTD_ANON_6, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 382, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 382, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'property')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 382, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_9()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resourceSynopsis'), _ImportedBinding__nsgroup.EntryDescription, scope=CTD_ANON_7, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 389, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 389, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resourceSynopsis')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 389, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_10()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resourceType'), _ImportedBinding__nsgroup.EntityReference, scope=CTD_ANON_8, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 396, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 396, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resourceType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 396, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_11()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rights'), _ImportedBinding__nsgroup.OpaqueData, scope=CTD_ANON_9, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 403, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 403, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rights')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 403, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_12()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'predecessor'), NameOrURI_, scope=CTD_ANON_10, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 423, 8)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 423, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'predecessor')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 423, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_13()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sourceAndNotation'), _ImportedBinding__nsgroup.SourceAndNotation, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 430, 8)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sourceAndNotation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 430, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_14()




ValidationResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), _ImportedBinding__nsgroup.OpaqueData, scope=ValidationResponse, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 557, 3)))

ValidationResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'validationResponse'), STD_ANON, scope=ValidationResponse, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 558, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 557, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValidationResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 557, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValidationResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'validationResponse')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 558, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ValidationResponse._Automaton = _BuildAutomaton_15()




SuccessIndicator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), _ImportedBinding__nsgroup.OpaqueData, scope=SuccessIndicator, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 576, 3)))

SuccessIndicator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'successIndicator'), STD_ANON_, scope=SuccessIndicator, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 577, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 576, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SuccessIndicator._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 576, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SuccessIndicator._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'successIndicator')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 577, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SuccessIndicator._Automaton = _BuildAutomaton_16()




LogEntries_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), LogEntry_, scope=LogEntries_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 631, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 631, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LogEntries_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 631, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LogEntries_._Automaton = _BuildAutomaton_17()




ChangeSetEntryList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), ChangeSetEntry, scope=ChangeSetEntryList, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 804, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 804, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ChangeSetEntryList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 804, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ChangeSetEntryList._Automaton = _BuildAutomaton_18()




EntityNameOrURI_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entityName'), _ImportedBinding__nsgroup.ScopedEntityName, scope=EntityNameOrURI_, documentation=u'A combination of a namespace identifier and a local name that, together, uniquely references an entity known to the service', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 829, 3)))

EntityNameOrURI_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'uri'), _ImportedBinding__nsgroup.String, scope=EntityNameOrURI_, documentation=u'An  that references a class, property or individual', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 834, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 829, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 834, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EntityNameOrURI_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entityName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 829, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(EntityNameOrURI_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'uri')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 834, 3))
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
EntityNameOrURI_._Automaton = _BuildAutomaton_19()




EntityNameOrURIList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), EntityNameOrURI_, scope=EntityNameOrURIList_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 848, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 848, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EntityNameOrURIList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 848, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EntityNameOrURIList_._Automaton = _BuildAutomaton_20()




NameOrURIList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), NameOrURI_, scope=NameOrURIList_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 876, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 876, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NameOrURIList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 876, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NameOrURIList_._Automaton = _BuildAutomaton_21()




QueryControl_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'maxToReturn'), _ImportedBinding__nsgroup.NaturalNumber, scope=QueryControl_, documentation=u'The maximum number of  that may be present in a return . Note that a service may choose to return less than  entries - this is simply an upper limit. If  is not supplied, the service may use whatever return block size it determines to be most appropriate.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 905, 3)))

QueryControl_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'timeLimit'), _ImportedBinding__nsgroup.AmountOfTime, scope=QueryControl_, documentation=u'The maximum amount of time that may be taken to process a query before a time out exception occurs. If not present, the service determines the maximum query time out.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 910, 3)))

QueryControl_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'format'), NameOrURI_, scope=QueryControl_, documentation=u'The local identifier or URI of the return format for query results.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 915, 3)))

QueryControl_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sortCriteria'), SortCriteria_, scope=QueryControl_, documentation=u'The local identifier or URI of the sort criteria for query results.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 920, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 905, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 910, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 915, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 920, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryControl_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'maxToReturn')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 905, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(QueryControl_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'timeLimit')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 910, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(QueryControl_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'format')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 915, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(QueryControl_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sortCriteria')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 920, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
QueryControl_._Automaton = _BuildAutomaton_22()




ReadContext_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active'), ActiveOrAll, scope=ReadContext_, documentation=u'Determines whether the query only applies to only active or all entries. ', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 954, 3), unicode_default=u'ACTIVE_ONLY'))

ReadContext_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'referenceLanguage'), NameOrURI_, scope=ReadContext_, documentation=u'The spoken or written language that should be used for the results of the inquiry, where appropriate.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 959, 3)))

ReadContext_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'changeSetContext'), _ImportedBinding__nsgroup.ChangeSetURI, scope=ReadContext_, documentation=u'The URI of an open change set whose contents should be included in the results of the access request.  is only applicable in services that support the  profile', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 964, 3)))

ReadContext_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'referenceTime'), _ImportedBinding__nsgroup.DateAndTime, scope=ReadContext_, documentation=u'The contextual date and time of the query.  is may only be present in services that support the  profile.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 969, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 954, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 959, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 964, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 969, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReadContext_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 954, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReadContext_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referenceLanguage')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 959, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ReadContext_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'changeSetContext')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 964, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ReadContext_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referenceTime')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 969, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReadContext_._Automaton = _BuildAutomaton_23()




SortCriteria_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), SortCriterion_, scope=SortCriteria_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 984, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 984, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SortCriteria_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 984, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SortCriteria_._Automaton = _BuildAutomaton_24()




SortCriterion_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sortDirection'), SortDirection, scope=SortCriterion_, documentation=u'The sort order to be applied to the element.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 994, 3)))

SortCriterion_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sortElement'), _ImportedBinding__nsgroup.ComponentReference, scope=SortCriterion_, documentation=u'The type and name of the attribute, property or special element to be sorted', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 999, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SortCriterion_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sortDirection')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 994, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SortCriterion_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sortElement')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 999, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SortCriterion_._Automaton = _BuildAutomaton_25()




URIList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'member'), _ImportedBinding__nsgroup.URI, scope=URIList, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1043, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1043, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(URIList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'member')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
URIList._Automaton = _BuildAutomaton_26()




UpdateChangeableMetadataRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedStatus'), CTD_ANON_12, scope=UpdateChangeableMetadataRequest_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1050, 3)))

UpdateChangeableMetadataRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedEntryState'), CTD_ANON_13, scope=UpdateChangeableMetadataRequest_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1057, 3)))

UpdateChangeableMetadataRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedEffectiveDate'), CTD_ANON_14, scope=UpdateChangeableMetadataRequest_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1064, 3)))

UpdateChangeableMetadataRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedChangeNotes'), CTD_ANON_15, scope=UpdateChangeableMetadataRequest_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1071, 3)))

UpdateChangeableMetadataRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedChangeSource'), CTD_ANON_16, scope=UpdateChangeableMetadataRequest_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1078, 3)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1050, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1057, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1064, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1071, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1078, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UpdateChangeableMetadataRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedStatus')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1050, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UpdateChangeableMetadataRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedEntryState')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1057, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UpdateChangeableMetadataRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedEffectiveDate')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1064, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UpdateChangeableMetadataRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedChangeNotes')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1071, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UpdateChangeableMetadataRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedChangeSource')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1078, 3))
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
UpdateChangeableMetadataRequest_._Automaton = _BuildAutomaton_27()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'status'), NameOrURI_, scope=CTD_ANON_12, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1053, 6)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1053, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'status')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1053, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_28()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entryState'), _ImportedBinding__nsgroup.EntryState, scope=CTD_ANON_13, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1060, 6)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entryState')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1060, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_29()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectiveDate'), _ImportedBinding__nsgroup.DateAndTime, scope=CTD_ANON_14, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1067, 6)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1067, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveDate')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1067, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_30()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'changeNotes'), _ImportedBinding__nsgroup.OpaqueData, scope=CTD_ANON_15, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1074, 6)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1074, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'changeNotes')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1074, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_31()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'changeSource'), _ImportedBinding__nsgroup.SourceReference, scope=CTD_ANON_16, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1081, 6)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1081, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'changeSource')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1081, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_32()




UpdateChangeSetMetadataRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedState'), CTD_ANON_17, scope=UpdateChangeSetMetadataRequest_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1091, 3)))

UpdateChangeSetMetadataRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedCreator'), CTD_ANON_18, scope=UpdateChangeSetMetadataRequest_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1098, 3)))

UpdateChangeSetMetadataRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedChangeInstructions'), CTD_ANON_19, scope=UpdateChangeSetMetadataRequest_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1105, 3)))

UpdateChangeSetMetadataRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedOfficialEffectiveDate'), CTD_ANON_20, scope=UpdateChangeSetMetadataRequest_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1112, 3)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1091, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1098, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1105, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1112, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UpdateChangeSetMetadataRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedState')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1091, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UpdateChangeSetMetadataRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedCreator')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1098, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UpdateChangeSetMetadataRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedChangeInstructions')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1105, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UpdateChangeSetMetadataRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedOfficialEffectiveDate')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1112, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UpdateChangeSetMetadataRequest_._Automaton = _BuildAutomaton_33()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'state'), _ImportedBinding__nsgroup.FinalizableState, scope=CTD_ANON_17, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1094, 6)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'state')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1094, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_34()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'creator'), NameOrURI_, scope=CTD_ANON_18, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1101, 6)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1101, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'creator')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1101, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_35()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'changeInstructions'), _ImportedBinding__nsgroup.OpaqueData, scope=CTD_ANON_19, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1108, 6)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1108, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'changeInstructions')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1108, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_36()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'officialEffectiveDate'), _ImportedBinding__nsgroup.DateAndTime, scope=CTD_ANON_20, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1115, 6)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1115, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'officialEffectiveDate')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 1115, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_37()




def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BaseMaintenanceService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
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
BaseMaintenanceService_._Automaton = _BuildAutomaton_38()




UpdateResourceDescription_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedAdditionalDocumentation'), CTD_ANON_2, scope=UpdateResourceDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 351, 3)))

UpdateResourceDescription_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedKeywords'), CTD_ANON_3, scope=UpdateResourceDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 358, 3)))

UpdateResourceDescription_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedSources'), CTD_ANON_4, scope=UpdateResourceDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 365, 3)))

UpdateResourceDescription_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedNotes'), CTD_ANON_5, scope=UpdateResourceDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 372, 3)))

UpdateResourceDescription_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedProperties'), CTD_ANON_6, scope=UpdateResourceDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 379, 3)))

UpdateResourceDescription_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceSynopsis'), CTD_ANON_7, scope=UpdateResourceDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 386, 3)))

UpdateResourceDescription_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceTypes'), CTD_ANON_8, scope=UpdateResourceDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 393, 3)))

UpdateResourceDescription_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedRights'), CTD_ANON_9, scope=UpdateResourceDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 400, 3)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
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
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedAdditionalDocumentation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 351, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedKeywords')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 358, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedSources')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 365, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedNotes')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 372, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedProperties')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 379, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceSynopsis')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 386, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceTypes')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 393, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedRights')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 400, 3))
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
UpdateResourceDescription_._Automaton = _BuildAutomaton_39()




HistoryService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'changeHistory'), _ImportedBinding__nsgroup.ChangeSetDirectoryURI, scope=HistoryService_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 453, 5)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(HistoryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(HistoryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(HistoryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(HistoryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(HistoryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(HistoryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(HistoryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(HistoryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(HistoryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(HistoryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'changeHistory')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 453, 5))
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
HistoryService_._Automaton = _BuildAutomaton_40()




ImportExportBase_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'supportedSourceAndNotation'), _ImportedBinding__nsgroup.SourceAndNotation, scope=ImportExportBase_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 529, 5)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImportExportBase_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImportExportBase_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImportExportBase_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImportExportBase_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImportExportBase_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImportExportBase_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImportExportBase_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImportExportBase_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImportExportBase_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ImportExportBase_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedSourceAndNotation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 529, 5))
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
ImportExportBase_._Automaton = _BuildAutomaton_41()




LogEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'logLevel'), LoggingLevel, scope=LogEntry_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 641, 3)))

LogEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'messageID'), _ImportedBinding__nsgroup.String, scope=LogEntry_, documentation=u'An external identifier that uniquely names the message.  is present to enable automated processing of log entries where appropriate. The significance and use of  is not addressed within the context of the CTS specification', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 643, 3)))

LogEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'processUID'), _ImportedBinding__nsgroup.String, scope=LogEntry_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 648, 3)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 643, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LogEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'logLevel')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 641, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LogEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'messageID')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 643, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LogEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'processUID')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 648, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LogEntry_._Automaton = _BuildAutomaton_42()




ProcessStatus_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'log'), LogEntry_, scope=ProcessStatus_, documentation=u'The set of log records created by the process', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 707, 3)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 707, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProcessStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'log')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 707, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ProcessStatus_._Automaton = _BuildAutomaton_43()




BaseQueryService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'knownProperty'), _ImportedBinding__nsgroup.PredicateReference, scope=BaseQueryService_, documentation=u'The set of properties that are used in one or more instances of the resource represented by this service. This list includes all properties that are can be used in queries in this service, independent of the entryState or temporal state of the resource(s) being searched. ', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5)))

BaseQueryService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'supportedMatchAlgorithm'), _ImportedBinding__nsgroup.MatchAlgorithmReference, scope=BaseQueryService_, documentation=u'The match algorithms that can be used in filters for this service instance.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 754, 5)))

BaseQueryService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'supportedModelAttribute'), _ImportedBinding__nsgroup.ModelAttributeReference, scope=BaseQueryService_, documentation=u'The set of model attributes that can be referenced in filter instances for the given service implementation.', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 759, 5)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownProperty')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 749, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedMatchAlgorithm')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 754, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BaseQueryService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedModelAttribute')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 759, 5))
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
BaseQueryService_._Automaton = _BuildAutomaton_44()




def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BaseReadService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
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
BaseReadService_._Automaton = _BuildAutomaton_45()




ChangeSetEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'applicationDate'), _ImportedBinding__nsgroup.DateAndTime, scope=ChangeSetEntry, documentation=u'The date and time that a change set was applied to a given service instance', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 786, 3)))

ChangeSetEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'changeSetURI'), _ImportedBinding__nsgroup.ChangeSetURI, scope=ChangeSetEntry, documentation=u'The URI of the change set that was applied', location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 791, 3)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'applicationDate')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 786, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ChangeSetEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'changeSetURI')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 791, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ChangeSetEntry._Automaton = _BuildAutomaton_46()




def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseUpdateService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseUpdateService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseUpdateService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseUpdateService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseUpdateService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseUpdateService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseUpdateService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseUpdateService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BaseUpdateService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
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
BaseUpdateService_._Automaton = _BuildAutomaton_47()




UpdateAbstractResourceDescription_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedReleaseDocumentation'), CTD_ANON, scope=UpdateAbstractResourceDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 325, 5)))

UpdateAbstractResourceDescription_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedReleaseFormats'), CTD_ANON_, scope=UpdateAbstractResourceDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 332, 5)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
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
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 325, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 332, 5))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UpdateAbstractResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedAdditionalDocumentation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 351, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UpdateAbstractResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedKeywords')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 358, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UpdateAbstractResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedSources')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 365, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UpdateAbstractResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedNotes')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 372, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UpdateAbstractResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedProperties')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 379, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(UpdateAbstractResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceSynopsis')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 386, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(UpdateAbstractResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceTypes')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 393, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(UpdateAbstractResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedRights')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 400, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(UpdateAbstractResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedReleaseDocumentation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 325, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(UpdateAbstractResourceDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedReleaseFormats')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 332, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UpdateAbstractResourceDescription_._Automaton = _BuildAutomaton_48()




UpdateResourceVersionDescription_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedPredecessor'), CTD_ANON_10, scope=UpdateResourceVersionDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 420, 5)))

UpdateResourceVersionDescription_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedSourceAndNotation'), CTD_ANON_11, scope=UpdateResourceVersionDescription_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 427, 5)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
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
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceVersionDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedAdditionalDocumentation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 351, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceVersionDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedKeywords')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 358, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceVersionDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedSources')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 365, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceVersionDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedNotes')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 372, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceVersionDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedProperties')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 379, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceVersionDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceSynopsis')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 386, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceVersionDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedResourceTypes')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 393, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceVersionDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedRights')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 400, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceVersionDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedPredecessor')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 420, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(UpdateResourceVersionDescription_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedSourceAndNotation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 427, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UpdateResourceVersionDescription_._Automaton = _BuildAutomaton_49()




def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseExportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseExportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseExportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseExportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseExportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseExportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseExportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseExportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseExportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BaseExportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedSourceAndNotation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 529, 5))
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
BaseExportService_._Automaton = _BuildAutomaton_50()




ExportStatus_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'errorHandling'), ErrorResponse, scope=ExportStatus_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 482, 5)))

ExportStatus_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'exportedIRIs'), pyxb.binding.datatypes.string, scope=ExportStatus_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 483, 5)))

ExportStatus_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'overwriteRule'), OverwriteRule, scope=ExportStatus_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 484, 5)))

ExportStatus_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resourcesToExport'), _ImportedBinding__nsgroup.DirectoryEntry, scope=ExportStatus_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 485, 5)))

ExportStatus_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'synchronicity'), SyncOrAsync, scope=ExportStatus_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 486, 5)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 707, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 483, 5))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExportStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'log')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 707, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExportStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'errorHandling')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 482, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExportStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'exportedIRIs')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 483, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExportStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'overwriteRule')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 484, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExportStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resourcesToExport')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 485, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ExportStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'synchronicity')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 486, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
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
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ExportStatus_._Automaton = _BuildAutomaton_51()




def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseImportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceName')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseImportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceDescription')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 258, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseImportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceVersion')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 263, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseImportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceProvider')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 268, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseImportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 273, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseImportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'defaultFormat')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 278, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseImportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedProfile')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 283, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseImportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'implementationType')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 288, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BaseImportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'knownNamespace')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 293, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BaseImportService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supportedSourceAndNotation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 529, 5))
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
BaseImportService_._Automaton = _BuildAutomaton_52()




ImportStatus_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'languageAndSyntax'), _ImportedBinding__nsgroup.OntologyLanguageAndSyntax, scope=ImportStatus_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 609, 5)))

ImportStatus_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'validation'), ValidationLevel, scope=ImportStatus_, location=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 610, 5)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 707, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImportStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'log')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 707, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImportStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'languageAndSyntax')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 609, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ImportStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'validation')), pyxb.utils.utility.Location(u'http://informatics.mayo.edu/cts2/spec/CTS2/1.1/core/CoreService.xsd', 610, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ImportStatus_._Automaton = _BuildAutomaton_53()

