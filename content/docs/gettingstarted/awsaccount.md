{
    "type": "gettingstarted",
    "layout": "type",
    "title": "Creating an Aws Account",
    "linktitle": "gettingstarted", 
    "card_icon": "ti-cloud",
    "card_body": "Create your Aws account and connect it to the Cdev Sdk",
    "weight": "2"
}

# Creating an AWS Account
{{<header_divider>}}

We will follow the [AWS Documentation](https://aws.amazon.com/getting-started/guides/setup-environment/) to make sure that your account is set up correctly.


{{<break 1>}}
## Create Your Account
Follow the steps for the first module for creating your account on [the official AWS documentation](https://aws.amazon.com/getting-started/guides/setup-environment/module-one/).

When following the steps provided by the AWS documentation, you can select a `Personal Account` and the `Basic Support` plan. Although it does require a credit card to create an account, most of the services in AWS have a free tier that provide enough credit to experiment and run small scale projects. 

{{<break 1>}}

## Secure Your Account
Follow the steps for the second module for [creating an admin account and securing the root user of your account](https://aws.amazon.com/getting-started/guides/setup-environment/module-two/).

{{<tool_tip key="tip" summary="Aws Security">}}
Securing your AWS account by using an IAM User as opposed to the Root User is a best practice. Using IAM to manage user and resource access is one of the most important security concerns when using AWS, so it is important to follow these steps and use the created IAM user's credentials with the Cdev Sdk.  
{{</tool_tip>}}


{{<break 1>}}

## Install the CLI
Follow the steps for the third module for [installing the AWS CLI and configuring your credentials](https://aws.amazon.com/getting-started/guides/setup-environment/module-three/).

Once you have created your credentials, Cdev will use the AWS credentials that are configured to deploy resources in the cloud. 

{{<break 1>}}

## Setting up Billing Alarms
We highly recommend taking the time to [create Billing Alerts on your AWS Account](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html). These billing alerts will help you proactively react to situations where something has gone wrong with the resources you have created as opposed to finding out at the end of the billing cycle. 

{{<break 2>}}
