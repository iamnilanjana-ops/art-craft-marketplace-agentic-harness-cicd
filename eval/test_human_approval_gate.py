def test_human_approval_gate_blocks_until_approved():
    def completion_authorized(decision: str) -> bool:
        return decision == "approve"

    assert completion_authorized("approve") is True
    assert completion_authorized("reject") is False
    assert completion_authorized("pending") is False