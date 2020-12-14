# -*- coding: utf-8 -*-

from rohberg.elasticsearchblocks import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IElasticSearchBlocksMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IElasticSearchBlocks(model.Schema):
    """ 
    """

    # TODO hide field blocks_plaintext
    blocks_plaintext = schema.Tuple(
        title=_(u'Blocks content in plain text'),
        required=False,
        value_type=schema.TextLine(),
        default=(),
        missing_value=(),
        )


@implementer(IElasticSearchBlocks)
@adapter(IElasticSearchBlocksMarker)
class ElasticSearchBlocks(object):
    def __init__(self, context):
        self.context = context

    @property
    # TODO getter should return the extract of blocks field. see indexer
    def blocks_plaintext(self):
        if safe_hasattr(self.context, 'blocks_plaintext'):
            return self.context.blocks_plaintext
        return None

    @blocks_plaintext.setter
    def blocks_plaintext(self, value):
        self.context.blocks_plaintext = value
