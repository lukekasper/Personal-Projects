## Cost Management

Factors that Effect Cost
- Azure shuifts cost from CapEx to OpEx
- Resource Type:
  - Type, settings, and region all affect resource cost
  - Metered instances are created for each resource to track usage and generate a cost record for billing
  - For storage: storage type, performance tier, access tier, and redundancy settings
  - For VMs: licensing for OS, other software, processor/number of cores, attached storage, network interface
- Consumption: Pay-as-you-go is standard, but can commit to using a set amount of resources in advance to get a discount (typically 1-3 years)
- Maintenance: make sure you manage cloud environment (if you deprovision a VM, ensure you deprovision unused networking and storage associated with it)
- Geography: pricing differs per region
  - Network traffic also impacted by geography (less expensive to move info within Europe than from Europe to Asia)
- Network traffic:
  - Bandwidth refers to data moving in and out of Azure datacenters
  - Some inbound data transfers are free, outbound pricing is based on zones
  - A zone is a grouping of regions for billing
- Subscription type: Some subscriptions inglcude usage allowances (which affect costs)
- Azure Marketplace:
  - purchase solutions and services from third-partry vendors
    - server with software installed and configured, managed netwrok firewall appliances, or connecting to third-party backup services
  - pay for Azure serivices + thrid party services and expertiese (billing strucutre set by vendor)
  - all solutions are certified and compliant with Azure policies/standards

Pricing and Total Cost of Ownership Calculators
- Pricing Calculator:
  - estimates cost of provisioning resources
    - individual resources, build out a solution, or use an example scenario
    - estimate compute, storatge (type, tier, redundancy) and associated network costs
- TCO Calculator:
  - compares on-premise to estimated cloud costs
  - define workloads: infastructure config (servers, databases, storage, outbound netowrk traffic)
  - add in assumptions like power and IT labor costs
  - view report

Princing Calculator Example:
- Web based applicaiton requirements:
  - The application is used internally. It's not accessible to customers.
  - This application doesn't require a massive amount of computing power.
  - The virtual machines and the database run all the time (730 hours per month).
  - The network processes about 1 TB of data per month.
  - The database doesn't need to be configured for high-performance workloads and requires no more than 32 GB of storage.
- Choose a VM (2), Database, and Network for a basic web-app

Cost Management Tool
- ability to check resource costs, create alerts based on resource spend, and create budgets that can be used to automate management of resources
- cost analysis is a subset of tool
  - can view total cost by billing cycle, region, resource, ect.
- cost alerts:
  - budget alerts:
    - notify when spending exceeds threshold (cost or usage based)
    - cost management budgets are created using Azure portal (cost) or Azure Consumption API (cost or consumption)
    - cost alerts can be viewed in the portal and can be sent out via email to recipients list
  - credit alerts:
    - notify when credit monetary commitments are consumed (90% and 100% of limit)
    - for businesses with Enterprise Agreements (EAs)
  - department spending quota alerts:
    - notify when spending reaches a fixed limit of your quota
    - quotas are configured via EA portal
- Budgets:
  - where you set an Azure spending limit
  - can be set on subscription, resource group, service type, ect.
  - will also get a budget alert automatically
  - can automate suspend/modify a resource when limit is reached

Resource Tags
- A way to organize resources (like subscription or group) by providing metadata about said resource
- Tags are used for:
  - resource management: locate and act on resources that are associated with specific workloads, environments, business units, and owners
  - cost and management optimization: group resources to report on costs, allocate internal cost centers, track budgets, and forecast estimated cost
  - operational management: group by criticality; enables formulation of Service Level Agreements (SLAs) for your users
  - security: such as public or confidential
  - governance and regulatory compliance: group by compliance (ie ISO 27001); can also be used as standards enforcement by requiring a tag by owner or
    department name
  - workload optimization and automation: group by workload or application name to organize how resources are deployed (ie Azure DevOps)
