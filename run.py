# keep-me-updated/run.py

from datetime import date
from pathlib import Path

def main():
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    report = f"""# Weekly Literature Digest

Date: {date.today().isoformat()}

## Findings

No live data source has been configured yet.

## Next steps

Add API keys or RSS feeds, then update this script.
"""

    (output_dir / "weekly_lit_digest.md").write_text(report)

if __name__ == "__main__":
    main()
