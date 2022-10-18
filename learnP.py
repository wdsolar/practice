{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "时间       object\n",
      "开盘      float64\n",
      "最高      float64\n",
      "最低      float64\n",
      "收盘      float64\n",
      "涨幅       object\n",
      "振幅       object\n",
      "总手       object\n",
      "金额       object\n",
      "换手%     float64\n",
      "成交次数      int64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df=pd.read_csv('.\\\\aa.csv',sep=',')\n",
    "\n",
    "print(df.dtypes)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.7 64-bit",
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
   "version": "3.9.7"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "e67a811310adfdf44927177fcf7e976d4bed0092255d654900fc30405dc0716e"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
