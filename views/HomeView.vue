<template>
  <v-container>
    <h1 class="text-h3 mb-5">Daily Team CTF Challenge</h1>
    <v-card class="mb-5">
      <v-card-title>Today's Challenge</v-card-title>
      <v-card-text>
        <p>A new challenge is released every day at midnight UTC. Work with your teammate to solve the issue!</p>
        <v-alert type="info" class="mt-3">
          Challenge #{{ challengeNumber }}: {{ challengeTitle }}
        </v-alert>
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" @click="startChallenge">Start Challenge with Teammate</v-btn>
      </v-card-actions>
    </v-card>

    <v-card class="mb-5">
      <v-card-title>Upcoming Challenges</v-card-title>
      <v-card-text>
        <v-list>
          <v-list-item v-for="challenge in upcomingChallenges" :key="challenge.number">
            <v-list-item-content>
              <v-list-item-title>Challenge #{{ challenge.number }}: {{ challenge.title }}</v-list-item-title>
              <v-list-item-subtitle>Available in {{ challenge.availableIn }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>

    <v-card v-if="showInstructions" class="mb-5">
      <v-card-title>Challenge Instructions</v-card-title>
      <v-card-text>
        <p>You've been connected with a teammate! Work together to solve the challenge.</p>
        <ol>
          <li>SSH into the challenge machine using the credentials below:</li>
          <pre>ssh user@challenge.example.com -p 2222</pre>
          <li>Once connected, navigate to the challenge directory:</li>
          <pre>cd /home/user/challenge</pre>
          <li>Investigate the issue and fix it within the time limit.</li>
          <li>Submit your solution by running the verification script:</li>
          <pre>./verify_solution.sh</pre>
        </ol>
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-title>Leaderboard</v-card-title>
      <v-card-text>
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th>Rank</th>
                <th>Team</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="team in leaderboard" :key="team.rank">
                <td>{{ team.rank }}</td>
                <td>{{ team.name }}</td>
                <td>{{ team.score }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      challengeNumber: 1, // This would be dynamically set based on the current day
      challengeTitle: 'Fix the Broken Web Server',
      showInstructions: false,
      upcomingChallenges: [
        { number: 2, title: 'Secure the Database', availableIn: '1 day' },
        { number: 3, title: 'Optimize the Load Balancer', availableIn: '2 days' },
      ],
      leaderboard: [
        { rank: 1, name: 'Team Alpha', score: 2500 },
        { rank: 2, name: 'Binary Bosses', score: 2300 },
        { rank: 3, name: 'Cyber Ninjas', score: 2100 },
        { rank: 4, name: 'Code Crushers', score: 1900 },
        { rank: 5, name: 'Hack Masters', score: 1700 },
      ],
    }
  },
  methods: {
    startChallenge() {
      // Here you would implement the logic to connect with a teammate
      this.showInstructions = true
      // You might want to add some loading state or notification about teammate matching
    }
  }
}
</script>
