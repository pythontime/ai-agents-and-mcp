# AI Agents and MCP Training Repository

A comprehensive training repository demonstrating the configuration, usage, and comparison of AI development agents (Claude Code and Amazon Q Developer) with Model Context Protocol (MCP) server integration.

## Features

- **Structured Rule Systems**: Comprehensive development rules for both Claude Code and Amazon Q Developer
- **Security-First Development**: Guidelines and examples for secure coding practices
- **MCP Server Integration**: Examples of integrating Model Context Protocol servers for enhanced AI capabilities
- **Legacy Application Hardening**: Practical examples of securing vulnerable applications
- **Infrastructure as Code**: Best practices for Terraform and AWS resource management
- **Development Workflow Automation**: Automated testing, linting, and deployment configurations
- **AI Agent Comparison**: Side-by-side demonstrations of different AI agents' capabilities
- **Real-world Examples**: Production-ready Flask applications with security implementations

## Prerequisites

### Required AWS Setup
- AWS CLI configured with appropriate credentials
- IAM permissions for S3, Lambda, and other services used in examples
- AWS account with billing alerts configured (for cost management examples)

### Development Environment
- Python 3.8+ with virtual environment support
- Claude Code CLI installed and configured
- Amazon Q Developer CLI installed and configured
- Git for version control
- Text editor or IDE with Markdown support

## Project Components

### Configuration Systems (`01_claude_code_config/`, `02_q_developer_config/`)
Structured rule systems that define development best practices, security guidelines, and workflow automation for AI agents. These configurations ensure consistent, secure, and efficient development practices.

**Key Features:**
- Priority-based rule implementation (Critical, High, Medium)
- MCP server consultation requirements
- Security-first development practices
- Error handling and troubleshooting guidelines

### Rule Categories (`02_q_developer_config/rules/`)
Organized by domain for easy reference and implementation:

- **Security**: Access control, data management, compliance
- **Development**: Python development, error handling, performance optimization
- **Infrastructure**: Terraform, cost estimation, deployment testing
- **General**: MCP consultation, planning, error troubleshooting
- **API**: Design standards and best practices
- **Monitoring**: Observability and alerting

### Demonstration Examples (`03_use_solutions/`)
Practical examples showing AI agents in action:

- **Legacy Application Security**: Before/after examples of securing vulnerable Flask applications
- **Security Hardening**: Implementation of Argon2 password hashing, input validation, and AWS integration
- **Development Workflows**: Automated testing, linting, and security scanning

### Secure Application Example (`03_use_solutions/legacy-app-secure/`)
Production-ready Flask application demonstrating:

- Secure password hashing with Argon2
- Input validation and sanitization
- AWS S3 integration with temporary credentials
- Comprehensive testing suite
- Security scanning with Bandit
- Code quality tools (Black, Pylint, MyPy)

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai-agents-and-mcp
   ```

2. **Set up Python environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies** (for the secure app example):
   ```bash
   cd 03_use_solutions/legacy-app-secure
   pip install -r requirements.txt
   ```

4. **Configure AI agents**:
   - Review configuration files in `01_claude_code_config/` and `02_q_developer_config/`
   - Adapt rules to your specific development needs
   - Set up MCP servers as documented in the configuration files

## Usage Examples

### Using the Rule Systems
Reference the structured rules when working with AI agents:

```bash
# For Claude Code development
cat 01_claude_code_config/CLAUDE.md

# For Amazon Q Developer
ls 02_q_developer_config/rules/
```

### Running the Secure Application
```bash
cd 03_use_solutions/legacy-app-secure
python app.py
```

### Security Scanning
```bash
# Run security analysis
bandit -r . -f json -o security-report.json

# Run code quality checks
pylint *.py
black --check *.py
mypy *.py
```

## Architecture

The repository follows a modular structure designed for training and practical application:

```
ai-agents-and-mcp/
├── 01_claude_code_config/     # Claude Code specific configurations
├── 02_q_developer_config/     # Amazon Q Developer configurations
│   └── rules/                 # Categorized development rules
├── 03_use_solutions/          # Practical examples and demonstrations
│   └── legacy-app-secure/     # Secure Flask application example
└── .claude/                   # Claude Code settings
```

## Next Steps

### Enhancements
- **Custom MCP Servers**: Develop domain-specific MCP servers for your organization
- **CI/CD Integration**: Implement the rule systems in your CI/CD pipelines
- **Team Adoption**: Customize rules for your team's specific needs and technologies
- **Security Automation**: Integrate security scanning into development workflows

### Contributing
1. Fork the repository
2. Create a feature branch
3. Follow the established rule systems in your development
4. Add tests for new functionality
5. Submit a pull request with detailed description

## Clean Up

### Development Environment
```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment (if needed)
rm -rf venv
```

### AWS Resources
If you've deployed any AWS resources during testing:
```bash
# Review and delete any created S3 buckets, Lambda functions, etc.
aws s3 ls  # Check for test buckets
aws lambda list-functions  # Check for test functions
```

## Troubleshooting

### Common Issues

**Virtual Environment Issues**:
- Ensure Python 3.8+ is installed
- Check PATH configuration for Python and pip
- Use `python3 -m venv` instead of `virtualenv` if available

**MCP Server Connection Issues**:
- Verify MCP server installation and configuration
- Check network connectivity and firewall settings
- Review MCP server logs for connection errors

**Security Scanning False Positives**:
- Review Bandit configuration in `.bandit`
- Add specific exclusions for known safe patterns
- Update security tools to latest versions

**AWS Credential Issues**:
- Verify AWS CLI configuration: `aws configure list`
- Check IAM permissions for required services
- Ensure temporary credentials haven't expired

### Getting Help
- Review the rule documentation in `02_q_developer_config/rules/`
- Check the secure application example for implementation patterns
- Consult MCP server documentation for integration issues

## License

This project is provided as training material. Please review and comply with your organization's policies regarding AI agent usage and development practices.