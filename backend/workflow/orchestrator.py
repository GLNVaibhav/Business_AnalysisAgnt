# sweeyam_team26-main/backend/workflow/orchestrator.py

from google import genai
from google.genai import types

from agents.agent1_surveillance import surveillance_agent
from agents.agent2_analysis import analysis_agent
from agents.agent3_alternatives import alternatives_agent
from agents.agent4_decision import decision_agent
from agents.business_analysis_agent import business_analysis_agent

from agents.demand_intelligence_agent import demand_intelligence_agent
from agents.inventory_alert_agent import inventory_alert_agent
from agents.vendor_price_optimization_agent import vendor_price_optimization_agent

from utils.schema_normalizer import (
    normalize_orders_schema,
    normalize_sellers_schema,
    normalize_inventory_schema
)

client = genai.Client()

# 🌐 MULTI-SECTOR KNOWLEDGE ENGINE RULES (PHASED ROLLOUT)
SECTOR_GUARDRAILS = {
    "ECOMMERCE": """
    Persona: Minimalist E-commerce Operations Auditor.
    Rules: Focus exclusively on stock turnover velocity, customer acquisition (CAC), and immediate margins. 
    Constraint: If an issue can be answered with a static threshold or standard calculation, strip out all predictive AI forecasting text.
    """,
    "HEALTHCARE": """
    Persona: HIPAA-Compliant Clinical Efficiency Officer.
    Rules: Strictly focus on patient throughput metrics, resource allocation, and facility overhead constraints.
    Constraint: Redact/flag potential PHI concepts. Eliminate complex medical jargon in favor of actionable administrative briefs.
    """,
    "FINANCE": """
    Persona: Quantitative Capital Adequacy Regulator.
    Rules: Enforce strict financial tracking rules and margin calculations on all cash-flow summaries.
    Constraint: Ban qualitative market sentiment prose. Deliver strict numeric risk matrices and deviations only.
    """
}

def apply_knowledge_filter(state_data: dict, current_sector: str) -> dict:
    """
    Actively intercepts the final business summary and applies Ponytail-style
    structural minimalism using an LLM critique loop.
    """
    sector_key = current_sector.upper()
    ruleset = SECTOR_GUARDRAILS.get(sector_key, SECTOR_GUARDRAILS["ECOMMERCE"])
    
    if "business_summary" in state_data and state_data["business_summary"]:
        raw_summary = state_data["business_summary"]
        
        system_prompt = f"""
        {ruleset}
        
        CRITICAL JOB: You are a strict editor. Review the text provided and strip out any 
        over-engineered assumptions, speculative jargon, or repetitive wording.
        Rewrite it to be dense, scannable, and directly practical for a stakeholder in the {sector_key} industry.
        """
        
        # Call a fast model to prune the final output down to strict minimalist compliance
        referee_response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Text to sanitize:\n{raw_summary}",
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.1  # Low temperature ensures rigid rule adherence
            )
        )
        
        # Overwrite the summary with the pristine, minimal version
        state_data["business_summary"] = referee_response.text
        state_data["meta_sector_framework"] = f"Verified under framework: {sector_key}"
        
    return state_data


def run_workflow(orders_df, reviews_df, sellers_df, inventory_df, sector: str = "ECOMMERCE"):
    """
    Runs the multi-agent analysis pipeline across multiple sectors dynamically.
    :param sector: Controls the behavioral constraints ('ECOMMERCE', 'HEALTHCARE', or 'FINANCE')
    """
    
    # 🔐 Normalize all schemas ONCE
    orders_df = normalize_orders_schema(orders_df)
    sellers_df = normalize_sellers_schema(sellers_df)
    inventory_df = normalize_inventory_schema(inventory_df)

    # Initial state configuration object
    state = {
        "alert": {},
        "analysis": {},
        "alternatives": [],
        "decision": {},
        "business_summary": "",
        "demand_insights": [],
        "inventory_alerts": [],
        "vendor_optimizations": [],
        "active_sector": sector.upper()  # Tractable sector marker
    }

    # --- 1. SEQUENTIAL CORE ANALYSIS WORKFLOW ---
    state = surveillance_agent(orders_df, reviews_df, state)
    state = analysis_agent(state)
    state = alternatives_agent(state, sellers_df)
    state = decision_agent(state)
    state = business_analysis_agent(state)  # Dynamic sector prompt handles this now!

    # --- 2. PARALLEL DOMAIN INTELLIGENCE ENGINE ---
    state["demand_insights"] = demand_intelligence_agent(orders_df)
    state["inventory_alerts"] = inventory_alert_agent(orders_df, inventory_df)
    state["vendor_optimizations"] = vendor_price_optimization_agent(
        orders_df, sellers_df
    )

    # --- 3. KNOWLEDGE GUARDRAIL INTERCEPTION MIDDLEWARE ---
    # Actively sanitizes and rewrites the final summary based on your rollout sector
    state = apply_knowledge_filter(state, current_sector=sector)

    return state
