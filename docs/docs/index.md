# opt_ab documentation!

## Description

optimization in ab design, testing, resultings

## Commands

**Процесс всегда такой:**

1. `ccds` -> создать структуру проекта.
2. `cd project_name` -> зайти в проект.
3. `python -m venv .venv` -> **создать** локальную среду.
4. `.\.venv\Scripts\Activate.ps1` -> **активировать** созданную среду.
5. `pip install -r requirements.txt` -> установить зависимости в активную среду.





The Makefile contains the central entry points for common tasks related to this project.

#### Makefile: Установка `make` через пакетный менеджер (Chocolatey)
`💡 Оптимальный Выбор`

**Концепция:** Использовать пакетный менеджер для Windows, такой как Chocolatey, чтобы установить `make` одной командой. Это самый чистый и управляемый способ.

**План действий:**

1. **Установить Chocolatey (если еще не установлен).** Это делается один раз. Откройте PowerShell **от имени администратора** и выполните команду:
    ```powershell
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```
    **Вектор верификации:** Это официальная команда установки с сайта [chocolatey.org](https://chocolatey.org/install).

2. **Установить `make`.** После установки Chocolatey откройте новый терминал (можно обычный, не от администратора) и выполните:
    ```powershell
    choco install make
    ```
    Chocolatey автоматически скачает, установит и, что самое важное, **пропишет путь к `make.exe` в системную переменную `PATH`**.

3. **Перезапустите VSC или терминал.** Это необходимо, чтобы терминал "увидел" обновленный `PATH`.

4. **Повторите попытку:**
    ```bash
    make requirements
    ```
