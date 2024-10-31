import requests
import sys


def main():
    try:
        if len(sys.argv) < 2:
            raise Exception("Missing command-line argument")

        sys_argument = sys.argv[1]
        try:
            bitcoin_amount = float(sys_argument)
        except ValueError:
            raise ValueError("Command-line argument is not a number")

        bitcoin_request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin_info = bitcoin_request.json()
        bitcoin_price = bitcoin_info.get("bpi", {}).get("USD", {}).get("rate_float")

        total = bitcoin_price * bitcoin_amount
        print(f"${total:,.4f}")

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    except Exception:
        print("Missing command-line argument")
        sys.exit(1)

    except requests.RequestException:
        print("Error al hacer un request a la API")
        sys.exit(1)


if __name__ == "__main__":
    main()
