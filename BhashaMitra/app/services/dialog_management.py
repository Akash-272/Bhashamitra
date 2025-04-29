from app.services.simplification_service import simplify_text
from app.utils.faq_retrieval import retrieve_faq_answer

def handle_user_query(query, context_text, target_lang):
    # Simulate response using FAQ + simplifier
    base_answer = retrieve_faq_answer(query, context_text)
    return simplify_text(base_answer)