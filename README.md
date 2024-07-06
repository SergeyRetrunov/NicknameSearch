# NicknameSearch
**Вводим никнейм и получаем ссылки на возможно существующий профиль**

# Установка

```
apt update && apt upgrade -y
```

```
pkg install python -y
```

```
pkg install git -y
```

```
pip install colorama
```

```
git clone https://github.com/SergeyRetrunov/NicknameSearch.git
```

```
cd NicknameSearch
```

```
python main.py
```

# Ошибка: 

**sh: /data/data/com.termux/files/usr/bin/clear: Permission denied**

*Решение:*  
Попробуйте использовать данную команду:
```
termux-setup-storage
```
На данный момент это единственный способ возможного решения проблемы.
