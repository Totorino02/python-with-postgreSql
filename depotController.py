import psycopg
from config import config


class DepotController:
    f"""
        This class let us to perform an action on a depot table
        Attributes:
            configFileName: str 
                Name of the config file in witch we have all the necessary informations for the connectivity
    
    Methods:
        createTable -> boolean
        insertData -> boolean
        findAll -> List
        findById -> Nom
        findBy -> List
    """

    def __init__(self, configFileName):
        self.configFileName = configFileName
        self.params = config(configFileName, "Postgresql")

    def createTable(self) -> bool:
        """
            Let us create the Depot Table
            :return: boolean
        """
        try:
            with psycopg.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS depot(
                        n_dep bigserial UNIQUE not null,
                        nom_dep varchar(70) not null,
                        adr varchar(70) not null
                    );
                    """)
                    connection.commit()
            return True
        except (Exception, psycopg.DataError) as error:
            print(error)
        return False

    def insertData(self, n_dep: int, dep_nom: str, adresse: str) -> bool:
        """
            :param n_dep: int
            :param dep_nom: str
            :param adresse: str
            :return:
        """
        try:
            connection = psycopg.connect(**self.params)
            cursor = connection.cursor()

            cursor.execute("INSERT INTO depot(n_dep, nom_dep, adr) VALUES (%s, %s, %s)", (n_dep, dep_nom, adresse))
            connection.commit()

            cursor.close()
            connection.close()
            return True
        except (Exception, psycopg.DataError) as error:
            print(error)
        return True

    def findAll(self) -> list:
        """
            This function let us get all the data from depot table
            :return:
        """
        try:
            with psycopg.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM depot;")
                    record = cursor.fetchall()
                    return record
        except (Exception, psycopg.DataError) as error:
            print(error)

    def findById(self, _id: int):
        """
            This function let us get depot by specify it's id
            :param _id: int
            :return: Depot
        """
        try:
            with psycopg.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    """
                    
                    !!! la virgule est importante car il le faut pour que python
                    creer un tuple contenant un seul élément 
                    
                    """
                    cursor.execute("SELECT * FROM depot WHERE n_dep = %s;", (_id,))
                    record = cursor.fetchall()
                    return record
        except (Exception, psycopg.DataError) as error:
            print(error)

    def findBy(self):
        """
            This function let us get depot by specify it's properties
        :return: Depot
        """
        try:
            with psycopg.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM depot WHERE n_dep = %s;", (id,))
                    record = cursor.fetchall()
                    return record
        except (Exception, psycopg.DataError) as error:
            print(error)


