"""Tests for publication experiments estimator selection."""

import numpy as np
import pytest
from tsml.compose import SklearnToTsmlRegressor
from tsml_eval.testing.testing_utils import _check_set_method, _check_set_method_results
from tsml_eval.utils.estimator_validation import is_sklearn_regressor

from set_tser_exp_regressor import _set_tser_exp_regressor, expansion_regressors


def test_set_expansion_regressor():
    """Test set_tser_exp_regressor method."""
    regressor_list = []
    regressor_dict = {}
    all_regressor_names = []
    _check_set_method(
        _set_tser_exp_regressor,
        expansion_regressors,
        regressor_list,
        regressor_dict,
        all_regressor_names,
    )

    _check_set_method_results(
        regressor_dict,
        estimator_name="Regressors",
        method_name="_set_tser_exp_regressor",
    )


def test_set_expansion_regressor_invalid():
    """Test set_tser_exp_regressor method with invalid estimator."""
    with pytest.raises(ValueError, match="UNKNOWN REGRESSOR"):
        _set_tser_exp_regressor("invalid")


@pytest.mark.parametrize(
    "name,fast_params",
    [
        ("1NN-DTW", {}),
        ("1NN-ED", {}),
        ("5NN-DTW", {}),
        ("5NN-ED", {}),
        ("FPCR", {}),
        ("FPCR-Bs", {}),
        ("Grid-SVR", {}),
        ("Ridge", {}),
        ("RandF", {"n_estimators": 5}),
        ("RotF", {"n_estimators": 5}),
        ("XGBoost", {"n_estimators": 5}),
        ("ROCKET", {"n_kernels": 20}),
        ("MultiROCKET", {"n_kernels": 84}),
        ("TSF", {}),
        ("DrCIF", {"n_estimators": 3, "n_intervals": 2, "att_subsample_size": 2}),
        (
            "FreshPRINCE",
            {"n_estimators": 5, "default_fc_parameters": "minimal"},
        ),
    ],
)
def test_fit_expansion_regressors(name, fast_params):
    """Test fitting and predicting with non-DL expansion regressors."""
    rng = np.random.default_rng(0)
    X = rng.normal(size=(12, 2, 20))
    y = rng.normal(size=12)

    try:
        regressor = _set_tser_exp_regressor(name, random_state=0)
    except ModuleNotFoundError as err:
        pytest.skip(f"Optional dependency not installed: {err}")

    if fast_params:
        regressor.set_params(**fast_params)
    if name == "TSF":
        regressor.estimators[0][1].set_params(n_estimators=5)
    if is_sklearn_regressor(regressor):
        regressor = SklearnToTsmlRegressor(
            regressor=regressor, concatenate_channels=True, random_state=0
        )

    regressor.fit(X, y)
    preds = regressor.predict(X)
    assert preds.shape == (12,)
