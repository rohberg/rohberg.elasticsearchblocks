# -*- coding: utf-8 -*-
from plone.dexterity.interfaces import IDexterityFTI
from Products.CMFPlone.interfaces import INonInstallable
from zope.component import queryUtility
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "rohberg.elasticsearchblocks:uninstall",
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.


def add_behavior(portal_type, behavior):
    fti = queryUtility(IDexterityFTI, name=portal_type)
    if fti is not None:
        # This prevents to add the behavior twice
        new = [
            currentbehavior
            for currentbehavior in fti.behaviors
            if currentbehavior != behavior
        ]
        new.append(behavior)
        fti.behaviors = tuple(new)


def post_install_testing(context):
    """Post install script for profile testing"""
    add_behavior("Document", "rohberg.elasticsearchblocks.manualfields")


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
