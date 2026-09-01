--- PROJECT 5: Supply Chain Warehouse Velocity Tracker

CREATE DATABASE Warehouse_Velocity_DB;
USE Warehouse_Velocity_DB;

CREATE TABLE warehouse_bays (
    bay_id INT PRIMARY KEY,
    aisle_number INT,
    storage_zone VARCHAR(50)
);

CREATE TABLE stock_velocity (
    velocity_id INT PRIMARY KEY,
    bay_id INT,
    stagnant_days INT,
    item_sku_text VARCHAR(50)
);

INSERT INTO warehouse_bays (bay_id, aisle_number, storage_zone) VALUES
(501, 12, 'Cold-Storage'),
(502, 14, 'Ambient'),
(503, 15, 'High-Density'),
(504, 12, 'Cold-Storage'),
(505, 18, 'Ambient');

INSERT INTO stock_velocity (velocity_id, bay_id, stagnant_days, item_sku_text) VALUES
(9901, 501, 45, 'SKU-101'),
(9902, 502, 12, 'SKU-102'),
(9903, 503, 78, 'SKU-103'),
(9904, 504, 55, 'SKU-104'),
(9905, 505, 5, 'SKU-105');


--- Milestone 1: The High-Risk Stagnant Zone Audit Ledger
SELECT warehouse_bays.storage_zone, SUM(stock_velocity.stagnant_days) AS total_stagnant_days
FROM warehouse_bays
INNER JOIN stock_velocity
ON warehouse_bays.bay_id = stock_velocity.bay_id
WHERE stock_velocity.stagnant_days > 10
GROUP BY warehouse_bays.storage_zone
HAVING total_stagnant_days > 60 ;

--- MILESTONE 2: The Multi-Tier Inventory Velocity Matrix
SELECT warehouse_bays.storage_zone, warehouse_bays.aisle_number, stock_velocity.stagnant_days,
CASE
  WHEN stock_velocity.stagnant_days >= 60 THEN 'Critical Stagnancy - Immediate Purge Required'
  WHEN stock_velocity.stagnant_days >= 30 THEN 'Slow Moving - Run Promotion'
ELSE 'Optimal Turnover Speeds'
END AS operational_velocity_grade
FROM warehouse_bays
INNER JOIN stock_velocity
ON warehouse_bays.bay_id = stock_velocity.bay_id ;

--- MILESTONE 3: The Ultimate Warehouse Velocity CTE Summary
WITH classified_velocity_feed AS (
SELECT warehouse_bays.storage_zone, warehouse_bays.aisle_number, stock_velocity.stagnant_days,
CASE
  WHEN stock_velocity.stagnant_days >= 60 THEN 'Critical Stagnancy - Immediate Purge Required'
  WHEN stock_velocity.stagnant_days >= 30 THEN 'Slow Moving - Run Promotion'
ELSE 'Optimal Turnover Speeds'
END AS operational_velocity_grade
FROM warehouse_bays
INNER JOIN stock_velocity
ON warehouse_bays.bay_id = stock_velocity.bay_id 
)
SELECT operational_velocity_grade,
       COUNT(*) AS total_bays_allocated,
       SUM(stagnant_days) AS cumulative_stagnant_days
FROM classified_velocity_feed
GROUP BY operational_velocity_grade ;