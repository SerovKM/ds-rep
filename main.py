# Импорт load_dotenv.
from dotenv import load_dotenv

import os

def print_author():
    # Загрузка переменных из .env
    load_dotenv(dotenv_path='D:/Учёба/Практикум-Data_Scientist/Спринт_8/my_git_project/new_file.env')
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

print_author()
