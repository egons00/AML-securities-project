-- 1st Query 
SELECT
    bal.date
  , cat.category_name
  , bal.security_code
  , sec.isin
  , secp.company_name
  , bal.currency
  , bal.daily_balance_eur AS daily_balance
    FROM schema.balance                       bal
             LEFT JOIN schema.category        cat ON bal.category_id = cat.category_id
             LEFT JOIN schema.sec_master      sec ON bal.security_code = sec.security_code
             LEFT JOIN schema.sec_master_comp secp ON secp.security_code = sec.security_code
    WHERE 1 = 1
      AND bal.date = '2021-03-01'
;


-- 2nd Query 
WITH sec_info AS (
    SELECT
        bal.date
      , cat.category_name
      , bal.security_code
      , sec.isin
      , secp.company_name
      , bal.currency
      , bal.daily_balance_eur AS daily_balance
        FROM schema.balance                       bal
                 LEFT JOIN schema.category        cat ON bal.category_id = cat.category_id
                 LEFT JOIN schema.sec_master      sec ON bal.security_code = sec.security_code
                 LEFT JOIN schema.sec_master_comp secp ON secp.security_code = sec.security_code
        WHERE 1 = 1
          AND bal.date = '2021-03-01'
)
SELECT
    date               AS date
  , category_name      AS category_name
  , currency           AS currency
  , SUM(daily_balance) AS total_daoly_balance_eur
    FROM sec_info
    WHERE 1 = 1
      AND isin NOT LIKE 'XS%'
      -- Like is very resource heavy, so I added other options that can be used too.
      -- AND LEFT(isin, 2) != 'XS'
      -- AND SUBSTRING(isin, 1, 2) != 'XS'
    GROUP BY 1, 2, 3