# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    oracle.py                                          :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/02 17:07:58 by bfitte            #+#    #+#             #
#    Updated: 2026/02/02 17:07:59 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

try:
    import os
    import sys
    from dotenv import load_dotenv
except ImportError as e:
    print(e)
    sys.exit(1)


class EnvError(Exception):
    def __init__(self, details: str):
        message: str = details
        super().__init__(message)


class EnvMissing(EnvError):
    def __init__(self, details: str):
        details = f"{details} value is missing in .env"
        super().__init__(details)


def main():
    """First it check if .env file exist and if it contains all requested
    variables. Then this function checks whether the contents of the
    variables are consistent according to matrix_mode.
    """
    try:
        if not os.path.exists(".env"):
            raise EnvError(".env file is missing!")
        print("\nORACLE STATUS: Reading the Matrix...")

        # Reading variables from a .env file and setting them in os.environ
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

        # Check if url is consistent according to matrix_mode
        if mode == "production":
            if not db_url.startswith("https"):
                print("Database: INSECURE - Production requires HTTPS")
            else:
                print("Database: Connected to remote instance")
        else:
            print("Database: Connected to local instance")

        # Check if the user added a key to API_KEY
        status = "Authenticated" if api_key and api_key != "YOUR_API_KEY" else\
                 "Not Authenticated"
        print(f"API Access: {status}")

        # Check consistent LOG_LEVEL value according to matrix_mode
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

        # Check if an API_KEY environment variable exists and is configured
        if api_key and api_key != "YOUR_API_KEY":
            print("[OK] No hardcoded secrets detected")
        else:
            print("[!!] Hardcoded or default secret detected")
        if os.path.exists(".env") and mode and db_url and api_key and\
                log_level and zion_url:
            print("[OK] .env file properly configured")
        else:
            print("[!!] .env file missing or isn't properly configured")

        # Check if it's production mode when the matrix_mode is define in
        # command line
        if mode == "production":
            print("[OK] Production overrides available")
        else:
            print("[--] Production overrides available (Mode is development)")
        print("\nThe Oracle sees all configurations.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
