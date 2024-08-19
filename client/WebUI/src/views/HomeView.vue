<script setup lang="ts">
import BaseLayoutScrollable from '@/components/layouts/BaseLayoutScrollable.vue';
</script>

<template>
    <BaseLayoutScrollable>
        <v-sheet class="ma-sm pa-sm d-flex flex-column gap-sm">
            <h1>Daily CTF Challenge</h1>
            <v-card class="mb-5" color="background">
                <v-card-title>Today's Challenge</v-card-title>
                <v-card-text>
                    <p>
                        A new challenge is released every day at midnight UTC.
                        Work with your teammate to solve the issue!
                    </p>
                    <v-alert type="info" class="mt-3">
                        Challenge #{{ challengeNumber }}: {{ challengeTitle }}
                    </v-alert>
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" @click="startChallenge"
                        >Start Challenge</v-btn
                    >
                </v-card-actions>
            </v-card>

            <v-card class="mb-5">
                <v-card-title>Upcoming Challenges</v-card-title>
                <v-card-text>
                    <v-list>
                        <v-list-item v-for="challenge in upcomingChallenges" :key="challenge.number">
                            <v-list-item-title>
                                Challenge #{{ challenge.number }}: {{ challenge.title }}
                            </v-list-item-title>
                            <v-list-item-subtitle>
                                Release Date: {{ challenge.releaseDate }}
                            </v-list-item-subtitle>
                        </v-list-item>
                    </v-list>
                </v-card-text>
            </v-card>

            <v-card class="mb-5">
                <v-card-title>Leaderboard</v-card-title>
                <v-card-text>
                    <v-data-table
                        :headers="leaderboardHeaders"
                        :items="leaderboardItems"
                        :items-per-page="5"
                        class="elevation-1"
                    ></v-data-table>
                </v-card-text>
            </v-card>

            <v-card v-if="showInstructions">
                <v-card-title>Challenge Instructions</v-card-title>
                <v-card-text>
                    <p class="mb-4">
                        This is a team challenge! You'll be paired with a teammate to solve the problem together.
                    </p>
                    <ol>
                        <li>
                            SSH into the challenge machine using the credentials
                            below:
                        </li>
                        <pre>ssh user@challenge.example.com -p 2222</pre>
                        <li>
                            Once connected, navigate to the challenge directory:
                        </li>
                        <pre>cd /home/user/challenge</pre>
                        <li>
                            Investigate the issue and fix it within the time
                            limit.
                        </li>
                        <li>
                            Submit your solution by running the verification
                            script:
                        </li>
                        <pre>./verify_solution.sh</pre>
                    </ol>
                </v-card-text>
            </v-card>
        </v-sheet>
    </BaseLayoutScrollable>
</template>

<script lang="ts">
export default {
    name: 'HomeView',
    data() {
        return {
            challengeNumber: 1, // This would be dynamically set based on the current day
            challengeTitle: 'Fix the Broken Web Server',
            showInstructions: false,
            upcomingChallenges: [
                { number: 2, title: 'Secure the Database', releaseDate: '2024-08-20' },
                { number: 3, title: 'Optimize Network Performance', releaseDate: '2024-08-21' },
            ],
            leaderboardHeaders: [
                { text: 'Rank', value: 'rank' },
                { text: 'Team', value: 'team' },
                { text: 'Score', value: 'score' },
                { text: 'Time', value: 'time' },
            ],
            leaderboardItems: [
                { rank: 1, team: 'ByteBusters', score: 1000, time: '1:23:45' },
                { rank: 2, team: 'CodeCrusaders', score: 950, time: '1:25:30' },
                { rank: 3, team: 'HackHeroes', score: 900, time: '1:28:15' },
                { rank: 4, team: 'CyberChampions', score: 850, time: '1:30:00' },
                { rank: 5, team: 'TechTitans', score: 800, time: '1:32:45' },
            ],
        };
    },
    methods: {
        startChallenge() {
            this.showInstructions = true;
            // Here you would typically implement the logic to connect with a teammate
            console.log('Connecting with a teammate...');
        },
    },
};
</script>
