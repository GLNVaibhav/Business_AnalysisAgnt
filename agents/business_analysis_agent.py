# sweeyam_team26-main/agents/business_analysis_agent.py

from google import genai
from google.genai import types

client = genai.Client()

# Sector-specific mental models injected before content generation
SECTOR_CONTEXTS = {
    "ECOMMERCE": """
    You are analyzing an E-commerce operation. Focus strictly on supply chain logistics, 
    inventory velocity, and unit margins. If safety stock thresholds are breached, 
    prioritize immediate operational resolution over long-term strategic predictions.
    """,
    "HEALTHCARE": """
    You are analyzing a Healthcare environment. Focus on capacity optimization, 
    operational throughput, and resource bottlenecks. Maintain strict compliance 
    with privacy boundaries and structure recommendations as clear administrative directives.
    """,
    "FINANCE": """
    You are analyzing a Financial framework. Focus strictly on data-backed quantitative matrices, 
    risk tolerances, and cash-flow variances. Exclude all emotional market commentary.
    """
}

def business_analysis_agent(state: dict) -> dict:
    """
    Processes the current pipeline state and constructs a sector-tailored 
    business analysis summary.
    """
    # 1. Dynamically read the active sector decided by the orchestrator
    sector = state.get("active_sector", "ECOMMERCE").upper()
    sector_guideline = SECTOR_CONTEXTS.get(sector, SECTOR_CONTEXTS["ECOMMERCE"])
    
    # 2. Gather raw facts compiled by preceding agents in the pipeline
    raw_inputs = f"""
    Current Alerts: {state.get('alert', {})}
    Analytical Findings: {state.get('analysis', {})}
    Identified Alternatives: {state.get('alternatives', [])}
    """
    
    # 3. Formulate the sector-aware prompt instruction
    system_instruction = f"""
    You are the Core Business Intelligence Brain for Team 26.
    {sector_guideline}
    
    INSTRUCTION: Write a high-level summary synthesising the raw data inputs. 
    Be direct, scannable, and drop conversational fluff.
    """
    
    # 4. Generate the payload
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"Raw Pipeline Inputs to synthesize:\n{raw_inputs}",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.2
        )
    )
    
    # 5. Populate state and pass forward
    state["business_summary"] = response.text
    return state
