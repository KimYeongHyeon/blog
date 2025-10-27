# Publication Auto-Update Scripts

## Overview

This directory contains scripts to automatically update publication information from Google Scholar.

## Files

- `update_publications.py` - Main script to fetch and update publications from Google Scholar

## Local Usage

### Prerequisites

```bash
pip install -r requirements.txt
```

### Run Script

```bash
cd /path/to/blog
python scripts/update_publications.py
```

This will:
1. Fetch your latest publications from Google Scholar
2. Update citation counts
3. Regenerate `content/publications.md`

## GitHub Actions Auto-Update

The repository is configured to automatically update publications weekly using GitHub Actions.

### Schedule

- **Automatic**: Every Monday at 9:00 AM KST
- **Manual**: Can be triggered manually from GitHub Actions tab

### Configuration

The workflow is defined in `.github/workflows/update-publications.yml`

To modify the schedule, edit the cron expression:
```yaml
schedule:
  - cron: '0 0 * * 1'  # Every Monday at 00:00 UTC (09:00 KST)
```

### Cron Schedule Examples

- Daily: `'0 0 * * *'`
- Weekly (Monday): `'0 0 * * 1'`
- Bi-weekly: `'0 0 1,15 * *'`
- Monthly: `'0 0 1 * *'`

## Manual Trigger

You can manually trigger the update from GitHub:

1. Go to your repository on GitHub
2. Click "Actions" tab
3. Select "Update Publications from Google Scholar"
4. Click "Run workflow"

## Customization

### Update Scholar ID

Edit `update_publications.py` and change:
```python
SCHOLAR_ID = "cLAlajcAAAAJ"  # Your Google Scholar ID
```

### Change Update Frequency

Edit `.github/workflows/update-publications.yml` and modify the cron schedule.

## Troubleshooting

### Script Fails to Run

1. Check Python version (requires 3.10+)
2. Verify dependencies are installed: `pip install -r requirements.txt`
3. Check Google Scholar ID is correct

### GitHub Actions Fails

1. Check workflow logs in GitHub Actions tab
2. Ensure repository has write permissions for GitHub Actions
3. Verify `requirements.txt` exists in repository root

## Notes

- Google Scholar may rate-limit requests if run too frequently
- The script includes your name variations for bold formatting: YeongHyeon Kim, YH Kim, KY Hyeon
- Citations are automatically updated each run

