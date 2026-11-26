# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers):
    # Outline (write your plan here first):
    #   1. Define a helper coroutine that returns n * 2.
    #   2. Create one coroutine per number.
    #   3. Run them all concurrently with asyncio.gather.
    #   4. Return the results as a list (gather keeps the original order).
    async def double(n):
        return n * 2

    coroutines = [double(n) for n in numbers]
    results = await asyncio.gather(*coroutines)
    return list(results)




async def fastest(jobs):
    # Outline:
    #   1. Define a helper coroutine that sleeps for the delay, then returns the label.
    #   2. Create one coroutine per (label, delay) pair.
    #   3. Iterate with asyncio.as_completed, which yields them in finishing order.
    #   4. Return the result of the first one to finish.
    async def job(label, delay):
        await asyncio.sleep(delay)
        return label

    coroutines = [job(label, delay) for label, delay in jobs]
    for c in asyncio.as_completed(coroutines):
        return await c


def echo_once(host, port, message):
    # Outline:
    #   1. Create a TCP socket with a with-block so it closes automatically.
    #   2. Connect to (host, port).
    #   3. Send the message encoded as bytes.
    #   4. Receive the reply and return it decoded as a string.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        data = s.recv(1024)
    return data.decode()


def main():
    # Optional scratch space - try the async parts here, e.g.:
    print(asyncio.run(gather_doubled([1, 2, 3, 4])))
    print(asyncio.run(fastest([("A", 0.06), ("B", 0.02), ("C", 0.04)])))


if __name__ == "__main__":
    main()