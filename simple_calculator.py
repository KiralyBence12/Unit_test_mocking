"""
EGYSZERŰ KALKULÁTOR - Mockolás példához

Ez a kalkulátor több külső szolgáltatást használ:
- HistoryService: Elmenti a műveleteket (adatbázisba)
- Logger: Naplózza a műveleteket (log fájlba)
- ValidationService: Ellenőrzi a bemeneteket

Ezeket mind mockolhatjuk a tesztekben!
"""


class SimpleCalculator:
    """Egyszerű kalkulátor osztály több függőséggel"""
    
    def __init__(self, history_service=None, logger=None, validation_service=None):
        """
        Args:
            history_service: Művelet előzmények mentéséhez (mockolható)
            logger: Naplózásért felelős (mockolható)
            validation_service: Bemenet validációért felelős (mockolható)
        """
        self.history_service = history_service
        self.logger = logger
        self.validation_service = validation_service
    
    def add(self, a, b):
        """
        Összeadás művelet
        
        Lépések:
        1. Validálja a bemeneteket
        2. Végzi a számítást
        3. Naplózza a műveletet
        4. Elmenti az előzményekbe
        5. Visszaadja az eredményt
        """
        # 1. Validáció (ha van validation_service)
        if self.validation_service:
            self.validation_service.validate_numbers(a, b)
        
        # 2. Számítás
        result = a + b
        
        # 3. Naplózás (ha van logger)
        if self.logger:
            self.logger.log_operation("add", a, b, result)
        
        # 4. Előzmények mentése (ha van history_service)
        if self.history_service:
            self.history_service.save_operation("add", a, b, result)
        
        return result
    
    def multiply(self, a, b):
        """
        Szorzás művelet
        
        Lépések:
        1. Validálja a bemeneteket
        2. Végzi a számítást
        3. Naplózza a műveletet
        4. Elmenti az előzményekbe
        5. Visszaadja az eredményt
        """
        # 1. Validáció
        if self.validation_service:
            self.validation_service.validate_numbers(a, b)
        
        # 2. Számítás
        result = a * b
        
        # 3. Naplózás
        if self.logger:
            self.logger.log_operation("multiply", a, b, result)
        
        # 4. Előzmények mentése
        if self.history_service:
            self.history_service.save_operation("multiply", a, b, result)
        
        return result
    
    def divide(self, a, b):
        """
        Osztás művelet
        
        Lépések:
        1. Validálja a bemeneteket (különösen a nullával való osztást)
        2. Végzi a számítást
        3. Naplózza a műveletet
        4. Elmenti az előzményekbe
        5. Visszaadja az eredményt
        """
        # 1. Validáció
        if self.validation_service:
            self.validation_service.validate_numbers(a, b)
            self.validation_service.validate_division(b)  # Nullával való osztás ellenőrzés
        
        # 2. Számítás
        result = a / b
        
        # 3. Naplózás
        if self.logger:
            self.logger.log_operation("divide", a, b, result)
        
        # 4. Előzmények mentése
        if self.history_service:
            self.history_service.save_operation("divide", a, b, result)
        
        return result
    
    def get_history_count(self):
        """
        Visszaadja, hány művelet van elmentve az előzményekben
        
        Returns:
            int: Az elmentett műveletek száma
        """
        if self.history_service:
            return self.history_service.get_operation_count()
        return 0

