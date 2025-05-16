"""
Module for processing customer comments and generating responses.
"""

class CommentProcessor:
    """Processor for customer comments."""
    
    def __init__(self, gemini_client):
        """
        Initialize the comment processor.
        
        Args:
            gemini_client (GeminiClient): The Gemini client to use for generating responses.
        """
        self.gemini_client = gemini_client
    
    def generate_response(self, product, comment):
        """
        Generate a response to a customer comment.
        
        Args:
            product (str): The product the comment is about.
            comment (str): The customer comment.
            
        Returns:
            str: The generated response.
        """
        prompt = self._create_prompt(product, comment)
        return self.gemini_client.generate_text(prompt)
    
    def _create_prompt(self, product, comment):
        """
        Create a prompt for the Gemini API.
        
        Args:
            product (str): The product the comment is about.
            comment (str): The customer comment.
            
        Returns:
            str: The prompt for the Gemini API.
        """
        return f"""
        Você é um assistente de atendimento ao cliente para uma loja online.
        
        Produto: {product}
        Comentário do cliente: {comment}
        
        Por favor, forneça uma resposta profissional, empática e útil para este comentário.
        A resposta deve:
        1. Agradecer ao cliente pelo feedback
        2. Abordar especificamente os pontos mencionados no comentário
        3. Oferecer soluções ou próximos passos, se aplicável
        4. Manter um tom amigável e prestativo
        5. Ser escrita em português do Brasil
        
        Resposta:
        """
