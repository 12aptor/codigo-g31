import json
from typing import List, Dict, Any

class SnakeDB:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data: List[Dict[str, Any]] = self._load_data()

    def _load_data(self):
        return []

    def _save_data(self):
        """Save data from RAM to File"""
        with open(self.file_path, 'w', encoding='utf-8') as file:
           json.dump(self.data, file, indent=4, ensure_ascii=False) 

    def insert(self, record: Dict[str, Any]):
        self.data.append(record)
        self._save_data()

    def get_all(self) -> List[Dict[str, Any]]:
        return self.data
    
    def search_as(self, field: str, value: Any) -> List[Dict[str, Any]]:
        """Search data by field and value"""
        results = []
        for record in self.data:
            if record.get(field) == value:
                results.append(record)

        return results
    
    def update_by_id(self, record_id: int, new_values: Dict[str, Any]):
        """Update record by id"""
        for record in self.data:
            if record.get('id') == record_id:
                record.update(new_values)
        self._save_data()

    def delete_by_id(self, record_id: int):
        """Delete record by id"""
        results = []
        for record in self.data:
            if record.get('id') != record_id:
                results.append(record)
        self._save_data()
