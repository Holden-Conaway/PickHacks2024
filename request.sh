#!/bin/bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"password-attempt": "password123"}' \
  http://localhost:5000/verify-password
