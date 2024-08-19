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

            <v-card v-if="showInstructions">
                <v-card-title>Challenge Instructions</v-card-title>
                <v-card-text>
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
        };
    },
    methods: {
        startChallenge() {
            this.showInstructions = true;
        },
    },
};
</script>
