"""
Module for handling customer messages and generating responses.
"""
from typing import Dict, Any
from src.db.product_db import ProductDB
from src.gemini_client import GeminiClient

class MessageHandler:
    """Handler for customer messages."""

    def __init__(self, gemini_client: GeminiClient, product_db: ProductDB):
        """
        Initialize the message handler.

        Args:
            gemini_client (GeminiClient): The Gemini client to use for generating responses.
            product_db (ProductDB): The product database.
        """
        self.gemini_client = gemini_client
        self.product_db = product_db

    def process_message(self, message_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a customer message and generate a response.

        Args:
            message_data (Dict[str, Any]): Dictionary containing the message data.
                Should include 'product_id' and 'message' keys.

        Returns:
            Dict[str, Any]: Dictionary containing the response data.
        """
        product_id = message_data.get('product_id')
        message = message_data.get('message', '')

        # Get product information
        product = self.product_db.get_product_by_id(product_id)
        if not product:
            return {
                'status': 'error',
                'message': f'Produto com ID {product_id} não encontrado.',
                'response': 'Desculpe, não conseguimos encontrar informações sobre este produto. Por favor, verifique o ID do produto e tente novamente.'
            }

        # Determine message type and generate response
        message_type = self._determine_message_type(message)
        response = self._generate_response(message, product, message_type)

        return {
            'status': 'success',
            'product_id': product_id,
            'product_name': product.get('name', ''),
            'message_type': message_type,
            'response': response
        }

    def _determine_message_type(self, message: str) -> str:
        """
        Determine the type of customer message.

        Args:
            message (str): The customer message.

        Returns:
            str: The message type ('product_question' or 'logistics_question').
        """
        # Keywords for logistics questions
        logistics_keywords = [
            'estoque', 'disponível', 'disponivel', 'quantidade', 'quando', 'prazo',
            'entrega', 'frete', 'envio', 'chegar', 'chegada', 'disponibilidade',
            'quanto tempo', 'dias úteis', 'dias uteis', 'semana', 'mês', 'mes'
        ]

        # Check if the message contains any logistics keywords
        message_lower = message.lower()
        for keyword in logistics_keywords:
            if keyword in message_lower:
                return 'logistics_question'

        # If no logistics keywords found, assume it's a product question
        return 'product_question'

    def _generate_response(self, message: str, product: Dict[str, Any], message_type: str) -> str:
        """
        Generate a response to a customer message.

        Args:
            message (str): The customer message.
            product (Dict[str, Any]): The product dictionary.
            message_type (str): The type of message ('product_question' or 'logistics_question').

        Returns:
            str: The generated response.
        """
        if message_type == 'logistics_question':
            # For logistics questions, return a generic response
            return (
                f"Agradecemos seu contato sobre o produto {product['name']}. "
                f"Para informações sobre estoque, prazo de entrega e outras questões logísticas, "
                f"nossa equipe de vendas precisa verificar os detalhes específicos. "
                f"Em breve, um de nossos vendedores entrará em contato com você para fornecer "
                f"informações precisas e atualizadas. Obrigado pela compreensão!"
            )
        else:
            # For product questions, use the Gemini API to generate a response
            prompt = self._create_prompt(product, message)
            return self.gemini_client.generate_text(prompt)

    def _create_prompt(self, product: Dict[str, Any], message: str) -> str:
        """
        Create a prompt for the Gemini API.

        Args:
            product (Dict[str, Any]): The product dictionary.
            message (str): The customer message.

        Returns:
            str: The prompt for the Gemini API.
        """
        # Extract relevant product information
        product_name = product.get('name', '')
        product_description = product.get('description', '')
        product_specs = product.get('specifications', {})
        product_usage = product.get('usage_instructions', '')

        # Format specifications as a string
        specs_str = ""
        for key, value in product_specs.items():
            if isinstance(value, list):
                value_str = ", ".join(value)
            else:
                value_str = str(value)
            specs_str += f"- {key}: {value_str}\n"

        return f"""
        Você é um assistente de atendimento ao cliente para uma loja de materiais de construção.

        Informações do produto:
        - Nome: {product_name}
        - Descrição: {product_description}
        - Especificações:
        {specs_str}
        - Instruções de uso: {product_usage}

        Pergunta do cliente: {message}

        Responda de forma direta e objetiva, com base nas informações do produto. Use português do Brasil.
        """
