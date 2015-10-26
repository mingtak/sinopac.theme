# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from sinopac.theme.testing import SINOPAC_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that sinopac.theme is properly installed."""

    layer = SINOPAC_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sinopac.theme is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('sinopac.theme'))

    def test_browserlayer(self):
        """Test that ISinopacThemeLayer is registered."""
        from sinopac.theme.interfaces import ISinopacThemeLayer
        from plone.browserlayer import utils
        self.assertIn(ISinopacThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SINOPAC_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['sinopac.theme'])

    def test_product_uninstalled(self):
        """Test if sinopac.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('sinopac.theme'))

    def test_browserlayer_removed(self):
        """Test that ISinopacThemeLayer is removed."""
        from sinopac.theme.interfaces import ISinopacThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISinopacThemeLayer, utils.registered_layers())
