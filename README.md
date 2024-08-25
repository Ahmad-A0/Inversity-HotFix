## Inversity ️‍🔥 Hotfix

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

![image](https://github.com/user-attachments/assets/067d2f3a-b169-482e-b67c-a95574b898ad)
![image](https://github.com/user-attachments/assets/f78f2829-0e30-4038-b908-178b8a68b51c)
![image](https://github.com/user-attachments/assets/6253a0ba-6e08-4e3e-8fa7-5a496ff7df68)


