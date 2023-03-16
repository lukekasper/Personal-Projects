Interacting with Azure:
- Can interact with Azure using PowerShell, BASH, Azure CLI Interactive mode, or portal
  - Interactive mode resembles an integrated development environment (IDE)
  
Physical Infastructure
- Regions: Azure datacenters are broken out by region (may have multiple in a single region)
  - Azure controls resources within a region to ensure workloads are balanceed
  - Region pairs: provides redundancy if an entire region were to fail
  - Sovereign Regions: instance of Azure isolated from the main instance
- Availability Zones:
  - Datacenters within a region
  - Set up to ensure redundancy if one goes down, and connected through high-spee, private fiber-optic networks
  - Primarily for VMs, managed disks, load balancers, and SQL databases
  - Services that support availability zones:
    - Zonal services: You pin the resource to a specific zone (for example, VMs, managed disks, IP addresses)
    - Zone-redundant services: The platform replicates automatically across zones (for example, zone-redundant storage, SQL Database)
    - Non-regional services: Services are always available from Azure geographies and are resilient to zone-wide outages as well as region-wide outages

Managment Infastructure
- Resources and resource groups: anything you create, provision, deploy, etc
  - Virtual Machines (VMs), virtual networks, databases, cognitive services
  - Resource groups are groupings of similar resources
    - A resource can only be in one group and groups cannot be nested
    - An action to a resource group effects all resources within it 
- Azure subscriptions:
  - Subscrition boundaries:
    - Billing: how an account is billed; can create multiple subscriptions for different billing requirements
    - Access Control: can create different subscriptions to reflect different organizational structures
    - Create additional subscriptions to:
      - set up separate environments for development and testing, security, or to isolate data for compliance reasons
      - reflect different organizational structures (IT team gets higher cost resources)
      - billing purposes (production workloads vs development/testing workloads)
- Azure management groups: way to organize subscriptions into sub-groups or containers
  - Can apply governance or compliance regulations to all subscriptions in a group
  - Can be nested
  - Examples:
    - Create a hierarchy that applies a policy: limit VM locations to the US West Region. This policy will inherit onto all the subscriptions that are 
      descendants of that management group and will apply to all VMs under those subscriptions. Policy can't be altered at resource or subscription level,
      inmproving governance
    - Provide user access to multiple subscriptions: can create one Azure role-based access control (Azure RBAC) assignment to provide access permission to 
      all sub-subscriptions
  - Key points:
    - 10,000 management groups can be supported in a single directory
    - A management group tree can support up to six levels of depth. This limit doesn't include the root level or the subscription level
    - Each management group and subscription can support only one parent
