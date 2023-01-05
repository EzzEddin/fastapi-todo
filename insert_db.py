from main import Todo, session

todo1 = Todo(text="learn fastapi", is_done=True)
todo2 = Todo(text="learn django")

session.add_all([todo1, todo2])
session.commit()
