![Deploy CF Template](https://github.com/what-name/heyitschris.com-backend/workflows/Deploy%20CF%20Template/badge.svg)

# Info
*Disclaimer: this project is actively being worked on.*
This repository holds the backend code for my personal website [heyitschris.com](https://heyitschris.com).
It includes:
- Service Control Policy for the designated sub-account
- IAM Policy for the `github-ci/cd` user
- A GitHub actions workflow that updates the backend infrastructure
- A CloudFormation template that describes the backend infrastructure
- (Upcoming) Unit tests for the VisitorCounter Lambda function
- Misc. objects that were required to transfer the project from my main, to a designated AWS Organizations sub-account.

## Misc.
Originally the domain was bought by an AWS account that turned into an Organizations master account. Therefore the domain needed to be transferred to the designated sub-account. For the process, see the `domainTransfer.md` file.

## CI/CD Workflow
As described in the `.github/workflows/main.yml`, there is a GitHub Actions workflow that is triggered every time there is a push to the master branch. This workflow updates the CloudFormation stack currently deployed. The AWS access keys are stored as GitHub Secrets and the user has very limited access to resources. (Upcoming) The CloudFormation template assumes a role to deploy the needed resources. This project is utilizing GitHub Actions over an AWS CodePipeline for cost savings and is a better alternative based on the scope of this project.