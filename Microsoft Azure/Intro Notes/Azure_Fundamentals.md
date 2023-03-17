## Core Components

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

## Azure compute and networking services

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
- Ideal when you only care about the code running on your service (not the infastructure or platform)
- Common when you need to perform work in response to an event (REST request), timer, or message, and it can be completed quickly
- Stateless functions reset each time its ran
- Stateful functions track prior activity

Application Hosting Options
- VMs, containers, and Azure App Service
- Azure App Service:
  - Build and host web apps, background jobs, mobile back-ends, and RESTful APIs without manangeing infrastructure
  - Automated deployments GitHub, Azure DevOps, or any Git repo
  - Supports Windows and Linux
  - Can host: web apps, API apps, WebJobs, Mobile apps
  - App Service handles most infrastructure decisions:
    - Deployment and mangement
    - Secured endpoints
    - Scaled sites to handle high traffic loads
    - Load balancing and traffic manager provide high availability
  - Mobile Apps:
    - sotre mobile app data in cloud-based SQL database
    - authenticate cusomers against common social providers
    - send push notifications
    - execute custom back-end logic in C# or Node.js

Azure Virtual Networking
- Allow Azure resources (VMs, web apps, ect) to communicate with one another, users on the internet, and on-premise client computers
- It is an extension of an on premise netweor with resources that link to other Azure resources
- Supports public and private endpoints enable communication between external or internal resources with other internal resources
  - Public endpoints have a public IP address and can be accessed from anywhere
  - Private endpoints exist within a virtual network and have a private IP address from within the address space of that virtual network
- Capabilities:
  - Isolation and segmentation:
    - Can create multiple isolated virtual networks
    - IP range only exists within virtual network and isn't internet routable
    - Can divide IP address space into subnets and allocate part of the defined address space to each subnet
    - Can use name resolution service built into Azure or configure virtual network to use internal or extranl DNS server
  - Internet communications:
    - Can enable internet connection by assigning pulic IP address to an resource or put resource behind a public load balancer
  - Communicate between Azure resources:
    - Virtual networks can connect all Azure resources such as the App Service Environment for Power Apps, Azure Kubernetes Service, and Azure virtual
      machine scale sets
    - Service endpoints can connect to Azure SQL databases, storage accounts, ect; allows linkage of multiple resources to virtual networks to improve
      security and provide optimal routing between resources
  - Communicate with on-premises resources
    - Can create a network that spans both on premise and cloud resources
    - Point-to-site: from a computer outside your organization back into your corporate network; client computer initiates an encrypted VPN to connect to
      virtual network
    - Site-to-site: devices in Azure can appear as being on the local network; encrypted and works over the internet
    - Azure ExpressRoute: private connectivity that doesn't travel over the internet; when you need greater bandwidth and even higher levels of security
  - Route network traffic:
    - Azure routes traffic, but you can override those settings
    - Route tables define rules on how traffic should be directed
    - Border Gateway Protocol (BGP) works with Azure VPN gateways, Azure Route Server, or Azure ExpressRoute to propagate on-premises BGP routes to Azure
      virtual networks
  - Filter network traffic:
    - Network security groups: contain inbound/outbound securty rules; can allow/block traffic based on IP, port, and protocol
    - Network virtual appliances: specialized VMs that can perform a network function like run a firewall or perform a wide area network (WAN) optimization
  - Connect virtual networks
    - Link networks through network peering
    - Traffic is private and is on Microsoft backbone network (not public internet)
    - Resources can communicate across virtual networks (even in seperate regions)
    - User-defined routes (UDR) allow control of routing tables between subnets within a network or between networks

Exercise "Configuring Network Access"
- Every VM on Azure is aassociated with at least one network security group
- Default rule is to allow inbound connections over port 22 (SSH); only allows administrators to access the system remotely
- Must allow inbound connections on port 80 to allow access over HTTP (internet)
- Can create a standalone network security group that include the inbound and outbound network access rules you need
- If you have multiple VMs that serve the same purpose, you can assign that NSG to each VM at the time you create it

