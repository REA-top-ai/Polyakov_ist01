from sqlalchemy.orm import Session
from models import Author, Post, Comment
from datetime import datetime
from sqlalchemy import or_
from sqlalchemy import func

def create_author(session: Session, name: str, email: str) -> Author:

    existing_ckeck = (
        session.query(Author)
        .filter(or_(Author.email == email, Author.name == name))
        .first()
    )

    if existing_ckeck:
        print(f"Автор уже существует: {existing_ckeck.name}, id={existing_ckeck.id}")
        return existing_ckeck

    new_author = Author(name=name, email=email)
    session.add(new_author)
    session.commit()
    session.refresh(new_author) # Обновляем объект, чтобы получить id
    return new_author

def get_author_by_email(session: Session, email: str) -> Author | None:
    return session.query(Author).filter(Author.email == email).first()

def get_author_by_name(session: Session, name: str) -> Author | None:
    return session.query(Author).filter(Author.name.ilike(f"%{name}%")).all()

def get_by_date(session: Session, date) -> list[Post]:
    return (
        session.query(Post).filter(func.date(Post.created_at) == date).all()
    )
def add_more_authors(session: Session, authors: list[dict]) -> list[Author]:
    result = []
    for a in authors:
        name = a["name"]
        email = a["email"]
        existing_check = (
            session.query(Author)
            .filter(or_(Author.email == email, Author.name == name))
            .first()
        )
        if existing_check:
            print(f"Автор уже существует: {existing_check.name}, id={existing_check.id}")
            result.append(existing_check)
            continue
        new_author = Author(name=name, email=email)
        session.add(new_author)
        session.commit()
        session.refresh(new_author)
        print(f"Добавлен новый автор: {new_author.name}, id={new_author.id}")
        result.append(new_author)
    return result

def get_ifs_comm(session: Session, post_id: int) -> list[Comment]:
    comments = (
        session.query(Comment)
        .filter(Comment.post_id == post_id)
        .all()
    )
    return comments

def create_post(session: Session, title: str, content: str, author_id: int, published: bool = False) -> Post:
    new_post = Post(
    title=title,
    content=content,
    author_id=author_id,
    published=published
    )

    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    return new_post
def get_published_posts(session: Session, limit: int = 10) -> list[Post]:
    return session.query(Post).filter(Post.published == True).limit(limit).all()

def get_posts_by_author(session: Session, author_id: int, limit: int = 10) -> list[Post]:
    return session.query(Post).filter(Post.author_id == author_id).limit(limit).all()

def update_post_status(session: Session, post_id: int, published: bool) -> bool:
    post = session.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return False # Пост не найден
    post.published = published
    session.commit()
    return True

def add_comment(session: Session, post_id: int, author_name: str, text: str) -> Comment:
    new_comment = Comment(
    post_id=post_id,
    author_name=author_name,
    text=text
    )
    session.add(new_comment)
    session.commit()
    session.refresh(new_comment)
    return new_comment
def get_top_authors_by_posts(session: Session, limit: int = 3) -> list[tuple[str, int]]:
    from sqlalchemy import func, desc
    result = (session.query(
    Author.name,
    func.count(Post.id).label('post_count')
    )
    .join(Post) # Присоединяем таблицу постов по foreign key
    .group_by(Author.id) # Группируем по автору
    .order_by(desc('post_count')) # Сортируем по убыванию количества
    .limit(limit)
    .all())
    return result