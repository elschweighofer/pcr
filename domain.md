

## Middleware to process PCR Runs

The app this microservice would be a Part of needs to be able to gather Results from PCR Thermocyclers or attached PCs, validate the output (e.g. quality controls etc.) and pass on the necessary Information to a larger Laboratory Information System (LIS). Ideally with no Patient Data stored, only identifying samples and querying necessary Information about Samples from the LIS. This Service does persistent Create, Read, Update and Delete for Results. Other Services could be a frontend, analyser administration / monitoring, Parsing and creating HL7 / FHIR, Kit Configuration etc.