{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNYmbEyPfb9/ZCCJ1Kw3CgY",
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
        "<a href=\"https://colab.research.google.com/github/aakash756/ml/blob/main/13.%20Car%20Price%20Prediction%20Model.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eEddAOHHybI9",
        "outputId": "14d81a74-b087-44f3-ca5e-fe2501d80f3a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mean Squared Error: 177777775.21\n",
            "Predicted Price for the New Car: $38,333.33\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.metrics import mean_squared_error\n",
        "# Sample car dataset (for demonstration purposes)\n",
        "# You should replace this with a more extensive and relevant dataset\n",
        "car_features = np.array([[2000, 150000, 4], [2010, 80000, 2], [2015, 50000, 1]])\n",
        "car_prices = np.array([5000, 15000, 25000])\n",
        "# Split the dataset into training and testing sets\n",
        "X_train, X_test, y_train, y_test = train_test_split(car_features, car_prices, test_size=0.2,\n",
        "random_state=42)\n",
        "# Initialize and train the Linear Regression model\n",
        "linear_regression_model = LinearRegression()\n",
        "linear_regression_model.fit(X_train, y_train)\n",
        "# Make predictions on the test set\n",
        "y_pred = linear_regression_model.predict(X_test)\n",
        "# Display mean squared error (for simplicity, not accuracy)\n",
        "mse = mean_squared_error(y_test, y_pred)\n",
        "print(f\"Mean Squared Error: {mse:.2f}\")\n",
        "# Example: Predict the price for a new car\n",
        "new_car_features = np.array([[2022, 10000, 2]])\n",
        "predicted_price = linear_regression_model.predict(new_car_features)\n",
        "print(f\"Predicted Price for the New Car: ${predicted_price[0]:,.2f}\")"
      ]
    }
  ]
}