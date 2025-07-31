def generate_report(**context):
    pg_hook = PostgresHook(postgres_conn_id='postgres_db')
    
    # Get daily statistics
    report_sql = """
        SELECT 
            city,
            AVG(temperature) as avg_temp,
            MAX(temperature) as max_temp,
            MIN(temperature) as min_temp
        FROM weather_data
        WHERE date = CURRENT_DATE
        GROUP BY city
    """
    
    report_df = pg_hook.get_pandas_df(report_sql)
    
    # Save report
    report_df.to_csv(f'/tmp/weather_report_{datetime.now().date()}.csv')
