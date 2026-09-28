import math

def desired(current,observed,target):
 if isinstance(current,bool) or int(current)!=current or not 1<=current<=10:raise ValueError('Current replicas must be an integer from 1–10')
 if not all(math.isfinite(x) for x in [observed,target]) or observed<0 or target<=0:raise ValueError('Utilization must be finite; target positive')
 ratio=observed/target
 recommendation=current if abs(1-ratio)<=.1 else math.ceil(current*ratio)
 return max(2,min(10,recommendation))
def analyze(p):
 c=float(p.get('current',2));u=float(p.get('observed',120));t=float(p.get('target',60));d=desired(c,u,t)
 return dict(metrics={'Current replicas':int(c),'Calculated desired':d,'Minimum / maximum':'2 / 10'},answer=f'ceil({c:g} × {u:g} / {t:g}), with 10% tolerance and 2–10 bounds.',notice='Educational calculation, not a live cluster reading. Kubernetes also accounts for missing metrics, readiness, stabilization and scale policies.',details={'cpu_requests':'100m per pod','HPA_target':'60%','real_validation':'See reports/ci-evidence.json after the Kubernetes workflow completes.'})
