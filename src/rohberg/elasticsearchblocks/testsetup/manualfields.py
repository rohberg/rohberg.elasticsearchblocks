# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from rohberg.elasticsearchblocks import _
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class IManualfieldsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IManualfields(model.Schema):
    """ """

    informationtype = schema.Set(
        title=_("Informationstyp"),
        value_type=schema.Choice(
            vocabulary="rohberg.elasticsearchblock.informationtype"
        ),
        required=False,
    )

    manualfile = NamedBlobFile(
        title=_("Upload Manual"),
        description=_("PDF recommended."),
        required=False,
    )
    manualfilecontent = schema.TextLine(
        readonly=True,
        title=_("Extracted Manual PDF content"),
        required=False,
        default="",
        missing_value="",
    )
    directives.omitted("manualfilecontent")
