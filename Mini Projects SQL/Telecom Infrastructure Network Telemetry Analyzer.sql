-- Telecom Infrastructure Network Telemetry Analyzer :-

CREATE DATABASE TELECOM;
USE TELECOM;

CREATE TABLE network_nodes (
    node_id INT PRIMARY KEY,
    location_region VARCHAR(50),
    hardware_generation VARCHAR(50)
);

CREATE TABLE node_telemetry (
    log_id INT PRIMARY KEY,
    node_id INT,
    data_payload_gb VARCHAR(50), -- Stored as text string on purpose!
    error_logs_count INT
);

INSERT INTO network_nodes (node_id, location_region, hardware_generation) VALUES
(701, 'North-HQ', '5G Core'),
(702, 'South-Hub', '4G LTE'),
(703, 'West-Node', '5G Core'),
(704, 'East-Branch', '4G LTE');

INSERT INTO node_telemetry (log_id, node_id, data_payload_gb, error_logs_count) VALUES
(11, 701, '2500', 0),
(12, 701, '3100', 2),
(13, 702, '850', 14),
(14, 703, '4200', 1),
(15, 704, '900', 22);


-- 1. Multi-Clause Overlapping Mutation Ledger
SELECT network_nodes.location_region, SUM(CAST(node_telemetry.data_payload_gb AS SIGNED)) AS total_bandwidth_used 
FROM network_nodes
INNER JOIN node_telemetry
ON network_nodes.node_id = node_telemetry.node_id
GROUP BY network_nodes.location_region
HAVING SUM(CAST(node_telemetry.data_payload_gb AS SIGNED)) > 2000 ;

-- 2. The Structural Network Health Evaluation Matrix
SELECT network_nodes.location_region, network_nodes.hardware_generation, node_telemetry.error_logs_count,
  CASE
    WHEN node_telemetry.error_logs_count > 15 THEN 'Critical Network Outage'
    WHEN node_telemetry.error_logs_count > 0 THEN 'Intermittent Maintenance Required'
    ELSE 'Fully Operational' 
  END AS node_stability_status
FROM network_nodes
INNER JOIN node_telemetry
ON network_nodes.node_id = node_telemetry.node_id ;

-- 3. The Ultimate Virtual Infrastructure CTE Summary
WITH network_health_feed AS (
SELECT network_nodes.location_region, network_nodes.hardware_generation, node_telemetry.error_logs_count,
       CAST(node_telemetry.data_payload_gb AS SIGNED) AS processed_gb,
  CASE
    WHEN node_telemetry.error_logs_count > 15 THEN 'Critical Network Outage'
    WHEN node_telemetry.error_logs_count > 0 THEN 'Intermittent Maintenance Required'
    ELSE 'Fully Operational' 
  END AS node_stability_status
FROM network_nodes
INNER JOIN node_telemetry
ON network_nodes.node_id = node_telemetry.node_id
)
SELECT node_stability_status,
       COUNT(*) AS total_logs_logged, 
       SUM(processed_gb) AS cumulative_bandwidth_gb
GROUP BY node_stability_status
