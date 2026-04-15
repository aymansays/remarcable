# remarcable - CI/CD Demo using Github Actions

## What this does

On every push to `main`, this pipeline gets triggered and executes stages:

1. Run test case on web app
2. Build docker image
3. Push to AWS ECR
4. Deploy to AWS ECS

Due to the nature of the demo, steps 3 & 4 are only placeholders.

## View Action

To view an example of an action in action, navigate to the [Actions](https://github.com/aymansays/remarcable/actions) tab and click to any of the latest workflow builds.

## Tech Stack

- Python 3.14, with Flask
- Docker
- Github Actions
- AWS ECS
- AWS ECR

## AI Assitance

ChatGPT was used to help with identifying requirements from the assignment. The AI tool helped draft a structure for the architecture document and this codebase. All words in the document, the code in this repo, and the architecture diagram were reviewed and typed. Other tools were used such as Stack Overflow, tech blogs, documentation (AWS, Github Actions, etc.) to create the final submission.
