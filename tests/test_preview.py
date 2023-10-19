# -*- coding: utf-8 -*-

import os

from PyPDFForm import PyPDFForm


def test_preview(template_stream, pdf_samples, request):
    expected_path = os.path.join(pdf_samples, "preview", "test_preview.pdf")
    with open(expected_path, "rb+") as f:
        preview = PyPDFForm(template_stream).preview

        request.config.results["expected_path"] = expected_path
        request.config.results["stream"] = preview

        expected = f.read()

        assert len(preview) == len(expected)
        assert preview == expected


def test_preview_sejda(sejda_template, pdf_samples, request):
    expected_path = os.path.join(pdf_samples, "preview", "test_preview_sejda.pdf")
    with open(expected_path, "rb+") as f:
        preview = PyPDFForm(sejda_template).preview

        request.config.results["expected_path"] = expected_path
        request.config.results["stream"] = preview

        expected = f.read()

        assert len(preview) == len(expected)
        assert preview == expected
