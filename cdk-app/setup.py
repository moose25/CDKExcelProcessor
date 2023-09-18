from aws_cdk import core

from excel_data_processor.excel_data_processor_stack import ExcelDataProcessorStack

app = core.App()
ExcelDataProcessorStack(app, "ExcelDataProcessorStack")
app.synth()
