# Import the tabulate module
from tabulate import tabulate as tb

def print_dataframe(string,df ,numfilas = 5):
    """
    Print the dataframe in a tabular format
    """
    print(string)
    table = tb(
        df.head(numfilas),
        headers='keys',
        tablefmt="fancy_grid",
        numalign="right",
        stralign="center",
        colalign=("center", "center", "right")
    )
    print(table)