# Claude Code Development Rules and Best Practices

## Overview
This document contains structured rules optimized for Claude Code development workflows. All rules are organized by priority level with specific, measurable requirements. Each instruction has a unique ID for tracking and reference.

**Key Differences from Amazon Q:**
- Adapted for Claude Code's tool ecosystem (Read, Write, Edit, Glob, Grep, Bash, Task agents)
- Leverages Claude's native planning capabilities and TodoWrite tool
- Uses MCP servers as available tools rather than consultation endpoints
- Broader applicability beyond AWS-specific development
- Optimized for Claude's natural language understanding and context management

## Rule Implementation Priority

### Phase 1: Critical Rules - MUST Implement First

#### 0. Conversation & Rule Acknowledgment (CRITICAL)
**Purpose**: Ensure transparency about which rules are being followed and maintain rule awareness.

- **CHECK_RULES**: MUST always consider applicable rules before using a tool or responding
- **PRINT_RULES**: MUST print "Rule used: `[section_name]` (ID)" at the very beginning of responses when acting based on a specific rule
- **PRINT_MULTIPLE**: If multiple rules are matched, list all: "Rule used: `[section1]` (ID1), `[section2]` (ID2)"
- **NO_GENERIC_MENTIONS**: DO NOT start responses with general mentions about using rules or context, but DO print specific rule usage as specified above
- **Error Handling**: If rule files are unreadable, continue but note the issue; if multiple conflicting rules apply, follow the highest priority rule and note the conflict

#### 1. MCP Server Consultation (CRITICAL)
**Purpose**: Ensure accuracy by consulting MCP servers for technical specifications and best practices.

- **CONSULT_MCP**: MUST always consult available MCP servers for technical accuracy, best practices, and current specifications before providing recommendations or implementing solutions
- **USE_TASK_AGENTS**: MUST use specialized Task agents (Explore, general-purpose) when appropriate for complex searches, codebase exploration, or multi-step research
- **VERIFY_CURRENT**: MUST verify information is current, especially for rapidly-evolving technologies, frameworks, and APIs - use MCP servers, WebSearch, or WebFetch as appropriate
- **MCP_FIRST**: When MCP servers are available for a domain (AWS, Terraform, cost estimation, documentation generation, etc.), prioritize them over web search
- **Error Handling**: If MCP servers are not available, use WebSearch/WebFetch to gather current information and note the limitation

#### 2. Development Planning (CRITICAL)
**Purpose**: Ensure systematic planning and validation for all new development.

- **USE_TODOWRITE**: MUST use TodoWrite tool to create structured task lists for any non-trivial development work (3+ steps or complex changes)
- **DISCRETE_STEPS**: MUST structure plans with discrete, measurable steps that can be validated independently
- **PLAN_APPROVAL**: MUST obtain explicit approval of the plan before beginning implementation
- **INCLUDE_DIAGRAMS**: SHOULD include architectural diagrams, flowcharts, or visual representations for complex system interactions
- **ONE_IN_PROGRESS**: MUST have exactly one task marked as in_progress at any time
- **IMMEDIATE_COMPLETION**: MUST mark tasks as completed immediately upon finishing (not batched)
- **Error Handling**: If TodoWrite is not appropriate for simple tasks, proceed directly but explain approach first

#### 3. Access Control (CRITICAL)
**Purpose**: Ensure secure access control practices and prevent privilege escalation.

- **LEAST_PRIVILEGE**: MUST follow the principle of least privilege - grant only minimum permissions required
- **NO_ADMIN_PERMISSIONS**: NEVER grant administrative, root, or wildcard permissions without explicit user confirmation
- **TEMPORARY_CREDENTIALS**: MUST use temporary credentials, IAM roles, service accounts, or tokens instead of long-lived access keys
- **NO_SECRETS_IN_CODE**: NEVER hard-code credentials, API keys, or secrets in source code
- **Error Handling**: If least privilege cannot be determined, start with minimal permissions and expand as needed with user approval

#### 4. Data Management (CRITICAL)
**Purpose**: Ensure proper data handling, privacy, and security.

- **DATA_ENCRYPTION**: MUST implement data encryption at rest and in transit for all sensitive data
- **INPUT_VALIDATION**: MUST sanitize and validate all user inputs to prevent injection attacks
- **CREDENTIAL_ROTATION**: SHOULD implement credential rotation mechanisms where applicable
- **NO_CREDENTIAL_HARVESTING**: NEVER create tools for bulk credential discovery or harvesting (SSH keys, browser cookies, cryptocurrency wallets)
- **DEFENSIVE_SECURITY_ONLY**: Only assist with defensive security tasks; refuse to create malicious code
- **Error Handling**: If encryption is not available for the platform, use access controls and document the security limitation

