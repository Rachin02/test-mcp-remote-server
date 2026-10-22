from fastmcp import FastMCP


mcp = FastMCP("substruction and return name")

@mcp.tool()
def subs(a:int , b: int) -> int :
    ''' Given two number. substruct b from a'''
    return b - a

@mcp.tool()
def return_name()->str:
    '''Return the owner name'''
    return "Rachin"

if __name__ == "__main__":
    mcp.run(transport="http", host = "0.0.0.0", port = 8000)
