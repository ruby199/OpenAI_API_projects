from sqlalchemy import create_mock_engine
from sqlalchemy import text

def dataframe_to_database(df, table_name):
    """Convert a pandas dataframe to a database.
        Args:
            df (dataframe) : pd.DataFRame which is to be converted to a database
            table_name (String): Name of the table within the database
        Returns:
            engine: SQLAlchemy engine object
    
    """

    engine = create_engine(f'sqlite:///:memory:/', echo=False)
    df.to_sql(name=table_name, con=engine, index=False)
    return engine

def handle_response(response):
    """Handles the response from OpenAI
    
    Arges:
        response (openAI response): REsponse json from OpenAI

    Returns:
        string: Proposed SQL query
    """

    query = response["choices"][0]["text"]
    if query.startswith("  "):
        query = "Select" + query
    return query
    
def execute_query(engine, query):
    """Execute a query on a database.
    
    Args:
        engine (SQLAlchemy engine object): database engine
        query (string): SQL query
        
    Returns:
        list: List of tuples containing the result of the query
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()