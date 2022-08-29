from cdev.aws.s3 import Bucket



myBucket = Bucket("demo_bucket")

myBucket2 = Bucket("demo_bucket2", nonce="123")