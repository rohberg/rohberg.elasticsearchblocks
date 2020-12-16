# -*- coding: utf-8 -*-

from rohberg.elasticsearchblocks import _
from plone import schema
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


from plone.restapi.behaviors import IBlocks
from plone.indexer.decorator import indexer
from plone.app.contenttypes.indexers import SearchableText
import six

import pprint


class IElasticSearchBlocksMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IElasticSearchBlocks(model.Schema):
    """ 
    """

    directives.read_permission(blocks_plaintext='cmf.ManagePortal')
    blocks_plaintext = schema.TextLine(
        title=_(u'Blocks content in plain text'),
        required=False,
        default=None
        )


def _extract_text(block):
    result = ""
    # # DraftJS
    # for paragraph in block.get("text",{}).get("blocks",[]):
    #     text = paragraph["text"]
    #     if six.PY2:
    #         if isinstance(text, six.text_type):
    #             text = text.encode("utf-8", "replace")
    #         if text:
    #             result = " ".join((result, text))
    #     else:
    #         result = " ".join((result, text))
    # Slate
    if block.get("plaintext",""):
        result = block.get("plaintext")
    elif block["@type"]=="columnsBlock":
        columns = block["data"]["blocks"]
        result = "  ".join(
            [
                getBlocksText(columns[clm]['blocks']) 
                for clm in columns
            ])
    return result

def getBlocksText(blocks):
    blocks_text = [
        _extract_text(blocks[block_uid])
        for block_uid in blocks
        if blocks[block_uid].get("@type", "") in ["slate", "columnsBlock"]
    ]
    text = "  ".join(blocks_text)
    
    return text
    
@implementer(IElasticSearchBlocks)
@adapter(IElasticSearchBlocksMarker)
class ElasticSearchBlocks(object):
    def __init__(self, context):
        self.context = context

    @property
    # TODO getter should return the extract of blocks field. still todo: slate blocks
    def blocks_plaintext(self):
        text = getBlocksText(self.context.blocks)
        print("\n\n*** blocks_plaintext of ", self.context)
        print(text)
        return text

    @blocks_plaintext.setter
    def blocks_plaintext(self, value):
        self.context.blocks_plaintext = value



