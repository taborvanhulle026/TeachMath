class Lesson:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def __str__(self):
        return f"{self.title}: {self.content}"

# 示例课程
def create_lessons():
    lesson1 = Lesson("Lesson 1", "Introduction to Algebra: Variables, Expressions, and Equations")
    lesson2 = Lesson("Lesson 2", "Introduction to Geometry: Shapes, Angles, and Theorems")
    return [lesson1, lesson2]
