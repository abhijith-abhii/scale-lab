# Scale Lab — learning guide

## What it does

Understand autoscaling under measured load. The intended user is platform engineering learners. Browser controls → validated Flask API → project analysis/workflow → results and export.

## Run and demonstrate

Follow the README installation block, then: Inspect the HPA calculation locally, then follow the kind workflow to build/load the worker image, apply the manifests, start load, and observe more than two replicas. Review recorded CI evidence.

## Important files

- `app.py` — local HTTP interface and request/error handling.
- `core.py` — project-specific logic.
- `tests/` — regression and correctness checks.
- `reports/` — recorded outputs and verification evidence.

## Three engineering decisions

1. Set CPU requests so utilization-based HPA has a valid denominator.
2. Separate a transparent calculation model from actual Kubernetes manifests and cluster observations.
3. Run an ephemeral kind cluster, Metrics Server and a real load workload in CI to observe replica growth.

## Five interview questions

1. **What problem does this project solve, and what is its unit of work?** Explain understand autoscaling under measured load, identify platform engineering learners as the audience, and trace one concrete example through the files above. Use the demonstration output rather than hypothetical impact.
2. **Why did you choose the first design decision?** Set CPU requests so utilization-based HPA has a valid denominator. Show the corresponding implementation and a test that would fail if that property were removed.
3. **How do you protect correctness when inputs or execution change?** Separate a transparent calculation model from actual Kubernetes manifests and cluster observations. Explain the relevant invalid-input or edge-case test and distinguish a checked property from an untested assumption.
4. **How do you make results inspectable and reproducible?** Run an ephemeral kind cluster, Metrics Server and a real load workload in CI to observe replica growth. Point to actual outputs and recorded commands. Explain why a successful example is weaker evidence than a tested boundary or independently reconciled total.
5. **What would you improve before real deployment or real-data use?** The calculator omits some Kubernetes controller details. Real validation uses a temporary single-node kind cluster, not a production cluster. The kubelet insecure-TLS flag is restricted to that disposable local cluster. Scale-down duration, node autoscaling and cloud costs are not benchmarked. Choose one limitation, describe the missing evidence, and propose a measurable acceptance check rather than promising production readiness.

## Independent exercise

Change CPU requests and explain why the same absolute CPU consumption produces a different utilization percentage.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Implemented and validated understand autoscaling under measured load using Kubernetes · kind · Python, with kubernetes deployment and documented correctness checks and limitations.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
