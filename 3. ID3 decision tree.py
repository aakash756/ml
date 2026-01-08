{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOzaNAWky3crqbyV/kUjKUq",
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
        "<a href=\"https://colab.research.google.com/github/aakash756/ml/blob/main/3.%20ID3%20decision%20tree.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "    def __init__(self, attribute=None, value=None, results=None, true_branch=None,\n",
        "                 false_branch=None):\n",
        "        self.attribute, self.value, self.results, self.true_branch, self.false_branch = attribute, value, results, \\\n",
        "            true_branch, false_branch\n",
        "def build_tree(rows):\n",
        "    if not rows:\n",
        "        return Node()\n",
        "    if len(set(row[-1] for row in rows)) == 1:\n",
        "        return Node(results=rows[0][-1])\n",
        "    num_attributes = len(rows[0]) - 1\n",
        "\n",
        "    best_gain = 0.0\n",
        "    best_attribute_idx = -1\n",
        "\n",
        "    for i in range(num_attributes):\n",
        "        gain = information_gain(rows, i)\n",
        "        if gain > best_gain:\n",
        "            best_gain = gain\n",
        "            best_attribute_idx = i\n",
        "\n",
        "    # If no attribute provides any information gain, create a leaf node with the majority class.\n",
        "    if best_gain == 0.0:\n",
        "        counts = class_counts(rows)\n",
        "        if not counts:\n",
        "            return Node()\n",
        "        majority_class = max(counts, key=counts.get)\n",
        "        return Node(results=majority_class)\n",
        "\n",
        "    split_attribute = best_attribute_idx\n",
        "    split_value = rows[0][split_attribute] # Use the value from the first row for this attribute for binary split\n",
        "\n",
        "    true_rows = [row for row in rows if row[split_attribute] == split_value]\n",
        "    false_rows = [row for row in rows if row[split_attribute] != split_value]\n",
        "\n",
        "    true_branch = build_tree(true_rows)\n",
        "    false_branch = build_tree(false_rows)\n",
        "\n",
        "    return Node(attribute=split_attribute, value=split_value, true_branch=true_branch,\n",
        "                false_branch=false_branch)\n",
        "def information_gain(rows, col):\n",
        "    total_entropy = entropy(rows)\n",
        "    values = set(row[col] for row in rows)\n",
        "    weighted_entropy = sum(len(list(filter(lambda row: row[col] == val, rows))) / len(rows) *\n",
        "                          entropy(list(filter(lambda row: row[col] == val, rows))) for val in values)\n",
        "    return total_entropy - weighted_entropy\n",
        "def entropy(rows):\n",
        "    from math import log2\n",
        "    if not rows:\n",
        "        return 0.0\n",
        "    counts = class_counts(rows)\n",
        "    return -sum((count / len(rows)) * log2(count / len(rows)) for count in counts.values() if count > 0)\n",
        "def class_counts(rows):\n",
        "    counts = {}\n",
        "    for row in rows:\n",
        "        label = row[-1]\n",
        "        if label not in counts:\n",
        "            counts[label] = 0\n",
        "        counts[label] += 1\n",
        "    return counts\n",
        "# Example dataset (you can modify this as needed)\n",
        "dataset = [\n",
        "    ['Sunny', 'Hot', 'High', 'Weak', 'No'],\n",
        "    ['Sunny', 'Hot', 'High', 'Strong', 'No'],\n",
        "    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],\n",
        "    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],\n",
        "    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],\n",
        "    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],\n",
        "    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],\n",
        "    ['Sunny', 'Mild', 'High', 'Weak', 'No'],\n",
        "    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],\n",
        "    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']\n",
        "]\n",
        "# Build the decision tree\n",
        "tree = build_tree(dataset)\n",
        "# Print the decision tree\n",
        "def print_tree(node, indent=\"\"):\n",
        "    if node is None:\n",
        "        return\n",
        "    if node.results is not None:\n",
        "        print(indent + str(node.results))\n",
        "    else:\n",
        "        print(indent + f'Attribute {node.attribute} : {node.value}? ')\n",
        "        print(indent + '--> True:')\n",
        "        print_tree(node.true_branch, indent + ' ')\n",
        "        print(indent + '--> False:')\n",
        "        print_tree(node.false_branch, indent + ' ')\n",
        "print_tree(tree)\n",
        "# Classify a new sample\n",
        "new_sample = ['Sunny', 'Cool', 'High', 'Strong']\n",
        "current_node = tree\n",
        "while current_node.results is None and current_node.attribute is not None:\n",
        "    # Added a check for None current_node to prevent error if tree is malformed or empty\n",
        "    if current_node is None:\n",
        "        break\n",
        "    if new_sample[current_node.attribute] == current_node.value:\n",
        "        current_node = current_node.true_branch\n",
        "    else:\n",
        "        current_node = current_node.false_branch\n",
        "# Ensure current_node is not None before trying to access its results\n",
        "classification_result = current_node.results if current_node else None\n",
        "print(f\"\\nClassification result for {new_sample}: {classification_result}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DGYIQktjnf85",
        "outputId": "0527cfae-68cb-419c-b6a5-53bff323c25f"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Attribute 3 : Weak? \n",
            "--> True:\n",
            " Attribute None : None? \n",
            " --> True:\n",
            " --> False:\n",
            "--> False:\n",
            " Attribute None : None? \n",
            " --> True:\n",
            " --> False:\n",
            "\n",
            "Classification result for ['Sunny', 'Cool', 'High', 'Strong']: None\n"
          ]
        }
      ]
    }
  ]
}