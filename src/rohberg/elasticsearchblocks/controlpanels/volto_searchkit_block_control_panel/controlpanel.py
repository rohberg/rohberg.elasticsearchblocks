# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import (
    ControlPanelFormWrapper,
    RegistryEditForm,
)
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from rohberg.elasticsearchblocks import _
from rohberg.elasticsearchblocks.interfaces import IRohbergElasticsearchblocksLayer
from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IVoltoSearchkitBlockControlPanel(Interface):
    myfield_name = schema.TextLine(
        title=_(
            "This is an example field for this control panel",
        ),
        description=_(
            "",
        ),
        default="",
        required=False,
        readonly=False,
    )


class VoltoSearchkitBlockControlPanel(RegistryEditForm):
    schema = IVoltoSearchkitBlockControlPanel
    schema_prefix = "rohberg.elasticsearchblocks.volto_searchkit_block_control_panel"
    label = _("Volto Searchkit Block Control Panel")


VoltoSearchkitBlockControlPanelView = layout.wrap_form(
    VoltoSearchkitBlockControlPanel, ControlPanelFormWrapper
)



@adapter(Interface, IRohbergElasticsearchblocksLayer)
class VoltoSearchkitBlockControlPanelConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IVoltoSearchkitBlockControlPanel
    configlet_id = "volto_searchkit_block_control_panel-controlpanel"
    configlet_category_id = "Products"
    title = _("Volto Searchkit Block Control Panel")
    group = ""
    schema_prefix = "rohberg.elasticsearchblocks.volto_searchkit_block_control_panel"
