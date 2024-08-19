<script setup lang="ts">
import BaseLayoutScrollable from '@/components/layouts/BaseLayoutScrollable.vue';
import { ref } from 'vue';

const challenges = ref([
    { number: 1, title: 'Fix the Broken Web Server' },
    { number: 2, title: 'Secure the File System' },
    { number: 3, title: 'Debug the Logging System' }
]);
const selectedChallenge = ref(challenges.value[0]);
const showInstructions = ref(false);
const showStartDialog = ref(false);
const sessionLink = ref('');

const upcomingChallenges = [
    {
        number: 4,
        title: 'Secure the Database',
        releaseDate: '2024-08-20',
    },
    {
        number: 5,
        title: 'Optimize Network Performance',
        releaseDate: '2024-08-21',
    },
];

const leaderboardHeaders = [
    { text: 'Rank', value: 'rank' },
    { text: 'Team', value: 'team' },
    { text: 'Score', value: 'score' },
    { text: 'Time', value: 'time' },
];

const leaderboardItems = [
    { rank: 1, team: 'ByteBusters', score: 1000, time: '1:23:45' },
    { rank: 2, team: 'CodeCrusaders', score: 950, time: '1:25:30' },
    { rank: 3, team: 'HackHeroes', score: 900, time: '1:28:15' },
    { rank: 4, team: 'CyberChampions', score: 850, time: '1:30:00' },
    { rank: 5, team: 'TechTitans', score: 800, time: '1:32:45' },
];

const uuidv4 = () => {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(
        /[xy]/g,
        function (c) {
            var r = (Math.random() * 16) | 0,
                v = c == 'x' ? r : (r & 0x3) | 0x8;
            return v.toString(16);
        }
    );
};

const confirmStartChallenge = async () => {
    showStartDialog.value = false;
    try {
        const response = await fetch('/api/start-challenge', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                challenge: `challenge${selectedChallenge.value.number}`,
                instance_id: uuidv4(),
            }),
        });
        const data = await response.json();
        if (data.link) {
            sessionLink.value = data.link;
            showInstructions.value = true;
        } else {
            console.error('No session link received');
        }
    } catch (error) {
        console.error('Error starting challenge:', error);
    }
};
</script>

<template>
    <BaseLayoutScrollable>
        <v-sheet class="ma-sm pa-sm d-flex flex-column gap-sm">
            <h1>Daily CTF Challenge</h1>
            <v-card class="mb-5" color="background">
                <v-card-title>Available Challenges</v-card-title>
                <v-card-text>
                    <p>
                        Select a challenge and work with your teammate to solve the issue!
                    </p>
                    <v-select
                        v-model="selectedChallenge"
                        :items="challenges"
                        item-title="title"
                        item-value="number"
                        return-object
                        label="Select a challenge"
                    ></v-select>
                    <v-alert type="info" class="mt-3">
                        Challenge #{{ selectedChallenge.number }}: {{ selectedChallenge.title }}
                    </v-alert>
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" @click="showStartDialog = true"
                        >Start Challenge with Teammate</v-btn
                    >
                </v-card-actions>
            </v-card>

            <v-dialog v-model="showStartDialog" max-width="500px">
                <v-card>
                    <v-card-title>Start Challenge?</v-card-title>
                    <v-card-text>
                        Warning: Clicking 'Start' will begin the challenge and
                        start the timer. Are you sure you want to proceed?
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="blue darken-1"
                            text
                            @click="showStartDialog = false"
                            >Cancel</v-btn
                        >
                        <v-btn
                            color="blue darken-1"
                            text
                            @click="confirmStartChallenge"
                            >Start</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <v-card v-if="showInstructions">
                <v-card-title>Challenge Instructions</v-card-title>
                <v-card-text>
                    <p class="mb-4">
                        This is a team challenge! You'll be paired with a
                        teammate to solve the problem together.
                    </p>
                    <ol>
                        <li>
                            Click the link below to start your challenge
                            session:
                        </li>
                        <v-btn
                            color="primary"
                            :href="sessionLink"
                            target="_blank"
                            class="mb-4"
                        >
                            Start Challenge Session
                        </v-btn>
                        <li>
                            Once connected, follow the instructions provided in
                            the challenge environment.
                        </li>
                        <li>
                            Investigate the issue and fix it within the time
                            limit.
                        </li>
                        <li>
                            Submit your solution using the method specified in
                            the challenge environment.
                        </li>
                    </ol>
                </v-card-text>
            </v-card>

            <v-card class="mb-5">
                <v-card-title>Upcoming Challenges</v-card-title>
                <v-card-text>
                    <v-list>
                        <v-list-item
                            v-for="challenge in upcomingChallenges"
                            :key="challenge.number"
                        >
                            <v-list-item-title>
                                Challenge #{{ challenge.number }}:
                                {{ challenge.title }}
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
        </v-sheet>
    </BaseLayoutScrollable>
</template>
