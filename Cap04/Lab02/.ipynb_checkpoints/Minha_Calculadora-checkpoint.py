{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "************Minha Calculadora em Python*************\n",
      "\n",
      "O que você quer fazer?\n",
      "1 - Somar\n",
      "2 - Subtrair\n",
      "3 - Multiplicar\n",
      "4 - Dividir\n",
      "\n",
      "Digite o número da opção escolhida: 5\n",
      "\n",
      "Digite o primeiro número: 6\n",
      "\n",
      "Digite o segundo número: 7\n",
      "\n",
      "Dificil escolher entre 4 opções de operação? Mas tudo bem... Tenta começar de novo.\n",
      "\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"\\n************Minha Calculadora em Python*************\")\n",
    "\n",
    "def add (x, y):\n",
    "    return x + y\n",
    "\n",
    "def subtract (x, y):\n",
    "    return x - y\n",
    "\n",
    "def multiply (x, y):\n",
    "    return x * y\n",
    "\n",
    "def divide (x, y):\n",
    "    return x / y\n",
    "\n",
    "print(\"\\nO que você quer fazer?\")\n",
    "print(\"1 - Somar\")\n",
    "print(\"2 - Subtrair\")\n",
    "print(\"3 - Multiplicar\")\n",
    "print(\"4 - Dividir\")\n",
    "\n",
    "escolha = input(\"\\nDigite o número da opção escolhida: \")\n",
    "\n",
    "num1 = int(input(\"\\nDigite o primeiro número: \"))\n",
    "num2 = int(input(\"\\nDigite o segundo número: \"))\n",
    "\n",
    "if escolha == '1':\n",
    "    print(\"\\n\")\n",
    "    print(num1, \"+\", num2, \"=\", add(num1, num2))\n",
    "    print(\"\\n\")\n",
    "\n",
    "    \n",
    "elif escolha == '2':\n",
    "    print(\"\\n\")\n",
    "    print(num1, \"-\", num2, \"=\", subtract(num1, num2))\n",
    "    print(\"\\n\")\n",
    "    \n",
    "elif escolha == '3':\n",
    "    print(\"\\n\")\n",
    "    print(num1, \"*\", num2, \"=\", multiply(num1, num2))\n",
    "    print(\"\\n\")\n",
    "    \n",
    "elif escolha == '4':\n",
    "    print(\"\\n\")\n",
    "    print(num1, \"/\", num2, \"=\", divide(num1, num2))\n",
    "    print(\"\\n\")\n",
    "    \n",
    "else:\n",
    "    print(\"\\nDificil escolher entre 4 opções de operação? Mas tudo bem... Tenta começar de novo.\\n\")\n",
    "    print(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
