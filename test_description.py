from prefect import flow, serve
from prefect_aws.s3 import S3Bucket
import random
s3_bucket_block = S3Bucket.load("s3")

@flow(persist_result=True, 
      result_storage=s3_bucket_block)
def addition(a:int=1, b:int=2) -> int:
    """Adds two numbers together

    Args:
        a (int): first num
        b (int): second num

    Returns:
        int: a+b

    Examples:
    >>> addition(2+3)
    5
    """
    return a + b


@flow(persist_result=True,
        result_storage=s3_bucket_block)
def generatenumber(random_seed:int) -> int:
    """
    Generates a random number

    Args:
        random_seed (int): seed for the random number generator

    Returns:
        int: a random number

    Examples:
    >>> generate_number(1)
    5
    """
    return random.randint(1, 100)
    


if __name__=="__main__":
    addition_deploy = addition.to_deployment(name="addition")
    generate_number_deploy = generatenumber.to_deployment(name="generatenumber")
    serve(addition_deploy, generate_number_deploy)