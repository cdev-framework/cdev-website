{
    "type": "examples",
    "layout": "type",
    "title": "Integrate S3 Buckets",
    "linktitle": "bucket",
    "card_icon": "ti-paint-bucket",
    "card_body": "Learn to create a S3 Bucket to store objects",
    "weight": "4"
}


# Working with S3 Buckets
{{<header_divider>}}

The Amazon Simple Storage Service (S3) was one of the first offerings by Aws, and it has become perhaps their most well know service. Cdev makes it easy to quickly create and integrate S3 Buckets into your projects.


{{<break 1>}}
## Create a S3 Bucket
{{<codesnippet `/source_code/s3_examples/single_bucket.py`>}}

You can use the `cdev run bucket` commands to push and pull objects to the bucket from your computer.

```bash
cdev run bucket.cp <local.json> bucket://<bucket-info>
```

{{<tool_tip key="tip" summary="Using the Aws cli">}}
You can also get the deployed name of your bucket with the `cdev output` command and then use the [aws cli tool](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) to transfer files.

```bash
cdev output <component_name>.bucket.demo_bucket.bucket_name
```

```bash
aws s3 cp <local_file> s3://<your-bucket-name>
```
{{</tool_tip>}}

{{<break 1>}}
## Creating Multiple Buckets
{{<codesnippet `/source_code/s3_examples/multiple_buckets.py`>}}

Note that a `Bucket` does not currently have any available settings and configuration, which means we must provide a `nonce` value to distinguish between the two resources. To learn more about how the `nonce` value works within the larger Cdev framework please read our [deep dive on our architecture](/docs/firstprinciples/resources/#components).


{{<break 1>}}
## Use a Serverless function to read objects from a S3 Bucket
{{<codesnippet `/source_code/s3_examples/get_items.py`>}}

The `Bucket` object provides the permissions and output to configure a Serverless function to be able to integrate and read objects. For more in depth information on how to configure Serverless Functions, read our [documentation on the available settings](/docs/examples/functions).

{{<break 1>}}
## Use a Serverless function to write objects to a S3 Bucket
{{<codesnippet `/source_code/s3_examples/write_items.py`>}}

The `Bucket` object provides the permissions and output to configure a Serverless function to be able to integrate and write objects. For more in depth information on how to configure Serverless Functions, read our [documentation on the available settings](/docs/examples/functions). 


{{<break 1>}}
## Use a Serverless function to handle events from a S3 Bucket
{{<codesnippet `/source_code/s3_examples/bucket_event.py`>}}

For more in depth information on how to configure `Serverless Functions`, read our [documentation on the available settings](/docs/examples/functions). 