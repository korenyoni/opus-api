#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `opus_api` package."""


import unittest
from click.testing import CliRunner

from opus_api import opus_api
from opus_api import cli


class TestOpus_api(unittest.TestCase):
    """Tests for `opus_api` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_langs(self):
        runner = CliRunner()
        result = runner.invoke(cli.main, ['langs'])
        assert result.exit_code == 0
        assert "zsm (zsm)" in result.output

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'OPUS (opus.lingfil.uu.se)' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message and exit.' in help_result.output