Virtual Private Networks (VPN)
- Uses an encrypted tunnel within another network
- Used to connect two or more private networks over an untrusted one (public internet)
- Traffic is encrypted on untrusted network, allowing networks to share sensitive info securely
- VPN gateways:
  - deployed in a dedicated subnet of the virtual network:
    - Connect on-premises datacenters to virtual networks through a site-to-site connection
    - Connect individual devices to virtual networks through a point-to-site connection
    - Connect virtual networks to other virtual networks through a network-to-network connection
  - Only one gateway per virtual network, but can use one gateway to connect to multipe locations
  - Specify BPN type as policy-based or route-based (how traffic is encrypted); both use a pre-shared key as method of authentication
  - Policy-based: specify statically the IP address of packets that should be encypted through each tunnel
  - Rout-based: IPSec tunnels are modeled as a network interface or virtual tunnel interface
    - IP routing (either static routes or dynamic routing protocols) decides which one of these tunnel interfaces to use when sending each packet
    - preferred for on-premise devices
    - more resilient to topology changes such as the creation of new subnets
    - used for:
      - Connections between virtual networks
      - Point-to-site connections
      - Multisite connections
      - Coexistence with an Azure ExpressRoute gateway
- High Availability Scenarios:
  - Ensure VPN is highly availabile and fault tolerant
  - Active/standby:
    - when maintenance or disruptions occur, standby VPN automatically assumes control within a few secs for maintenance or 90 sec for disruptions
  - Active/active:
    - seperate IPs and tunnels for each VPN instance
    - can extend the high availability by deploying an additional VPN device on-premises
  - ExpressRoute failover:
    - provide a VPN gateway that uses internet as an alternative when ExpressRoute has physical disruptions
    - ensures there is always a connection to the virtual networks
  - Zone-redundant gateways:
    - deploying in availability zones seperates gateways within a region, protecting against zone-level failures
    - require different gateway stock keeping unites (SKUs) and use standard publeic IP address (vice basic public IP addresses)

Azure ExpressRoute
- ExpressRoute Circuit provides connection between on premise networks and cloud (private connection)
- Can be from an any-to-any (IP VPN) network, point-to-point Ethernet network, or virtual cross-connection through a connectivity provider at a colocation
  facility
- More reliability, faster speeds, consistent latencies, and higher security than over the Internet
- Features and Benefits:
  - Connectivity to cloud services in all regions such as:
    - Microsoft Office 365
    - Microsoft Dynamics 365
    - Azure compute services, such as Azure Virtual Machines
    - Azure cloud services, such as Azure Cosmos DB and Azure Storage
  -  Global connectivity: can enable ExpressRoute Global Reach to exchange data across your on-premises sites by connecting your ExpressRoute circuits
  -  Dynamic routing: BGP enables dynamic routing between your on-premises network and services running on the cloud
  -  Redundancy: each connectivity provider uses redundant devices; can configure multiple circuits to complement this feature
- ExpressRoute connectivity models:
  - Co-location at a cloud exchange: datacenter, office, or other facility is physically co-located at a cloud exchange, such as an ISP
    - if so, can request a virtual cross-connect to the cloud
  - Point-to-point Ethernet connection
  - Any-to-any networks: can integrate your wide area network (WAN) by providing connections to your offices and datacenters
  - Directly from ExpressRoute sites: connect into the Microsoft's global network at a peering location; supports Active/Active connectivity at scale
- Security considerations:
  - private connections mean data does not travel over internet
  - Even if you have an ExpressRoute connection, DNS queries, certificate revocation list checking, and Azure Content Delivery Network requests are still
    sent over the public internet

Azure DNS
- Hosting service for DNS domains; provides name resolution using Azure infastructure
- Can manage your DNS records using the same credentials, APIs, tools, and billing as your other Azure services
- Beneifts:
  - Reliability and performance: uses anycast networking, so each DNS query is answered by the closest available DNS server to provide fast performance and
    high availability
  - Security: based on Azure Resource Manager
    - azure role-based access control (Azure RBAC) to control who has access to specific actions
    - activity logs to monitor how a user in your organization modified a resource or to find an error when troubleshooting
    - resource locking to lock a subscription, resource group, or resource
  - Ease of use: can manage records and provide DNS for external resources as well
    - can manage domains and records with Azure portal, powershell and cross-platform CLI
    - applications that require automated DNS management can integrate with the service by using the REST API and SDKs
  - Customizable virtual networks with private domains: allows use of your own custom domain names in your private virtual networks
  - Alias records: can use to refer to a resource, such as an Azure public IP address, an Azure Traffic Manager profile, or an Azure Content Delivery
    Network (CDN) endpoint
    - if a resource IP changes, alias record automaticall updates itself during DNS resolution
    - alias record set points to the service instance, and the service instance is associated with an IP address
