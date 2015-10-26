# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import sinopac.theme


class SinopacThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=sinopac.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinopac.theme:default')


SINOPAC_THEME_FIXTURE = SinopacThemeLayer()


SINOPAC_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINOPAC_THEME_FIXTURE,),
    name='SinopacThemeLayer:IntegrationTesting'
)


SINOPAC_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINOPAC_THEME_FIXTURE,),
    name='SinopacThemeLayer:FunctionalTesting'
)


SINOPAC_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINOPAC_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='SinopacThemeLayer:AcceptanceTesting'
)
