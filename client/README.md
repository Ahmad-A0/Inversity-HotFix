# Inversity Front-End Template

Welcome to the Inversity Front-End Template! This repository is your starting point for building apps using the Inversity layout, theme and styling. It includes all the essential files and configurations to get your front-end layout up and running smoothly.

![image](https://github.com/user-attachments/assets/7cd49137-31fe-45dd-8b29-1c424fa1bf09)

## Layout of the /WebUI Directory

The `/WebUI` directory is where all the magic happens. Here's a quick tour of what's inside:

- **/public**: Home to the images and favicon used on the site. Think of it as the visual assets folder.
- **/src**: The source code that powers the site. This is where you'll spend most of your time.
  - **/components**: Building blocks used within top-level views.
  - **/plugins**: Custom code to enhance libraries (like Vuetify) used by the front-end.
  - **/router**: Controls the internal routing of the site with Vue Router.
  - **/styles**: Top-level SCSS styles used across the site. Time to get creative with your designs!
  - **/views**: The top-level views that make up the pages of the site.
- **App.vue**: The main component that renders everything else, including the current router view. It's the beating heart of your app.

## Getting Started

Ready to jump in? The default view, which is currently linked to the router's '/' path, is at `/WebUI/src/views/HomeView.vue`. Have a go at tinkering with this file and try updating the contents. Thanks to the docker-compose setup, you can see your changes in real time every time you save files within the `/src` dir. Experiment and watch your ideas come to life!

## Running the Project

To get the project up and running with Docker Compose, follow these simple steps:

1. **Make sure Docker and Docker Compose are installed** on your machine. You can grab them from [Docker's official website](https://www.docker.com/).

2. **Build and start the containers (run this at the top level of the repo)**:
    ```sh
    docker-compose up --build
    ```

3. **Access the application**: 
    Fire up your web browser and head over to `http://localhost:5173` to see your site in action.

## Stopping the Project

When you're ready to take a break or shut things down, use this command to stop the running containers:

```sh
docker-compose down
