# Test_API Django & Stripe & Environ

Реализовал  Django + Stripe API
В Django  создал модель Item с полямми: name, description, price. Цены в Stripe указываются до центов, создал функцию для перевода точной суммы центов в доллары, со знаком после заяпятой ->
 например 4500 cents == 45.0 usd etc.
На локальном сервере при запросе url == "/" получаем вывод всех доступных товаров, при переходе по ссылке товара получаем url /item/{id}/ при вызове метода GET и при нажатии ->
кнопки buy получаем url /buy/{id} при вызове метода GET и выполняется запрос stripe.checkout.Session.create(...)
В проекте использовал Class-based Views вместе с функциями def(get) для более быстрой обработки, чем при использовании обычных функций.

Реализовал возможность просмотра моделей в admin панели и environment variables, .env.example является представлением переменных для основного файла .env


Для создания виртуального окружения перейдите в директорию проекта и  используйте команду: (pyhton or python3) -m venv (названия виртуального окружения)
После создания виртального окружения активируйте его командой, находясь в той же директории: source (название виртуального окружения)/bin/activate 
Для установки всех необходимых пакето используйте: (pyhton or python3) -m pip install -r requirements.txt
После запустите миграцию для создания базы данных: (pyhton or python3) manage.py migrate
Создайте суперпользвателя для входа в admin панель: (pyhton or python3) manage.py createsuperuser
После входа в админ панель, создайте в модели Item товары, которые хотите продать(протестировать) и после переходите на локальные сервер с url "" для просмотра и покупки товаров!

![Снимок экрана от 2022-09-12 20-52-57](https://user-images.githubusercontent.com/92216309/189733381-d7af0e70-7b0b-4d5d-84db-fa7dd127a22a.png)
![Снимок экрана от 2022-09-12 20-44-16](https://user-images.githubusercontent.com/92216309/189733387-786133df-7da5-454e-92d6-de2588aa97a6.png)
![Снимок экрана от 2022-09-12 20-42-38](https://user-images.githubusercontent.com/92216309/189733389-665888a9-fda7-4e23-ae93-63adebe5f24d.png)
![Снимок экрана от 2022-09-12 20-44-26](https://user-images.githubusercontent.com/92216309/189733392-b245fd9f-588c-4680-8a6c-92282fe4f2b1.png)
![Снимок экрана от 2022-09-12 20-48-16](https://user-images.githubusercontent.com/92216309/189733394-4b9d3288-1655-4cce-9f06-51220e2266f9.png)
![Снимок экрана от 2022-09-12 20-44-37](https://user-images.githubusercontent.com/92216309/189733395-9cfe1395-f47d-4735-b4ab-c4f067e52368.png)
![Снимок экрана от 2022-09-12 20-47-44](https://user-images.githubusercontent.com/92216309/189733398-9c93cacc-f019-473f-b5c2-d006aee8cb9a.png)
![Снимок экрана от 2022-09-12 20-41-55](https://user-images.githubusercontent.com/92216309/189733400-a53ec3d3-d0e1-4232-bd1d-4b2a10cd0a02.png)
![Снимок экрана от 2022-09-12 20-41-46](https://user-images.githubusercontent.com/92216309/189733401-4fbacd67-dd28-4257-98c7-9297da5c8443.png)
![Снимок экрана от 2022-09-12 20-42-25](https://user-images.githubusercontent.com/92216309/189733406-53226cf2-ab52-4f0e-b136-f1dd6479f66d.png)


