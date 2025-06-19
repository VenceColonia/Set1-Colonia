{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "1b1569f5-c49f-4f1a-8ea3-903131869be2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def savings(gross_pay, tax_rate, expenses):\n",
    "    after_tax_pay = gross_pay * (1 - tax_rate)\n",
    "    take_home_pay = after_tax_pay - expenses\n",
    "    return int(take_home_pay)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7963aa70-8eb7-4cff-b00d-26868e2eb57c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "990 kg\n"
     ]
    }
   ],
   "source": [
    "def material_waste(total_material, material_units, num_jobs, job_consumption):\n",
    "    total_material_consumption = num_jobs*job_consumption\n",
    "    remaining_total_material = total_material - total_material_consumption\n",
    "    return f\"{remaining_total_material} {material_units}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "69d13c0a-0797-4c84-88f1-e15a544a9e78",
   "metadata": {},
   "outputs": [],
   "source": [
    "def interest(principal,rate,periods):\n",
    "    simple_interest = principal*(rate*periods)\n",
    "    final_investment_value = principal + simple_interest//1\n",
    "    return int(final_investment_value)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "824d1d73-a2e7-4c24-a31e-fbee28165cd8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
