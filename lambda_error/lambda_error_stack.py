from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
)
from constructs import Construct


class LambdaErrorStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        handler = lambda_.Function(
            self,
            "WidgetHandler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("lambda_handler"),
            handler="handler.main",
            environment={},
        )
