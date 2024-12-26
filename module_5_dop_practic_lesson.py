import time


# Класс User
class User:
    def __init__(self, nickname, password, age):
        """Инициализация атрибутов с именем: пароль, возраст"""
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        """
        Возвращаем строку, строка, возвращаемая __repr__, должна быть такой,
        чтобы она могла быть снова интерпретирована как код,
        если использовать eval(), что позволяет создать новый объект с теми же данными.
        Другими словами строка возвращаемая __repr__ должна быть валидным кодом
        """
        return f"User(nickname={self.nickname}, age={self.age})"

    def __str__(self):
        """Метод используется для создания строкового представления объекта"""
        return f"Пользователь: {self.nickname}, возраст: {self.age}"

    def __eq__(self, other):
        """Метод для сравнения двух объектов класса User"""
        if isinstance(other, User):
            return self.nickname == other.nickname
        return False


# Класс Video
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        """Инициализация атрибутов с именем: заголовок, длительность, остановка, ограничение по возрасту"""
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        """Метод используется для создания строкового представления объекта"""
        return f'Видео: {self.title}, длительность: {self.duration} секунд'

    def __eq__(self, other):
        """Метод для сравнения двух объектов класса Video"""
        if isinstance(other, Video):
            return self.title == other.title and self.duration == other.duration
        return False


# Класс UrTube
class UrTube:
    def __init__(self):
        """Инициализация атрибутов с именем: список пользователей, список фильмов, текущий пользователь"""
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, title):
        """Метод позволяет использовать оператор in для проверки имеется ли элемент в объекте"""
        for video in self.videos:
            if video.title == title:
                return True
        return False

    def __repr__(self):
        return f"UrTube(users={len(self.users)}, videos={len(self.videos)})"

    def __str__(self):
        """Метод используется для создания строкового представления объекта"""
        return f"Кол-во пользователей:  {len(self.users)}, Кол-во фильмов: {len(self.videos)}"

    def log_in(self, nickname, password):
        hashed_password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word_lower = search_word.lower()
        matching_videos = []
        for video in self.videos:
            if search_word_lower in video.title.lower():
                matching_videos.append(video.title)
        return matching_videos

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                while video.time_now < video.duration:
                    video.time_now += 1
                    print(video.time_now, end=" ")
                    time.sleep(0.1)
                print("Конец видео")
                video.time_now = 0
                return
        else:
            print("Видео не найдено")


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
