from orchestrator import detect_reviewer_conflict


def test_ho05_forced_reviewer_disagreement_escalates_to_human():
    events = [
        {
            "type": "subagent",
            "role": "reviewer",
            "review_items": [
                {"section": "implementation", "verdict": "approve"}
            ],
        },
        {
            "type": "subagent",
            "role": "reviewer",
            "review_items": [
                {"section": "implementation", "verdict": "reject"}
            ],
        },
    ]

    escalated, conflicts = detect_reviewer_conflict(events)

    assert escalated is True
    assert "implementation" in conflicts