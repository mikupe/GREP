{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['/opt/jupyter/.venv/lib/python3.5/site-packages/ipykernel_launcher.py', '-f', '/home/petrming/.local/share/jupyter/runtime/kernel-c3249ebf-8127-412e-86ea-53da89af3620.json']\n"
     ]
    }
   ],
   "source": [
    "#!/opt/pyenv/---\n",
    "#!/bin/env python3\n",
    "\n",
    "import sys\n",
    "    \n",
    "#pattern = sys.argv[1]\n",
    "#filename = sys.argv[2]\n",
    "\n",
    "pattern, path = sys.argv[1:]\n",
    "            \n",
    "with open(filename) as f:\n",
    "    for line in f:\n",
    "        if pattern in line:\n",
    "            print(line, end=\"\")\n",
    "\n",
    "\n",
    "#def main():\n",
    "   \n",
    "\n",
    "#if __name__ == \"__main__\":\n",
    "#    main()\n",
    "\n",
    " "
   ]
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
