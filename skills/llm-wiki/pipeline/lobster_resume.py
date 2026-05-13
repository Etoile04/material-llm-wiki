"""
Lobster Pipeline Resume - Checkpoint persistence for batch ingest.

Supports:
- Save/restore per-paper checkpoint state
- Batch resume from last failed step
- Progress tracking across runs
- Auto-cleanup of completed checkpoints

Usage:
    python3 lobster_resume.py --mode save --slug <slug> --step <step> --status <status> [--data json]
    python3 lobster_resume.py --mode resume --batch-file <file>
    python3 lobster_resume.py --mode status --slug <slug>
    python3 lobster_resume.py --mode list
    python3 lobster_resume.py --mode cleanup --older-than <hours>
"""
import json, os, sys, time, argparse, glob
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))
CHECKPOINT_DIR = os.environ.get('CHECKPOINT_DIR', 
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'checkpoint'))

class CheckpointManager:
    """Manage per-paper checkpoints for Lobster pipeline resume."""
    
    def __init__(self, checkpoint_dir=None):
        self.checkpoint_dir = checkpoint_dir or CHECKPOINT_DIR
        os.makedirs(self.checkpoint_dir, exist_ok=True)
    
    def _filepath(self, slug):
        return os.path.join(self.checkpoint_dir, f"{slug}.json")
    
    def save(self, slug, step, status, data=None):
        state = {
            "slug": slug,
            "step": step,
            "status": status,
            "data": data or {},
            "timestamp": datetime.now(CST).isoformat(),
            "unix_ts": time.time(),
        }
        with open(self._filepath(slug), 'w') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        return state
    
    def load(self, slug):
        fp = self._filepath(slug)
        if not os.path.isfile(fp):
            return None
        with open(fp) as f:
            return json.load(f)
    
    def remove(self, slug):
        fp = self._filepath(slug)
        if os.path.isfile(fp):
            os.remove(fp)
    
    def list_checkpoints(self):
        results = []
        for fp in sorted(glob.glob(os.path.join(self.checkpoint_dir, "*.json"))):
            with open(fp) as f:
                state = json.load(f)
            results.append({
                "slug": state.get("slug", os.path.basename(fp).replace(".json","")),
                "step": state.get("step"),
                "status": state.get("status"),
                "timestamp": state.get("timestamp"),
            })
        return results
    
    def get_resumable(self, batch_slugs=None):
        if batch_slugs:
            results = []
            for slug in batch_slugs:
                state = self.load(slug)
                if state and state["status"] in ("failed", "partial"):
                    results.append(state)
            return results
        else:
            all_cp = self.list_checkpoints()
            return [cp for cp in all_cp if cp["status"] in ("failed", "partial")]
    
    def cleanup_old(self, older_than_hours=24):
        cutoff = time.time() - older_than_hours * 3600
        removed = 0
        for fp in glob.glob(os.path.join(self.checkpoint_dir, "*.json")):
            with open(fp) as f:
                state = json.load(f)
            if state.get("unix_ts", 0) < cutoff:
                os.remove(fp)
                removed += 1
        return removed

def main():
    parser = argparse.ArgumentParser(description='Lobster Resume Checkpoint Manager')
    parser.add_argument('--mode', choices=['save','resume','status','list','cleanup'], required=True)
    parser.add_argument('--slug')
    parser.add_argument('--step')
    parser.add_argument('--status')
    parser.add_argument('--data', default='{}')
    parser.add_argument('--batch-file')
    parser.add_argument('--older-than', type=int, default=24)
    args = parser.parse_args()
    
    cm = CheckpointManager()
    
    if args.mode == 'save':
        assert args.slug and args.step and args.status, "save requires --slug --step --status"
        state = cm.save(args.slug, args.step, args.status, json.loads(args.data))
        print(json.dumps(state, ensure_ascii=False, indent=2))
    elif args.mode == 'status':
        assert args.slug, "status requires --slug"
        state = cm.load(args.slug)
        if state:
            print(json.dumps(state, ensure_ascii=False, indent=2))
        else:
            print(json.dumps({"error": "not found", "slug": args.slug}))
    elif args.mode == 'list':
        cps = cm.list_checkpoints()
        print(json.dumps(cps, ensure_ascii=False, indent=2))
    elif args.mode == 'resume':
        assert args.batch_file, "resume requires --batch-file"
        with open(args.batch_file) as f:
            batch = json.load(f)
        slugs = [p.get("slug") for p in batch]
        resumable = cm.get_resumable(slugs)
        print(json.dumps(resumable, ensure_ascii=False, indent=2))
    elif args.mode == 'cleanup':
        removed = cm.cleanup_old(args.older_than)
        print(f"Removed {removed} old checkpoints")

if __name__ == '__main__':
    main()
