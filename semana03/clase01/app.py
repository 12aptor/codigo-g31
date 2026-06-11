"""Crear una aplicación de consola
para gestionar tareas:

[ ] Ver las tareas en un tabla
[ ] Marcar las tareas como completadas
[ ] Agregar tareas"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from snake_db import SnakeDB
from typing import Dict, Any

# Modelo de datos
class Task:
    def __init__(self, nro, description, category):
        self.nro = nro
        self.description = description
        self.category = category
        self.completed = False

    def complete_task(self):
        self.completed = True

    def json(self) -> Dict[str, Any]:
        return {
            'nro': self.nro,
            'description': self.description,
            'category': self.category,
            'completed': self.completed
        }

# Lógica de negocio
class TaskManager:
    def __init__(self):
        self.db = SnakeDB("snake_db.json")

    def add_task(self, task: Dict[str, Any]):
        self.db.insert(task)

    def get_tasks(self):
        return self.db.get_all()

# Interfaz visual
class Interface:
    def __init__(self, manager: TaskManager):
        self.manager = manager
        self.console = Console()

    def show_welcome_ui(self):
        panel = Panel("[bold blue]Gestor de Tareas iniciado[/bold blue]\n[green]Listo para la acción[/green]", expand=False)
        self.console.print(panel)

    def show_tasks_table(self):
        table = Table(title="Tareas del día")
        table.add_column("N°", justify="center", style="cyan")
        table.add_column("Descripción", style="magenta")
        table.add_column("Categoría", style="yellow")
        table.add_column("Estado", justify="center")

        # for t in self.manager.get_tasks():
        #     status = "[bold green]✓[/bold green]" if t.completed else "[bold red]χ[/bold red]"
        #     table.add_row(str(t.nro), t.description, t.category, status)
        
        self.console.print(table)

def main():
    manager = TaskManager()
    manager.add_task(Task(1, "Entrenamiento físico intensivo", "Disciplina").json())
    manager.add_task(Task(2, "Estudio de estructura de datos", "Desarrollo").json())
    manager.add_task(Task(3, "Revisión de logs del servidor", "Sistemas").json())

    # manager.get_tasks()[0].complete_task()

    ui = Interface(manager)
    ui.show_welcome_ui()
    ui.show_tasks_table()

if __name__ == '__main__':
    main()

"""RETORNAMOS 9:21"""