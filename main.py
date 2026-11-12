from user import User
from post import Post

app_user_one = User("rb@er.com", "RoBö", "pwd", "master of desaster")

app_user_one.get_user_info()

app_user_two = User("tr@er.com", "Fiona", "pwd", "bachelor of desaster")
app_user_two.get_user_info()

new_post = Post("on a mission today", app_user_two.name)
new_post.get_post_info()