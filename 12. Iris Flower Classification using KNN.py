{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNqqkRPhsQvuhZz/3J6qUxd",
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
        "<a href=\"https://colab.research.google.com/github/aakash756/ml/blob/main/12.%20Iris%20Flower%20Classification%20using%20KNN.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.datasets import load_iris\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.neighbors import KNeighborsClassifier\n",
        "from sklearn.metrics import accuracy_score\n",
        "import numpy as np\n",
        "X, y = load_iris(return_X_y=True)\n",
        "np.random.seed(42)\n",
        "y_noisy = y.copy()\n",
        "mask = np.random.choice([True, False], size=len(y), p=[0.1, 0.9])\n",
        "y_noisy[mask] = np.random.randint(0, 3, size=np.sum(mask))\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y_noisy, test_size=0.2, random_state=42)\n",
        "knn_classifier = KNeighborsClassifier(n_neighbors=3)\n",
        "knn_classifier.fit(X_train, y_train)\n",
        "y_pred = knn_classifier.predict(X_test)\n",
        "accuracy = accuracy_score(y_test, y_pred)*100\n",
        "print(f\"Accuracy: {accuracy:.2f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y5CkTl1T89lf",
        "outputId": "007c8b5b-5f20-4b2e-8c7e-e038ff35fd40"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 90.00\n"
          ]
        }
      ]
    }
  ]
}