CREATE DATABASE SaaS_Billing_DB;
USE SaaS_Billing_DB;

CREATE TABLE subscribers (
    account_id INT PRIMARY KEY,
    company_name VARCHAR(50),
    onboarding_region VARCHAR(10)
);

CREATE TABLE billing_cycles (
    cycle_id INT PRIMARY KEY,
    account_id INT,
    mrr_amount DECIMAL(10,2),
    account_status VARCHAR(20)
);

INSERT INTO subscribers (account_id, company_name, onboarding_region) VALUES
(201, 'AlphaTech', 'NA'),
(202, 'BetaLabs', 'EMEA'),
(203, 'GammaSystems', 'APAC'),
(204, 'DeltaData', 'NA'),
(205, 'EpsilonCloud', 'EMEA');

INSERT INTO billing_cycles (cycle_id, account_id, mrr_amount, account_status) VALUES
(8001, 201, 4500.00, 'Active'),
(8002, 202, 1200.00, 'Churned'),
(8003, 203, 8500.00, 'Active'),
(8004, 204, 3200.00, 'Active'),
(8005, 205, 9800.00, 'Pending');

SELECT subscribers.company_name, SUM(billing_cycles.mrr_amount) AS total_contract_value
FROM subscribers
INNER JOIN billing_cycles
ON subscribers.account_id = billing_cycles.account_id
WHERE subscribers.onboarding_region = 'NA' AND billing_cycles.account_status = 'Active'
GROUP BY subscribers.company_name ;

SELECT subscribers.company_name, billing_cycles.mrr_amount,
CASE
  WHEN billing_cycles.mrr_amount >= 7500.00 THEN 'Enterprise Tier'
  WHEN billing_cycles.mrr_amount >= 4000.00 THEN 'Mid-Market Premier Tier'
ELSE 'Standard Growth Tier' 
END AS revenue_account_classification
FROM subscribers
INNER JOIN billing_cycles
ON subscribers.account_id = billing_cycles.account_id ;

WITH classified_revenue_feed AS (
  SELECT subscribers.company_name, billing_cycles.mrr_amount,
CASE
  WHEN billing_cycles.mrr_amount >= 7500.00 THEN 'Enterprise Tier'
  WHEN billing_cycles.mrr_amount >= 4000.00 THEN 'Mid-Market Premier Tier'
ELSE 'Standard Growth Tier' 
END AS revenue_account_classification
FROM subscribers
INNER JOIN billing_cycles
ON subscribers.account_id = billing_cycles.account_id 
)
SELECT 
      revenue_account_classification, 
      COUNT(*) AS total_account_count, 
      SUM(mrr_amount) AS cumulative_mrr_volume
FROM classified_revenue_feed
GROUP BY revenue_account_classification ;


