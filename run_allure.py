import os
import subprocess
import sys

def main():
    print("Ищем Java...")
    try:
        # Ищем папку с Java на диске C:
        jdk = next(d for d in os.listdir('C:\\') if d.startswith('jdk'))
        os.environ['JAVA_HOME'] = f'C:\\{jdk}'
        print(f"Найдена Java: C:\\{jdk}")
    except StopIteration:
        print("Ошибка: Java (JDK) не найдена на диске C:")
        sys.exit(1)

    print("Запускаем Allure...")
    # Запускаем Allure
    subprocess.run([r'C:\allure-2.32.0\bin\allure.bat', 'serve', 'allure-results'])

if __name__ == "__main__":
    main()