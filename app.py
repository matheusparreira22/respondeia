"""
Main application file for the customer comment response system.
This application uses the Gemini API to generate responses to customer comments about
construction materials products.
"""
import os
from dotenv import load_dotenv
from src.gemini_client import GeminiClient
from src.db.product_db import ProductDB
from src.message_handler import MessageHandler

def main():
    """Main function to run the application."""
    # Load environment variables
    load_dotenv()

    # Initialize the Gemini client
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        return

    # Initialize components
    gemini_client = GeminiClient(api_key)
    product_db = ProductDB()
    message_handler = MessageHandler(gemini_client, product_db)

    # Example usage
    print("Sistema de Resposta a Comentários de Clientes - Materiais de Construção")
    print("----------------------------------------------------------------------")
    print("Digite 'exit' para sair da aplicação.")
    print("Digite 'list' para listar todos os produtos disponíveis.")

    while True:
        command = input("\nComando (list, responder, exit): ")
        if command.lower() == 'exit':
            break

        if command.lower() == 'list':
            list_products(product_db)
            continue

        if command.lower() == 'responder':
            process_customer_message(message_handler)
            continue

        print("Comando não reconhecido. Tente 'list', 'responder' ou 'exit'.")

def list_products(product_db):
    """List all products in the database."""
    products = product_db.get_all_products()
    print("\nProdutos disponíveis:")
    print("---------------------")
    for product in products:
        print(f"ID: {product['id']} - {product['name']} ({product['category']})")

def process_customer_message(message_handler):
    """Process a customer message."""
    product_id = input("ID do produto: ")
    if product_id.lower() == 'exit':
        return

    message = input("Mensagem do cliente: ")
    if message.lower() == 'exit':
        return

    # Create message data
    message_data = {
        'product_id': product_id,
        'message': message
    }

    response_data = message_handler.process_message(message_data)
    print(f"\n{response_data['response']}")

if __name__ == "__main__":
    main()
