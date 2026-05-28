from database import SessionLocal, engine, Base
from models import Author, Post, Comment
from crud import *
from datetime import date

def main():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        print("Начинаем тестирование...\n")
        print("Создаём авторов...")
        author1 = create_author(session,"Анна Петрова", "anna@example.com")
        author2 = create_author(session,"Иван Сидоров", "ivan@example.com")
        print(f"{author1.name} (id={author1.id})")
        print(f"{author2.name} (id={author2.id})\n")
        print("Создаём посты...")
        post1 = create_post(session, "Первый пост", "Это содержание первогопоста. Оно достаточно длинное.", author1.id, published=True)
        post2 = create_post(session,"Черновик","Этот пост пока неопубликован.", author1.id, published=False)
        post3 = create_post(session,"Пост Ивана","Текст от Ивана.", author2.id, published=True)
        print(f"'{post1.title}' (опубликован)")
        print(f"'{post2.title}' (черновик)")
        print(f"'{post3.title}' (опубликован)\n")
        print("Добавляем комментарии...")
        add_comment(session, post1.id, "Читатель1", "Отличная статья, оченьполезно!")
        add_comment(session, post1.id, "Читатель2", "Спасибо за материал, жду продолжения.")
        add_comment(session, post1.id,"Аноним","Коротко.")
        print("3 комментария добавлены к первому посту\n")
        print("Публикуем черновик...")
        success = update_post_status(session, post2.id, published=True)
        if success:
            print(f"'{post2.title}' теперь опубликован\n")
        print("📰 Все опубликованные посты:")
        published = get_published_posts(session)
        for post in published:
            print(f"'{post.title}' — автор: {post.author.name}")
        print()
    # 6. Топ авторов по количеству постов
        print("🏆 Топ авторов по количеству постов:")
        top_authors = get_top_authors_by_posts(session, limit=3)
        for rank, (name, count) in enumerate(top_authors, 1):
            print(f"{rank}. {name}: {count} пост(ов)")
        print()
    # 7. Проверка: поиск автора по email
        print("Поиск автора по email...")
        found = get_author_by_email(session, "anna@example.com")
        if found:
            print(f"Найдено: {found.name}")
        else:
            print("Автор не найден")
    # 8. Поиск автора по имени
        task_one = get_author_by_name(session, 'Анна')
        if task_one:
            for auth in task_one:
                print(f'found {auth.name}')
        else:
            print('gg')
    # 9. Поиск по дате
        task_two = get_by_date(session, date(2026, 5, 25))
        if task_two:
            for post in task_two:
                print(f"Пост: {post.title}, дата: {post.created_at}")
        else:
            print("За эту дату опубликованных постов нет")
    #10. Добавление много авторов и тд
        new_authors = add_more_authors(
            session,
            [
                {"name": "Петр Иванов", "email": "petr@example.com"},
                {"name": "Мария Смирнова", "email": "maria@example.com"},
                {"name": "Олег Кузнецов", "email": "oleg@example.com"},
            ]
        )
        for author in new_authors:
            print(f"Добавлен автор: {author.name}, id={author.id}")
        comments = get_ifs_comm(session, post1.id)

        if comments:
            for comment in comments:
                print(f"{comment.author_name}: {comment.text}")
        else:
            print("Комментариев нет")
    except Exception as e:
        print(f"Ошибка: {e}")
        session.rollback()  # Отменяем все изменения при ошибке
    finally:
        session.close()  # Обязательно закрываем сессию!
        print("\nТестирование завершено. Сессия закрыта.")
if __name__ == "__main__":
    main()