- Management of tags:
  - can add, modify or delete tags through typical Azure intergaces (powershell, CLI, portal, resouce manager templates, or REST API)
  - can use Azure policy to enforce tagging rules
  - resources [do not] inherit tags from groups/subscriptions, only at one level
  - tag consists of a name and a value (ie Name: AppName, Value: LukesRecipes)

## Tools for Governance and Compliance

Azure Blueprints
- Let you standardized cloud subscriptions or environment deployments
- Define repeatable settings and policies (template) for subscriptions
- Artifacts:
  - Each component in a blueprint definition
  - Can contain parameters (like allowed location for an allowance setting) that can be set at definition or blueprint assignment (not required)
  - Artifacts can include: role assignments, policy assignments, Azure Resource Manager templates, and resource groups
- How do they help monitor deployments?
  - Version-able, allowing updates to be made and assigning a new version to update
    - Helps to track which deployments used which configuration
  - Relationship between blueprint definition and assignment is preserved to better track/audit deployments

Azure Policy
- Service that lets you create, assign, and manage policies that control/audit resources
  - Enforce different rules across configurations to stay compliant with corporate standards
- Define both individual or group policies (initiatives)
- Highlights uncompliant resources, or prevents them from being created
- Can be set at each level (resource, group, subscription, ect)
  - Are inherited to lower levels
- Azure Policy comes with built-in definitions for Storage, Networking, Compute, Security Center, and Monitoring
  - Ie) a policy defining size of VMs is evoked when creating or resizing VMs in environment, and Azure monitors all other VMs (even those created before the
    policy)
- Can automatically remediate noncompliant resources (assign a missing tag)
  - Can tag resources you don't want automatically fixed as an exception
- Also integrates with Azure DevOps
  - Apply continuous integration and delivery pipeline policies
  - Pertain to both pre and post-deployment app phases
- Initiatives are a way to group related policies to help track compliance state for a larger goal
  - Ex) Azure Policy of Enable Monitoring in Azure Security Center contains the following policies:
    - Monitor unencrypted SQL Database
    - Monitor OS vulnerabilities
    - Monitor missing Endpoint Protection
			
Resource Locks
- Prevents resources from being accidentally deleted or changed
- Can be applied to resources, groups, or subscriptions (inherited)
- Delete (users can modify) and ReadOnly locks available
- Can manage locks in any of the Azure interfaces (portal, CLI, Powershell, Azure Resource Manager template)
- To modify a locked resource, must remove the lock first
	
Service Trust portal
- Provides content, tools and resources about Microsoft security, privacy, and compliance practices
- contains details about Microsoft's implementation of controls and processes that protect our cloud services and the customer data

## Tools for Managing and Deploying Azure Resources

Interacting with Azure
- Azure Portal:
  - Web-based console (GUI) as an alternate to cmd line tools
  - build, manage, and monitor web apps to cloud deployments
  - create custom dashboards for organization
  - configure accessibility options
  - presence at every datacenter
    - resiliant to failures and avoids network slowdowns by being close to users 
  - no downtime for maintenance
- Azure Cloud Shell:
  - browser-based shell tool
    - Azure PowerShell and Azure Command Line Interface (CLI)
  - can access from portal by hitting cloud shell icon
    - browser-based means no local installation or configuration
    - authenticated with your Azure credentials (knows ID and permissions upon login)
    - can choose preferred shell:PowerShell or Bash (CLI)
  - PowerShell:
    - run cmdlets which call REST API to perform management tasks in Azure
      - routine setup, teardown, and maintenance of resource or connected resources
      - deployment of entire infastructure
    - script makes process automatable
    - in addition to Azure Cloud Shell, can also confugre on Windows, Linux, and mac platforms
  - CLI: same as PowerShell with different syntax (bash commands)

