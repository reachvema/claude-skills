# Debug Deployment Issues with Claude into Azure

## Objective
Troubleshoot and resolve common Azure deployment issues using systematic debugging approaches.

## Common Issues
- Container startup failures
- Image pull errors from ACR
- Authentication and permission issues
- Environment variable configuration errors
- Network connectivity problems
- Resource quota limitations
- Application crashes or restarts
- Performance and scaling issues

## Debugging Steps
1. Check container app logs and events
2. Verify image accessibility in ACR
3. Validate environment variables and secrets
4. Review managed identity and RBAC permissions
5. Test network connectivity and DNS resolution
6. Inspect resource metrics and quotas
7. Verify ingress and routing configuration
8. Check application health probes

## Azure CLI Commands
```bash
# View container app logs
az containerapp logs show --name <app-name> --resource-group <rg>

# Check container app status
az containerapp show --name <app-name> --resource-group <rg>

# View revision history
az containerapp revision list --name <app-name> --resource-group <rg>

# Stream logs in real-time
az containerapp logs tail --name <app-name> --resource-group <rg>
```

## Tools & Resources
- Azure Portal (Container Apps blade)
- Azure CLI
- Log Analytics queries
- Application Insights
- Azure Monitor

## Outputs
- Root cause analysis
- Resolution steps and fixes
- Configuration corrections
- Preventive recommendations
