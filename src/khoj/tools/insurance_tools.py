from langchain.tools import tool
from typing import Dict, Any

@tool
def calculate_premium(age: int, coverage: int, term: int) -> Dict[str, Any]:
    """
    Calculate insurance premium based on parameters
    
    Args:
        age: Customer age
        coverage: Coverage amount in million VND
        term: Insurance term in years
    """
    # Simple calculation (thay bằng logic thật)
    base_rate = 0.02  # 2% của số tiền bảo hiểm
    age_factor = 1 + (age - 25) * 0.01  # Tăng theo tuổi
    term_discount = 0.95 if term >= 10 else 1.0
    
    annual_premium = coverage * 1_000_000 * base_rate * age_factor * term_discount
    monthly_premium = annual_premium / 12
    
    return {
        "annual_premium": int(annual_premium),
        "monthly_premium": int(monthly_premium),
        "coverage_amount": coverage * 1_000_000,
        "term_years": term
    }

@tool
def lookup_policy(policy_number: str) -> Dict[str, Any]:
    """
    Look up insurance policy by number
    
    Args:
        policy_number: Policy contract number
    """
    # Mock data - thay bằng DB query thật
    mock_db = {
        "BH001": {
            "policy_number": "BH001",
            "customer_name": "Nguyễn Văn A",
            "product": "Bảo hiểm nhân thọ",
            "coverage": 500_000_000,
            "status": "active",
            "start_date": "2024-01-01",
            "end_date": "2044-01-01"
        }
    }
    
    return mock_db.get(policy_number, {"error": "Policy not found"})

@tool  
def check_claim_status(claim_id: str) -> Dict[str, Any]:
    """
    Check insurance claim processing status
    
    Args:
        claim_id: Claim request ID
    """
    # Mock data
    mock_claims = {
        "CLM001": {
            "claim_id": "CLM001",
            "status": "processing",
            "submitted_date": "2024-10-15",
            "expected_completion": "2024-11-15",
            "amount_claimed": 10_000_000,
            "notes": "Đang chờ hồ sơ bổ sung"
        }
    }
    
    return mock_claims.get(claim_id, {"error": "Claim not found"})