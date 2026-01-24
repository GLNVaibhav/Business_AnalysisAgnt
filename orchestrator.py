from agents.agent1_surveillance import surveillance_agent
from agents.agent2_analysis import analysis_agent
from agents.agent3_alternatives import alternatives_agent
from agents.agent4_decision import decision_agent
from agents.business_analysis_agent import business_analysis_agent
from agents.demand_intelligence_agent import demand_intelligence_agent
from agents.inventory_alert_agent import inventory_alert_agent
from agents.vendor_price_optimization_agent import vendor_price_optimization_agent


def run_workflow(orders_df, reviews_df, sellers_df, inventory_df):
    """
    Stable orchestrator — NO user_goal, NO ambiguity
    """

    analysis_state = {
        "context": {
            "domain": "e-commerce",
            "entity_type": "seller"
        },
        "alert": {},
        "analysis": {},
        "alternatives": [],
        "decision": {},
        "demand_insights": [],
        "inventory_alerts": [],
        "vendor_optimizations": [],
        "business_summary": ""
    }

    # Core pipeline
    analysis_state = surveillance_agent(orders_df, reviews_df, analysis_state)
    analysis_state = analysis_agent(analysis_state)
    analysis_state = alternatives_agent(analysis_state, sellers_df)
    analysis_state = decision_agent(analysis_state)
    analysis_state["business_summary"] = business_analysis_agent(analysis_state)

    # Proactive intelligence (safe additions)
    analysis_state["demand_insights"] = demand_intelligence_agent(orders_df)
    analysis_state["inventory_alerts"] = inventory_alert_agent(
        orders_df, inventory_df
    )
    analysis_state["vendor_optimizations"] = vendor_price_optimization_agent(
        orders_df, sellers_df
    )

    return analysis_state
