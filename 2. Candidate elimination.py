{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM9Hd0/MPjTYbVHpug9KJSh",
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
        "<a href=\"https://colab.research.google.com/github/aakash756/ml/blob/main/2.%20Candidate%20elimination.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import copy\n",
        "def initialize_hypotheses(n):\n",
        "    hypotheses = []\n",
        "    specific_hypothesis = ['0'] * n\n",
        "    general_hypothesis = ['?'] * n\n",
        "    hypotheses.append(specific_hypothesis)\n",
        "    hypotheses.append(general_hypothesis)\n",
        "    return hypotheses\n",
        "def candidate_elimination(training_data):\n",
        "    num_attributes = len(training_data[0]) - 1\n",
        "    hypotheses = initialize_hypotheses(num_attributes)\n",
        "\n",
        "    for example in training_data:\n",
        "        if example[-1] == 'Yes':\n",
        "            for i in range(num_attributes):\n",
        "                if hypotheses[0][i] != '0' and hypotheses[0][i] != example[i]:\n",
        "                    hypotheses[0][i] = '?'\n",
        "            # Note: 'i' here will be the last value from the previous loop, which might be a logical flaw in the original code's intent.\n",
        "            # The `hypotheses.remove(h)` modifies the list while iterating, so iterating over a copy is safer.\n",
        "            # To preserve original logic, we will keep iterating on the original list for simplicity of indentation fix,\n",
        "            # but this might lead to unexpected behavior if list is modified during iteration.\n",
        "            for h in hypotheses[1:]:\n",
        "                if h[i] != '?' and h[i] != example[i]:\n",
        "                    hypotheses.remove(h)\n",
        "        else:\n",
        "            temp_hypotheses = copy.deepcopy(hypotheses)\n",
        "            for h in temp_hypotheses:\n",
        "                if h[:-1] != example[:-1] + ['?']:\n",
        "                    if h in hypotheses: # Check if h is still in the original list before attempting to remove\n",
        "                        hypotheses.remove(h)\n",
        "                for i in range(num_attributes):\n",
        "                    if example[i] != h[i] and h[i] != '?':\n",
        "                        new_hypothesis = copy.deepcopy(h)\n",
        "                        new_hypothesis[i] = '?'\n",
        "                        if new_hypothesis not in hypotheses:\n",
        "                            hypotheses.append(new_hypothesis)\n",
        "    return hypotheses\n",
        "\n",
        "training_data = [\n",
        "    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],\n",
        "    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],\n",
        "    ['Rainy', 'Cold', 'High', 'Weak', 'Cool', 'Change', 'No'],\n",
        "    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']\n",
        "]\n",
        "result_hypotheses = candidate_elimination(training_data)\n",
        "print(\"Result Hypotheses:\")\n",
        "for h in result_hypotheses:\n",
        "    print(h)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "auvljtaRm0pq",
        "outputId": "34e7e00b-0406-48ee-b5df-db349b5d49a4"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result Hypotheses:\n",
            "['?', '0', '0', '0', '0', '0']\n",
            "['0', '0', '0', '0', '0', '?']\n"
          ]
        }
      ]
    }
  ]
}