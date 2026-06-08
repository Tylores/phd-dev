# R Brown,1 J Liu,1 B Nordman1



# J Kolln,2 T Slay,2 S Widergren2



# D Narang3



# T Bohn4



# Y Xue5

January 2024



# 1 Lawrence Berkeley National Laboratory



# 2 Pacific Northwest National Laboratory



# 3 National Renewable Energy Laboratory



# 4 Argonne National Laboratory



# 5 Oak Ridge National Laboratory

Abstract This document provides guidance to develop and align communications interfaces that are highly interoperable and adhere to a set of energy services interface (ESI) principles. It can be applied in the context of information and communications technology interface standards and implementation profiles that enable the integration of a facility with responsive distributed energy resources (DER) into an electric power system consistent with the fundamental ESI principles. In this context, a DER facility may consist of a single DER with a communicating controller or may be as complex as a microgrid campus with several buildings and many DERs. This document is not a technical interface standard, but the process and guidance described can be used to check that existing, augmented, or new interface standards meet the interoperability requirements of the ESI concept. In this way, this guide for the ESI specification can support future advancements in developing and aligning interoperability standards and implementation profiles. The intended audience for this document is DER integration practitioners and ecosystem groups that are in the business of developing and implementing communications interfaces for DER integration. It is intended that these groups apply the information and processes in this document to develop communications standards and implementation profiles that are consistent with fundamental ESI principles.

Acknowledgments This research was supported by the Grid Modernization Initiative of the Department of Energy (DOE) as part of its Grid Modernization Laboratory Consortium, a strategic partnership between DOE and the national laboratories to bring together leading experts, technologies, and resources to collaborate on the goal of modernizing the nation’s grid. The authors acknowledge the help and guidance received from DOE manager, Christopher Irwin, in developing the plan for this document and encouraging outreach to relevant stakeholders. Thanks also go to review and input.

Definitions, Acronyms and Abbreviations DER distributed energy resource DOE Department of Energy ESI Energy Services Interface GMLC Grid Modernization Laboratory Consortium GWAC GridWise Architecture Council IMM interoperability maturity model NIST National Institute of Standards and Technology UUID universally unique identifier For the purposes of this document, the following terms and definitions apply. Defined terms are italicized throughout the document to indicate to the reader that alternate definitions may exist elsewhere, but this document uses the term as defined in this section.

coordination architecture Concepts, principles, and structure applied to the way components of an integrated system coordinate their operation to achieve individual and systemic goals. DER Responsive generation, storage, or load connected at the distribution system level. Responsive means that the operation of the assets can be managed to provide one or more grid-DER service. DER facility A facility that includes one or more DER. DER interconnection agreement An agreement between the electric utility and customer establishing all terms and conditions associated with operating DER in parallel with the utility’s electric power system. (NARUC n.d.) ESI A bi-directional, service-oriented, logical interface that supports the secure communication of information between entities inside and outside of a DER facility boundary to facilitate various energy interactions between electrical loads, storage, and generation (i.e., grid-DER services) within customer facilities and external entities. (Widergren et al. 2018) facility management function A function that manages the operation of the electrical devices and systems at a facility. In the ESI concept, this function interacts with outside parties through the ESI. grid architecture The application of system architecture, network theory, and control theory to the electric power grid. A grid architecture is the highest-level description of the complete grid. It is a key tool to help understand and define the many complex interactions that exist in present and future grids. grid-DER service A service provided between a DER facility and an external interacting party (usually a grid entity) as coordinated by ESI interactions. The service definition describes what is expected to be provided but does not specify how it is accomplished or how it will be used. Managing the quantity of energy consumption over a period of time is an example of a grid-DER service.

grid-DER service agreement An agreement that specifies what a service provider will accomplish for a service requester, how it will be measured, and any compensation (monetary or otherwise) from the service requester for performing that service. layered decomposition (Chiang et al. 2007) Hierarchical disaggregation of a complex problem into a series of simpler subproblems with clear and relatively simple interfaces between them. These subproblems are solved locally with interaction links to larger coordination domains and internally with subdomains. implementation profile A set of chosen classes, subsets, options, parameters, and functions of one or more base standards that are necessary to achieve interoperability for a specified implementation. service-oriented interface Service-oriented interactions describe what is expected (a service) rather than how the performance expectation or objective is met. This style of software interface facilitates the communication of services in terms of performance expectations to other system components (service requesters) by service provider components through a network communication protocol. Its principles are independent of vendors and technologies.

Contents Abstract................................ ................................ ................................ ................................ ....... ii Acknowledgments ................................ ................................ ................................ ...................... iii Definitions, Acronyms and Abbreviations ................................ ................................ ................... iv Contents ................................ ................................ ................................ ................................ .... vi Figures ................................ ................................ ................................ ................................ ...... vii Tables ................................ ................................ ................................ ................................ ....... vii



