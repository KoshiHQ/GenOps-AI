#!/bin/bash

# Script to create pull request for Flowise documentation improvements
# Working directory: /Users/guyderry/CascadeProjects/GenOps-AI-OTel/GenOps-AI

set -e  # Exit on any error

echo "🚀 Creating pull request for Flowise documentation improvements..."

# Navigate to project directory
cd "/Users/guyderry/CascadeProjects/GenOps-AI-OTel/GenOps-AI"

# Check current git status
echo "📋 Checking git status..."
git status

# Check current branch
echo "🌿 Current branch:"
git branch --show-current

# Create and switch to feature branch
echo "🔄 Creating feature branch..."
git checkout -b feature/flowise-docs-enhancement

# Add modified files
echo "📝 Staging documentation files..."
git add docs/flowise-quickstart.md docs/integrations/flowise.md

# Create commit
echo "💾 Creating commit..."
git commit -m "Enhance Flowise documentation for improved developer experience

- Improve quickstart guide with realistic timelines and complete examples
- Add missing Examples section to integration guide with comprehensive overview
- Fix internal links and enhance developer onboarding flow
- Add clear chatflow ID discovery methods for new developers

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push to GitHub
echo "⬆️ Pushing branch to GitHub..."
git push -u origin feature/flowise-docs-enhancement

# Create pull request
echo "🔗 Creating pull request..."
gh pr create --title "Enhance Flowise documentation for improved developer experience" --body "## Summary
- Improve quickstart guide with realistic timelines and complete examples
- Add missing Examples section to integration guide with comprehensive overview  
- Fix internal links and enhance developer onboarding flow
- Add clear chatflow ID discovery methods for new developers

## Test plan
- [x] Verify all internal links work correctly
- [x] Confirm examples are complete and copy-paste ready
- [x] Test chatflow ID discovery methods
- [x] Validate documentation structure and formatting

🤖 Generated with [Claude Code](https://claude.ai/code)"

echo "✅ Pull request created successfully!"