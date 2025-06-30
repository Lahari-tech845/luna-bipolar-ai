import json
import datetime
import random

def lambda_handler(event, context):
    """
    LUNA - Lifeline for Understanding Neurological Assistance
    AI companion for bipolar disorder support
    """
    
    # Parse incoming request
    try:
        body = json.loads(event.get('body', '{}')) if event.get('body') else {}
    except:
        body = {}
    
    path = event.get('path', '/hello')
    method = event.get('httpMethod', 'GET')
    
    # Route requests
    if path == '/checkin':
        return handle_daily_checkin(body)
    elif path == '/mood':
        return handle_mood_tracking(body)
    elif path == '/crisis':
        return handle_crisis_detection(body)
    elif path == '/chat':
        return handle_ai_chat(body)
    else:
        return create_response(200, {
            "message": "Hello! I'm LUNA - your AI companion for bipolar support.",
            "available_endpoints": ["/checkin", "/mood", "/crisis", "/chat"],
            "timestamp": datetime.datetime.now().isoformat()
        })

def handle_daily_checkin(body):
    """Daily mood and wellness check-in"""
    user_name = body.get('name', 'friend')
    mood_score = body.get('mood_score', 5)
    sleep_hours = body.get('sleep_hours', 7)
    
    # Analyze bipolar episode risk
    risk_level = analyze_episode_risk(mood_score, sleep_hours)
    
    # Generate personalized response
    response_message = generate_checkin_response(user_name, mood_score, risk_level)
    
    return create_response(200, {
        "message": response_message,
        "mood_score": mood_score,
        "sleep_hours": sleep_hours,
        "risk_level": risk_level,
        "recommendations": get_recommendations(risk_level),
        "next_checkin": "Tomorrow at the same time",
        "luna_says": f"Thank you for checking in, {user_name}. I'm here whenever you need support."
    })

def handle_mood_tracking(body):
    """Track mood patterns for bipolar disorder"""
    current_mood = body.get('mood_score', 5)
    energy_level = body.get('energy_level', 5)
    
    # Detect mood patterns
    pattern = detect_mood_pattern(current_mood, energy_level)
    
    return create_response(200, {
        "current_mood": current_mood,
        "energy_level": energy_level,
        "pattern_detected": pattern,
        "luna_insight": get_mood_insight(pattern),
        "coping_strategies": get_coping_strategies(pattern)
    })

def handle_crisis_detection(body):
    """Crisis intervention for bipolar episodes"""
    user_message = body.get('message', '').lower()
    crisis_indicators = body.get('crisis_indicators', [])
    
    # Check for crisis keywords
    manic_keywords = ['cant sleep', 'invincible', 'spending spree', 'racing thoughts', 'dont need sleep']
    depressive_keywords = ['want to die', 'hurt myself', 'hopeless', 'worthless', 'cant go on']
    
    crisis_type = None
    if any(keyword in user_message for keyword in manic_keywords):
        crisis_type = "manic_episode"
    elif any(keyword in user_message for keyword in depressive_keywords):
        crisis_type = "depressive_episode"
    
    if crisis_type:
        intervention = get_crisis_intervention(crisis_type)
        return create_response(200, {
            "crisis_detected": True,
            "crisis_type": crisis_type,
            "immediate_support": intervention,
            "emergency_contacts": "988 Suicide & Crisis Lifeline",
            "luna_message": "I'm here with you. You're not alone. Let's get through this together."
        })
    
    return create_response(200, {
        "crisis_detected": False,
        "luna_message": "I'm listening. How can I support you today?"
    })

def handle_ai_chat(body):
    """AI-powered conversation for emotional support"""
    user_message = body.get('message', '')
    user_name = body.get('name', 'friend')
    
    # Generate empathetic AI response
    ai_response = generate_ai_response(user_message, user_name)
    
    return create_response(200, {
        "user_message": user_message,
        "luna_response": ai_response,
        "support_resources": [
            "National Suicide Prevention Lifeline: 988",
            "Crisis Text Line: Text HOME to 741741",
            "NAMI Support: 1-800-950-NAMI"
        ]
    })

def analyze_episode_risk(mood_score, sleep_hours):
    """Analyze risk of bipolar episode"""
    if mood_score >= 8 and sleep_hours <= 4:
        return "high_manic_risk"
    elif mood_score <= 2 and sleep_hours >= 10:
        return "high_depressive_risk"
    elif mood_score >= 7 or mood_score <= 3:
        return "moderate_risk"
    else:
        return "stable"

def generate_checkin_response(name, mood_score, risk_level):
    """Generate personalized check-in response"""
    responses = {
        "high_manic_risk": f"Hi {name}, I notice your mood is very high with little sleep. This might be a manic episode starting. Please reach out to your doctor and try some grounding exercises.",
        "high_depressive_risk": f"Hello {name}, I can see you're struggling today. Remember these feelings will pass. You're not alone, and I'm here to support you.",
        "moderate_risk": f"Hi {name}, I see some mood changes today. Let's focus on your self-care routine and coping strategies.",
        "stable": f"Good to see you, {name}! You're maintaining good stability. Keep up with your healthy routines."
    }
    return responses.get(risk_level, f"Hello {name}, thank you for checking in with me today.")