# 1.0 Introduction to the ESI Concept ................................ ................................ ........................... 1



# 2.0 ESI Guiding Principles ................................ ................................ ................................ ......... 4



# 3.0 Grid-DER Services ................................ ................................ ................................ .............. 6



# 4.0 Lifecycle Phases ................................ ................................ ................................ .................. 7



# 5.0 Example Grid-DER Service Interactions ................................ ................................ .............. 9

## 5.1 Energy Service ................................ ................................ ................................ ............. 9

## 5.2 Reserve Service ................................ ................................ ................................ ......... 10



# 6.0 Dimensions of Interoperability for an ESI ................................ ................................ ........... 11

## 6.1 Interoperability Categories................................ ................................ .......................... 11

## 6.2 Interoperability Maturity Levels ................................ ................................ ................... 12



# 7.0 ESI Review Process ................................ ................................ ................................ .......... 14

## 7.1 Recommended ESI Review Process ................................ ................................ .......... 14



# 8.0 References ................................ ................................ ................................ ........................ 17

Appendix A : Example Criteria Review ................................ ................................ .................... A.1

Figures Figure 1: The DER facility contains one or more DER controlled by a Facility Management Function. ................................ ................................ ....................... 2 Figure 2: The ESI and adjacent entities. ................................ ................................ ............ 3 Figure 3: NIST Smart Grid Conceptual Model and subdomains (Gopstein et al. 2021). ..... 3 Figure 4: The lifecycle phases and the types of interactions that might occur. ................... 7 Figure 5: Example energy service interaction. ................................ ................................ ... 9 Figure 6: Example reserve service interaction. ................................ ................................ 10 Figure 7: Through leadership, engage subject matter experts through the leadership of the industry consortium. ................................ ................................ .................... 14 Figure 8: Document the existing methods and data objects and evaluate compliance with ESI principles. ................................ ................................ ........................... 15 Figure 9: Perform the interoperability maturity assessment and provide feedback. .......... 16

Tables Table 1: IMM Maturity Levels ................................ ................................ ......................... 13 Table A-1: Example application of IMM Criterion 8 during registration phase. .................. A.2 Table A-2: Example application of IMM Criteria during scheduling phase. ....................... A.4



# 1.0 Introduction to the ESI Concept

An energy services interface (ESI) is defined as “a bi-directional, service-oriented, logical interface that supports the secure communication of information between entities inside and outside of a customer boundary to facilitate various energy interactions between electrical loads, storage, and generation within customer facilities and external entities.” (Widergren et al. 2018) By being service-oriented, ESI interactions describe what is expected (a service) rather than how the performance expectation or objective is met. An ESI follows a grid-DER service agreement that defines the nature of the service exchange and the terms of the agreement between the service requestor and service provider.1 The grid architecture concept of layered decomposition organizes the approach to solving a complex problem into a series of subproblems with clear interfaces between them. One of these subproblems, in the context of the ESI, is a distributed energy resource (DER) facility, shown in Figure 1. The grid-DER service provider is in charge of managing the DER facility, which could contain one or more DERs. The concept of the DER facility abstracts and hides the type and number of DER being managed at the facility and focuses on the interaction between a grid- DER service requester and the DER facility. The facility management function is responsible for the coordination of the asset(s) on behalf of the owner(s). Note that the ownership of meters is complicated, and they may be under the purview of one or both interacting parties. Metering and submetering should be described in the grid-DER service agreement.



# 1 This document follows a previous work titled Energy Services Interface: Requirements Document, which

outlined the elements needed in an ESI specification. The ESI services requirements document described the desired contents of the ESI specification and provided examples of the type of material that needs to be included in it, including examples of situations (or illustrative applications) for using an ESI to coordinate DER flexibility for grid operations.

Figure 1: The DER facility contains one or more DER controlled by a Facility Management Function. In practical application, the ESI concept is a logical framework that can be used to implement a layered decomposition-coordination approach to managing electricity.2 An implementation that adheres to the ESI concept requires alignment by the parties on either side of the logical interface. That includes the communication methods and supporting technology, the understanding of the information exchanged, and the allowable sequence of business processes that each side needs to support. This alignment is captured in agreements on standards, the implementation profiles explaining the options being used in these standards, security policies, business agreements, and supporting methods and tools, such as resource discovery directories. A graphic representation of this ESI concept with parties on either side of the interface is shown in Figure 2.



# 2 This follows, for example, the OpenADR notion that an entity can be both a virtual end node (VEN) and

a virtual top node (VTN) depending on the entity’s relationship to other entities.

