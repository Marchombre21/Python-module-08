try:
    from dotenv import load_dotenv
    import os
except ImportError:
    print("It's an error")


class EnvError(Exception):
    def __init__(self, details: str):
        message: str = details
        super().__init__(message)


class EnvMissing(EnvError):
    def __init__(self, details: str):
        details: str = f"{details} value is missing in .env"
        super().__init__(details)


def main():
    try:
        if not os.path.exists(".env"):
            raise EnvError(".env file is missing!")
        print("\nORACLE STATUS: Reading the Matrix...")
        load_dotenv()
        mode = os.getenv("MATRIX_MODE", "development").lower()
        db_url = os.getenv("DATABASE_URL", "")
        api_key = os.getenv("API_KEY", "")
        log_level = os.getenv("LOG_LEVEL", "DEBUG").upper()
        zion_url = os.getenv("ZION_ENDPOINT", "")
        if not mode:
            raise EnvMissing("MATRIX_MODE")
        if not db_url:
            raise EnvMissing("DATABASE_URL")
        if not api_key:
            raise EnvMissing("API_KEY")
        if not log_level:
            raise EnvMissing("LOG_LEVEL")
        if not zion_url:
            raise EnvMissing("ZION_ENDPOINT")
        print("\nConfiguration loaded:")
        print(f"Mode: {mode}")
        if mode == "production":
            if not db_url.startswith("https"):
                print("Database: INSECURE - Production requires HTTPS")
            else:
                print("Database: Connected to remote instance")
        else:
            print("Database: Connected to local instance")
        status = "Authenticated" if api_key and api_key != "YOUR_API_KEY" else\
                 "Not Authenticated"
        print(f"API Access: {status}")
        if mode == "production" and log_level == "DEBUG":
            log_level = "INFO"
        elif mode == "development" and log_level != "DEBUG":
            log_level = "DEBUG"
        print(f"Log level: {log_level}")
        if not zion_url.startswith("https"):
            print("Zion Network: INSECURE - Resistance network requires HTTPS")
        else:
            print("Zion Network: Online")
        print("\nEnvironment security check:")
        if api_key and api_key != "YOUR_API_KEY":
            print("[OK] No hardcoded secrets detected")
        else:
            print("[!!] Hardcoded or default secret detected")
        if os.path.exists(".env"):
            print("[OK] .env file properly configured")
        else:
            print("[!!] .env file missing")
        if mode == "production":
            print("[OK] Production overrides available")
        else:
            print("[--] Production overrides available (Mode is development)")
        print("\nThe Oracle sees all configurations.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
