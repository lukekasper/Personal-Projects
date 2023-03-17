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

Virtual Machines
- Provide IaaS in the form of a virtualized server
- Ideal choice when:
  - Total control over operating system (OS) is needed
  - Need to run custom software
  - Use custom hosting configurations
- As an IaaS, must configure, update, and maintain software on VM
- An image is a template used to create a VM and may already include an OS and other software, like development tools or web hosting environments
- Scale sets:
  - create and manage a group of identical, load-balanced VMs
  - allows you to centrally manage, configure, and update a large number of VMs in minutes
  - number of VM instances can automatically increase or decrease in response to demand, or you can set it to scale based on a defined schedule
  - automatically deploys a load balancer
  - good for large scale services such as: compute, big data, and container workloads
- Availability sets:
  - ensure that VMs stagger updates and have varied power and network connectivity (making system more robust to failures)
  - Update domain: groups VMs that can be rebooted at the same time, allows user to push an update and ensures only one update domain group will be             offline at a single time
  - Fault domain: groups VMs by common power source and network switch (protecting against failures)
- When to use VMs:
  - During testing and development
    - can quickly create and test different os and app configs
  - When running applications in the cloud
    - can start up or shut down VMs automatically when needed to optimize efficiency and cost
  - When extending your datacenter to the cloud
  - During disaster recovery
    - can create temporary VMs to run critical apps until datacenter comes back online
  - Moving from physcial server to cloud
    - VMs can directly replicate phyical server configuration and os
- Can pick resources associated with the VM like:
  - size (purpose, number of processor cores, amount of RAM)
  - storage disks (hard drives, solid state, ect)
  - networking (virtual network, public IP address, port configuration)

Virtual Desktops
- A VM that serves as a desktop and application virtualization service
- Runs across any OS or device
- Enhanced security:
  - Azure Active Directory (AD) provides centralized security management
  - Supports multifactor authentication
  - Can secure access to data with granular role-based access controls (RBACs)
  - Reduced risk of data being left on a personal device due to seperation of hardware and data/apps
  - Users are isolated in both single and multi-session environments
- Multi-session Windows deployment:
  - Enterprise multi-session is the only Windwos client-based OS that enables multiple concurrent users on a single VM
  - More consistent with broader application support compared with Windows server-based OS

Azure Containers
- Used to run multiple instances of an app (using different OSs) on a single host machine
- They are a virtualization environment, which you can run multiple of on a single physical or virtual host
- Don't manage the OS for a container
- VMs virtualize the hardware, while Containers virtualize the OS
- Containers are more light wait and agile than VMs
  - Just need to wait for the app to launch rather than the OS and the app (VMs)
- Docker is one of the most common containers, which is supported by Azure
- If complete control is needed, VM is preferred; if not, portability, performance characterisitics, and management capabilities of containers are better
- Azure Container Instances:
  - Fastest and simplest way to deply a container; don't have to manage VMs or adopt additional services
  - They are a PaaS, you upload your containers and the service runs them for you
- Microservice Architecture:
  - break solution itno smaller, independent pieces
  - Ex) container for front end, back end, and storage
  - Can scale portions of the application seperately depending on the need

Azure Functions
- Event-driven serverless compute option, alleveiating the need to keep services running when there are no events (like VMs or containers)
- Serverless computing: management of servers and infastructure is handled by cloud service
- No infastructure management, scalability, only pay for what you use (event driven)
