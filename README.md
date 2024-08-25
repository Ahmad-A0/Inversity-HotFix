## Inversity Hotfix

This was my submission for the Inversity LearnerTakeover Challenge, it's a CTF style challenge where you and a teamate restore broken VMs after an outage/zero-day.

### Deployment

```sh
$ docker compose up
```

### Details

* VueJS is used for the frontend, and makes simple calls through the `/api` route to communicate with the backend
* Flask backend spins up pairs of Challenge and Judge containers
   * The Judge container periodically executes commands inside of the challenge container to check for completion
* sshx.io is used to enable multiplayer terminals on the web for collaboration

