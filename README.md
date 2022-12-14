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
![Снимок экрана от 2022-09-12 20-42-38](https://user-images.githubusercontent.com/92216309/189734194-d7ccd754-f849-4025-8866-a3cc6b8ff276.png)
![Снимок экрана от 2022-09-12 20-44-26](https://user-images.githubusercontent.com/92216309/189734197-ed210ef4-b137-4bcc-bdd9-2934a26d4fbd.png)
![Снимок экрана от 2022-09-12 20-48-16](https://user-images.githubusercontent.com/92216309/189734199-b91ea687-ff14-4502-ab8d-675fc34c9a57.png)
![Снимок экрана от 2022-09-12 20-44-37](https://user-images.githubusercontent.com/92216309/189734203-b166a0db-0886-4d8e-8579-b9f8e88e5629.png)
![Снимок экрана от 2022-09-12 20-47-44](https://user-images.githubusercontent.com/92216309/189734206-72b9fae8-9fbe-4828-91ad-e13c5e7766ec.png)
![Снимок экрана от 2022-09-12 20-41-55](https://user-images.githubusercontent.com/92216309/189734210-ceecd112-329a-4938-8573-97e6e13a6e29.png)
![Снимок экрана от 2022-09-12 20-41-46](https://user-images.githubusercontent.com/92216309/189734213-dcb76eab-e34a-44b8-b5af-cc8a08cd3529.png)
![Снимок экрана от 2022-09-12 20-47-44](https://user-images.githubusercontent.com/92216309/189734320-4681d210-cdf5-4710-acc2-7e0a103a8742.png)