#### 5. Compliance & Code Quality (CRITICAL)
**Purpose**: Ensure adherence to best practices and quality standards.

- **SECURITY_REVIEWS**: MUST flag security concerns in code changes involving authentication, authorization, or data access
- **NO_MALICIOUS_CODE**: NEVER create, modify, or improve code that may be used maliciously
- **EXPLAIN_SECURITY_IMPACT**: MUST explain security implications when implementing security-sensitive features
- **Error Handling**: If security implications are unclear, research and ask clarifying questions before proceeding

### Phase 2: High Priority Rules - Core Practices

#### 6. Tool Usage Optimization (HIGH)
**Purpose**: Use Claude Code tools efficiently and appropriately.

- **USE_SPECIALIZED_TOOLS**: MUST use specialized tools (Read, Edit, Write, Glob, Grep) instead of Bash for file operations
- **PARALLEL_TOOLS**: MUST call independent tools in parallel within a single message for optimal performance
- **EXPLORE_AGENT**: MUST use Task agent with subagent_type=Explore for codebase exploration questions (not needle queries)
- **NO_BASH_COMMUNICATION**: NEVER use bash echo or commands to communicate with user; output text directly
- **PROPER_QUOTING**: MUST quote file paths with spaces in Bash commands
- **Error Handling**: If preferred tool is not available, use alternatives and explain the approach

#### 7. General Development Practices (HIGH)
**Purpose**: Define general development practices and workflow standards.

- **NAMING_CONVENTIONS**: MUST follow language-appropriate naming conventions consistently
- **TESTING**: MUST implement comprehensive testing including unit tests, integration tests, and validation tests
- **CONFIG_MANAGEMENT**: MUST externalize configuration from code using environment variables, config files, or parameter stores
- **PREFER_EDIT**: MUST prefer editing existing files over creating new files unless explicitly required
- **Error Handling**: If naming conventions conflict with existing code, follow existing patterns and note inconsistency

#### 8. Error Troubleshooting (HIGH)
**Purpose**: Ensure systematic debugging and troubleshooting.

- **DEBUG_SYSTEMATICALLY**: MUST debug systematically when errors occur - analyze error messages, check logs, identify root causes before attempting fixes
- **MCP_ERROR_FIXES**: MUST use available MCP servers for identifying fixes, solutions, and best practices when troubleshooting errors
- **USE_SEARCH_TOOLS**: MUST use WebSearch for error messages, stack traces, and solutions to unfamiliar errors when MCP servers don't cover the domain
- **READ_BEFORE_EDIT**: MUST read files before editing them (Edit and Write tools require prior Read)
- **VERIFY_FIXES**: MUST verify fixes resolve the issue (run tests, check output, validate behavior)
- **Error Handling**: If MCP servers are not available for error resolution, use available debugging tools and WebSearch, then document the limitation

#### 9. Error Handling & Logging (HIGH)
**Purpose**: Ensure proper error handling and logging practices in code.

- **ERROR_HANDLING**: MUST include comprehensive error handling with try-catch blocks, proper exception handling, and graceful failure modes
- **LOGGING**: MUST implement structured logging with appropriate log levels (DEBUG, INFO, WARN, ERROR)
- **CONTEXT_IN_ERRORS**: MUST include relevant context in error messages (what operation failed, input values, expected vs actual)
- **Error Handling**: If logging framework is not available, use basic console output and document the limitation

#### 10. Code Documentation (HIGH)
**Purpose**: Ensure comprehensive documentation for all code.

- **USE_DOC_MCP**: MUST use code documentation generation MCP server for automated documentation when available
- **DOCUMENT_APIS**: MUST document all public APIs, interfaces, and complex business logic with clear descriptions, parameters, return values, and usage examples
- **CODE_COMMENTS**: SHOULD add comments for non-obvious logic, algorithms, or business rules
- **INCLUDE_REFERENCES**: SHOULD include file_path:line_number references when discussing specific code locations
- **NO_PROACTIVE_DOCS**: NEVER proactively create documentation files (*.md, README) unless explicitly requested
- **Error Handling**: If code documentation generation MCP server is not available, create manual documentation and flag for automation

#### 11. Deployment Testing (HIGH)
**Purpose**: Ensure complete lifecycle testing and automation.

