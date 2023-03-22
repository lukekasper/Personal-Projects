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
  - Set up to ensure redundancy if one goes down, and connected through high-speed, private fiber-optic networks
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

## Storage Services

Storage Accounts
- Provides a unique namespace for data that's accessible from anywhere over HTTP or HTTPS
- Redundancy options:
  - Locally redundant storage (LRS)
  - Geo-redundant storage (GRS)
  - Read-access geo-redundant storage (RA-GRS)
  - Zone-redundant storage (ZRS)
  - Geo-zone-redundant storage (GZRS)
  - Read-access geo-zone-redundant storage (RA-GZRS)
- Storage account endpoints:
  - combination of account name and the Azure Storage service endpoint forms the endpoints
  - names must be between 3 and 24 characters, and contain numbers and lower case letters only
  - must be unique

Storatge Redundancy
- Tradeoff between lower cost and higher availability
- Reundancy in Primary Region:
  - data is always replicated 3 times in primary region
  - Locally Redundant Storage (LRS): replicated 3 times within a data center in primary region
    - provides 11 nines durability (99.999999999%) of objects over a given year
    - lowest cost option
    - protects against server rack/drive failures, but not against datacenter-wide disasters
  - Zone-Redundant Storage (ZRS): replicated synchronously across 3 availability zones
    - 12 nines durability
    - data is accessible for read and write if a zone becomes unavailable (Azure automatically provides network updates like DNS repointing)
    - recommended for restricting data within a country/region for governance requirements
- Redundancy in a secondary region:
  - provides a secondary backup in the event of catastrophic event in primary region, backup is asychronous (may result in some data loss)
    - Recovery Point Objective (RPO) is the point in time to which data can be recovered (typically less than 15 min)
  - based on Azure Pairs (cannot be changed)
  - data in secondary region not availabile for read/write access unless failover to secondary region occurs
  - Geo-redundant storage (GRS): synchronously 3 times within a data center and asynchronously 3 times within a secondary data center (like LRS)
    - 16 nines durability
  - Geo-zone-redundant storage (GZRS): 3 copies in primary region (ZRS) and 3 times in secondary region dataceneter (LRS)
    - 16 nines durability
  - Read Access-GRS (RA-GRS) and Read Access-GZRS (RA-GZRS):
    - Enables user to read data in secondary region even if failover has not occured
    - Data may not be up to date due to RPO

Storage Services
- Azure Data Services:
  - Azure Blobs: scalable object store for text and binary data; includes support for big data analytics through Data Lake Storage Gen2
  - Azure Files: managed file shares for cloud or on-premises deployments
  - Azure Queues: messaging store for reliable messaging between application components
  - Azure Disks: block-level storage volumes for Azure VM
- Benefits:
  - Durable and highly available: redundancy
  - Secure: data is encrypted and access controlled
  - Scalable
  - Managed: Azure handles hardware maintenance, updates, and critical issues
  - Accessible: accessible anywhere over HTTP/HTTPS; client libraries in many languages; access to data using any of Azure access methods (ie portal)
- Blob Storage:
  - unstructured; no restrictions on data type
  - Ideal for:
    - Serving images or documents directly to a browser
    - Storing files for distributed access
    - Streaming video and audio
    - Storing data for backup and restore, disaster recovery, and archiving
    - Storing data for analysis by an on-premises or Azure-hosted service
  - Blob storage tiers:
    - useful to organize data by frequency of access and planned retention period
    - Hot access tier: data is accessed frequently (website images)
    - Cool access tier: accessed infrequently and stored for at least 30 days (customer invoices)
    - Archive access tier: rarely accessed and stored for at least 180 days; flexible latency requirements (long-term backups)
    - considerations:
      - Archive tier cannot be set at account level (only hot/cool)
      - all can be set at blob level, during or after upload
      - cool access tier can tolerate slightly lower availbliity, but still high durability, retrieval latency, and throughput characteristics
      - archive storage is offline; lowest cost to store but highest cost to access
