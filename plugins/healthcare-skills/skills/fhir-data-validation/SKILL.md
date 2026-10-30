---
name: fhir-data-validation
description: Validate HL7 FHIR resources for structure, required fields, codes, and units; normalize and report validation errors. Use when ingesting or emitting FHIR data.
---

# FHIR Data Validation

## When to use
- Validating inbound/outbound FHIR resources (e.g., Patient, Observation, Encounter).
- Ensuring data conforms to organizational profiles and code systems.

## Instructions
1. Validate the resource structure against the expected FHIR version and profile.
2. Check required fields, value types, and permitted code systems/values where applicable.
3. Normalize dates/timezones and units (e.g., UCUM) and ensure consistent coding.
4. Produce a structured error report including JSON pointer paths and human-readable messages.