Figure 2: The ESI and adjacent entities. The ESI concept can be implemented in any type of coordination architecture. The National Institute of Standards and Technology (NIST) Smart Grid Conceptual Model offers an example of a coordination architecture. At the highest level of abstraction, the NIST Smart Grid Conceptual Model depicts communications and electrical flows between domains. The domains are termed, generation including DER, distribution, customer, markets, transmission, service provider, and operations. Each domain contains actors with specific roles that perform various services and interact with actors in other domains via the communication flows depicted. The conceptual domain can be mapped to subdomains. This concept is shown in Figure 3.

Figure 3: NIST Smart Grid Conceptual Model and subdomains (Gopstein et al. 2021).



# 2.0 ESI Guiding Principles

These are guiding principles that an ESI and its implementation will adhere to.

• The ESI is a service-oriented interface used to communicate what is needed when, not how to deliver it. The service is defined in a performance-based manner. This approach embraces a distributed, decision-making, scalable coordination framework that emphasizes modularity and loose coupling of the interacting system components. Grid-DER services are described in terms of performance requirements, not device-specific functionalities. This approach also facilitates automated (machine-to-machine) communications to support business practices (to provide grid-DER Services). Boundaries of responsibility on either side of the ESI are clear and protected by the style of the interface.

• The ESI maintains privacy: This core principle is intended to satisfy information privacy concerns. The facility management function does not expose the identity or other details of individual DER but rather only the collective capability of all DER in the DER facility for a particular grid-DER service.

• The ESI is device agnostic: This avoids specialized interfaces based on DER technology type and streamlines adaptation to new DER technology or advances in existing technology. The ESI is universally applicable to all types of DER if they qualify to address the agreed- upon grid-DER service. To assess whether an implementation meets these principles, consider the following statements:



# 1 The grid-DER service agreement supported by the ESI is clearly articulated.

a. The service describes the performance expectations of the service provider (what is to be delivered and when).

b. The service description does not describe how the service is performed.

c. The service description does not specify device types or technologies.

d. The service describes how the service provider’s performance to deliver the service will be measured and evaluated.



# 2 The service provider is responsible for managing the collective capability of all the DER

facility resources.

a. The service provider manages the DER facility resources to meet the service performance expectations.

b. The service requestor does not directly or remotely control the DER facility resources but uses the ESI to coordinate with the service provider.

c. The service provider does not expose the identity or details of specific devices or technologies except as may be needed to demonstrate qualifications to perform the service.

The following general assumptions related to the implementation of the ESI are intended to provide context to interface and standards developers:

• In practice, an ESI may be implemented using one or more communications protocols and an implementation profile.3

• An ESI is implemented in the context of supporting grid-DER service agreements.

• A DER facility management function exists that manages one or more DERs at the facility.

• A DER interconnection agreement is in place (e.g., between the DER owner and the local utility).

• Grid-DER service performance requirements are defined in a grid-DER service agreement. The service provider may need to demonstrate the ability to meet these performance requirements in order to qualify to provide a grid-DER service.

Transactive Services, among others. An example of an implementation profile is the common smart inverter profile.



# 3.0 Grid-DER Services

A previous document (Kolln et al. 2023) in this series described common grid-DER services. They are described in terms of attributes and performance characteristics that would be prescribed in a grid-DER service agreement between a service requestor and provider. In this way, specific operational objectives of the interacting parties become unnecessary to disclose (e.g., the energy service could be used to satisfy multiple operational objectives). A summary description of these is below:

• Energy Service: A scheduled production or consumption of energy at the DER facility point of interconnection (an electrical location) over a specified period.

• Reserve Service: A specified capacity to produce or consume energy at the DER facility point of interconnection (an electrical location) when called upon within a specified period and duration.

• Regulation Service: Continuously provide an increase or decrease in real power at the DER facility point of interconnection (an electrical location) over a specified scheduled period against a predefined real-power basepoint following a service requestor’s signal.

• Voltage Management Service: Provides voltage support (raise or lower) to manage voltage at the DER facility point of interconnection (an electrical location) within a voltage range over a specified period. (Typically used to correct excursions outside voltage limits.)

• Frequency Response Service: The DER facility responds to a change in system frequency nearly instantaneously by consuming or producing active power over a specified period. (Typically used to moderate a sudden frequency change. Requires local detection of frequency deviation and autonomous response.)

• Blackstart Service: The DER facility can start or remain available without grid electrical supply to energize part of the electrical power system over a specified period. (The service is part of a restoration plan used following blackouts.)



# 4.0 Lifecycle Phases

