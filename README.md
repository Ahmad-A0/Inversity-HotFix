## Inversity Hotfix

This was my submission for the Inversity LearnerTakeover Challenge, it's a CTF style challenge where you and a teamate restore broken VMs after an outage/zero-day.

### Deployment

```sh
$ docker compose up
```

**Key Components:**

1. **Flask Backend (Python):**
   - Directory: `inversity-provisioner`
   - Responsibilities:
     - Exposes a REST API (`app.py`) for challenge selection and completion.
     - Dynamically provisions Docker containers for each challenge instance.
     - Communicates with challenge containers to verify solutions and manage state.

2. **Vue.js Frontend:**
   - Directory: `inversity-frontend`
   - Responsibilities:
     - Provides a user-friendly interface for browsing and interacting with challenges.
     - Communicates with the Flask backend to initiate challenge provisioning and submit solutions.

3. **Challenge and Judge Containers:**
   - Directories: Individual subdirectories within the project (e.g., `challenge1`, `judge1`, `challenge2`, `judge2`)
   - Each challenge is has it's own challenge and judge images, the judge periodically runs tests inside of the challenge image to check for completion
   - Containers contain:
     - Challenge environment setup (files, dependencies, etc.)
     - Judging logic (`judge.py`) to automatically assess user solutions.