- **TEST_DELETION**: MUST test both deployment and deletion/cleanup of resources in the same testing cycle
- **DEPROVISION_AUTOMATION**: MUST create corresponding cleanup/teardown procedures when creating provisioning automation
- **VERIFY_CLEANUP**: MUST verify cleanup completes successfully and no resources leak
- **Error Handling**: If deletion testing fails, document cleanup issues and provide manual steps

#### 12. Infrastructure as Code (HIGH)
**Purpose**: Ensure consistent IaC practices (Terraform, CloudFormation, etc.).

- **USE_MODULES**: MUST use modules/reusable components to promote code reusability
- **USE_VARIABLES**: MUST use variables instead of hard-coding values, with proper descriptions and types
- **USE_DATA_SOURCES**: MUST use data sources/lookups instead of variables for dynamic values
- **CURRENT_PROVIDERS**: MUST use current, supported versions with version constraints - consult MCP servers for current versions
- **FORMAT_BEFORE_COMMIT**: MUST run formatting tools (terraform fmt, etc.) before commits
- **STATE_MANAGEMENT**: SHOULD implement remote state management with locking for team environments
- **VALIDATE_PLAN**: MUST validate and preview changes before applying
- **Error Handling**: If modules are not available, create reusable components and document for future extraction

#### 13. API Design Standards (HIGH)
**Purpose**: Ensure consistent and robust API design.

- **API_VERSIONING**: SHOULD implement API versioning strategies to maintain backward compatibility
- **HTTP_STANDARDS**: MUST use standard HTTP status codes and error response formats
- **RATE_LIMITING**: SHOULD implement rate limiting and throttling for public APIs
- **API_DOCUMENTATION**: MUST document API endpoints with request/response examples
- **Error Handling**: If versioning cannot be implemented, document API changes carefully

#### 14. Performance Optimization (HIGH)
**Purpose**: Ensure performance considerations are integrated into development.

- **PERFORMANCE_ANALYSIS**: SHOULD consider performance implications for code changes
- **CACHING_STRATEGY**: SHOULD implement caching strategies where appropriate
- **PERFORMANCE_BENCHMARKING**: SHOULD profile and benchmark critical code paths when making optimizations
- **AVOID_N_PLUS_ONE**: MUST avoid N+1 query problems in database operations
- **Error Handling**: If performance profiling tools are not available, use basic timing measurements

### Phase 3: Medium Priority Rules - Optimization

#### 15. Version Control (MEDIUM)
**Purpose**: Ensure consistent version control practices.

- **COMMIT_MESSAGES**: MUST write clear, descriptive commit messages following conventional commit format when possible
- **COMMIT_FORMAT**: MUST use heredoc for multi-line commit messages to ensure proper formatting
- **INCLUDE_COAUTHOR**: MUST include "Co-Authored-By: Claude <noreply@anthropic.com>" in commits
- **INCLUDE_SIGNATURE**: MUST include "🤖 Generated with [Claude Code](https://claude.com/claude-code)" in commits
- **CHECKPOINT_COMMIT**: MUST commit changes when user mentions "checkpointing" or similar requests
- **NEVER_FORCE_PUSH**: NEVER run force push to main/master without explicit user request and warning
- **NO_SKIP_HOOKS**: NEVER skip git hooks unless explicitly requested
- **Error Handling**: If commit message format conflicts with project standards, follow project standards

#### 16. Cloud Function Development (MEDIUM)
**Purpose**: Ensure cloud functions (Lambda, Cloud Functions, etc.) are developed properly.

- **ARCHITECTURE_COMPATIBILITY**: MUST test with correct architecture (arm64 for AWS Lambda, etc.)
- **DOCKER_ARCHITECTURE**: MUST ensure Docker images support target architecture
- **LOCAL_TESTING**: SHOULD test cloud functions locally before deployment
- **COLD_START_OPTIMIZATION**: SHOULD optimize for cold start performance
- **Error Handling**: If architecture testing is not available, document the limitation and test in target environment

#### 17. Cost Estimation (MEDIUM)
**Purpose**: Ensure cost analysis is performed for proposed infrastructure.

