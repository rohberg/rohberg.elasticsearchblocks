# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import (
    ControlPanelFormWrapper,
    RegistryEditForm,
)
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from rohberg.elasticsearchblocks import _
from rohberg.elasticsearchblocks.interfaces import IRohbergElasticsearchblocksLayer
from plone import schema
from zope.component import adapter
from zope.interface import Interface


class IVoltoSearchkitBlockControlPanel(Interface):
    testsearch_elasticsearch_url = schema.TextLine(
        title=_(
            "elasticsearch url",
        ),
        default="https://localhost:9200",
        required=False,
        readonly=False,
    )
    testsearch_elasticsearch_index = schema.TextLine(
        title=_(
            "elasticsearch index",
        ),
        default="plone2020",
        required=False,
        readonly=False,
    )
    testsearch_backend = schema.TextLine(
        title=_(
            "backend",
        ),
        default="http://127.0.0.1:8080/Plone",
        required=False,
        readonly=False,
    )
    testsearch_frontend = schema.TextLine(
        title=_(
            "frontend",
        ),
        default="http://myproject.example.com/",
        required=False,
        readonly=False,
    )

    allowed_content_types = schema.List(
        title=_("Allowed types"),
        value_type=schema.TextLine(),
        required=False,
        missing_value=[],
        default=[],
    )
    directives.widget(
        "allowed_content_types",
        AjaxSelectFieldWidget,
        vocabulary="plone.app.vocabularies.UserFriendlyTypes",
    )

    allowed_review_states = schema.List(
        title=_("Allowed states"),
        value_type=schema.TextLine(),
        required=False,
        missing_value=[],
        default=[],
    )
    directives.widget(
        "allowed_review_states",
        AjaxSelectFieldWidget,
        vocabulary="plone.app.vocabularies.WorkflowStates",
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
