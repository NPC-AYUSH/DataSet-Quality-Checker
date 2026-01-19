import subprocess
import sys

def main():
    print("🚀 Starting Dataset Quality Checker (Backend + Frontend)")

    backend_cmd = (
        "uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"
    )

    frontend_cmd = (
        "streamlit run frontend/streamlit_app.py --server.port 8501"
    )

    backend = subprocess.Popen(backend_cmd, shell=True)
    frontend = subprocess.Popen(frontend_cmd, shell=True)

    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        backend.terminate()
        frontend.terminate()
        sys.exit(0)

if __name__ == "__main__":
    main()
