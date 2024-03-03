#declaring targets for what is required
required_pages_to_read = 10
required_lessons_to_watch = 4

#letting user to enter their results
readed_pages = int(input("Enter how many pages you have readen:"))
watched_lessons = int(input("enter how many lessons you have watched:"))

#sending to the screen final result of user
print(readed_pages == required_pages_to_read and watched_lessons == required_lessons_to_watch)
print(readed_pages != required_pages_to_read and watched_lessons == required_lessons_to_watch)
print(readed_pages == required_pages_to_read or watched_lessons == required_lessons_to_watch)
print(readed_pages == required_pages_to_read or watched_lessons != required_lessons_to_watch)