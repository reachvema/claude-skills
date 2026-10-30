---
name: phi-deidentification
description: Detect and redact or mask protected health information (PHI) per organizational de-identification policy. Use for data sharing, analytics, and testing datasets.
---

# PHI De-identification

## When to use
- Preparing datasets for analytics, research, or lower environments.
- Removing or masking direct and quasi-identifiers from free text or structured data.

## Instructions
1. Identify direct identifiers (e.g., names, addresses, phone numbers, MRNs) and redact or tokenize them.
2. Mask quasi-identifiers using approved techniques (e.g., generalization, suppression) per policy.
3. Preserve data utility where possible by retaining non-identifying attributes and categorical mappings.
4. Produce an audit log of transformations applied and fields affected.
