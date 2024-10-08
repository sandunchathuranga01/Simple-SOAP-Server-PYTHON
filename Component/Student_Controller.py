from spyne import ServiceBase, rpc, Unicode, Integer
from sqlalchemy.orm import Session
from Component.Student_entity import Student
from Component.DB_config import get_db


# Define a Spyne service to handle SOAP requests
class StudentService(ServiceBase):

    # Create student
    @rpc(Unicode, Unicode, _returns=Unicode)
    def create_student(ctx, name, description):
        db: Session = next(get_db())
        new_student = Student(name=name, description=description)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return f"Item {new_student.name} created successfully with ID: {new_student.id}"

    # Read all items
    @rpc(_returns=Unicode)
    def read_student(ctx):
        db: Session = next(get_db())
        students = db.query(Student).all()  # Retrieve all students
        result = ""
        for student in students:
            result += f"ID: {student.id}, Name: {student.name}, Description: {student.description}\n"
        return result if result else "No students found"

    # Read single item by ID
    @rpc(Integer, _returns=Unicode)
    def read_student_by_id(ctx, student_id):
        db: Session = next(get_db())
        student = db.query(Student).filter(Student.id == student_id).first()
        if student:
            return f"ID: {student.id}, Name: {student.name}, Description: {student.description}"
        else:
            return f"Student with ID {student_id} not found"

    # Update an item
    @rpc(Integer, Unicode, Unicode, _returns=Unicode)
    def update_item(ctx, student_id, name, description):
        db: Session = next(get_db())
        student = db.query(Student).filter(Student.id == student_id).first()
        if student:
            student.name = name
            student.description = description
            db.commit()
            db.refresh(student)
            return f"Item {student_id} updated successfully"
        else:
            return f"Item with ID {student_id} not found"

    # Delete an item
    @rpc(Integer, _returns=Unicode)
    def delete_item(ctx, student_id):
        db: Session = next(get_db())
        student = db.query(Student).filter(Student.id == student_id).first()
        if student:
            db.delete(student)
            db.commit()
            return f"Item {student_id} deleted successfully"
        else:
            return f"Item with ID {student_id} not found"
