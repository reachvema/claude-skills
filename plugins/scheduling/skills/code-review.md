# Code Review

## Objective
Perform comprehensive code reviews by analyzing git working tree changes from main branch to ensure code quality, best practices, and maintainability.

## Key Actions
- Retrieve changes from git working tree compared to main branch
- Analyze code differences (added, modified, deleted)
- Review code structure and organization
- Check for adherence to coding standards
- Identify potential bugs and logic errors
- Evaluate error handling and edge cases
- Assess security vulnerabilities
- Review test coverage for changes
- Check for proper documentation and comments

## Git Commands
```bash
# Get working tree changes from main
git diff main

# Get staged changes from main
git diff --cached main

# Get all changes (staged and unstaged) from main
git diff main HEAD

# Get list of changed files
git diff --name-only main

# Get detailed stats
git diff --stat main
```

## Review Checklist

### Code Quality
- Code readability and clarity
- Proper naming conventions (variables, functions, classes)
- Code duplication and DRY principle
- Function/method complexity and length
- Proper code formatting and indentation

### Best Practices
- SOLID principles adherence
- Design pattern usage appropriateness
- Separation of concerns
- Dependency management
- Configuration management (no hardcoded values)

### Performance
- Efficient algorithms and data structures
- Database query optimization
- Proper async/await usage
- Memory leak prevention
- Resource cleanup and disposal

### Security
- Input validation and sanitization
- SQL injection prevention
- XSS prevention
- Authentication and authorization checks
- Sensitive data handling
- Proper error messages (no data leakage)

### Testing
- Unit test coverage for new code
- Integration test considerations
- Edge case handling
- Test quality and assertions

### Documentation
- Inline code comments for complex logic
- XML documentation for public APIs
- README updates if needed
- API documentation updates

## Review Workflow
1. Fetch latest main branch: `git fetch origin main`
2. Compare working tree to main: `git diff main`
3. Analyze each changed file systematically
4. Document findings by severity (Critical, Major, Minor, Suggestion)
5. Provide specific line references and recommendations
6. Suggest refactoring opportunities

## Output Format
```
## Code Review Summary

### Files Changed: X
### Critical Issues: X
### Major Issues: X
### Minor Issues: X
### Suggestions: X

---

### Critical Issues
- **File**: path/to/file.cs:line_number
  - **Issue**: Description
  - **Recommendation**: Specific fix

### Major Issues
...

### Minor Issues
...

### Suggestions
...

### Positive Observations
- Well-structured code
- Good test coverage
- Clear documentation
```

## Tools & Techniques
- Git diff analysis
- Static code analysis
- Linting rules validation
- Complexity metrics
- Security scanning

## Outputs
- Comprehensive review report
- Prioritized issue list with severity
- Actionable recommendations
- Code improvement suggestions
- Approval status or required changes