- **COST_ESTIMATES**: SHOULD generate detailed cost estimates for any proposed resources including both static costs (fixed monthly charges) and dynamic costs (usage-based charges) with realistic usage examples and scenarios
- **USE_COST_MCP**: SHOULD use cost estimation MCP servers when available for accurate pricing
- **WEB_COST_RESOURCES**: SHOULD use web resources, AWS Pricing Calculator, or pricing documentation when dedicated cost estimation MCP is not available
- **COST_OPTIMIZATION**: SHOULD suggest cost optimization opportunities when appropriate
- **Error Handling**: If cost estimation tools are not available, provide general cost guidance and recommend manual calculation

#### 18. Observability (MEDIUM)
**Purpose**: Ensure proper monitoring and traceability.

- **KPI_MONITORING**: SHOULD ensure important KPIs and metrics are logged or exposed
- **WORKFLOW_TRACING**: SHOULD use correlation IDs, trace IDs, or labels to track requests through distributed systems
- **HEALTH_CHECKS**: SHOULD implement health checks and readiness probes for services
- **ALERTING**: SHOULD recommend alerting for critical system metrics
- **Error Handling**: If metrics system is not available, use structured logging

## Rule Dependencies

Understanding rule dependencies ensures proper implementation order:

- **CHECK_RULES** → All other rules (ensures rule awareness before action)
- **CONSULT_MCP** → All other MCP-specific rules (foundation for technical accuracy)
- **USE_TODOWRITE** → Complex multi-step tasks (planning before execution)
- **LEAST_PRIVILEGE** → All security-related rules (security foundation)
- **USE_SPECIALIZED_TOOLS** → All file operations (efficiency)
- **READ_BEFORE_EDIT** → All file editing operations (tool requirement)
- **ERROR_HANDLING** → **LOGGING** (error handling requires logging)
- **EXPLORE_AGENT** → Codebase exploration (use right tool for the job)
- **USE_DOC_MCP** → **DOCUMENT_APIS** (automated documentation flow)
- **MCP_ERROR_FIXES** → Error troubleshooting (use MCP servers for solutions)

## Quick Reference by Domain

### Conversation & Rule Awareness
- Rule Acknowledgment (CRITICAL): CHECK_RULES, PRINT_RULES, PRINT_MULTIPLE, NO_GENERIC_MENTIONS

### Planning & Task Management
- Planning (CRITICAL): USE_TODOWRITE, DISCRETE_STEPS, PLAN_APPROVAL, ONE_IN_PROGRESS, IMMEDIATE_COMPLETION
- Tool Usage (HIGH): USE_SPECIALIZED_TOOLS, PARALLEL_TOOLS, EXPLORE_AGENT, NO_BASH_COMMUNICATION

### Security
- Access Control (CRITICAL): LEAST_PRIVILEGE, NO_ADMIN_PERMISSIONS, TEMPORARY_CREDENTIALS, NO_SECRETS_IN_CODE
- Data Management (CRITICAL): DATA_ENCRYPTION, INPUT_VALIDATION, CREDENTIAL_ROTATION, NO_CREDENTIAL_HARVESTING, DEFENSIVE_SECURITY_ONLY
- Compliance (CRITICAL): SECURITY_REVIEWS, NO_MALICIOUS_CODE, EXPLAIN_SECURITY_IMPACT

### Development Workflow
- General Development (HIGH): NAMING_CONVENTIONS, TESTING, CONFIG_MANAGEMENT, PREFER_EDIT
- Error Handling (HIGH): ERROR_HANDLING, LOGGING, CONTEXT_IN_ERRORS, DEBUG_SYSTEMATICALLY, VERIFY_FIXES
- Documentation (HIGH): DOCUMENT_APIS, CODE_COMMENTS, INCLUDE_REFERENCES
- Version Control (MEDIUM): COMMIT_MESSAGES, COMMIT_FORMAT, INCLUDE_COAUTHOR, CHECKPOINT_COMMIT

### Infrastructure & Deployment
- Infrastructure as Code (HIGH): USE_MODULES, USE_VARIABLES, USE_DATA_SOURCES, FORMAT_BEFORE_COMMIT, VALIDATE_PLAN
- Deployment Testing (HIGH): TEST_DELETION, DEPROVISION_AUTOMATION, VERIFY_CLEANUP
- Cloud Functions (MEDIUM): ARCHITECTURE_COMPATIBILITY, DOCKER_ARCHITECTURE, COLD_START_OPTIMIZATION
- Cost Management (MEDIUM): COST_ESTIMATES, USE_COST_TOOLS, COST_OPTIMIZATION

### API & Services
- API Design (HIGH): API_VERSIONING, HTTP_STANDARDS, RATE_LIMITING, API_DOCUMENTATION
- Performance (HIGH): PERFORMANCE_ANALYSIS, CACHING_STRATEGY, AVOID_N_PLUS_ONE

