#!/usr/bin/env python3
import xml.etree.ElementTree as ET
from pathlib import Path
import json
THRESH=100000.0
MAX_EVENTS=100000
root=Path('networks')
files=sorted([p for p in root.rglob('*.rou.xml')])
summary=[]
max_rate_global=0.0
top_flows=[]
for f in files:
    total=0
    trips=0
    trips_with_fromTaz=0
    flows=0
    flows_with_rate=0
    max_rate=0.0
    suspicious=[]
    try:
        for ev,el in ET.iterparse(f, events=('end',)):
            tag = el.tag
            total += 1
            if tag == 'trip':
                trips += 1
                if 'fromTaz' in el.attrib or 'toTaz' in el.attrib:
                    trips_with_fromTaz += 1
            elif tag == 'flow':
                flows += 1
                num = el.attrib.get('number')
                vph = el.attrib.get('vehsPerHour')
                begin = float(el.attrib.get('begin',0))
                end = float(el.attrib.get('end', begin+1))
                if num is not None:
                    try:
                        rate = float(num) * 3600.0 / max(1e-6, end-begin)
                    except Exception:
                        rate = 0.0
                elif vph is not None:
                    try:
                        rate = float(vph)
                    except Exception:
                        rate = 0.0
                else:
                    rate = 0.0
                if rate>0:
                    flows_with_rate += 1
                if rate>max_rate:
                    max_rate = rate
                if rate>THRESH:
                    suspicious.append({'attrib': dict(el.attrib), 'rate': rate})
                    top_flows.append({'file': str(f), 'attrib': dict(el.attrib), 'rate': rate})
            el.clear()
            if total>=MAX_EVENTS and trips>=1000 and flows>=100:
                break
    except Exception as e:
        summary.append({'file': str(f), 'error': str(e)})
        continue
    scanned_full = (total < MAX_EVENTS)
    summary.append({'file': str(f), 'total_events': total, 'trips': trips, 'trips_with_fromTaz': trips_with_fromTaz, 'flows': flows, 'flows_with_rate': flows_with_rate, 'max_flow_rate': max_rate, 'suspicious_flows_count': len(suspicious), 'scanned_full': scanned_full})
    if max_rate>max_rate_global:
        max_rate_global = max_rate
out = {'files_found': len(files), 'files': summary, 'max_rate_global': max_rate_global, 'top_suspicious_flows': sorted(top_flows, key=lambda x: -x['rate'])[:50]}
out_path = Path('scripts/od_scan_results.json')
with open(out_path, 'w') as fh:
    json.dump(out, fh, indent=2)
print('WROTE', out_path)
print('FILES_FOUND', len(files), 'max_rate_global', max_rate_global)
