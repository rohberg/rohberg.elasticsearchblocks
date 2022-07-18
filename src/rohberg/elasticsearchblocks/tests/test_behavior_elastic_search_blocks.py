# -*- coding: utf-8 -*-
from plone.app.testing import setRoles, TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from rohberg.elasticsearchblocks.behaviors.elastic_search_blocks import (
    IElasticSearchBlocksMarker,
)
from rohberg.elasticsearchblocks.testing import (
    ROHBERG_ELASTICSEARCHBLOCKS_INTEGRATION_TESTING  # noqa,
)
from zope.component import getUtility

import unittest


class ElasticSearchBlocksIntegrationTest(unittest.TestCase):

    layer = ROHBERG_ELASTICSEARCHBLOCKS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_elastic_search_blocks(self):
        behavior = getUtility(IBehavior, 'rohberg.elasticsearchblocks.elastic_search_blocks')
        self.assertEqual(
            behavior.marker,
            IElasticSearchBlocksMarker,
        )
