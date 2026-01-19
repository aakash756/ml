{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN1Mmc3M6/Re5s/0RKVD4Jd",
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
        "<a href=\"https://colab.research.google.com/github/aakash756/ml/blob/main/8.%20Linear%20regression.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.datasets import load_iris\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.metrics import accuracy_score\n",
        "import numpy as np\n",
        "# Load the iris dataset\n",
        "X, y = load_iris(return_X_y=True)\n",
        "# Convert the problem into a binary classification task\n",
        "y_binary = (y == 0).astype(int) # 1 if class 0 (setosa), 0 otherwise\n",
        "# Introduce more random noise to target values\n",
        "np.random.seed(42)\n",
        "y_noisy = y_binary + np.random.normal(scale=0.4, size=len(y_binary))\n",
        "# Split the dataset into training and testing sets\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, (y_noisy >= 0.5).astype(int), test_size=0.2,\n",
        "random_state=42)\n",
        "# Initialize and train the Linear Regression model\n",
        "linear_regression_model = LinearRegression().fit(X_train, y_train)\n",
        "# Make predictions on the test set\n",
        "y_pred = linear_regression_model.predict(X_test)\n",
        "y_pred_binary = (y_pred >= 0.5).astype(int) # Convert predicted probabilities to binary\n",
        "# Display accuracy\n",
        "accuracy = accuracy_score(y_test, y_pred_binary) * 100\n",
        "print(f\"Accuracy: {accuracy:.2f}%\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YG0d6LIv7-XP",
        "outputId": "825ae02e-cec2-4ec4-9c72-534bb6602dca"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 86.67%\n"
          ]
        }
      ]
    }
  ]
}