An ESI implementation needs to support the types of interactions and information exchanged between the service requester and service provider to support a grid-DER service agreement. The lifecycle phases shown in Figure 4 provide a template for the types of interactions that will be evaluated when developing an ESI specification. The interactions will depend on the terms and conditions of the associated service agreement. The lifecycle phases aim to cover the full interaction experience of the DER facility with one or more external parties. To address this broad scope, a grid-DER service agreement will likely need to reference multiple technical standards, appropriate implementation profiles of those standards, as well as specific business and regulatory policy requirements. To the extent that aspects of these agreements can be codified in broadly accepted terms and conditions, interoperability will be easier to achieve, and adoption speed enhanced. Interface standards for DER coordination today tend to focus on the Schedule and Operate Phases. Register and Qualify, Measure and Verify, and Settle Phases are seen as more specialized for each deployment. An ESI specification needs to cover all the phases for a deployment to achieve interoperability, recognizing that agreements in one phase may become assumed requirements in another.

Figure 4: The lifecycle phases and the types of interactions that might occur. These interactions could be realized through multiple information and communication technology interfaces. For example, a web-based interface could be used for registration interactions. Another interface could be used between a utility DER management system and a facility management system to address schedule and operations interactions. And a separate meter interface for energy interval data exchange could be used to verify that the performance

expectation was met. However, interoperability will require coordination throughout these lifecycle interactions. For example, to schedule and operate, the DER facility identifier established during the registration lifecycle phase may be necessary. Evaluation of an ESI implementation to support the lifecycle phases will also need to be performed to demonstrate that these interactions also comply with the ESI principles. The major interactions cover the following phases: Register and Qualify This phase establishes that the service requester and the service provider are entering into a grid-DER service agreement. That entails the identification credentials of the parties involved and an understanding of the requirements and capabilities required to provide the service and how it will be compensated. Features like resource discovery could occur during this phase to aid in determining things like location and performance characteristics. Registration associates the DER facility with an agreement to provide the service. Qualification may include proof of the performance capability of the DER facility. Agreement terms and conditions cover the way performance and settlement are determined, which will be necessary in other life-cycle categories. Schedule This interaction takes place prior to grid-DER services being provided. The grid-DER service agreement may explain how the grid-DER service requester provides advance notice of the schedule for the period of service to allow the grid-DER service provider to plan for delivery of the service. This phase may also include the negotiation of pricing or incentives, depending on the terms of the agreement. The facility management function could require assets to prepare to provide a change in energy based on an operational signal, as in the case of a reserve service activation request. Operate This interaction occurs in real time as the grid-DER service is being delivered. The grid-DER service provider actively controls its resource(s) to fulfill the performance expectation. Communications are based on the terms of the agreement but could include the status of the service or an initiation signal. The agreement may or may not require ongoing communication between the interacting parties during this phase. Measure and Verify This phase measures the performance of the service provider to meet the terms of the agreement. The type and frequency of measurement information exchanged should be of a nature and quality that determine the performance of the service provider. The collected information is used to adjudicate settlement in the next phase. Settle This phase uses the information collected during the measure and verify phase to reconcile the performance of the service provider. This interaction occurs after the completion of the service period. For example, settlement may be performed periodically at the end of the billing period. The result of this interaction is a settlement between the grid-DER service requester and service provider for the period of performance.



# 5.0 Example Grid-DER Service Interactions

The ESI is implemented in the context of a grid-DER service agreement. The service agreement defines business and interoperability requirements as well as the responsibilities of participants across all lifecycle phases. For the purposes of this document, the focus is on two grid-DER services: 1) energy service and 2) reserve service.

## 5.1 Energy Service

An energy service contracts with a DER facility to consume or produce energy over a scheduled period. The diagram shown in Figure 5 describes an example of energy-service interaction. In this example of grid-DER service interaction, the energy service agreement is established during the Register and Qualify Phase. The DER facility’s performance capabilities and the agreement’s service requirements determine if the DER facility is qualified to participate.4 This example assumes the grid service provider has prequalified and registered for energy service.

Figure 5: Example energy service interaction. The ESI must enable the interactions required, consistent with the service agreement, throughout all of the lifecycle phases. The simple energy service interaction above includes a confirmation that the schedule is agreed to by both parties. The operation of the DER facility does not require communication in the example, but this could be a requirement of the grid-DER service agreement if so defined. Measurement by both parties occurs in this example so that they both understand that the service was performed as agreed upon to support the settlement process.

## 5.2 Reserve Service

A reserve grid-DER service agreement establishes the availability of energy for production or consumption to be called upon during a performance period. The service requestor may call upon the DER facility to produce or consume this energy by signaling the service provider to operate based on the reserved amount of energy. The period of operation can occur within the time scheduled in the reserve service agreement. The grid-DER service agreement, as with all grid-DER services, will specify the qualification and performance requirements, including any penalties for non-performance. This example presumes the facility has already qualified to provide the reserve service.

Figure 6: Example reserve service interaction.



