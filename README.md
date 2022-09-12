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

![Снимок экрана от 2022-09-12 20-52-57](https://user-images.githubusercontent.com/92216309/189733499-2e874894-d129-42e0-9b16-01c932433055.png)
![Снимок экрана от 2022-09-12 20-44-16](https://user-images.githubusercontent.com/92216309/189733503-ebce0af4-e3c2-460f-9f6c-10d7289f02c0.png)
![Снимок экрана от 2022-09-12 20-42-38](https://user-images.githubusercontent.com/92216309/189733505-c662c085-aa2e-47f9-83ec-fc92d614b7a6.png)
![Снимок экрана от 2022-09-12 20-44-26](https://user-images.githubusercontent.com/92216309/189733509-f18a9d9e-bb24-4619-a1bd-33ca961ee21c.png)
![Снимок экрана от 2022-09-12 20-48-16](https://user-images.githubusercontent.com/92216309/189733515-881028d1-67d8-4443-a76b-01542bfeb94c.png)
![Снимок экрана от 2022-09-12 20-44-37](https://user-images.githubusercontent.com/92216309/189733518-2b22ab2b-3870-4a7a-a769-9f930af48684.png)
![Снимок экрана от 2022-09-12 20-47-44](https://user-images.githubusercontent.com/92216309/189733520-1ea8ce7c-7a74-4d8a-9078-cbb5757cfcd0.png)
![Снимок экрана от 2022-09-12 20-41-55](https://user-images.githubusercontent.com/92216309/189733522-aeccca29-f6d4-4776-854e-a2f04c0d5711.png)
![Снимок экрана от 2022-09-12 20-41-46](https://user-images.githubusercontent.com/92216309/189733525-d779b735-387a-466e-bd76-87440fb80db7.png)



