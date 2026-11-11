# Unsupervised Feature Based Algorithms for Time Series Extrinsic Regression

Code and results for the paper "Unsupervised Feature Based Algorithms for Time Series
Extrinsic Regression" published in Data Mining and Knowledge Discovery, which expands
the time series extrinsic regression (TSER) archive to 63 datasets and benchmarks
regression algorithms on it.

The paper is open access and available from
[Springer](https://doi.org/10.1007/s10618-024-01027-w).

## Contents

| Path | Description |
|---|---|
| [results/5.A.1](results/5.A.1) | RMSE for 13 regressors on the 19 original TSER archive datasets, 5 resamples (Figure 6) |
| [results/5.A.2](results/5.A.2) | RMSE for the same 13 regressors on the 63 datasets of the expanded archive, 30 resamples (Figure 7) |
| [results/5.B](results/5.B) | RMSE for 11 regressors on 62 datasets, 30 resamples |
| [results/5.C](results/5.C) | RMSE for 8 regressors on 62 datasets, including DrCIF and FreshPRINCE, 30 resamples |
| [set_tser_exp_regressor.py](set_tser_exp_regressor.py) | The estimator configurations used in the experiments |
| [run_experiments.py](run_experiments.py) | Script to run a single experiment |
| [tser_archive_expansion.ipynb](tser_archive_expansion.ipynb) | Example of using the regressors directly |
| [static_publication_reqs.txt](static_publication_reqs.txt) | Dependency versions used at the time of publication |

Each results file has one row per dataset and one column per resample.

The results folders are named after the sections of the
[first arXiv version](https://arxiv.org/abs/2305.01429v1) of the paper: Section V-A
(Figures 3 and 4 there), V-B (Figure 5) and V-C (Figure 6). The figure numbers in the
table are those of the published paper, where the regressors from `5.B` and `5.C` are
compared together in Figure 8.

## Datasets

The 63 TSER datasets are available on Zenodo as the
[TSML Extended Time Series Extrinsic Regression Archive 2024](https://zenodo.org/records/11236865)
and from
[Google Drive](https://drive.google.com/file/d/1CXFof3vs6ypcqU5s5aBEZHVe2OtSVvOF/view?usp=sharing).
More information on the datasets is available at
[timeseriesclassification.com](http://www.timeseriesclassification.com).

## Running the experiments

There are two ways to run the code: with the latest versions, or with the versions
recorded at the time of publication. Results from the latest versions may differ from
the published results files, as the algorithms have changed since publication.

### Latest versions

Clone this repository and install the latest `tsml-eval` with all optional estimator
dependencies:

    pip install -r requirements.txt

This is the same as:

    pip install tsml-eval[all_extras,deep_learning]

Not all estimator dependencies are installed by default with `pip install tsml-eval`.
For a smaller install, you can install these individually as required.

Run [run_experiments.py](run_experiments.py) from the repository root with the
following arguments:

1. Path to the data directory
2. Path to the results directory
3. The name of the model to run (see
   [set_tser_exp_regressor.py](set_tser_exp_regressor.py), i.e. Ridge, DrCIF,
   InceptionE)
4. The name of the problem to run
5. The resample number to run (0 is base train/test split)

i.e. to run Covid3Month using linear regression on the base train/test split:

    python run_experiments.py data/ results/ Ridge Covid3Month 0

Running the script without arguments runs ROCKET on a small example dataset included
with `tsml-eval` and writes to `test_output/`.

The code in this repository was last checked in November 2026 with `tsml-eval` 0.7.0,
`aeon` 1.5.0 and `tsml` 0.10.0 on Python 3.12. It is not actively maintained against
new releases.

### As published

The dependency versions recorded at the time of publication include `aeon` 0.3.0 and
`tsml` 0.2.1. The code in this repository has since been updated for newer versions,
so to run the code from that time use the `tsml-eval` repository at the last commit
which used these versions. This requires Python 3.8 to 3.11. Results from this setup
may not match the published results files exactly.

    git clone https://github.com/time-series-machine-learning/tsml-eval.git
    cd tsml-eval
    git checkout 1efd1b46
    pip install -r tsml_eval/publications/y2023/tser_archive_expansion/requirements.txt
    pip install --no-deps .
    python tsml_eval/publications/y2023/tser_archive_expansion/run_experiments.py data/ results/ Ridge Covid3Month 0

The requirements file is the same as
[static_publication_reqs.txt](static_publication_reqs.txt) in this repository. It
was generated on Windows, so `pywin32`, `tensorflow-intel`, `ansicon` and `jinxed`
should be removed on other operating systems.

The `tsml-eval` release available when the paper was first made public was 0.1.0,
which contains an earlier version of this code:

    pip install tsml-eval==0.1.0

## Using the regressors

The regressors used in the experiments are available in the
[aeon](https://github.com/aeon-toolkit/aeon) and
[tsml](https://github.com/time-series-machine-learning/tsml-py) Python packages and
follow the `scikit-learn` interface. See
[tser_archive_expansion.ipynb](tser_archive_expansion.ipynb) for an example, which can
be run online using Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/time-series-machine-learning/tser-archive-expansion-2024/main?filepath=tser_archive_expansion.ipynb)

## Citation

If you use this work, please cite the paper:

```bibtex
@article{guijo2024unsupervised,
  title={Unsupervised feature based algorithms for time series extrinsic regression},
  author={Guijo-Rubio, David and Middlehurst, Matthew and Arcencio, Guilherme and Silva, Diego Furtado and Bagnall, Anthony},
  journal={Data Mining and Knowledge Discovery},
  volume={38},
  pages={2141--2185},
  year={2024},
  publisher={Springer},
  doi={10.1007/s10618-024-01027-w}
}
```

## Contact

For questions about the paper or this repository, contact Matthew Middlehurst at
[m.b.middlehurst@bradford.ac.uk](mailto:m.b.middlehurst@bradford.ac.uk) or on the
[aeon Discord](https://discord.gg/D6rzqHGKRJ) (`matthewmiddlehurst`).