# 4 The DER interconnection agreement defines codified DER behavior as may be referenced by the grid-

DER service agreement. The service agreement should not be in conflict with the interconnection agreement and the behaviors defined in it.



# 6.0 Dimensions of Interoperability for an ESI

This ESI interface specification guide uses the Interoperability Maturity Model (IMM) (Knight, 2020 ) as a basis. The IMM covers dimensions of interoperability to support interoperation across an ESI. The IMM is a tool that was developed to measure the effectiveness of methods for integrating the information and communications technology aspects of intelligent devices and systems to coordinate their operation with the rest of the electric power system. The tool focuses on the evaluation of the interfaces used to integrate these devices and systems. Application of the tool identifies gaps between current and desired levels of interoperability. In an earlier Grid Modernization Laboratory Consortium (GMLC) project, the IMM was adapted to assess interoperability issues and identify potential basic application profiles in the communications interface standard, IEEE Std 2030.5, and its application using implementation profiles. This guide draws on the IMM to develop the ESI interoperability criteria described in this document. These criteria can be used to assess the interoperability maturity of an ESI for any standard (or multiple standards) as required to meet the ESI principles throughout the lifecycle phases.

## 6.1 Interoperability Categories

The interoperability criteria are organized into the following categories. Configuration and Evolution Criteria 1 through 8 address topics related to vocabularies, concepts, and definitions across multiple communities and companies. This means that all resources need to be unambiguously defined to avoid clashes between identification systems. This is important over time as new automation components enter and leave the system because resource identification is essential for discovery and configuration. This also provides the ability to upgrade (evolve) over time and to scale without affecting interoperability. Security and Safety Criteria 9 through 12 are concerned with aligning security policies and maintaining a balance between minimizing exposure to threats while supporting performance and usability. This includes the capability to troubleshoot and debug problems that span disparate system boundaries while placing the integrity and safe operation of the electric power system above the health of any single automation component. The criteria include planning for fault conditions that disrupt normal operations. Operation and Performance Criteria 13 through 16 focus on synchronicity and quality of service, as well as other operational concerns. Operational concerns include maintaining integrity and consistency, error handling, and ensuring that distributed processes can meet expected interaction performance and reliability requirements.

Organizational Criteria 17 and 18 represent the pragmatic aspects of interoperability. They explore the policy and business drivers for interactions. The need for businesses (or business automation components) to accomplish tasks by exchanging and acting on information is what drives interoperability. This requires agreement on the business process interaction that is expected to take place across an interface. Informational Criteria 19, 20, and 21 emphasize the semantic aspects of interoperability. They focus on what information is being exchanged and its meaning. This includes both human and device- recognizable information. Semantic modeling describes the terms for and relationships between entities in the information model that are pertinent to conducting business across the ESI. This includes any constraints that may exist on the relationships between entities. Technical Criteria 22 and 23 address the message syntax, format, delivery, confirmation or validation, and integrity of the information exchange. They focus on how information is represented within a message exchange and on the communication medium. This pertains to the physical, digital exchange of data between systems, including its encoding and messaging protocols, to ensure the reliable delivery of the message contents. Community In addition, several criteria are focused on the culture qualities and collaboration activities that are required to help drive interoperability process improvements and that reflect stakeholder community maturity with respect to interoperability. These additional criteria include the participation of organizations in efforts to improve interoperability in general as the interface evolves over time. Note that in the initial stages of ESI development, a formal community of stakeholders may not exist; therefore, other criteria will be emphasized.

## 6.2 Interoperability Maturity Levels

The IMM was developed as a way to measure interoperability. Using the IMM, one can gauge the relative sophistication of various maturity characteristics to show areas for improvement in interoperability. As noted in the GMLC ESI Requirements Document (Brown et al. 2023), “Measuring interoperability maturity involves looking for evidence that practices (capability or integration) are being performed and, where they are not (to the level desired), creating a list of gaps so that the steps to reach the desired level of interoperability can be planned. Assessing the degree of interoperability maturity requires evaluating the IMM criteria and grading them on a level of 1 to 5. The levels of maturity used in the IMM are based on the Capability Maturity Model Integration (CMMI) (CMII Institute 2010). This is the same system that was used by The GridWise Architecture Council (GWAC) for the Beta release of the IMM, which described the a roadmap exercise to identify where there may be gaps in that standard (IEEE 2019).(see Table 1) (GWAC 2011).

Table 1: IMM Maturity Levels

“By looking at each level of maturity for each category the evaluation team can make an informed decision about which categories are of most interest for advancing interoperability improvements. Within the categories there are the individual criteria, each of which also has five levels of descriptions that can be used to assess interoperability maturity in a more specific manner. The IMM thus cannot only help identify important aspects of interoperability but can also be used to identify gaps between current and desired maturity.” (Brown et al. 2023)



