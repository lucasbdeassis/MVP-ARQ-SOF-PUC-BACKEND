from datetime import datetime

from flask import Blueprint, g, request

from hermes.api.auth import requires_auth
from hermes.api.spec import add_schema
from hermes.application.factories import InjectorFactory
from hermes.domain.transaction import Transaction
from hermes.views.transaction_schema import (
    CreateTransactionSchema,
    UpdateTransactionSchema,
)

transaction_controller = Blueprint("transaction_controller", __name__)

add_schema([CreateTransactionSchema, UpdateTransactionSchema, Transaction])


@transaction_controller.route("/transactions", methods=["GET"])
@requires_auth()
def list_transactions():
    """
    ---
    get:
      summary: Returns a list of transactions
      description: Returns a list of transactions
      security:
        - token: []
      responses:
        200:
          description: list of transactions
          content:
            application/json:
              schema: Transaction
    """
    month = request.args.get("month")
    year = request.args.get("year", datetime.now().year)
    with InjectorFactory() as factory:
        service = factory.transaction_service(g.user)
        if month and year:
            transactions = service.get_by_month(month, year)
            return [transaction.model_dump() for transaction in transactions], 200
        transactions = service.list_transactions()
        return [transaction.model_dump() for transaction in transactions], 200


@transaction_controller.route("/transactions", methods=["POST"])
@requires_auth()
def create_transaction():
    """
    ---
    post:
      summary: Adds a new transaction
      description: Adds a new transaction
      security:
        - token: []
      requestBody:
        required: true
        content:
          application/json:
            schema: CreateTransactionSchema
      responses:
        200:
          description: the created transaction
          content:
            application/json:
              schema: CreateTransactionSchema
    """
    try:
        print(request.json)
        transaction_create = CreateTransactionSchema(**request.json)  # type: ignore
    except Exception as e:
        return {"error": str(e)}, 400
    with InjectorFactory() as factory:
        service = factory.transaction_service(g.user)
        transactions = service.create_transaction(transaction_create)
        return [transaction.model_dump() for transaction in transactions], 200


@transaction_controller.route("/transactions/<id>", methods=["GET"])
@requires_auth()
def get_transaction(id):
    """
    ---
    get:
      summary: Returns a transaction
      description: Returns a transaction
      security:
        - token: []
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type : string
      responses:
        200:
          description: a transaction
          content:
            application/json:
              schema: Transaction
        404:
          description: Transaction not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Transaction not found
    """
    with InjectorFactory() as factory:
        service = factory.transaction_service(g.user)
        transaction = service.get_transaction(id)
        if not transaction:
            return {"error": "Transaction not found"}, 404
        return transaction.model_dump(), 200


@transaction_controller.route("/transactions/<id>", methods=["PUT"])
@requires_auth()
def update_transaction(id):
    """
    ---
    put:
      summary: Updates a transaction
      description: Updates a transaction
      security:
        - token: []
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type : string
      requestBody:
        required: true
        content:
          application/json:
            schema: UpdateTransactionSchema
      responses:
        200:
          description: the updated transaction
          content:
            application/json:
              schema: Transaction
        404:
          description: Transaction not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Transaction not found
    """
    try:
        transaction_update = UpdateTransactionSchema(**request.json)  # type: ignore
    except Exception as e:
        print(e)
        return {"error": str(e)}, 400
    with InjectorFactory() as factory:
        service = factory.transaction_service(g.user)
        transaction = service.update_transaction(id, transaction_update)
        if not transaction:
            return {"error": "Transaction not found"}, 404
        return transaction.model_dump(), 200


@transaction_controller.route("/transactions/<id>", methods=["DELETE"])
@requires_auth()
def delete_transaction(id):
    """
    ---
    delete:
      summary: Removes a transaction
      description: Removes a transaction
      security:
        - token: []
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type : string
      responses:
        200:
          description: success message
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Transaction deleted successfully
        404:
          description: Transaction not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Transaction not found
    """
    with InjectorFactory() as factory:
        service = factory.transaction_service(g.user)
        service.delete_transaction(id)
        return {"message": "Transaction deleted successfully"}, 200
