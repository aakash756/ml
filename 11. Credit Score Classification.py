{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP0c++rFbdPW+CMA8JEgAPX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aakash756/ml/blob/main/11.%20Credit%20Score%20Classification.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.metrics import accuracy_score, classification_report\n",
        "from sklearn.datasets import make_classification\n",
        "X, y = make_classification(n_samples=1000, n_features=5, n_informative=3, n_redundant=1,\n",
        "random_state=42)\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
        "decision_tree_classifier = DecisionTreeClassifier()\n",
        "decision_tree_classifier.fit(X_train, y_train)\n",
        "y_pred = decision_tree_classifier.predict(X_test)\n",
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "print(f\"Accuracy: {accuracy:.2f}\")\n",
        "print(\"Classification Report:\")\n",
        "print(classification_report(y_test, y_pred))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "imJ5Uhfk9lTP",
        "outputId": "a662011c-c6e9-44be-bb14-f46ec688a85a"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 0.95\n",
            "Classification Report:\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.94      0.94      0.94        87\n",
            "           1       0.96      0.96      0.96       113\n",
            "\n",
            "    accuracy                           0.95       200\n",
            "   macro avg       0.95      0.95      0.95       200\n",
            "weighted avg       0.95      0.95      0.95       200\n",
            "\n"
          ]
        }
      ]
    }
  ]
}