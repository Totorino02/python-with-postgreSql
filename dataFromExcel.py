import psycopg
import xlrd
from config import config


class DataFromExcel:
    f"""
        Interface let us get data from Excel file and push it on a database
        Attributes:
            configFileName: str
                The name of the config file in witch we have all the necessary informations for the connectivity
            fileName: str
                The name of the excel file
            sheetName: str
                The name of the sheet in the excel file 
        Methods:
            createTable -> boolean
            getAlldata -> List
            getDataAt -> string/int
            insertData -> List
            
    """

    def __init__(self, configFileName, fileName, sheetName):
        self.fileName = fileName
        self.params = config(configFileName, "Postgresql")
        self.book = xlrd.open_workbook(fileName)
        self.sheet = self.book.sheet_by_name(sheetName)

    def createTable(self):
        """
            Let us create the Pokemon Table
            :return: boolean
        """
        try:
            with psycopg.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pokemon (
                        id bigserial PRIMARY KEY,
                        name TEXT NOT NULL,
                        type1 TEXT NOT NULL,
                        type2 TEXT NOT NULL,
                        hp INTEGER NOT NULL,
                        attack INTEGER NOT NULL,
                        defense INTEGER NOT NULL,
                        sp_atk INTEGER NOT NULL,
                        sp_def INTEGER NOT NULL,
                        speed INTEGER NOT NULL,
                        generation INTEGER NOT NULL,
                        legendary INTEGER NOT NULL    
                    );
                    """)
                    connection.commit()
            return True
        except (Exception, psycopg.DataError) as error:
            print(error)
        return False

    def getAllData(self):
        """
            Get all the data of the excel file in List format
            :return: Data
        """
        data = list()
        for r in range(1, self.sheet.nrows):
            row = [self.getDataAt(r, i) for i in range(1, 12)]
            data.append(row)
        return data

    def getDataAt(self, line: int, column: int):
        """
            Get the data witch is locate at the position (line, column) of the sheet
            :param line: int
            :param column: int
            :return:
        """
        return self.sheet.cell(line, column).value

    def insertData(self, data: list):
        """
            Let us insert the data in pokemon table on the database
            :param data: List
            :return:
        """
        try:
            with psycopg.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    for row in data:
                        cursor.execute("""
                        INSERT INTO pokemon(name, type1, type2, hp, attack, defense, sp_atk, sp_def, speed, generation, legendary)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, row)
                        connection.commit()
            return True
        except (Exception, psycopg.DataError) as error:
            print(error)
        return False


