-- This script prints the full description of the table
SELECT CONCAT('Table ', TABLE_NAME, ' ', CREATE_STATEMENT)
FROM (
    SELECT 
        TABLE_NAME,
        CONCAT('CREATE TABLE `', TABLE_NAME, '` (\n', GROUP_CONCAT(COLUMN_DESC ORDER BY ORDINAL_POSITION SEPARATOR ',\n'), '\n) ENGINE=', ENGINE, ' DEFAULT CHARSET=', CHARSET) AS CREATE_STATEMENT
    FROM (
        SELECT 
            TABLE_NAME,
            COLUMN_NAME,
            CONCAT('  `', COLUMN_NAME, '` ', COLUMN_TYPE, IF(IS_NULLABLE = 'NO', ' NOT NULL', ''), IF(COLUMN_DEFAULT IS NOT NULL, CONCAT(' DEFAULT ', QUOTE(COLUMN_DEFAULT)), ''), IF(COLUMN_COMMENT != '', CONCAT(' COMMENT ', QUOTE(COLUMN_COMMENT)), '')) AS COLUMN_DESC,
            ORDINAL_POSITION,
            ENGINE,
            CHARSET
        FROM 
            INFORMATION_SCHEMA.COLUMNS
        WHERE 
            TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table'
    ) AS table_info
    GROUP BY 
        TABLE_NAME
) AS table_creation_statement;
