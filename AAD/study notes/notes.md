Flask
- is a web framework
- A web framework is a software library or toolkit that simplifies web application development.
- These frameworks handle crucial aspects such as URL routing, request handling, database integration, templating, and more.
- Other examples: FastAPI, Django, 
  - Flask - popular beginner friendly framework
  - Django - popular full stack framework
  - Fast API - web framework specializing in speed
  
Web Server
- a web server is responsible for receiving incoming HTTP requests from clients (e.g., web browsers) and sending back HTTP responses.
- the intermediary between clients and web applications. Web servers listen on specific network ports, handle low-level communication, and manage the execution of web applications.
- Examples: Nginx, apache
- nginx service start: `brew services start nginx`
- nginix config file: `/opt/homebrew/etc/nginx/nginx.conf` or `/etc/nginx/nginx.conf`



Forward Proxy
- Location: Placed between the client and the internet.
- Function: Hides the client's IP address from the server.
- Use Cases:
  - Anonymity: Protects user privacy by masking their identity.
  - Caching: Stores frequently accessed content locally to improve performance.
  - Filtering: Can block access to certain websites or content.

Reverse Proxy
- Location: Placed between the server and the internet.
- Function: Acts as a load balancer, distributing traffic across multiple servers.
- Use Cases:
  - Load Balancing: Ensures even distribution of requests to prevent server overload.
  - Caching: Stores frequently accessed content to reduce server load.
  
Reverse Proxy: How it works
- The client first sends a request to the load balancer first, then one program redirects the client request to the backend server, this program is known as a reverse proxy. 

NoSQL databases can be categorized into four main types
- Document-Based: These databases store data in document-like structures, such as JSON or BSON.
- Key-Value: These databases store data as key-value pairs, where the key acts as a unique identifier, and the value holds the associated data.
- Column-Family: These databases store data in column families, which are groups of related columns.
- Graph-Based: These databases are designed for storing and querying data that has complex relationships and interconnected structures

System Design vs Software Architecture
- Sofware Architecture is about the what of the system: what components are included, how they are organized, and what principles guide the design.
- System design is about the how of the system: how components interact, how data flows, and how algorithms work.
  - A lot more detailed. 
  - For implementation

Software Architecture: The Blueprint
  - Overall structure: This is the foundation, walls, and roof plan. It defines the basic layout and organization of the house.
  - Style: Is it a modern, traditional, or colonial-style house? This is the overall aesthetic and approach to the design.
  - Materials: Will it be made of brick, wood, or concrete? These are the fundamental materials used in construction.
System Design: The Interior Design
  - Rooms: How many bedrooms, bathrooms, and living spaces are needed?
  - Layout: Where should the kitchen, dining room, and living room be located?
  - Furnishings: What kind of furniture, appliances, and fixtures will be used?
  - Decor: The color scheme, lighting, and overall aesthetic of the interior.
  