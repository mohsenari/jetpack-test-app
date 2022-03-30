# jetpack-test-app
A Python test application built using jetpack-io

## Requirements
* [installing jetpack CLI](https://docs.jetpack.io/guides/quickstart#installing-the-jetpack-cli)
* [Connecting to jetpack trial cluster](https://docs.jetpack.io/guides/quickstart#connecting-to-the-trial-cluster) and creating jetpack account
* AWS account
    * An S3 bucket in AWS
    * AWS Access Key ID and AWS Secret Access Key from IAM

## Steps to run
1. Clone this repo: 
    ```bash
    git clone github.com/mohsenari/jetpack-test-app
    ```

2. Go to the project directory 
    
    ```bash
    cd jetpack-test-app
    ```

2. Update `aws_config.py` by replacing `placeholder` with values you have for `aws_access_key`, `aws_secret_key`, and `bucket_name` from your AWS account.
    ```python
    aws_access_key: "placeholder"
    aws_secret_key: "placeholder"
    bucket_name:    "placeholder"
    ```
3. Deploy your app to jetpack cluster:
    ```bash
    jetpack up
    ```
4. Run the deployed jetroutine following [Jetpack's instructions](https://docs.jetpack.io/guides/jetroutines#step-3-call-your-jetroutine).


