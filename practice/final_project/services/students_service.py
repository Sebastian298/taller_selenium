import requests
from typing import List
from practice.final_project.models.student import Student


class StudentsService:

    @staticmethod
    def get_students() -> List[Student]:
        students = []
        response = requests.get('https://taller-selenium.netlify.app/students.json')
        students_data = response.json()

        for student in students_data:
            student_instance = Student(
                no_control=student['noControl'],
                nombre=student['nombreCompleto'],
                correo=student['correoInstitucional'],
                semestre=student['semestre'],
                grupo=student['grupo'],
                talla=student['talla'],
                genero=student['genero'],
                taller_registrado=student['tallerRegistrado'],
                cuota_cubierta=student['cuotaCubierta']
            )
            students.append(student_instance)

        return students