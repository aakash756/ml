{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMq0q0fJG29/dETcRcszJ93",
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
        "<a href=\"https://colab.research.google.com/github/aakash756/ml/blob/main/10.%20Expectation%20%26%20Maximization%20Algorithm.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "from scipy.stats import norm\n",
        "# Generate some sample data\n",
        "np.random.seed(42)\n",
        "data = np.concatenate([np.random.normal(0, 1, 100), np.random.normal(5, 1, 100)])\n",
        "# Initialize parameters\n",
        "mu1, mu2 = np.random.rand(2) * 10\n",
        "sigma1, sigma2 = np.random.rand(2) * 5\n",
        "pi = 0.5\n",
        "# EM algorithm\n",
        "for _ in range(100):\n",
        " # Expectation step\n",
        " likelihood1 = norm.pdf(data, mu1, sigma1)\n",
        " likelihood2 = norm.pdf(data, mu2, sigma2)\n",
        " weight1 = pi * likelihood1 / (pi * likelihood1 + (1 - pi) * likelihood2)\n",
        " weight2 = 1 - weight1\n",
        " # Maximization step\n",
        " mu1 = np.sum(weight1 * data) / np.sum(weight1)\n",
        " mu2 = np.sum(weight2 * data) / np.sum(weight2)\n",
        " sigma1 = np.sqrt(np.sum(weight1 * (data - mu1)**2) / np.sum(weight1))\n",
        " sigma2 = np.sqrt(np.sum(weight2 * (data - mu2)**2) / np.sum(weight2))\n",
        " pi = np.mean(weight1)\n",
        "# Print the final parameters\n",
        "print(\"Final Parameters:\")\n",
        "print(f\"Cluster 1 - Mean: {mu1:.2f}, Standard Deviation: {sigma1:.2f}\")\n",
        "print(f\"Cluster 2 - Mean: {mu2:.2f}, Standard Deviation: {sigma2:.2f}\")\n",
        "print(f\"Cluster Weights - Cluster 1: {pi:.2f}, Cluster 2: {1 - pi:.2f}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NiCWVZi_8TOP",
        "outputId": "b68b58c1-b87a-4801-f669-46f2164bd9ea"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Final Parameters:\n",
            "Cluster 1 - Mean: 5.02, Standard Deviation: 0.95\n",
            "Cluster 2 - Mean: -0.10, Standard Deviation: 0.90\n",
            "Cluster Weights - Cluster 1: 0.50, Cluster 2: 0.50\n"
          ]
        }
      ]
    }
  ]
}