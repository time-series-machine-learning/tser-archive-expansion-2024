"""Test file checking that the expansion regression experiments run correctly."""

import os
import runpy
import sys

from tsml_eval.testing.testing_utils import _TEST_DATA_PATH
from tsml_eval.utils.results_validation import validate_results_file

from run_experiments import (
    _REPO_PATH,
    _TSER_ARCHIVE_TEST_RESULTS_PATH,
    _run_experiment,
)


def test_run_expansion_regression_experiment(monkeypatch):
    """Test paper regression experiments with test data and regressor."""
    regressor = "ROCKET"
    dataset = "MinimalGasPrices"
    resample = 0

    args = [
        _TEST_DATA_PATH,
        _TSER_ARCHIVE_TEST_RESULTS_PATH,
        regressor,
        dataset,
        resample,
        "-ow",
    ]

    _run_experiment(args)

    test_file = (
        f"{_TSER_ARCHIVE_TEST_RESULTS_PATH}{regressor}/Predictions/{dataset}/"
        "testResample0.csv"
    )
    assert os.path.exists(test_file)
    assert validate_results_file(test_file)

    # this covers both the main method and present result file checking
    monkeypatch.setattr(sys, "argv", sys.argv[:1])
    runpy.run_path(f"{_REPO_PATH}/run_experiments.py", run_name="__main__")

    os.remove(test_file)