- Azure Files:
  - Accessible via Server Message Block (SMB) or Network File System (NFS) - macOS and Linux only
  - SMB files can be cached on Azure File Sync for acess near where data is being used
  - Benefits:
    - Shared access: SMB and NFS industry standards ensures no need to worry about application compatibility
    - Fully managed: No need to manage hardware or OS
    - Scripting and tooling: PowerShell cmdlets and Azure CLI can be used to create, mount, and manage Azure file shares as part of the administration of
      Azure applications. You can create and manage Azure file shares using Azure portal and Azure Storage Explorer
    - Resiliency: No need to deal with local power outages or network issues
    - Familiar programmability: can access data using system I/O APIs, Azure Storage Client Libraries, or Azure Storage REST API
- Queue Storage:
  - stores large numbers of messages up to 64 KB in size (each)
  - commonly used to create a backlog of work to process asynchronously
  - can be combined with Azure Functions to take an action when a message is recieved
    - ie) submit button on website triggers a message to Queue storage; Azure Function then runs an action once message was received
- Disk Storage: block-level storage volumes managed by Azure for use with Azure VMs; virutalized version of a physical disk

Data Migration Options
- Azure Migrate: 
  - Unified migration platform: single portal to start, run, and track your migration to Azure
  - Range of tools: A range of tools for assessment and migration
    - Independent Software Vendor (ISV)
    - Azure Migrate: Discovery and assessment - Discover and assess on-premises servers running on VMware, Hyper-V, and physical servers in preparation for
      migration
    - Azure Migrate: Server Migration - Migrate VMware VMs, Hyper-V VMs, physical servers, other virtualized servers, and public cloud VMs
    - Data Migration Assistant - stand-alone tool to assess SQL Servers
    - Azure Database Migration Service - Migrate on-premises databases to Azure VMs running SQL Server, Azure SQL Database, or SQL Managed Instances
    - Web app migration assistant - tandalone tool to assess on-premises websites for migration to Azure App Service; use to to migrate .NET and PHP web apps
    - Azure Data Box: move large amounts of offline data
      - phsycial box shipped to datacenter to upload up to 80 terabytes of data
      - use cases:large data with limitied or no network connectivity
        - import: onetime migration, moving media library, migrating VM farm/SQL server, iniitla bulk transfer, periodic update
        - export: disaster recovery, security requirements (government compliance), migrate to another DataCenter (DC) or cloud provider 
  - Assessment and migration: In Azure Migrate hub, assess and migrate your on-premises infrastructure to Azure

File Movement Options
- tools to facilitate moving individual files
- AzCopy: command-line utility to copy blobs/files
  - can upload, download, copy, or synchronize; or move files between clouds
  - synchronization is a one-way process
- Storage Explorer: app that provides GUI to manage files
  - uses AzCopy on backend (no synchronization)
- File Sync: centralize file shares in Azure files and keep flexibility, perfomrance, and compatibility of Windows file server
  - automatically stay bi-directionally synced
  - use protocols to access data locally (SMB, NFS, FTPS)
  - have caches across the world
  - replace a failed server by installing on a new server in same DC
  - configure cloud tiering; replicate heavily accessed files locally and store remaining ones on cloud

## Azure Identity, Access, and Security

Directory Services
- Acive Directory (AD): enables you to sign in, access Microsoft cloud and apps, and cloud apps you develop; can also help maintain on-premise AD
  - For on premise, provides idnentity and access manageement
- When connecting your AD to Azure AD, Microsoft can help protect against suspicious sign-in attempts
- Who uses Azure AD?
  - IT administrators: control acces to resources
  - App developers: add SSO functionality or enable apps to work with user's existing credentials
  - Users: manage identities and password reset
  - Online service subscribers: anybody using Microsoft 365, ect
