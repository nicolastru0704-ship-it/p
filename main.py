from pathlib import Path
import sys

def main():
    # Añadir carpeta src al sys.path para poder importar el paquete
    root = Path(__file__).resolve().parent
    src = root / "src"
    if str(src) not in sys.path:
        sys.path.insert(0, str(src))

    from sistema_transporte.cli import menu
    menu()

if __name__ == "__main__":
    main()
