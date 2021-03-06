import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="the_eventbridge_etl",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "the_eventbridge_etl"},
    packages=setuptools.find_packages(where="the_eventbridge_etl"),

    install_requires=[
        "aws-cdk.core==1.31.0",
        "aws-cdk.aws-lambda==1.31.0",
        "aws-cdk.aws-lambda-event-sources==1.31.0",
        "aws-cdk.aws-dynamodb==1.31.0",
        "aws-cdk.aws-s3==1.31.0",
        "aws-cdk.aws-sqs==1.31.0",
        "aws-cdk.aws-s3-notifications==1.31.0",
        "aws-cdk.aws-iam==1.31.0",
        "aws-cdk.aws-ec2==1.31.0",
        "aws-cdk.aws-ecs==1.31.0",
        "aws-cdk.aws-logs==1.31.0",
        "aws-cdk.aws-events==1.31.0",
        "aws-cdk.aws-events-targets==1.31.0"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
