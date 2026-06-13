# Import asyncio for async/await support
import asyncio
# Import randint to randomly choose next state (0 or 1)
from random import randint

# Coroutine for the starting state
async def start_state():
    # Print that we entered Start State
    print('Start State called\n')
    # Randomly pick 0 or 1 to decide transition
    input_value = randint(0, 1)
    # Non‑blocking sleep for 1 second (simulates work)
    await asyncio.sleep(1)
    # If random value is 0, go to state2; otherwise go to state1
    if input_value == 0:
        result = await state2(input_value)   # await the chosen state
    else:
        result = await state1(input_value)
    # After the chain of states ends, print the accumulated result
    print('Resume of the Transition : \nStart State calling ' + result)

# Coroutine for State 1
async def state1(transition_value):
    # Build a string storing this state's info (with the incoming value)
    output_value = f'State 1 with transition value = {transition_value}\n'
    # Randomly choose next transition (0 → state3, 1 → state2)
    input_value = randint(0, 1)
    await asyncio.sleep(1)          # delay before evaluating
    print('...evaluating...')
    if input_value == 0:
        result = await state3(input_value)   # go to state3
    else:
        result = await state2(input_value)   # go to state2
    # Return this state's string plus the result from the called state
    return output_value + 'State 1 calling %s' % result

# Coroutine for State 2
async def state2(transition_value):
    output_value = f'State 2 with transition value = {transition_value}\n'
    input_value = randint(0, 1)          # 0 → state1, 1 → state3
    await asyncio.sleep(1)
    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)
    return output_value + 'State 2 calling %s' % result

# Coroutine for State 3
async def state3(transition_value):
    output_value = f'State 3 with transition value = {transition_value}\n'
    input_value = randint(0, 1)          # 0 → state1, 1 → end_state
    await asyncio.sleep(1)
    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)   # terminate
    return output_value + 'State 3 calling %s' % result

# Coroutine for the final End State (no further transitions)
async def end_state(transition_value):
    output_value = f'End State with transition value = {transition_value}\n'
    print('...stop computation...')
    return output_value      # just return the final string

# Main block: runs when script is executed directly
if __name__ == '__main__':
    print('Finite State Machine simulation with Asyncio Coroutine')
    # Get the default asyncio event loop
    loop = asyncio.get_event_loop()
    # Run the start_state coroutine until it completes
    loop.run_until_complete(start_state())
    # Close the loop to free resources
    loop.close()


    #output
#     loop = asyncio.get_event_loop()
# Start State called

# ...evaluating...
# ...evaluating...
# ...evaluating...
# ...evaluating...
# ...evaluating...
# ...evaluating...
# ...evaluating...
# ...evaluating...
# ...evaluating...
# ...stop computation...
# Resume of the Transition : 
# Start State calling State 1 with transition value = 1
# State 1 calling State 2 with transition value = 1
# State 2 calling State 1 with transition value = 0
# State 1 calling State 3 with transition value = 0
# State 3 calling State 1 with transition value = 0
# State 1 calling State 2 with transition value = 1
# State 2 calling State 3 with transition value = 1
# State 3 calling State 1 with transition value = 0
# State 1 calling State 3 with transition value = 0
# State 3 calling End State with transition value = 1