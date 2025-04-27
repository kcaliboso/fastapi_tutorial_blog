from sqlalchemy.orm import Session
from app.database.models.post import Post
from app.database.schemas.post import PostCreate, PostUpdate


def get_posts(db: Session, limit: int, offset: int):
    return db.query(Post).limit(limit).offset(offset)


def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def create_post(db: Session, post: PostCreate):
    db_post = Post(title=post.title, content=post.content, status=post.status)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post(db: Session, post_id: int, updated_post: PostUpdate):
    try:
        db_post = db.query(Post).filter(Post.id == post_id).first()

        if not db_post:
            return None

        update_data = updated_post.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_post, key, value)

        db.commit()
        db.refresh(db_post)

        return db_post
    except:
        return None


def delete_post(db: Session, post_id: int):
    try:
        db_post = db.query(Post).filter(Post.id == post_id).first()

        if not db_post:
            return None

        db.delete(db_post)
        db.commit()

        return True
    except:
        return None
