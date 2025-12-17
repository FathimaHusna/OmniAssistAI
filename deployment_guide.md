# Deployment Guide - Render

Follow these steps to deploy OmniAssist AI to Render for free.

## Prerequisites
1.  **GitHub Account**: You need to have your code pushed to a GitHub repository.
2.  **Render Account**: Sign up at [render.com](https://render.com/).

## Step 1: Push Code to GitHub
If you haven't already, push your code to a new GitHub repository:
```bash
git init
git add .
git commit -m "Initial commit"
# Create a new repo on GitHub, then run the commands shown there, e.g.:
# git remote add origin https://github.com/YOUR_USERNAME/omniassist-ai.git
# git push -u origin main
```

## Step 2: Create Web Service on Render
1.  Log in to your Render dashboard.
2.  Click **New +** and select **Web Service**.
3.  Connect your GitHub account and select the `omniassist-ai` repository.
4.  Give it a name (e.g., `omniassist-demo`).
5.  **Runtime**: Select `Docker`.
6.  **Instance Type**: Select `Free`.

## Step 3: Configure Environment Variables
Scroll down to the **Environment Variables** section and add the following keys from your `.env` file:

| Key | Value |
| :--- | :--- |
| `OPENAI_API_KEY` | `sk-...` (Your OpenAI Key) |
| `ELEVENLABS_API_KEY` | `...` (Your ElevenLabs Key) |
| `SMTP_SERVER` | `smtp.gmail.com` |
| `SMTP_PORT` | `587` |
| `SMTP_USERNAME` | `your_email@gmail.com` |
| `SMTP_PASSWORD` | `your_app_password` |

## Step 4: Deploy
1.  Click **Create Web Service**.
2.  Render will start building your Docker image. This may take a few minutes.
3.  Once finished, you will see a green **Live** badge.
4.  Your app will be available at `https://omniassist-demo.onrender.com`.

## Step 5: Verify
1.  Go to the URL provided by Render.
2.  Navigate to `/static/index.html` (e.g., `https://omniassist-demo.onrender.com/static/index.html`).
3.  Test the chat!
