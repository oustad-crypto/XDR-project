from fastapi import APIRouter, HTTPException

router = APIRouter()

# Sample data structure to store rules (this can be replaced with a database)
rules_db = {}

@router.get("/rules")
def get_rules():
    return {"rules": list(rules_db.values())}

@router.get("/rules/{rule_id}")
def get_rule(rule_id: int):
    if rule_id not in rules_db:
        raise HTTPException(status_code=404, detail="Rule not found")
    return {"rule": rules_db[rule_id]}

@router.post("/rules")
def create_rule(rule: dict):
    rule_id = len(rules_db) + 1  # Simple ID generation
    rules_db[rule_id] = rule
    return {"rule_id": rule_id, "rule": rule}

@router.put("/rules/{rule_id}")
def update_rule(rule_id: int, rule: dict):
    if rule_id not in rules_db:
        raise HTTPException(status_code=404, detail="Rule not found")
    rules_db[rule_id] = rule
    return {"rule_id": rule_id, "rule": rule}

@router.delete("/rules/{rule_id}")
def delete_rule(rule_id: int):
    if rule_id not in rules_db:
        raise HTTPException(status_code=404, detail="Rule not found")
    del rules_db[rule_id]
    return {"detail": "Rule deleted"}