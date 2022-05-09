from app import createApp, db

app = createApp()

from app.blueprints.blog.models import Post, User

@app.shell_context_processor
def makeContext():
    return {
        'db': db,
        'User': User,
        'Post': Post
    }

    