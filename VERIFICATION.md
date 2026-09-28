# Scale Lab — verification

Verification date: 28 September 2026. Tests and examples were executed; they are not illustrative pass claims.

- Project checks: 12 passed.
- Dependency/setup verification: fresh isolated Python 3.12 environment passed.
- Main browser/API workflow: verified locally; actual result saved in reports/example-output.json.
- Publication: [public repository](https://github.com/abhijith-abhii/scale-lab) verified under **abhijith-abhii**.
- Actual application screenshot: reports/screenshots/app.png. Browser rendered successfully at 1280px width.

## Verification boundaries
- Actual kind cluster scaled from two to six available replicas; multi-node production operation and scale-down benchmarks are outside scope.


## Evidence
- `reports/test-results.txt`: actual test output.
- `reports/clean-setup.json`: isolated setup result where applicable.
- `reports/publication-check.json`: credential-pattern and file audit.
- `DATA_AND_SOURCES.md`: source and license notes.

## GitHub verification

- [Kubernetes autoscaling experiment: passed](https://github.com/abhijith-abhii/scale-lab/actions/runs/36416473050)

Verified source revision: `2528536d124b2bc50e3d06e4727091d3d4fe9689`. Subsequent presentation-only changes do not change that implementation evidence.

The saved cluster evidence shows six available replicas following the initial two-replica deployment. See `reports/hpa-evidence.txt`.
