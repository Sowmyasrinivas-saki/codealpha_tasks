# Task 3 — Secure Coding Review

## Objective
Perform a secure code audit and provide remediation.

## Contents
- `insecure_auth_app.py` — Vulnerable code
- `secure_auth_app.py` — Fixed version
- `CODE_REVIEW.md` — Detailed review notes

## Highlights
- Identified SQL Injection risk
- Removed plaintext password storage
- Applied parameterized queries
- demonstrated hashing

## How To Verify
Run `secure_auth_app.py` to see secure behavior.
