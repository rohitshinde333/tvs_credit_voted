# tvs_credit_voted

### Step 1
- `python -m venv venv`

### Step 2
- `pip install -r requirements.txt`

### Step 3
- `python .\api.py`

### Step 4
- `localhost:5000/predict` with json 
- {
    "RevolvingUtilizationOfUnsecuredLines": 0.964673,
    "age": 40,
    "NumberOfTime30-59DaysPastDueNotWorse": 3,
    "DebtRatio": 0.382965,
    "MonthlyIncome": 13700,
    "NumberOfOpenCreditLinesAndLoans": 9,
    "NumberOfTimes90DaysLate": 3,
    "NumberRealEstateLoansOrLines": 1,
    "NumberOfTime60-89DaysPastDueNotWorse": 1,
    "NumberOfDependents": 2
 }