### Operations
- Observability (MEDIUM): KPI_MONITORING, WORKFLOW_TRACING, HEALTH_CHECKS, ALERTING

### Research & Verification
- MCP Consultation (CRITICAL): CONSULT_MCP, MCP_FIRST, USE_TASK_AGENTS, VERIFY_CURRENT
- Error Fixes (HIGH): MCP_ERROR_FIXES, USE_SEARCH_TOOLS
- Documentation (HIGH): USE_DOC_MCP, DOCUMENT_APIS
- Cost Analysis (MEDIUM): USE_COST_MCP, WEB_COST_RESOURCES

## Implementation Guidelines for Common Tasks

### For All Conversations and Responses
1. Use **CHECK_RULES** before using tools or responding to ensure applicable rules are considered
2. Use **PRINT_RULES** to announce which specific rules are being followed at the start of the response (e.g., "Rule used: `MCP Server Consultation` (CONSULT_MCP)")
3. If multiple rules apply, use **PRINT_MULTIPLE** to list all applicable rules
4. Avoid generic statements about following rules per **NO_GENERIC_MENTIONS** - be specific about which rules are active

### For All New Development
1. Use **CONSULT_MCP** to verify current best practices if unfamiliar with technology (check for relevant MCP servers first)
2. Use **USE_TODOWRITE** to create structured task list for complex work
3. Mark tasks **IN_PROGRESS** one at a time
4. Follow **LEAST_PRIVILEGE** and **NO_SECRETS_IN_CODE** for security
5. Implement **ERROR_HANDLING** and **LOGGING**
6. Create **TESTING** for new features
7. Use **USE_DOC_MCP** or **DOCUMENT_APIS** for public interfaces
8. Write **COMMIT_MESSAGES** with proper format and co-author

### For Codebase Exploration
1. Use **EXPLORE_AGENT** (Task with subagent_type=Explore) for broad questions like:
   - "How does authentication work?"
   - "What is the codebase structure?"
   - "Where are errors handled?"
2. Use **Glob** for finding specific files by pattern
3. Use **Grep** for finding specific code/text
4. Use **Read** for examining specific files
5. Use **PARALLEL_TOOLS** to read multiple files at once

### For File Operations
1. Use **Glob** to find files (not `find` or `ls`)
2. Use **Grep** to search content (not `grep` or `rg` via Bash)
3. Use **Read** to read files (not `cat`/`head`/`tail`)
4. Use **Edit** to modify files (not `sed`/`awk`)
5. Use **Write** to create new files (not `echo >` or heredoc)
6. Remember **READ_BEFORE_EDIT** - must Read before Edit/Write

### For Infrastructure Changes
1. Create **USE_TODOWRITE** task list
2. Use **CONSULT_MCP** for current provider documentation (AWS, Terraform, etc.)
3. Follow IaC best practices (**USE_MODULES**, **USE_VARIABLES**, **CURRENT_PROVIDERS**, etc.)
4. Test both deployment and **TEST_DELETION**
5. Create **DEPROVISION_AUTOMATION**
6. Generate **COST_ESTIMATES** using **USE_COST_MCP** when appropriate
7. Implement monitoring (**KPI_MONITORING**, **HEALTH_CHECKS**)
8. Run **FORMAT_BEFORE_COMMIT** before committing

### For API Development
1. Use **HTTP_STANDARDS** for status codes and responses
2. Implement **INPUT_VALIDATION** for all inputs
3. Consider **API_VERSIONING** for public APIs
4. Implement **RATE_LIMITING** if exposed publicly
5. Use **WORKFLOW_TRACING** with correlation IDs
6. Create **API_DOCUMENTATION** with examples
7. Avoid **AVOID_N_PLUS_ONE** database issues

### For Debugging/Troubleshooting
1. Follow **DEBUG_SYSTEMATICALLY** - analyze before fixing
2. Use **MCP_ERROR_FIXES** to consult MCP servers for solutions and best practices
3. Use **USE_SEARCH_TOOLS** (WebSearch) for unfamiliar errors when MCP doesn't cover the domain
4. Check logs and error messages carefully
5. Ensure **CONTEXT_IN_ERRORS** when implementing error handling
6. **VERIFY_FIXES** after making changes