Azure Arc
- Azure Resource Manager (ARM): Arc extends compliance to hybrid and multi-cloud configurations
- Centralized way to:
  - Manage entire environment together by projecting non-Azure resources into ARM
  - Manage multi-cloud and hybrid virtual machines, Kubernetes clusters, and databases as if they are running in Azure
  - Use familiar Azure services and management capabilities
  - Continue using traditional ITOps while introducing DevOps practices to support new cloud and native patterns
  - Configure custom locations as an abstraction layer on top of Azure Arc-enabled Kubernetes clusters and cluster extensions
- Can manage following resource types outside of Azure: servers, Kubernets clusters, Azure data services, SQL server, VMs (preview) 

Azure Resource Manager and ARM Templates
- management and deployment service for Azure
  - is involved anytime you interact with an Azure resource
  - recieves any request (from tools, APIs, SDKs), provides authentication, and sends request to Azure service which takes the action
- Benefits:
  - manage infrastructure through declarative templates rather than scripts
    - JSON file that defines what you want to deploy to Azure
  - handle resources as a group
  - have confidence re-deployments are consistent
  - define dependencies, to ensure resources are deployed in correct order
  - apply access control to all services (RBAC is integrated into platform)
  - apply tags
  - clarify billing by viewing costs by tag
- ARM templates:
  - infrastructure as code: manage infastrucutre as lines of code (use of Azure Cloud Shell, PowerShell, or CLI)
    - Use Azure Blueprints to deploy policies in an automated fashion and ARM template to deploy resources as code
  - deployment code is verified before any code is run
  - ochestrates creation of resources in parallel (simultaneously)
  - only define desired state and configuration of resource, template does the rest
  - can execute PowerShell and Bash scripts before or after the resource has been set up
  - Benefits:
    - Declarative syntax: declare what you want to deploy, but don't need to write the actual programming commands
    - Repeatable results
    - Orchestration: ARM creates resources in correct order (no need to worry about order of operations), and in parallel
    - Modular files: break template into smaller, reuseable components and link together at deployment time
      - nest templates
    - Extensibility: can use deployment scripts in PowerShell or Bash to extend ability to set up resources
      - can be in template or an external source
      - complete entire end-to-end evironemnt setup in a single ARM

## Monitoring Tools

Azure Advisor
- evaluates resources and makes recommendations to help improve reliability, security, and performance, achieve operational excellence, and reduce costs
- designed to help save time on cloud optimization
- can take actions right away, postpone, or dismiss
- 5 categories of recommendations:
  - Reliability
  - Security
  - Performance: speed of applicaitons
  - Operational excellence: process and workflow efficiency, resource manageability, and best deployment practices
  - Cost

Azure Service Health
- Assess status of individual resources and overall global infastructure
- Azure Status: broad picture of Azure status globally
  - incidents with widespread impact
- Service Health: focuses on services and regions you are using
  - incidents impacting communications and outages, planned maintenance, and other health advisories
- Resource Health: individual cloud resources
- Historical alerts help you track issues that may have seemed like an anomoly initially
- Provides links to support

Azure Monitor
- platform for collecting, analyzing, visualizing, and acting on data on resources
- can monitor Azure, on-premises, and multi-cloud resources
- Log Analytics:
  - write and run log queries on data gathered by Azure Monitor
  - can write a simple query and sort, filter, and analyze result
  - advanced queries can perform statistical analysis and visualize data
- Azure Monitor Alerts:
  - automates alert when threshold is crossed and can perform automated action
  - alerts based on log events or metrics (CPU utilization)
    - rules based on logs allow complex logic across data from multiple sources
  - action groups define who to notify when alert is triggered
- Application Insights:
  - monitors web applications on Azure, on-premise, and other clouds
  - configure through installing an SDK or using an Application Insights agent
  - used to monitor:
    - request rates, response times, and failure rates
    - dependency rates, response times, and failure rates, to show whether external services are slowing down performance
    - page views and load performance reported by users' browsers
    - AJAX calls from web pages, including rates, response times, and failure rate
    - user and session counts
    - performance counters from Windows or Linux server machines, such as CPU, memory, and network usage
  - can periodically send synthetic requests to monitor health even during low activity periods

