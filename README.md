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

![Снимок экрана от 2022-09-12 20-42-25](https://user-images.githubusercontent.com/92216309/189733759-8aa46f05-3194-4395-8a49-ea550cd7fbc4.png)
![Снимок экрана от 2022-09-12 20-44-16](https://user-images.githubusercontent.com/92216309/189733762-b02e37a7-b8fd-489c-ad89-a5e39894994f.png)
![Снимок экрана от 2022-09-12 20-42-38](https://user-images.githubusercontent.com/92216309/189733766-7cd90c37-218b-4576-b56d-6bc585cd7d67.png)
![Снимок экрана от 2022-09-12 20-48-16](https://user-images.githubusercontent.com/92216309/189733769-8e04608a-d350-490e-8d23-17761a0a3a9f.png)
![Снимок экрана от 2022-09-12 20-44-37](https://user-images.githubusercontent.com/92216309/189733773-dea3a992-14af-4017-a7d7-e0399162a015.png)
![Снимок экрана от 2022-09-12 20-47-44](https://user-images.githubusercontent.com/92216309/189733777-11756268-ad82-4bfd-9a4f-8bafcd7662a7.png)
![Снимок экрана от 2022-09-12 20-41-55](https://user-images.githubusercontent.com/92216309/189733780-d4950482-9faf-4074-beea-7426c78a5bac.png)
![Снимок экрана от 2022-09-12 20-41-46](https://user-images.githubusercontent.com/92216309/189733784-247c04cb-32ca-4afb-bac2-98bf8432a6ed.png)



