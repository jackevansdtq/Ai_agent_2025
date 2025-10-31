from khoj.processor.conversation.insurance_intents import classify_insurance_intent, InsuranceIntent
from khoj.tools.insurance_tools import calculate_premium, lookup_policy, check_claim_status

# Thêm vào hàm chat endpoint
@api.post("/api/chat")
async def chat(request: ChatRequest):
    # ... existing code ...
    
    # Add insurance intent classification
    intent = classify_insurance_intent(request.message)
    
    # Route based on intent
    if intent == InsuranceIntent.COMPLAINT:
        # Handoff to human immediately
        return await handoff_to_human_agent(request)
    
    elif intent == InsuranceIntent.CLAIM_SUPPORT:
        # Use claim tools
        tools = [check_claim_status]
    
    elif intent == InsuranceIntent.PREMIUM_CALCULATION:
        tools = [calculate_premium]
    
    elif intent == InsuranceIntent.POLICY_LOOKUP:
        tools = [lookup_policy]
    
    else:
        tools = []  # General RAG-based chat
    
    # Continue with existing chat logic + tools
    response = await generate_response(
        message=request.message,
        tools=tools,
        context=retrieved_context
    )
    
    return response