# 7.0 ESI Review Process

The ESI review process is intended to aid in the development and alignment of an ESI- compliant specification, including the evaluation of related standards and implementation profiles. The ESI should meet the interoperability requirements for the interface throughout the lifecycle phases without violating any of the ESI principles. The following methodology guides the process that should be followed for any standard thought to support grid-DER service interactions. The ESI specification can additionally be applied to converge ESI-centric standards and implementation profiles, which otherwise may have divergent aspects based on the various ad hoc implementations.

## 7.1 Recommended ESI Review Process

The IMM gap analysis and the ESI specification activities must include participants who are very familiar with the standard, implementation profile, or protocol. The leadership of standards development organizations, alliances, or other industry consortia should be engaged to help identify those subject matter experts that might be champions of the ESI and its associated concepts. This group of experts will discuss the ESI concepts to identify the level of interest. This process may need to be repeated until key champions of the work are identified. These champions will drive the process forward and further engage a team of experts in their respective organizations. The team will then identify the grid service or services, for example, use cases, as the basis for the ESI development process and the timeline for the project. A simplified flow diagram of this activity is shown in Figure 7.

Figure 7: Through leadership, engage subject matter experts through the leadership of the industry consortium. This guide recommends an initial assessment of the protocols, interface standards, and implementation profiles that apply to the ESI implementation to ensure that the methods and data objects used do not violate the ESI principles. This process is described in Figure 8 Once existing methods and data objects used for information exchange are identified and documented, starting with those needed for the first lifecycle phase and first service, the reviewers will determine if there are any violations of the ESI principles. If there are no violations, the method becomes a candidate for the ESI specification. If the principles are violated, an alternative method should be identified. If no alternative exists, a gap has been identified and should be recorded for a gap analysis. The review continues with the methods and objects necessary for the following lifecycle phase until the ESI compliance evaluation has been completed for the methods and data objects required for all lifecycle phases. This process is then repeated for each service that the ESI implementation will support.

Figure 8: Document the existing methods and data objects and evaluate compliance with ESI principles. Interface specifications, including the ESI, need to meet interoperability maturity requirements at the levels desired by the stakeholders. Mature standards and profiles offer predictable results, reduce the time and costs associated with custom or ad hoc integration, and are more likely to be widely adopted. This assessment is the next step in developing an ESI specification and can be performed using the IMM criteria, which are included in the Appendix B spreadsheet. The IMM provides a methodology to determine if there are gaps in interoperability that should be addressed to increase the maturity of the implementation. The evaluation process is described by the flow diagram in Figure 9.

Figure 9: Perform the interoperability maturity assessment and provide feedback. The process starts with the first criterion and the first lifecycle phase. For each criterion and lifecycle phase, the team of reviewers will ask the question, “How do we apply the protocol to meet this criterion during this lifecycle phase?”. If the criterion is met with a satisfactory level of maturity (shown in Table 1) through all the applicable lifecycle phases, move on to evaluate the next criterion. If it has not reached an appropriate level and a gap is identified, it should be recorded for the gap analysis. Once the criterion has been addressed for all lifecycle phases, the team can move on to evaluate the standard, profile, or protocol against the next interoperability criterion until the assessment has been completed for all IMM criteria. Any gaps that have been identified can be used to improve a standard, advance interoperability, and provide a path to a highly interoperable, ESI compliant implementation profile. The gap analysis should also include recommendations for potential changes to the standard, profile, or protocol and be submitted to the appropriate standards development organization, alliance, or industry consortium. Appendix A provides examples of two criteria assessments performed on



# 8.0 References

Brown, R., A. Khandekar, J. Liu, B. Nordman, J. Kolln, S. Widergren, D. Narang, T. Bohn, and



# Y Xue. 2023. Energy Services Interface: Requirements Document. LBNL- 2001549, Lawrence

