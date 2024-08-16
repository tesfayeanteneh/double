{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyMfkTwmfujTp1SRvNgd/1Eq",
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
        "<a href=\"https://colab.research.google.com/github/tesfayeanteneh/double/blob/main/double_pendulum.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import casadi as ca\n",
        "import numpy as np\n",
        "\n",
        "def double_pendulum_dynamics():\n",
        "    # Define symbolic variables\n",
        "    q1 = ca.SX.sym('q1')\n",
        "    q2 = ca.SX.sym('q2')\n",
        "    dq1 = ca.SX.sym('dq1')\n",
        "    dq2 = ca.SX.sym('dq2')\n",
        "    u1 = ca.SX.sym('u1')\n",
        "    u2 = ca.SX.sym('u2')\n",
        "    x = ca.vertcat(q1, q2, dq1, dq2)\n",
        "    u = ca.vertcat(u1, u2)\n",
        "\n",
        "    # Constants\n",
        "    l1 = 1.0\n",
        "    l2 = 1.0\n",
        "    m1 = 1.0\n",
        "    m2 = 1.0\n",
        "    g = 9.81\n",
        "\n",
        "    # Equations of motion\n",
        "    ddq1 = (l1**2 * l2 * m2 * dq1**2 * ca.sin(-2 * q2 + 2 * q1) +\n",
        "            2 * u2 * ca.cos(-q2 + q1) * l1 +\n",
        "            2 * (g * ca.sin(-2 * q2 + q1) * l1 * m2 / 2 +\n",
        "                 ca.sin(-q2 + q1) * dq2**2 * l1 * l2 * m2 +\n",
        "                 g * l1 * (m1 + m2 / 2) * ca.sin(q1) - u1) * l2) / (\n",
        "            l1**2 * l2 * (m2 * ca.cos(-2 * q2 + 2 * q1) - 2 * m1 - m2))\n",
        "\n",
        "    ddq2 = (-g * l1 * l2 * m2 * (m1 + m2) * ca.sin(-q2 + 2 * q1) -\n",
        "            l1 * l2**2 * m2**2 * dq2**2 * ca.sin(-2 * q2 + 2 * q1) -\n",
        "            2 * dq1**2 * l1**2 * l2 * m2 * (m1 + m2) * ca.sin(-q2 + q1) +\n",
        "            2 * u1 * ca.cos(-q2 + q1) * l2 * m2 +\n",
        "            l1 * (m1 + m2) * (ca.sin(q2) * g * l2 * m2 - 2 * u2)) / (\n",
        "            l2**2 * l1 * m2 * (m2 * ca.cos(-2 * q2 + 2 * q1) - 2 * m1 - m2))\n",
        "\n",
        "    dx = ca.vertcat(dq1, dq2, ddq1, ddq2)\n",
        "    return ca.Function('f', [x, u], [dx])\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    f = double_pendulum_dynamics()\n",
        "    x0 = np.array([-0.8, 0.0, 0.0, 0.0])\n",
        "    u0 = np.array([0.0, 0.0])\n",
        "    print(\"State derivative at x0, u0:\", f(x0, u0))\n"
      ],
      "metadata": {
        "id": "DppHqDyz7VLk",
        "outputId": "c0383b90-01ba-48f3-c2ba-20a9740ecd4a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "State derivative at x0, u0: [0, 0, 9.29257, -6.4742]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ZEMoFjI37VHo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "XnfirWa57VCh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "SkFrot4v7U05"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}