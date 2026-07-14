"""
Evaluation utilities for classification experiments.
"""

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)


def evaluate_classification(y_true, y_pred, y_prob):
    """
    Compute classification metrics for a single train/test split.

    Parameters
    ----------
    y_true : array-like
        True class labels.
    y_pred : array-like
        Predicted class labels.
    y_prob : array-like of shape (n_samples, n_classes)
        Predicted class probabilities.

    Returns
    -------
    dict
        Dictionary containing evaluation metrics.
    """

    return {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Macro Precision": precision_score(
            y_true,
            y_pred,
            average="macro",
            zero_division=0,
        ),
        "Macro Recall": recall_score(
            y_true,
            y_pred,
            average="macro",
            zero_division=0,
        ),
        "Macro F1": f1_score(
            y_true,
            y_pred,
            average="macro",
            zero_division=0,
        ),
        "Macro ROC AUC": roc_auc_score(
            y_true,
            y_prob,
            multi_class="ovr",
            average="macro",
        ),
    }


def summarize_results(results):
    """
    Compute mean and standard deviation of evaluation metrics.

    Parameters
    ----------
    results : list of dict
        One dictionary of evaluation metrics per cross-validation split.

    Returns
    -------
    pandas.DataFrame
        Summary table containing the mean and standard deviation
        of each evaluation metric.
    """

    results = pd.DataFrame(results)

    summary = results.agg(["mean", "std"]).T
    summary.columns = ["Mean", "Std"]

    return summary