Berkeley National Laboratory, Berkeley, CA. Chiang, M., S. H. Low, A. R. Calderbank, and J. C. Doyle, “Layering as Optimization Decomposition: A Mathematical Theory of Network Architectures,” in Proceedings of the IEEE, vol. 95, no. 1, pp. 255-312, Jan. 2007, doi: 10.1109/JPROC.2006.887322. CMMI Institute. 2010. Capability Maturity Model Integration. ISACA. Schaumburg, IL. Accessed June 2021 at, http://cmmiinstitute.com/. Gopstein, A., C. Nguyen, C. O'Fallon, N. Hastings, and D. A. Wollman. 2021. NIST Framework and Roadmap for Smart Grid Interoperability Standards, Release 4.0. NIST Framework and Roadmap for Smart Grid Interoperability Standards, Release 4.0, Special Publication (NIST SP), National Institute of Standards and Technology, Gaithersburg, MD, [online], https://doi.org/10.6028/NIST.SP.1108r4, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=931882 GWAC (GridWise® Architecture Council). 2011. Smart Grid Interoperability Maturity Model, Beta Version. Accessed June 2021 at https://gridwiseac.org/pdfs/imm/sg_imm_beta_final_12_01_2011.pdf. IEEE. 2018. “Smart Energy Profile Application Protocol.” Section 10.9. IEEE Standards Association, IEEE 2030.5-2018. https://standards.ieee.org/ieee/2030.5/5897/. IEEE. 2019. “Interoperability Maturity Roadmap--IEEE Std 2030.5.” In Interoperability Maturity Roadmap--IEEE Std 2030.5, vol., no., pp.1-51, 31 Oct. 2019. https://ieeexplore.ieee.org/document/8894220. Knight, M. R., S. E. Widergren, A. Khandekar, J. J. Kolln, D. Narang, and B. Nordman. 2020. Interoperability Maturity Model: A Qualitative and Quantitative Approach for Measuring. PNNL- 29683, Pacific Northwest National Laboratory, Richland, WA. https://gridmod.labworks.org/index.php/resources/interoperability-maturity-model. Kolln, J. T., J. Liu, S. E. Widergren, and R. Brown. 2023. Common Grid Services: Terms and Definitions Report. PNNL-34483, Pacific Northwest National Laboratory, Richland, WA. https://doi.org/10.2172/1992370. NARUC. N.d. Augmented from “An Introduction to Interconnection Policy in the United States,” NARUC. Accessed June 2021 at https://pubs.naruc.org/pub.cfm?id=5375FAA8-2354-D714- 51DB-01C5769A4007. Widergren, S. E., M. R. Knight, R. B. Melton, D. Narang, M. Martin, B. Nordman, A. Khandekar, and K. S. Hardy. 2018. Interoperability Strategic Vision: A GMLC White Paper. PNNL-27320. Pacific Northwest National Laboratory, Richland, WA. doi:10.2172/1430426, accessed February 2022 at, https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-27320.pdf.

A.1 Appendix A: Example Criteria Review The result of applying interoperability maturity model (IMM) criteria to the lifecycle phases is intended to answer the question: What are the requirements for energy services interface (ESI) compliance for each criterion? An example of applying Criterion 8 is illustrated in Table A-1.1 Explanations and descriptions of the types of information that apply and process descriptions are in red. For this example, the grid-DER service is the energy service described in Section 5.1 and shown in Figure 5. This will be used for each of the following lifecycles in this example review. For this example, the DER facility is managed by the grid service provider, and the grid service requestor interfaces directly through IEEE Std 2030.5-2018. It is worth noting that these services are provided to fulfill a grid service agreement, which includes details such as performance requirements, qualifications, and the settlement process. Lifecycles:



# 1 Register and Qualify

The grid service requestor and grid service provider must be registered with each other.

• Universally unique identifier (UUID) for grid service provider

• UUID for grid service requestor

• billing information o account number o service number o service location

• power properties o rated power o operating modes

• performance requirement:

• performance qualification:

• settlement:



# 2 Schedule

The following information must be discoverable to support energy scheduling:

• unique contract identifier

• schedule received

• start time: 5:00 p.m.

• end time: 7:00 p.m.

• energy requirement: 10 MW o energy requirements and qualifications will be negotiated differently depending on the specification used. In this example, we will assume the grid service request used the registered power information to reset the energy qualification value.

• energy qualification: 1 MW

• service terms: $134



# 1 Note: this feeds IMM Criterion 7 as well.

A.2



# 3 Operate

• verify schedule is active

• report schedule started



# 4 Measure and Verify

• performance measurement



# 5 Settle

• schedule complete

• performance report Table A-1: Example application of IMM Criterion 8 during registration phase. Criterion 8 (Configuration and Evolution) Resource discovery methods for assisting with identification and integration between actors (such as access to information like owner, DER type, location, etc.) are supported. Applied to the ESI: The ESI specification has resource discovery methods to support integration of interacting actors. Implementation Assumptions: Details not included in the specification that are relevant to criterion Review Process: Orient the reviewers to understand what specific information should be focused on Review resource discovery and announcement capabilities of the standard. For example, support for registries or access lists that methods can post to and query so that things can be discovered. Those things could be grid-DER service programs or a participant that is signing up for a program, etc. Example Questions: Example questions to inform the intent of the criterion Q8.1 - Does the specification support the initial handshake. Q8.2 - Do the resource discovery methods support mutual understanding of device capability? Q8.3 - Are resource discovery methods supporting configuration documented? Notes: Highlight information that may be context specific to guide reviewers The discovery service will allow actors to associate information such as tariff or program, location, performance characteristics/requirements, and participation availability. Location in document: Iterate the review process for each grid service and respective lifecycle to identify how the criterion is satisfied. IEEE Std 2030.5 Pg 59 Section 7 notes that “IEEE 2030.5 specifies DNS-based methods for service discovery, resource discovery, and hostname to IP address resolution.” Section 4.4 outlines the schema used for communication. (reference schema for all communication fields)

