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

1. **How does CPU-based HPA choose a replica target?** A simplified calculation scales current replicas by observed utilization divided by target utilization, then applies bounds and tolerance. The browser calculator is separate from the actual controller.

2. **Why do CPU requests matter?** The utilization percentage is relative to the requested CPU, so changing requests changes the denominator even if actual CPU consumption stays the same.

3. **What did the cluster test observe?** The disposable kind cluster started with two replicas and a real load generator. The first saved run recorded six desired and available worker replicas after HPA scale-up.

4. **Why use an insecure kubelet TLS flag in the test?** The flag accommodates the disposable kind cluster’s certificates for Metrics Server. It is scoped to that local test environment and is not a production configuration recommendation.

5. **What has not been benchmarked?** Scale-down time, node autoscaling, multiple failure domains and cloud cost. A short single-node experiment cannot establish production capacity or availability.

## Independent exercise

Change CPU requests and explain why the same absolute CPU consumption produces a different utilization percentage.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Configured a Kubernetes worker with resource requests, probes and HPA; observed a disposable CI cluster scale from two to six available replicas under load.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
