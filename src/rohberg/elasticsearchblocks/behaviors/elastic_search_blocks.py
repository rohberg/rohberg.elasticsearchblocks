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


from plone.restapi.behaviors import IBlocks
from plone.indexer.decorator import indexer
from plone.app.contenttypes.indexers import SearchableText
import six

import pprint

def _extract_text(block):
    print("** _extract_text block", block)
    result = ""
    try:
        for paragraph in block.get("text").get("blocks"):
            text = paragraph["text"]
            if six.PY2:
                if isinstance(text, six.text_type):
                    text = text.encode("utf-8", "replace")
                if text:
                    result = " ".join((result, text))
            else:
                result = " ".join((result, text))
    except Exception as e:
        print("Exception: ", e)
    return result


class IElasticSearchBlocksMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IElasticSearchBlocks(model.Schema):
    """ 
    """

    # TODO hide field blocks_plaintext
    blocks_plaintext = schema.TextLine(
        title=_(u'Blocks content in plain text'),
        required=False,
        default=None
        )


@implementer(IElasticSearchBlocks)
@adapter(IElasticSearchBlocksMarker)
class ElasticSearchBlocks(object):
    def __init__(self, context):
        self.context = context

    @property
    # TODO getter should return the extract of blocks field. still todo: slate blocks
    def blocks_plaintext(self):
        # if safe_hasattr(self.context, 'blocks_plaintext'):
        #     return self.context.blocks_plaintext
        # return None

        context = self.context
        # std_text = SearchableText(obj)
        myblocks = context.blocks
        # print('** blocks_plaintext: blocks')
        # pprint.pprint(myblocks)
        # import pdb; pdb.set_trace()
        blocks_text = [
            _extract_text(myblocks[block_uid])
            for block_uid in myblocks
            if myblocks[block_uid].get("@type", "") == "text"
        ]
        # blocks_text.append(std_text)
        print('*** blocks_plaintext: blocks_text', blocks_text)
        text = " ".join(blocks_text)
        return text

    @blocks_plaintext.setter
    def blocks_plaintext(self, value):
        self.context.blocks_plaintext = value



