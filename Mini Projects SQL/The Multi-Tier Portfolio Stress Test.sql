CREATE DATABASE BANK ;
  USE BANK ;
  
  
CREATE TABLE bank_accounts (
    account_id INT PRIMARY KEY,
    client_name VARCHAR(50),
    risk_score INT
);

CREATE TABLE loan_balances (
    account_id INT PRIMARY KEY,
    outstanding_debt DECIMAL(12,2),
    loan_type VARCHAR(50)
);

INSERT INTO bank_accounts (account_id, client_name, risk_score) VALUES
(9001, 'Arjun', 780),
(9002, 'Neha', 520),
(9003, 'Vikram', 690),
(9004, 'Ananya', 450);

INSERT INTO loan_balances (account_id, outstanding_debt, loan_type) VALUES
(9001, 250000.00, 'Mortgage'),
(9002, 45000.00, 'Personal'),
(9003, 12000.00, 'Auto'),
(9004, 85000.00, 'Personal');


SELECT bank_accounts.client_name, SUM(loan_balances.outstanding_debt) AS portfolio_exposure
FROM bank_accounts
INNER JOIN loan_balances
  ON bank_accounts.account_id = loan_balances.account_id
WHERE bank_accounts.risk_score < 600
GROUP BY bank_accounts.client_name ;


SELECT bank_accounts.client_name, loan_balances.outstanding_debt,
  CASE
    WHEN bank_accounts.risk_score >= 750 THEN 'Tier 1 Prime'
    WHEN bank_accounts.risk_score >= 650 THEN 'Tier 2 Mid-Grade'
    ELSE 'Tier 3 Subprime'
  END AS credit_risk_classification
FROM bank_accounts
INNER JOIN loan_balances
  ON bank_accounts.account_id = loan_balances.account_id ;

WITH classified_portfolio AS (
SELECT bank_accounts.client_name, loan_balances.outstanding_debt,
  CASE
    WHEN bank_accounts.risk_score >= 750 THEN 'Tier 1 Prime'
    WHEN bank_accounts.risk_score >= 650 THEN 'Tier 2 Mid-Grade'
    ELSE 'Tier 3 Subprime'
  END AS credit_risk_classification
FROM bank_accounts
INNER JOIN loan_balances
  ON bank_accounts.account_id = loan_balances.account_id 
) 
SELECT credit_risk_classification, COUNT(*) AS account_count, SUM(outstanding_debt) AS total_tier_debt
FROM classified_portfolio
GROUP BY credit_risk_classification ;


