from database import Thread

threads = Thread.select()
print(threads[0].name)
print(threads[3].name)

threads = Thread.select().where(Thread.name == "Keisuke01").get()
print(Thread.name, Thread.title, Thread.body)