Section 6.9 Registration outlines in-band and out-of-band process

Section 7 Discovery outlines the process for out-of-band and in-band DER Facilities

Section C.1-7 demonstrates the registration and discovery process which supports link traversal .

Section 10.10 Distributed Energy Resource function set

A.3 All Registration Client Server Self Device::LFDI (Section 8.4) All Registration Client Server EndDevice::LFDI (Section 8.5) All Registration Client Server CustomerAccount::customerAccount CustomerAgreement::serviceAccount CustomerAgreement::serviceLocation (Section 10.7) All Registration Client Server DERCapability::rtgMaxVA DERCapability::modesSupported (Section 10.10) All Schedule Server Client DERProgram::mRID DERControl::mRID All Schedule Server Client DERControlResponse All Schedule Server Client DERControl::interval::start All Schedule Server Client DERControl::interval::duration All Schedule Server Client DERControl::DERControlBase::opModFixedW All Operate Server Client DERControl::EventStatus::currentStatus All Operate Client Server DERControlResponse::status All Operate Client Server DERControlResponse::status The next example, seen in Table A-2, shows applying IMM Criterion 7 to the same example lifecycles described above. Lifecycles:



# 1 Register and Qualify

The grid service requestor and grid service provider must be registered with each other.

• UUID for grid service provider

• UUID for grid service requestor

• billing information o account number o service number



# 2 Schedule

The following information must be discoverable to support energy scheduling:

• unique contract identifier



# 3 Operate

• N/A



# 4 Measure and Verify

• N/A



# 5 Settle

• N/A

A.4 Table A-2: Example application of IMM Criteria during scheduling phase. Criterion 7 (Configuration and Evolution) Unambiguous resource identification and its management is described. Applied to the ESI: The ESI specification supports unambiguous identification of resources DER facilities referenced across the interface. Implementation Assumptions: Details not included in the specification that are relevant to criterion An identity management feature exists for creating and maintaining uniqueness. Archives for reconciliation and audit have lasting unique references to reliably process history. Review Process: Orient the reviewers to understand what specific information should be focused on Review of standard where resource identification applies and how uniqueness is managed. Example Questions: Example questions to inform the intent of the criterion Q7.1 - Do all DER facilities have a unique way to be identified? Q7.2 - Is there a system in place to manage allocation of identifiers? Q7.3 - Is there documentation describing the identifiers and how they are assigned, managed, and retired? Notes: Highlight information that may be context specific to guide reviewers Implementation profiles may already specify how unique resource identifiers are created and managed including roles for third party management, such as a consortium or government agency. Information exchange requires unambiguous references to the interacting parties and associated information. Location in document: Iterate the review process for each grid service and respective lifecycle to identify how the criterion is satisfied Section 3.1 Definitions defines a Smart Energy Root certificate authority, but the actual organization is not defined.

Unique numbers are enforced using Internet Assigned Numbers Authority (IANA), Private Enterprise Number (PEN) Request, IETF RFC 3986, Uniform Resource Identifier (URI): Generic Syntax

Section 6.3.4 Long-form device identifier

Section (6.11.3) Manufacturing PKI

Section (B.2.3.4) Types package outlines the master resource ID type Service Lifecycle From To Method/Data Object All All Client Server SelfDevice::LFDI (Section 8.4) All All Client Server EndDevice::LFDI (Section 8.5) All All Server Client CustomerAccount::customerAccount CustomerAgreement::serviceAccount CustomerAgreement::serviceLocation (Section 10.7) All All Server Client DERProgram::mRID DERControl::mRID

A.5 Applying this methodology, IMM criteria can be used to assess and develop an implementation profile to meet the ESI principles throughout the associated lifecycle phases. Results will be used to identify gaps in specific communications standards that are commonly used in energy exchange transactions and provide recommendations to standards development organizations for increasing maturity and support for ESI. The first example, shown in Table A-2, highlights an ESI rule violation. The DERCapability::type element, described in the schema, is a violation of the device-agnostic principle of the ESI and should be set to “0” to indicate not applicable or unknown. The DERControl:deviceCategory, outlined in Section 10.10 (see Table A-1, under Location in document), should have all bits set to indicate all device category types or ignored to ensure device-agnostic participation. Another potential solution would be to use an alternative control function set. The Flow Reservation makes it device agnostic.