- What does Azure AD do?
  - Authentication: verify indentity, password reset, multifactor authentication, banned passwords, smart lockout
  - Single Sign-On (SSO): one username/password to access multiple apps
  - Application management: manage cloud/on premise apps; has features like application proxy, SaaS apps, My Apps portal, and SSO
  - Device management: device registration; enables mangement through Microsoft Intune; device-based Conditional Acecss policies (allow access only to known     devices)
- Azure AD Connect: synchronizes users between on premise and cloud
- Azure AD Domain Services: provides managed domain services like domain join, group policy, lightweight directory access protocol (LDAP), and Kerberos/NTLM
  authentication
  - Allows use of directory services (DS) without need to deply, manage, and patch DCs in the cloud
  - provides a smoother lift-and-shift of on-premises resources to Azure
  - How it works:
    - Define a unique namespace for domain name
    - Replica set of DCs are deployed into selected region
    - Azure manages DCs for you (including backups and encryption at rest using Azure Disk Encryption)
  - Pefroms a one way sync from AD to AD DS

Authentication Methods
- Single sign-on (SSO): one credential accesses multiple resources from different providers
  - apps must trust the initial authenticator (sign-on is only as secure as this authenticator)
  - using SSO makes it easier for users to manage IDs and IT to manage users
- Multifactor Authentication (MFA): prompt user for extra form of ID
  - something the user knows, something the user has (text code), something the user is (face-id)
  - can be enabled on cloud with Azure MFA
- Passwordless Authentication:
  - 3 ways azure integrates this with Azure AD:
    - Windows Hello for Business: Biometric and PIN credential for user's PC
      - Public Key Infastructure (PKI) integration and support for SSO
    - Microsoft Authenticator App: turns phone into a storng, passwordless credential
      - get a notification, match number on screen to one on their phone, use biometric or PIN to confirm
    - FIDO2 Security Keys: Fast IDentity Online uses external security key or platform key built into a device (hardware)
      - typically a USB device, but could be Bluetooth or NFC

External Identities
- Azure AD External Identities refers to how users can interact with people, devices, and services outside of their organization
- External users can "bring their own identities" like corproate digital ID or social media, they can use their own credentials to sign in
- External User's ID provider manages their ID, and you manage access to apps with Azure AD or Azure AD B2C
  - Business to business (B2B) collaboration: let external users use their preferred ID to sign-in
    - typically represented in directory as guest users
  - B2B direct connect: establish a two-way mutual trust with another Azure AD organization
    - currently supports Teams shared channels
    - not represented in your directory, but visible in Teams
  - Azure AD business to customer (B2C): publish SaaS or custom-developed apps to customers, using B2C fro identity and access management
  - Can use a combination of above capabilities

Conditional Access
- Tailor access based on identitiy signals (who, where, what device?)
- Empowers user's to be productive wherever while protecting company assets
- More granular control:
  - user may only need MFA if in a specific location or on an unfamiliar device
- Process follows collection of ID signals, decision making process, enforcement of access control

Role-Based Access Control (RBAC)
- Only grant access up to the level needed to complete work
- Azure provides built-in roles which describe common access rules for cloud resources
  - can also define your own rules
  - roles have associated access permissions
  - can add new users to role, or point role to a new resource
- RBAC is applied to a scope (management group, subscription, resource group, or resource)
- Some roles may be: admins, users managing resources, observers (read access only), or automated processes
- RBAC is enforced when a resource is passed through an Azure Resource Manager
  - management service that provides a way to organize and secure cloud resources
  - accessed from cloud portal, sell, Powershell, or CLI
  - does not enforce permissions at app or data level (app security must be handled by the application)
  - uses an allow model:
    - if one assignment grants you read acess and another write acess, you have both

Zero Trust Model
- Security model that protects resources against worst case scenario
  - assumes breach at outset, and verifies each request as if its from an uncontrolled network
- Principles:
  - Verify explicitly: Always authenticate and authorize based on all available data points
  - Use least privilege access: Limit access with Just-In-Time and Just-Enough-Access (JIT/JEA), risk-based adaptive policies, and data protection
  - Assume breach: Minimize blast radius and segment access; verify end-to-end encryption; use analytics to get visibility, drive threat detection, and
    improve defenses
