Intro to Cloud
- Cloud computing: delivery of computing services over the internet
  - Includes virtual machines, storage, databases, and networking; also includes things like Internet of Things (IoT), machine learning (ML), and artificial intelligence (AI)
  - All cloud services provide compute power and storage
    - Compute power: how much processing your computer can do (can add or remove computing power as needed)
    - Storage: amount of data a computer can store
      - Cloud provider ensures backups to data, operating system is up to date, system is running 24/7
- Uses internet to deliver services, eleminating physical constraints for IT expansion like constructing additional datacenters
  - Actual hardware and servers are hosted by providers datacenter, reducing upkeep costs for the user

Shared Responsibility Model
- Responsibilities for upkeep are shared between cloud provider and consumer
  - Physical security, power, cooling, and network connectivity are the responsibility of the cloud provider
  - Consumer is responsible for the data and information stored in the cloud and access security
  - Service model will determine responsibility for things like: Operating systems, Network controls, Applications, Identity and infrastructure
    - Infastructure as a Service (IaaS), platform as a service (PaaS), software as a service (IaaS)

Cloud Models
- Define the deployment type of cloud resources
- Private cloud:
  - A cloud used by a single entitiy
  - Much greater control for the company
  - Greater cost and fewer benefits compared to public cloud
  - May be hosted at on-site datacenter, or third party
- Public cloud:
  - Built, controlled, and maintained by a third party
  - Anyone can purchase services and access resources
- Hybrid cloud:
  - Uses both public and private clouds
- Multi-cloud:
  - Use multiple public cloud providers, using different features from each
- Azure Arc: set of technologies that help manage cloud environments
  - Azure VMware Solution lets you run your VMware workloads in Azure with seamless integration and scalability

Consumption-Based Model
- Two types of expenses to consider for IT infastructure models: capital expenditure (CapEx) and operational expenditure (OpEx)
  - CapEx: one-time cost for tangible resources
  - OpEx: money spent on products/services over time (cloud computing)
- Consumption model: you only pay for the IT resources you use, not the electrecity, security, ect associated with maintaing a datacenter
  - No upfront costs
  - No need to purchase and manage costly infrastructure that users might not use to its fullest potential
  - The ability to pay for more resources when they're needed
  - The ability to stop paying for resources that are no longer needed

Benefits of High Availability and Scalability
- High availability: minimal disruptions to services
  - For Azure, availability (up time) is part of the serivce level agreements (SLAs)
- Scalability: ability to adjust resources to meet demand
  - Vertical: increasing resource capability
    - If you need more processing power, can add more CPUs or RAM
  - Horizontal: increasing the number of resources
    - Add additional virutal machines if demand increases

Benefits of Reliability and Predictability
- Reliability: system can recover from failures and continue to function
  - Cloud's decentralized nature allows application to switch to a different region if one region goes down (often automatically)
- Predicatability:
  - Performance: predicts resources needed to deliver solution to cusotmers
    - Autoscaling: can deploy additional resources to meet the demand
    - Load Balancing: helps redirect overload to less stressed areas
    - High Availability
  - Cost: forecasting cost of cloud spend
    - Using cloud analytics, you can optimize resource allocation and predict costs
    - Total Cost of Ownership (TCO) or Pricing Calculator help estimate cloud spend

Bennefits of Security and Governance
- Governance:
  - Set templates ensure resources meet corporate standards and goverment regulatory requirements
  - Can automatically update resources when standards change
  - Cloud-based auditing flags resources out of compliance and provides mitigation strategies
- Security: cloud offers options to entirely control security (IaaS) or have it automatically managed (SaaS)
  - Cloud is well suited to handle distributed denial of service (DDoS) attacks

Benefits of Manageability
- Management of the cloud: managing your cloud resources
  - Automatically scale resources
  - Deply from preconfigured template, removing need for manual configuration
  - Monitor health of resources and automatically replace failed ones
  - Automatic alerts to provide performance in real time
- Management in the cloud: how to manage cloud environemnt
  - Through a web portal, cmd line, APIs, PowerShell

IaaS:
- User is responsible for: operating system installation, configuration, and maintenance; network configuration; database and storage configuration
- Essentially just renting the hardware
- Makes sense for:
  - Lift-and-shift migration: You’re standing up cloud resources similar to your on-prem datacenter, and then simply moving the things running on-prem to         running on the IaaS infrastructure
  - Testing and development: You have established configurations for development and test environments that you need to rapidly replicate. You can stand up       or shut down the different environments rapidly with an IaaS structure, while maintaining complete control

PaaS:
- Cloud provider: also maintains the operating systems, middleware, development tools, and business intelligence services
  - Don't have to worry about licensing or patching for operating systems and databases
- Makes sense for:
  - Development framework: PaaS provides a framework that developers can build upon to develop or customize cloud-based applications. Similar to the way you     create an Excel macro, PaaS lets developers create applications using built-in software components. Cloud features such as scalability, high
    availability, and multi-tenant capability are included, reducing the amount of coding that developers must do
  - Analytics or business intelligence: Tools provided as a service with PaaS allow organizations to analyze and mine their data, finding insights and  
    patterns and predicting outcomes to improve forecasting, product design decisions, investment returns, and other business decisions
    
SaaS:
- User is renting a fully developed application
- Common uses:
  - Email and messaging
  - Business productivity applications
  - Finance and expense tracking

