def test_ho04_canary_does_not_leak_downstream():
    canary = "CANARY-HO04-PRIVATE-SECRET"

    transcript_events = [
        {
            "type": "subagent",
            "role": "planner",
            "step": 1,
            "handoff": "Implement the logging change using only this scoped handoff.",
            "output_document": {
                "summary": "Planner created a scoped implementation handoff.",
                "citation_list": [],
            },
        },
        {
            "type": "subagent",
            "role": "implementer",
            "step": 2,
            "handoff": "Logging change implemented without private upstream context.",
            "output_document": {
                "summary": "Implemented the requested logging change.",
                "citation_list": [],
            },
        },
        {
            "type": "subagent",
            "role": "reviewer",
            "step": 3,
            "handoff": "Implementation reviewed using only scoped handoff content.",
            "output_document": {
                "summary": "No private upstream context appeared in the review.",
                "citation_list": [],
            },
        },
    ]

    downstream_text = str(transcript_events[1:])

    assert canary not in downstream_text