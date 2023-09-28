from hermes.services.nubank import NubankService

transactions = [
    {
        "description": "Eds Bar e Restaurante",
        "category": "transaction",
        "amount": 2784,
        "time": "2023-09-07T06:36:09Z",
        "source": "upfront_national",
        "title": "restaurante",
        "amount_without_iof": 2784,
        "account": "5e6008db-6b95-490d-9c18-ccd0fb67bc80",
        "details": {"status": "unsettled", "subcategory": "card_present"},
        "id": "64f96f60-4cea-4c95-ad53-fabc8a33051d",
        "_links": {
            "self": {
                "href": "https://prod-s9-facade.nubank.com.br/api/transactions/64f96f60-4cea-4c95-ad53-fabc8a33051d"
            }
        },
        "tokenized": False,
        "href": "nuapp://transaction/64f96f60-4cea-4c95-ad53-fabc8a33051d",
    },
    {
        "description": "Barto Olegario Maciel",
        "category": "transaction",
        "amount": 4858,
        "time": "2023-09-07T00:16:49Z",
        "source": "upfront_national",
        "title": "restaurante",
        "amount_without_iof": 4858,
        "account": "5e6008db-6b95-490d-9c18-ccd0fb67bc80",
        "details": {"status": "settled", "subcategory": "card_present"},
        "id": "64f91672-de7b-4f25-8f8a-12a80f723a89",
        "_links": {
            "self": {
                "href": "https://prod-s9-facade.nubank.com.br/api/transactions/64f91672-de7b-4f25-8f8a-12a80f723a89"
            }
        },
        "tokenized": False,
        "href": "nuapp://transaction/64f91672-de7b-4f25-8f8a-12a80f723a89",
    },
    {
        "description": "Raia",
        "category": "transaction",
        "amount": 1415,
        "time": "2023-09-06T20:55:53Z",
        "source": "upfront_national",
        "title": "saúde",
        "amount_without_iof": 1415,
        "account": "5e6008db-6b95-490d-9c18-ccd0fb67bc80",
        "details": {"status": "settled", "subcategory": "card_present"},
        "id": "64f8e763-5f49-4826-9e4e-6f7d3c5c8f0b",
        "_links": {
            "self": {
                "href": "https://prod-s9-facade.nubank.com.br/api/transactions/64f8e763-5f49-4826-9e4e-6f7d3c5c8f0b"
            }
        },
        "tokenized": True,
        "href": "nuapp://transaction/64f8e763-5f49-4826-9e4e-6f7d3c5c8f0b",
    },
    {
        "description": "Pg*Ml",
        "category": "transaction",
        "amount": 3000,
        "time": "2023-09-06T19:19:59Z",
        "source": "upfront_national",
        "title": "serviços",
        "amount_without_iof": 3000,
        "account": "5e6008db-6b95-490d-9c18-ccd0fb67bc80",
        "details": {"status": "settled", "subcategory": "card_not_present"},
        "id": "64f8d0ee-2e94-4a62-8f4e-95e38c688996",
        "_links": {
            "self": {
                "href": "https://prod-s9-facade.nubank.com.br/api/transactions/64f8d0ee-2e94-4a62-8f4e-95e38c688996"
            }
        },
        "tokenized": False,
        "href": "nuapp://transaction/64f8d0ee-2e94-4a62-8f4e-95e38c688996",
    },
    {
        "description": "Mercadolivre*3produto",
        "category": "transaction",
        "amount": 13905,
        "time": "2023-09-06T13:41:19Z",
        "source": "upfront_national",
        "title": "serviços",
        "amount_without_iof": 13905,
        "account": "5e6008db-6b95-490d-9c18-ccd0fb67bc80",
        "details": {"status": "settled", "subcategory": "card_not_present"},
        "id": "64f88180-b8b0-4c5a-a51d-e2ce5717e552",
        "_links": {
            "self": {
                "href": "https://prod-s9-facade.nubank.com.br/api/transactions/64f88180-b8b0-4c5a-a51d-e2ce5717e552"
            }
        },
        "tokenized": True,
        "href": "nuapp://transaction/64f88180-b8b0-4c5a-a51d-e2ce5717e552",
    },
    {
        "description": "Pg*Ml",
        "category": "transaction",
        "amount": 3000,
        "time": "2023-09-06T12:28:38Z",
        "source": "upfront_national",
        "title": "serviços",
        "amount_without_iof": 3000,
        "account": "5e6008db-6b95-490d-9c18-ccd0fb67bc80",
        "details": {"status": "settled", "subcategory": "card_not_present"},
        "id": "64f87077-5d4a-4cfa-9381-52aade16cdba",
        "_links": {
            "self": {
                "href": "https://prod-s9-facade.nubank.com.br/api/transactions/64f87077-5d4a-4cfa-9381-52aade16cdba"
            }
        },
        "tokenized": False,
        "href": "nuapp://transaction/64f87077-5d4a-4cfa-9381-52aade16cdba",
    },
    {
        "description": "Pg *Rechia Store",
        "category": "transaction",
        "amount": 11724,
        "time": "2023-09-05T14:55:23Z",
        "source": "upfront_national",
        "title": "vestuário",
        "amount_without_iof": 11724,
        "account": "5e6008db-6b95-490d-9c18-ccd0fb67bc80",
        "details": {"status": "settled", "subcategory": "card_not_present"},
        "id": "64f7415b-94b9-455c-b90b-569db67a840b",
        "_links": {
            "self": {
                "href": "https://prod-s9-facade.nubank.com.br/api/transactions/64f7415b-94b9-455c-b90b-569db67a840b"
            }
        },
        "tokenized": False,
        "href": "nuapp://transaction/64f7415b-94b9-455c-b90b-569db67a840b",
    },
    {
        "description": "Amazon",
        "category": "transaction",
        "amount": 20705,
        "time": "2023-09-05T09:17:07Z",
        "source": "installments_merchant",
        "title": "eletrónicos",
        "amount_without_iof": 20705,
        "account": "5e6008db-6b95-490d-9c18-ccd0fb67bc80",
        "details": {
            "status": "settled",
            "charges": {"count": 4, "amount": 5176},
            "subcategory": "card_not_present",
        },
        "id": "64f6f218-b7cd-4906-989a-3a6a81a1ddf8",
        "_links": {
            "self": {
                "href": "https://prod-s9-facade.nubank.com.br/api/transactions/64f6f218-b7cd-4906-989a-3a6a81a1ddf8"
            }
        },
        "tokenized": False,
        "href": "nuapp://transaction/64f6f218-b7cd-4906-989a-3a6a81a1ddf8",
    },
]


class TestNubankService:
    def test_get_transactions(self):
        transactions = NubankService().get_transactions()
        print(transactions)

    def test_create_transaction(self):
        service = NubankService()
        for transaction in transactions:
            service._create_transaction(transaction)
