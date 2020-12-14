# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import rohberg.elasticsearchblocks


class RohbergElasticsearchblocksLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=rohberg.elasticsearchblocks)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rohberg.elasticsearchblocks:default')


ROHBERG_ELASTICSEARCHBLOCKS_FIXTURE = RohbergElasticsearchblocksLayer()


ROHBERG_ELASTICSEARCHBLOCKS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ROHBERG_ELASTICSEARCHBLOCKS_FIXTURE,),
    name='RohbergElasticsearchblocksLayer:IntegrationTesting',
)


ROHBERG_ELASTICSEARCHBLOCKS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ROHBERG_ELASTICSEARCHBLOCKS_FIXTURE,),
    name='RohbergElasticsearchblocksLayer:FunctionalTesting',
)


ROHBERG_ELASTICSEARCHBLOCKS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ROHBERG_ELASTICSEARCHBLOCKS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RohbergElasticsearchblocksLayer:AcceptanceTesting',
)