def get_recommendations(risk_level):
    """Get specific recommendations based on risk level"""
    recommendations = {
        "high_manic_risk": [
            "Contact your psychiatrist immediately",
            "Avoid major financial decisions",
            "Try grounding exercises (5-4-3-2-1 technique)",
            "Limit stimulation (dim lights, quiet environment)",
            "Ask a trusted friend to stay with you"
        ],
        "high_depressive_risk": [
            "Reach out to your support network",
            "Try gentle physical activity (short walk)",
            "Practice deep breathing exercises",
            "Maintain regular meals",
            "Consider calling crisis hotline: 988"
        ],
        "moderate_risk": [
            "Monitor your mood closely",
            "Stick to your medication schedule",
            "Maintain regular sleep routine",
            "Practice mindfulness or meditation"
        ],
        "stable": [
            "Continue your current routine",
            "Keep tracking your mood daily",
            "Engage in activities you enjoy",
            "Stay connected with supportive people"
        ]
    }
    return recommendations.get(risk_level, [])

def detect_mood_pattern(mood, energy):
    """Detect bipolar mood patterns"""
    if mood >= 7 and energy >= 7:
        return "possible_hypomania"
    elif mood <= 3 and energy <= 3:
        return "possible_depression"
    elif abs(mood - 5) >= 2:
        return "mood_fluctuation"
    else:
        return "stable_mood"

def get_mood_insight(pattern):
    """Provide insights about mood patterns"""
    insights = {
        "possible_hypomania": "Your elevated mood and energy might indicate a hypomanic phase. Stay mindful of your decisions and sleep schedule.",
        "possible_depression": "Low mood and energy suggest you might be entering a depressive phase. Focus on basic self-care and reaching out for support.",
        "mood_fluctuation": "I notice some mood changes. This is normal, but let's keep monitoring to identify any patterns.",
        "stable_mood": "Your mood appears stable today. This is great! Consistency in mood management is key."
    }
    return insights.get(pattern, "Keep tracking your mood to help identify patterns.")

def get_coping_strategies(pattern):
    """Provide coping strategies based on mood pattern"""
    strategies = {
        "possible_hypomania": [
            "Practice slow, deep breathing",
            "Write in a journal to process thoughts",
            "Limit caffeine and stimulants",
            "Create a calming environment"
        ],
        "possible_depression": [
            "Take small, manageable steps",
            "Connect with one supportive person",
            "Try gentle movement or stretching",
            "Focus on basic needs (food, water, rest)"
        ],
        "mood_fluctuation": [
            "Use mood tracking apps",
            "Practice mindfulness meditation",
            "Maintain consistent daily routines",
            "Identify your mood triggers"
        ],
        "stable_mood": [
            "Continue what's working well",
            "Plan enjoyable activities",
            "Maintain social connections",
            "Practice gratitude exercises"
        ]
    }
    return strategies.get(pattern, ["Focus on self-care", "Stay connected with support system"])

def get_crisis_intervention(crisis_type):
    """Provide immediate crisis intervention"""
    interventions = {
        "manic_episode": {
            "immediate_steps": [
                "Find a quiet, calm space",
                "Call your psychiatrist or crisis line",
                "Avoid making major decisions",
                "Ask someone trusted to stay with you"
            ],
            "grounding_technique": "Try the 5-4-3-2-1 technique: Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you taste."
        },
        "depressive_episode": {
            "immediate_steps": [
                "Call 988 (Suicide & Crisis Lifeline)",
                "Reach out to a trusted friend or family member",
                "Go to your nearest emergency room if needed",
                "Remove any harmful objects from your vicinity"
            ],
            "comfort_reminder": "These intense feelings will pass. You matter, and help is available."
        }
    }
    return interventions.get(crisis_type, {"message": "I'm here to help. Please reach out to a mental health professional."})

def generate_ai_response(message, name):
    """Generate empathetic AI responses"""
    message_lower = message.lower()
    
    if 'sad' in message_lower or 'depressed' in message_lower:
        return f"I hear that you're feeling sad, {name}. Those feelings are valid, and it's okay to have difficult days. What's one small thing that might bring you a tiny bit of comfort right now?"
    
    elif 'anxious' in message_lower or 'worried' in message_lower:
        return f"Anxiety can feel overwhelming, {name}. Let's take this one breath at a time. Try breathing in for 4 counts, holding for 4, and breathing out for 6. I'm here with you."
    
    elif 'manic' in message_lower or 'hyper' in message_lower:
        return f"It sounds like you have a lot of energy right now, {name}. Let's channel that energy safely. Have you been sleeping well? Sometimes slowing down can help us think more clearly."
    
    elif 'medication' in message_lower:
        return f"Medication is an important part of managing bipolar disorder, {name}. If you're having concerns about your medication, please discuss them with your doctor. I'm here to support you through the process."
    
    else:
        return f"Thank you for sharing with me, {name}. I'm listening and I care about how you're feeling. Remember, you're not alone in this journey. What would be most helpful for you right now?"

def create_response(status_code, body):
    """Create properly formatted API response"""
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps(body, default=str)
    }
