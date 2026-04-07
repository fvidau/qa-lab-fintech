import requests

BASE_URL = "http://localhost:3000"


def test_get_transactions_status_200():
    response = requests.get(f"{BASE_URL}/transactions")
    assert response.status_code == 200


def test_transactions_response_is_list():
    response = requests.get(f"{BASE_URL}/transactions")
    data = response.json()
    assert isinstance(data, list)


def test_transaction_has_required_fields():
    response = requests.get(f"{BASE_URL}/transactions")
    data = response.json()

    for tx in data:
        assert "id" in tx
        assert "fromAccountId" in tx
        assert "toAccountId" in tx
        assert "amount" in tx
        assert "currency" in tx
        assert "status" in tx


def test_transaction_accounts_exist():
    transactions_response = requests.get(f"{BASE_URL}/transactions")
    accounts_response = requests.get(f"{BASE_URL}/accounts")

    assert transactions_response.status_code == 200
    assert accounts_response.status_code == 200

    transactions = transactions_response.json()
    accounts = accounts_response.json()

    account_ids = {int(account["id"]) for account in accounts}

    for tx in transactions:
        assert tx["fromAccountId"] in account_ids
        assert tx["toAccountId"] in account_ids