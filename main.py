from depotController import DepotController
from dataFromExcel import DataFromExcel

# DepotController
depotController = DepotController("conf.ini")

# depot = DepotController("conf.ini")

if __name__ == '__main__':
    dataFromExcel = DataFromExcel("conf.ini", "pokemon_data_.xls", "pokemon_data")

    print(dataFromExcel.insertData(dataFromExcel.getAllData()))







