{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNY9TTbVV11QSdusQazl8W0",
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
        "<a href=\"https://colab.research.google.com/github/aakash756/ml/blob/main/15.%20Iris%20Flower%20Classification%20using%20Naive%20Bayes%20classifier.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.datasets import load_iris\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.naive_bayes import GaussianNB\n",
        "from sklearn.metrics import accuracy_score\n",
        "import numpy as np\n",
        "# Load the iris dataset\n",
        "X, y = load_iris(return_X_y=True)\n",
        "# Introduce some random noise to the labels\n",
        "np.random.seed(42)\n",
        "y_noisy = y.copy()\n",
        "mask = np.random.choice([True, False], size=len(y), p=[0.1, 0.9])\n",
        "y_noisy[mask] = np.random.randint(0, 3, size=np.sum(mask))\n",
        "# Split the dataset into training and testing sets\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y_noisy, test_size=0.2, random_state=42)\n",
        "# Initialize and train the Gaussian Naive Bayes classifier\n",
        "naive_bayes_classifier = GaussianNB()\n",
        "naive_bayes_classifier.fit(X_train, y_train)\n",
        "# Make predictions on the test set\n",
        "y_pred = naive_bayes_classifier.predict(X_test)\n",
        "# Display accuracy\n",
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "print(f\"Accuracy: {accuracy:.2f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aOTFvegB1vBe",
        "outputId": "56fa5d90-bfb3-4337-d932-573ebb7a07e9"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 0.87\n"
          ]
        }
      ]
    }
  ]
}