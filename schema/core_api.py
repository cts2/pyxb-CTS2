# ./core_api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:84e79441b554a4367822e7e49bbfb85b3f4be5f8
# Generated 2013-04-18 16:41:20.526042 by PyXB version 1.2.2
# Namespace http://www.omg.org/spec/CTS2/1.1/Core [xmlns:core]

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
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.omg.org/spec/CTS2/1.1/Core', create_if_missing=True)
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

from _nsgroup import EntityExpression # {http://www.omg.org/spec/CTS2/1.1/Core}EntityExpression
from _nsgroup import String # {http://www.omg.org/spec/CTS2/1.1/Core}String
from _nsgroup import DateAndTime # {http://www.omg.org/spec/CTS2/1.1/Core}DateAndTime
from _nsgroup import Enumeration # {http://www.omg.org/spec/CTS2/1.1/Core}Enumeration
from _nsgroup import LocalIdentifier # {http://www.omg.org/spec/CTS2/1.1/Core}LocalIdentifier
from _nsgroup import NamespaceIdentifier # {http://www.omg.org/spec/CTS2/1.1/Core}NamespaceIdentifier
from _nsgroup import URI # {http://www.omg.org/spec/CTS2/1.1/Core}URI
from _nsgroup import MatchStrength # {http://www.omg.org/spec/CTS2/1.1/Core}MatchStrength
from _nsgroup import NaturalNumber # {http://www.omg.org/spec/CTS2/1.1/Core}NaturalNumber
from _nsgroup import AmountOfTime # {http://www.omg.org/spec/CTS2/1.1/Core}AmountOfTime
from _nsgroup import tsAnyType # {http://www.omg.org/spec/CTS2/1.1/Core}tsAnyType
from _nsgroup import OpaqueData # {http://www.omg.org/spec/CTS2/1.1/Core}OpaqueData
from _nsgroup import EntityReferenceList # {http://www.omg.org/spec/CTS2/1.1/Core}EntityReferenceList
from _nsgroup import ScopedEntityName # {http://www.omg.org/spec/CTS2/1.1/Core}ScopedEntityName
from _nsgroup import EntityExpression_ # {http://www.omg.org/spec/CTS2/1.1/Core}EntityExpression
from _nsgroup import CodeSystemVersionReference # {http://www.omg.org/spec/CTS2/1.1/Core}CodeSystemVersionReference
from _nsgroup import MapVersionReference # {http://www.omg.org/spec/CTS2/1.1/Core}MapVersionReference
from _nsgroup import SourceAndRoleReference # {http://www.omg.org/spec/CTS2/1.1/Core}SourceAndRoleReference
from _nsgroup import ValueSetDefinitionReference # {http://www.omg.org/spec/CTS2/1.1/Core}ValueSetDefinitionReference
from _nsgroup import Filter # {http://www.omg.org/spec/CTS2/1.1/Core}Filter
from _nsgroup import SortCriteria # {http://www.omg.org/spec/CTS2/1.1/Core}SortCriteria
from _nsgroup import OntologyLanguageAndSyntax # {http://www.omg.org/spec/CTS2/1.1/Core}OntologyLanguageAndSyntax
from _nsgroup import SourceAndNotation # {http://www.omg.org/spec/CTS2/1.1/Core}SourceAndNotation
from _nsgroup import AnonymousStatement # {http://www.omg.org/spec/CTS2/1.1/Core}AnonymousStatement
from _nsgroup import Boolean # {http://www.omg.org/spec/CTS2/1.1/Core}Boolean
from _nsgroup import Parameter # {http://www.omg.org/spec/CTS2/1.1/Core}Parameter
from _nsgroup import RESTResource # {http://www.omg.org/spec/CTS2/1.1/Core}RESTResource
from _nsgroup import Message # {http://www.omg.org/spec/CTS2/1.1/Core}Message
from _nsgroup import EntryDescription # {http://www.omg.org/spec/CTS2/1.1/Core}EntryDescription
from _nsgroup import PersistentURI # {http://www.omg.org/spec/CTS2/1.1/Core}PersistentURI
from _nsgroup import LocalURI # {http://www.omg.org/spec/CTS2/1.1/Core}LocalURI
from _nsgroup import EntryState # {http://www.omg.org/spec/CTS2/1.1/Core}EntryState
from _nsgroup import ChangeType # {http://www.omg.org/spec/CTS2/1.1/Core}ChangeType
from _nsgroup import ChangeCommitted # {http://www.omg.org/spec/CTS2/1.1/Core}ChangeCommitted
from _nsgroup import FinalizableState # {http://www.omg.org/spec/CTS2/1.1/Core}FinalizableState
from _nsgroup import CompleteDirectory # {http://www.omg.org/spec/CTS2/1.1/Core}CompleteDirectory
from _nsgroup import EntityReference # {http://www.omg.org/spec/CTS2/1.1/Core}EntityReference
from _nsgroup import SetOperator # {http://www.omg.org/spec/CTS2/1.1/Core}SetOperator
from _nsgroup import SortDirection # {http://www.omg.org/spec/CTS2/1.1/Core}SortDirection
from _nsgroup import AssociationDirection # {http://www.omg.org/spec/CTS2/1.1/Core}AssociationDirection
from _nsgroup import TargetReferenceType # {http://www.omg.org/spec/CTS2/1.1/Core}TargetReferenceType
from _nsgroup import CodeSystemName # {http://www.omg.org/spec/CTS2/1.1/Core}CodeSystemName
from _nsgroup import CodeSystemVersionName # {http://www.omg.org/spec/CTS2/1.1/Core}CodeSystemVersionName
from _nsgroup import ConceptDomainName # {http://www.omg.org/spec/CTS2/1.1/Core}ConceptDomainName
from _nsgroup import MapName # {http://www.omg.org/spec/CTS2/1.1/Core}MapName
from _nsgroup import MapVersionName # {http://www.omg.org/spec/CTS2/1.1/Core}MapVersionName
from _nsgroup import ValueSetName # {http://www.omg.org/spec/CTS2/1.1/Core}ValueSetName
from _nsgroup import VersionTagName # {http://www.omg.org/spec/CTS2/1.1/Core}VersionTagName
from _nsgroup import NoteType # {http://www.omg.org/spec/CTS2/1.1/Core}NoteType
from _nsgroup import DefinitionRole # {http://www.omg.org/spec/CTS2/1.1/Core}DefinitionRole
from _nsgroup import CTS2ResourceType # {http://www.omg.org/spec/CTS2/1.1/Core}CTS2ResourceType
from _nsgroup import StatementTarget # {http://www.omg.org/spec/CTS2/1.1/Core}StatementTarget
from _nsgroup import ChangeSetURI # {http://www.omg.org/spec/CTS2/1.1/Core}ChangeSetURI
from _nsgroup import DocumentURI # {http://www.omg.org/spec/CTS2/1.1/Core}DocumentURI
from _nsgroup import ExternalURI # {http://www.omg.org/spec/CTS2/1.1/Core}ExternalURI
from _nsgroup import DirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}DirectoryURI
from _nsgroup import RenderingURI # {http://www.omg.org/spec/CTS2/1.1/Core}RenderingURI
from _nsgroup import ServiceURI # {http://www.omg.org/spec/CTS2/1.1/Core}ServiceURI
from _nsgroup import Changeable # {http://www.omg.org/spec/CTS2/1.1/Core}Changeable
from _nsgroup import Finalizable # {http://www.omg.org/spec/CTS2/1.1/Core}Finalizable
from _nsgroup import AnonymousEntityReference # {http://www.omg.org/spec/CTS2/1.1/Core}AnonymousEntityReference
from _nsgroup import SortCriterion # {http://www.omg.org/spec/CTS2/1.1/Core}SortCriterion
from _nsgroup import PropertyReference # {http://www.omg.org/spec/CTS2/1.1/Core}PropertyReference
from _nsgroup import ChangeDescription # {http://www.omg.org/spec/CTS2/1.1/Core}ChangeDescription
from _nsgroup import ChangeSetBase # {http://www.omg.org/spec/CTS2/1.1/Core}ChangeSetBase
from _nsgroup import Directory # {http://www.omg.org/spec/CTS2/1.1/Core}Directory
from _nsgroup import DirectoryEntry # {http://www.omg.org/spec/CTS2/1.1/Core}DirectoryEntry
from _nsgroup import AssociationDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}AssociationDirectoryURI
from _nsgroup import ChangeSetDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}ChangeSetDirectoryURI
from _nsgroup import CodeSystemCatalogEntryDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}CodeSystemCatalogEntryDirectoryURI
from _nsgroup import CodeSystemVersionCatalogEntryDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}CodeSystemVersionCatalogEntryDirectoryURI
from _nsgroup import ConceptDomainCatalogEntryDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}ConceptDomainCatalogEntryDirectoryURI
from _nsgroup import ConceptDomainBindingDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}ConceptDomainBindingDirectoryURI
from _nsgroup import EntityDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}EntityDirectoryURI
from _nsgroup import MapCatalogEntryDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}MapCatalogEntryDirectoryURI
from _nsgroup import MapVersionDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}MapVersionDirectoryURI
from _nsgroup import MapEntryDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}MapEntryDirectoryURI
from _nsgroup import StatementDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}StatementDirectoryURI
from _nsgroup import ValueSetCatalogEntryDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}ValueSetCatalogEntryDirectoryURI
from _nsgroup import ValueSetDefinitionDirectoryURI # {http://www.omg.org/spec/CTS2/1.1/Core}ValueSetDefinitionDirectoryURI
from _nsgroup import DescriptionInCodeSystem # {http://www.omg.org/spec/CTS2/1.1/Core}DescriptionInCodeSystem
from _nsgroup import NamedEntityReference # {http://www.omg.org/spec/CTS2/1.1/Core}NamedEntityReference
from _nsgroup import URIAndEntityName # {http://www.omg.org/spec/CTS2/1.1/Core}URIAndEntityName
from _nsgroup import NameAndMeaningReference # {http://www.omg.org/spec/CTS2/1.1/Core}NameAndMeaningReference
from _nsgroup import FilterComponent # {http://www.omg.org/spec/CTS2/1.1/Core}FilterComponent
from _nsgroup import Note # {http://www.omg.org/spec/CTS2/1.1/Core}Note
from _nsgroup import ResourceDescription # {http://www.omg.org/spec/CTS2/1.1/Core}ResourceDescription
from _nsgroup import Property # {http://www.omg.org/spec/CTS2/1.1/Core}Property
from _nsgroup import AssociationReference # {http://www.omg.org/spec/CTS2/1.1/Core}AssociationReference
from _nsgroup import OntologyEngineeringToolReference # {http://www.omg.org/spec/CTS2/1.1/Core}OntologyEngineeringToolReference
from _nsgroup import OntologyEngineeringMethodologyReference # {http://www.omg.org/spec/CTS2/1.1/Core}OntologyEngineeringMethodologyReference
from _nsgroup import BindingQualifierReference # {http://www.omg.org/spec/CTS2/1.1/Core}BindingQualifierReference
from _nsgroup import FormalityLevelReference # {http://www.omg.org/spec/CTS2/1.1/Core}FormalityLevelReference
from _nsgroup import CaseSignificanceReference # {http://www.omg.org/spec/CTS2/1.1/Core}CaseSignificanceReference
from _nsgroup import CodeSystemCategoryReference # {http://www.omg.org/spec/CTS2/1.1/Core}CodeSystemCategoryReference
from _nsgroup import CodeSystemReference # {http://www.omg.org/spec/CTS2/1.1/Core}CodeSystemReference
from _nsgroup import ConceptDomainReference # {http://www.omg.org/spec/CTS2/1.1/Core}ConceptDomainReference
from _nsgroup import ContextReference # {http://www.omg.org/spec/CTS2/1.1/Core}ContextReference
from _nsgroup import DesignationFidelityReference # {http://www.omg.org/spec/CTS2/1.1/Core}DesignationFidelityReference
from _nsgroup import DesignationTypeReference # {http://www.omg.org/spec/CTS2/1.1/Core}DesignationTypeReference
from _nsgroup import FormatReference # {http://www.omg.org/spec/CTS2/1.1/Core}FormatReference
from _nsgroup import LanguageReference # {http://www.omg.org/spec/CTS2/1.1/Core}LanguageReference
from _nsgroup import MapReference # {http://www.omg.org/spec/CTS2/1.1/Core}MapReference
from _nsgroup import MapCorrelationReference # {http://www.omg.org/spec/CTS2/1.1/Core}MapCorrelationReference
from _nsgroup import MatchAlgorithmReference # {http://www.omg.org/spec/CTS2/1.1/Core}MatchAlgorithmReference
from _nsgroup import ModelAttributeReference # {http://www.omg.org/spec/CTS2/1.1/Core}ModelAttributeReference
from _nsgroup import NamespaceReference # {http://www.omg.org/spec/CTS2/1.1/Core}NamespaceReference
from _nsgroup import OntologyDomainReference # {http://www.omg.org/spec/CTS2/1.1/Core}OntologyDomainReference
from _nsgroup import OntologyLanguageReference # {http://www.omg.org/spec/CTS2/1.1/Core}OntologyLanguageReference
from _nsgroup import OntologySyntaxReference # {http://www.omg.org/spec/CTS2/1.1/Core}OntologySyntaxReference
from _nsgroup import OntologyTaskReference # {http://www.omg.org/spec/CTS2/1.1/Core}OntologyTaskReference
from _nsgroup import OntologyTypeReference # {http://www.omg.org/spec/CTS2/1.1/Core}OntologyTypeReference
from _nsgroup import PredicateReference # {http://www.omg.org/spec/CTS2/1.1/Core}PredicateReference
from _nsgroup import ReasoningAlgorithmReference # {http://www.omg.org/spec/CTS2/1.1/Core}ReasoningAlgorithmReference
from _nsgroup import RoleReference # {http://www.omg.org/spec/CTS2/1.1/Core}RoleReference
from _nsgroup import SourceReference # {http://www.omg.org/spec/CTS2/1.1/Core}SourceReference
from _nsgroup import StatusReference # {http://www.omg.org/spec/CTS2/1.1/Core}StatusReference
from _nsgroup import ValueSetReference # {http://www.omg.org/spec/CTS2/1.1/Core}ValueSetReference
from _nsgroup import VersionTagReference # {http://www.omg.org/spec/CTS2/1.1/Core}VersionTagReference
from _nsgroup import Definition # {http://www.omg.org/spec/CTS2/1.1/Core}Definition
from _nsgroup import Example # {http://www.omg.org/spec/CTS2/1.1/Core}Example
from _nsgroup import Comment # {http://www.omg.org/spec/CTS2/1.1/Core}Comment
from _nsgroup import ResourceDescriptionDirectoryEntry # {http://www.omg.org/spec/CTS2/1.1/Core}ResourceDescriptionDirectoryEntry
from _nsgroup import AbstractResourceDescription # {http://www.omg.org/spec/CTS2/1.1/Core}AbstractResourceDescription
from _nsgroup import ResourceVersionDescription # {http://www.omg.org/spec/CTS2/1.1/Core}ResourceVersionDescription
from _nsgroup import AbstractResourceDescriptionDirectoryEntry # {http://www.omg.org/spec/CTS2/1.1/Core}AbstractResourceDescriptionDirectoryEntry
from _nsgroup import ResourceVersionDescriptionDirectoryEntry # {http://www.omg.org/spec/CTS2/1.1/Core}ResourceVersionDescriptionDirectoryEntry
