import sys
import subprocess


def main() -> None:
    command = [sys.executable, "-m", "heroku"]
    try:
        result = subprocess.run(command)
        sys.exit(result.returncode)
    except FileNotFoundError:
        print("Не удалось найти исполняемый файл Python. Убедитесь, что Python установлен и доступен в PATH.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()


