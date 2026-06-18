# sweeyam_team26-main/backend/workflow/sector_rules.py

SECTOR_CONSTRAINTS = {
    # PHASE 1: E-COMMERCE (Immediate Roll-out)
    "ECOMMERCE": {
        "framework": "Lean Inventory, Supply Chain Velocity & Direct-to-Consumer Unit Economics",
        "guardrails": """
        1. THE SQUEEZE: Ruthlessly analyze stock turn ratios, customer acquisition cost (CAC), and lifetime value (LTV).
        2. NO FLUFF: If a simple inventory replenishment formula or stock threshold triggers an alert, do not build an elaborate forecasting matrix.
        3. ERROR HANDLING: If vendor data or inventory.csv has discrepancies, flag them immediately as immediate supply chain bottlenecks.
        """
    },
    
    # PHASE 2: HEALTHCARE (Next Horizon)
    "HEALTHCARE": {
        "framework": "HIPAA Compliance, Patient Data Security & Clinical Operations Efficiency",
        "guardrails": """
        1. DATA PRIVACY BOUNDARY: Treat all data as potentially containing PHI. Never expose raw clinical identifiers to unverified agent sub-routines.
        2. OPERATIONAL FOCUS: Prioritize resource allocation, patient throughput metrics, and equipment utilization.
        3. MINIMALIST TERMINOLOGY: Strip excessive medical jargon. Present clinical conclusions as actionable operational directives.
        """
    },
    
    # PHASE 3: FINANCE (Final Horizon)
    "FINANCE": {
        "framework": "SEC Compliance, Quantitative Capital Adequacy & Risk Management",
        "guardrails": """
        1. FISCAL RIGOR: Enforce double-entry tracking logic principles on all synthetic cash-flow or balance calculations.
        2. SPECCING BOUNDARY: Explicitly segregate speculative portfolio alpha predictions from historical cash trends. 
        3. PONYTAIL EXTRACTION: Strip qualitative market sentiment prose. Deliver hard numeric matrices, margins of safety, and standard deviations.
        """
    }
}
