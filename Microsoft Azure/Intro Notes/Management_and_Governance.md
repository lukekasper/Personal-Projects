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
  - Inputs: infastructure config (servers, databases, storage, outbound netowrk traffic)
    - add in assumptions like power and IT labor costs

Princing Calculator Example:
- Web based applicaiton requirements:
  - The application is used internally. It's not accessible to customers.
  - This application doesn't require a massive amount of computing power.
  - The virtual machines and the database run all the time (730 hours per month).
  - The network processes about 1 TB of data per month.
  - The database doesn't need to be configured for high-performance workloads and requires no more than 32 GB of storage.
- Choose a VM (2), Database, and Network for a basic web-app

