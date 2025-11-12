"""
Smart Database Helper - Automatically handles PostgreSQL queries
This eliminates the need to add adapt_query() to every single route
"""

# Add this to db_config.py or import in app.py

def execute_query_auto(cursor, query, params=None):
    """
    Automatically adapts and executes queries for PostgreSQL
    Works with both parameterized and non-parameterized queries
    """
    from db_config import adapt_query
    
    # Adapt the query for PostgreSQL (? to %s)
    adapted_query = adapt_query(query)
    
    # Execute with or without parameters
    if params:
        cursor.execute(adapted_query, params)
    else:
        cursor.execute(adapted_query)
    
    return cursor

# Usage in routes:
# Instead of: cursor.execute(query, params)
# Use: execute_query_auto(cursor, query, params)

print("✅ Helper function ready to add to app.py or db_config.py")
