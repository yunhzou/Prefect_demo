from async_test import  d_elevator
import asyncio

if __name__ == "__main__":
    result= asyncio.run(d_elevator())
    result_true = [result[i].state.result() for i in range(len(result))]
    print(result_true)