from enum import Enum

class InsuranceIntent(Enum):
    PRODUCT_INQUIRY = "product_inquiry"      # Hỏi về sản phẩm
    PREMIUM_CALCULATION = "premium_calc"      # Tính phí
    CLAIM_SUPPORT = "claim_support"          # Hỗ trợ bồi thường
    POLICY_LOOKUP = "policy_lookup"          # Tra cứu hợp đồng
    COMPLAINT = "complaint"                  # Khiếu nại
    GENERAL_FAQ = "general_faq"              # Câu hỏi chung

def classify_insurance_intent(message: str) -> InsuranceIntent:
    """Classify user intent for insurance queries"""
    message_lower = message.lower()
    
    # Keywords matching
    if any(word in message_lower for word in ["giá", "phí", "bao nhiêu", "chi phí"]):
        return InsuranceIntent.PREMIUM_CALCULATION
    
    elif any(word in message_lower for word in ["bồi thường", "claim", "yêu cầu", "tai nạn"]):
        return InsuranceIntent.CLAIM_SUPPORT
    
    elif any(word in message_lower for word in ["hợp đồng", "policy", "tra cứu", "số"]):
        return InsuranceIntent.POLICY_LOOKUP
    
    elif any(word in message_lower for word in ["khiếu nại", "complain", "không hài lòng"]):
        return InsuranceIntent.COMPLAINT
    
    elif any(word in message_lower for word in ["sản phẩm", "gói", "loại bảo hiểm"]):
        return InsuranceIntent.PRODUCT_INQUIRY
    
    else:
        return InsuranceIntent.GENERAL_FAQ