- Philosophy switches from allowing only devices on an assumed secure network, to allowing devices anywhere but mandating authentication every time

Defense-In-Depth
- Objective is to protect information
- Strategy uses a series of mechanisms to slow advance of attack
- Layers:
  - Physical security: protect computing hardware
  - ID and access layer:
    - control access to infrastrucutre and change control
    - use SSO and MFA
    - audit events and changes
  - Perimeter layer: DDoS protection
    - filter large-scale attacks before they affect availability for users
    - user firewalls to identify and alert on malicious attacks
  - Network layer:
    - limit communications between resources
    - deny by default
    - restrict inbound internet access and limit outbound access where appropriate
    - implement secure connectivity to on-premises networks
  - Compute layer: make sure compute resources are secure
    - secures access to VMs
    - implement endpoint protection on devices and keep systems patched and current 
  - Application layer:
    - ensure applications are secure and reduce vulnerabilities
    - store sensitive app secrets in secure medium
    - make security a design requirement
  - Data layer: controls access to business/customer data that needs protecting; regulatory requirements often mandate this
    - attackers are after data thats:
      - stored in a database
      - stored on a disk inside a VM
      - stored in a SaaS app
      - managed through cloud storage

Defender for Cloud
- monitoring tool for security posture management and threat protection
- Azure services are monitored automatically (no deployment needed)
- a Log Analytics agent can be used to gather security data
  - handled directly for azure machines
- for hybrid/multicloud: defender plans are extended with the help of Azure Arc Cloud security posture management (CSPM) features (no need for agents)
- native protections help detect threats across:
  - PaaS services: Azure App Service, Azure SQL, Azure Storage Account, and more
    - can perform cloud anomaly detection on Azure activity logs using native integration wtih Microsoft Defender for Cloud Apps
  - Azure data services: help automatically classify data in Azure SQL; get assessments for vulnerabilities across SQL and storage services + recommendations
  - Networks: limit exposure to brute force attacks
    - reduce access to VM ports using just-in-time VM access (prevent unecessary access)
    - set secure access policies on selected ports, allow source IP address ranges or addresses, and set a time limit
- Hybrid cloud: to extend to on-premise machines, deploy Azure Arc and enable Defender's enhanced security features
- Multi-cloud: 
  - Defender for Cloud's CSPM features: agentless plan to asses other cloud resources
    - can specify assessment according to cloud's security recommendations
    - assessed for compliance with cloud's built-in standards
    - asset inventory page is a multicloud enabled feature
  - Defender for containers: extends threat detection and advanced defenses to other clouds
  - Defener for servers
- 3 Vital roles of cloud defender:
  - Assess:
    - identify and track vulnerabilities in VMs, container registries, and SQL servers
    - defender for servers includes automatic, native integration with Microsoft Defender for Endpoint; allows for Microsoft threat and vulnerability
      management
    - can review and respond to scans from within Defender for Cloud
  - Secure:
    - can set policies to run on management groups, subscriptions, or for a whole tenant
    - defender automatically assesses if new resources are configured to security best practices
      - flag resources not up to standard and provides a prioritized list of recommendations (secure score)
      - help reduce attack surface across resources
    - recs supported by Azure Security Benchmark; set of guidelines for security and compliance best practices based on common frameworks
      - secures configurations standards across resources
    - secure score provides health of security posture, and controls give you a list of things to improve on
  - Defend
    - Security alerts:
      - Can: 
        - describe details of affected resource
        - suggest remediation steps
        - can provide an option to trigger a logic app in response
      - can export alert
      - includes fusion kill-chain analysis
        - helps analyze the nature of attack (where it started and what kind of impact it had)
    - Advanced threat protection:
      - securing management ports of VMs with just-in-time access, adaptive application controls (which apps should and shouldn't run on machines)
