# VK Playlist

**How can I find the token?** 

[Create a vk app](https://new.vk.com/editapp?act=create), then copy its ID and paste it into this string instead of `APP_ID`:

```
https://oauth.vk.com/authorize?client_id=APP_ID&scope=audio,offline&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token
```

You will be redirected to a page with a similar URL. Copy the `access_token` param:

```
https://oauth.vk.com/blank.html#access_token=blahblahitsover9000lettersanddigits&expires_in=0&user_id=USER_ID
```

Save it to an env variable:

```
export VK_TOKEN=blahblahitsover9000lettersanddigits
```

--------

Бекап аудиозаписей с плейлиста ВКонтакте (до 6000) средствами Python и Vk API
https://habrahabr.ru/post/247987/ (Selenium)

Делаем бэкап музыкальной базы vkontakte с помощью Python
https://habrahabr.ru/post/143860/

Использование api vk python: Скачивание стены Вконтакте
http://alexkutsan.blogspot.ru/2013/07/api-vk-python.html

Работа с VK API на Python 3.x
https://sohabr.net/habr/post/242365/?version=67420

simple vkontakte music downloader
https://github.com/stleon/vk_music

vkontakte music downloader (на Perl)
https://github.com/genaev/vmd

Download music from vk.com (You need account and simple application on vk.com)
https://github.com/ugputu/VkSaver

Пишем модуль для авторизации в VK API
https://habrahabr.ru/post/143972/

Пишем программу-загрузчик для музыки ВКонтакте
http://theasder.github.io/tutorial/2014/07/22/download_vk_music_from_post.html

obscure-music-downloader
https://github.com/kaneru/obscure-music-downloader
