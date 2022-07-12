# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from rohberg.igib import _
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class IManualfieldsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IManualfields(model.Schema):
    """ """

    informationtype = schema.Set(
        title=_("Informationstyp"),
        value_type=schema.Choice(vocabulary="igib.informationtypeneu"),
        required=False,
    )

    manualfile = NamedBlobFile(
        title=_("Manual hochladen"),
        description=_("Das Format ist idealerweise PDF."),
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


@implementer(IManualfields)
@adapter(IManualfieldsMarker)
class Manualfields(object):
    def __init__(self, context):
        self.context = context

    @property
    def informationtype(self):
        if safe_hasattr(self.context, "informationtype"):
            return self.context.informationtype
        return None

    @informationtype.setter
    def informationtype(self, value):
        self.context.informationtype = value

    @property
    def manualfile(self):
        if safe_hasattr(self.context, "manualfile"):
            return self.context.manualfile
        return None

    @manualfile.setter
    def manualfile(self, value):
        self.context.manualfile = value
