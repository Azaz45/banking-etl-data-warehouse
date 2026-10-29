
-- 1. Total successful transaction amount
SELECT SUM(amount) AS total_successful_amount
FROM transactions
WHERE status = 'Success';

-- 2. Transaction count by type
SELECT transaction_type, COUNT(*) AS total_transactions
FROM transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;

-- 3. Daily transaction summary
SELECT transaction_date,
       COUNT(*) AS transaction_count,
       SUM(amount) AS total_amount
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date;

-- 4. Top 10 customers by transaction amount
SELECT customer_id,
       SUM(amount) AS total_amount,
       COUNT(*) AS transaction_count
FROM transactions
WHERE status = 'Success'
GROUP BY customer_id
ORDER BY total_amount DESC
LIMIT 10;

-- 5. Transaction status summary
SELECT status, COUNT(*) AS total_transactions
FROM transactions
GROUP BY status;