### For Git Operations
1. Use **COMMIT_FORMAT** with heredoc for multi-line messages
2. Include **INCLUDE_COAUTHOR** and **INCLUDE_SIGNATURE**
3. Never use **NEVER_FORCE_PUSH** to main/master without confirmation
4. Never use **NO_SKIP_HOOKS** unless explicitly requested
5. Follow **CHECKPOINT_COMMIT** when user requests checkpointing

## Claude Code-Specific Best Practices

### Understanding MCP Servers vs Claude Code Tools

**MCP Servers** (Model Context Protocol):
- Knowledge and consultation endpoints for domain-specific information
- Examples: AWS documentation, Terraform docs, cost estimation, code documentation generation
- Use for: Getting current best practices, technical specifications, pricing information, generating documentation
- When to use: Before implementation, when unfamiliar with technology, for accurate cost estimates, error troubleshooting

**Claude Code Tools**:
- File and codebase operation tools built into Claude Code
- Examples: Read, Write, Edit, Glob, Grep, Bash, Task agents
- Use for: File operations, code searching, codebase exploration, executing commands
- When to use: Working with files, searching code, exploring project structure, running builds/tests

**Key Principle**: Use MCP servers for **knowledge**, use Claude Code tools for **operations**

### Task Agent Usage
- Use **Explore agent** for codebase exploration ("quick", "medium", or "very thorough")
- Use **general-purpose agent** for complex multi-step tasks
- Launch agents in **PARALLEL** when tasks are independent
- Provide detailed prompts specifying what information to return

### Tool Efficiency
- **PARALLEL_TOOLS**: Make multiple independent tool calls in single message
- Read multiple files at once when gathering context
- Use Glob patterns like `**/*.ts` to find files efficiently
- Use Grep with `output_mode: "files_with_matches"` for quick searches

### Context Management
- Use specialized tools to reduce context usage
- Use Task agents for extensive exploration instead of manual searches
- Reference code with **INCLUDE_REFERENCES** format (file_path:line_number)

### Security Constraints
- **DEFENSIVE_SECURITY_ONLY**: Only assist with defensive security
- **NO_CREDENTIAL_HARVESTING**: Never create bulk credential discovery tools
- **NO_MALICIOUS_CODE**: Never create/improve potentially malicious code
- Can analyze existing code, write reports, explain vulnerabilities

## Error Handling Strategy

Each rule includes specific error handling guidance. General principles:
- Document all limitations when ideal implementation is not possible
- Implement fallback strategies that maintain security
- Note inconsistencies with existing patterns
- Flag areas for future improvement
- Never compromise on CRITICAL priority security requirements
- Ask clarifying questions when uncertain

## Differences from Amazon Q Rules

**Preserved MCP Guidance:**
- MCP server consultation remains CRITICAL priority
- MCP servers work in both Amazon Q and Claude Code
- All MCP-specific rules maintained (CONSULT_MCP, MCP_ERROR_FIXES, USE_DOC_MCP, USE_COST_MCP)

**Removed/Modified:**
- "Ultrathink" references (Claude has native planning with TodoWrite)
- AWS-specific resource tagging (too narrow for general rule)
- Some AWS-specific terminology made more technology-agnostic

**Added for Claude Code:**
- TodoWrite workflow and requirements (USE_TODOWRITE, ONE_IN_PROGRESS, IMMEDIATE_COMPLETION)
- Tool selection guidance (Read/Write/Edit/Glob/Grep/Bash/Task)
- Parallel tool execution (PARALLEL_TOOLS)
- Task agent usage patterns (EXPLORE_AGENT)
- Context management strategies
- Claude Code-specific security constraints (DEFENSIVE_SECURITY_ONLY, NO_CREDENTIAL_HARVESTING)
- Git commit co-author and signature requirements (INCLUDE_COAUTHOR, INCLUDE_SIGNATURE)
- File operation preferences (USE_SPECIALIZED_TOOLS, PREFER_EDIT)
- Clear distinction between MCP servers (knowledge) and Claude Code tools (operations)

**Adapted:**
- Planning with ultrathink → Planning with TodoWrite
- AWS-focused examples → Technology-agnostic examples
- Amazon Q workflow → Claude Code workflow

## Usage Notes

- All rule instructions have unique IDs for tracking and reference
- Rules are designed to be actionable, measurable, flexible, and traceable
- When documenting compliance or exceptions, reference specific rule IDs
- Use these rules as a comprehensive checklist for development work
- Adapt error handling strategies to specific project constraints while maintaining security standards
- Prioritize CRITICAL rules; HIGH rules for production code; MEDIUM rules for optimization
