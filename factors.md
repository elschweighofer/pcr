# 12 Factors

## I. Codebase

One codebase tracked in revision control, many deploys
*Azure Devops Repo, Container Image in Azure Repo and on Docker Hub and can be pulled and run where neeeded*

## II. Dependencies

Explicitly declare and isolate dependencies
*requirements.txt file declares dependencies, isolated from host by (Docker) Container*

## III. Config

Store config in the environment
*.env File contains

+ *MONGO_DB_HOST*
+ *MONGO_DB_PORT*
+ *MONGO_DB_USER*
+ *MONGO_DB_PASSWORD*
+ *LISTEN_PORT*

## IV. Backing services

Treat backing services as attached resources
*see III.*

## V. Build, release, run

Strictly separate build and run stages
*The Container Image is already built by an Azure Devops Pipeline, to run the Image is pulled from the Container Registry / Docker Hub.*

## VI. Processes

Execute the app as one or more stateless processes
*State is only stored in the Mongo DB.*
*For Caching a Backing Service like Redis could be added*

## VII. Port binding

Export services via port binding
*Listen Port can be customized with Environment Variable*

## VIII. Concurrency

Scale out via the process model
*Should be achieved by Containerization?*

## IX. Disposability

Maximize robustness with fast startup and graceful shutdown
*Should be achieved by Containerization?*

## X. Dev/prod parity

Keep development, staging, and production as similar as possible
*Mongo DB can be run locally. The Webserver used 
for the FastAPI Webframework, Uvicorn, can be used 
for development and production as well (unlike e.g. the Flask Development Server where this is not recommended)*

## XI. Logs

Treat logs as event streams
*The Logger is configured to write to sys.stdout, this could then be picked up by a log router like required by 12 Factor.*
*Logging is not complete so far and still needs to be added to most functions*

## XII. Admin processes

Run admin/management tasks as one-off processes
*There are not really management Tasks except for the DB, and exectuing python scripts from the Repl in a container did not really work - so not achieved*
