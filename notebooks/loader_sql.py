import sqlalchemy as sa
import urllib
import pandas as pd
from tqdm import tqdm
import dask.dataframe as dd


class PandasToSQL:
    """
    This class wrap to_sql function from pandas with tqdm progress bar
    SQL alchemy with fast_executemany parameter for quickness
    
    source: https://stackoverflow.com/a/58698842
    """

    def __init__(self, server = "server" , 
                 database = 'database' , 
                 username = 'username' , 
                 password = 'password'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password


    def chunker(self,seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))
    
    

    def pandas_loader(self,dataframe,dbTable,npartitions):
        conn= urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        engine = sa.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn),fast_executemany=True)
        chunksize = int(len(dataframe) / npartitions)
        with tqdm(total=len(dataframe)) as pbar:
            for i, cdf in enumerate(self.chunker(dataframe, chunksize)):
                replace = "replace" if i == 0 else "append"
                cdf.to_sql(dbTable, schema='dbo', con = engine, index=False, if_exists=replace)
                pbar.update(chunksize)
                tqdm._instances.clear()
      

    def dask_loader(self,ddataframe,dbTable):
        conn= urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        engine = sa.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn),fast_executemany=True)
        for i in tqdm(range(ddataframe.npartitions)):
            replace = "replace" if i == 0 else "append"
            partition = ddataframe.get_partition(i)
            from_dask_to_pandas = partition.compute()
            from_dask_to_pandas.to_sql(dbTable, schema='dbo', con =engine, index=False, if_exists=replace)
            