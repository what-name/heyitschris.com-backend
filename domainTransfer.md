# Transferring a domain between AWS accounts
This is the process of how to transfer a domain that was bought on AWS to a different account.
The destination account can be part of your Organization or completely seperate. **Use at your own risk.**
For more information, see the [AWS Docs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-between-aws-accounts.html) and [my Medium post](https://medium.com/@chris_nagy/the-journey-of-transferring-a-domain-to-another-aws-account-10293f901cb5).

## Important note
Transferring domains between AWS accounts has only been possible recently. If you're like me and don't update your CLI tools regularly, make sure you have the `aws` CLI tool at version `2.0.9` or above, since the required commands are only available in that version and upwards.

## Process - Domain
1. Initialize the domain transfer from the source account with the following CLI command:
`aws route53domains transfer-domain-to-another-aws-account --domain-name mydomain.com --account-id <dest-acc-id>`
2. This command outputs a password in this form: `PASSWORD: [T3;$3Bk\":g$4-`. Note down this password.
3. Execute the following command where the `--profile dest-acc-profile` refers to the destination account
`aws --profile dest-acc-profile route53domains accept-domain-transfer-from-another-aws-account --cli-input-json file://acceptDomainTransfer.json`
The `acceptDomainTransfer.json` file should have the following content:
```json
{
   "DomainName": "mydomain.com",
   "Password": "[T3;$3Bk\":g$4-"
}
```
4. This command outputs a `job-id` which does not need to be noted. If you receive no errors after `3.`, the domain transfer was successful.

## Process - Hosted Zone
There is no easy way of transferring a hosted zone to another AWS account. There needs to be a new Hosted Zone created on the new account and deployed utilizing the Blue/Green approach if no downtime is required. In my experience, it is rather difficult to have a complete setup on two accounts and be able to just switch the DNS records of the domain name. I created the new Hosted Zone within the CloudFormation template but it is currently not allowed to have two CloudFront distributions with the same CNAME aliases. Therefore the original CloudFront distribution's alias was removed (it works without an alias as well) and added to the new distribution just before the DNS change.
