import asyncio
import time # Note: The time library is imported but not used because we use asyncio.sleep instead.
from random import randint

# The starting point of our Finite State Machine (FSM).
async def start_state():
    print('Start State called\n')
    # Generate a random number: either 0 or 1.
    input_value = randint(0, 1)

    # Pause for 1 second to simulate doing some work.
    await asyncio.sleep(1)

    # Decide which state to go to next based on the random number.
    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)

    # Print the final history of all the state changes.
    print('Resume of the Transition : \nStart State calling ' + result)


# First intermediate state.
async def state1(transition_value):
    output_value = f'State 1 with transition value = {transition_value}\n'
    # Generate a new random number for the next decision.
    input_value = randint(0, 1)

    # Pause for 1 second.
    await asyncio.sleep(1)
    print('...evaluating...')

    # Decide the next state.
    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)

    # Return the current state info plus the result of the next states.
    return output_value + f'State 1 calling {result}'


# Second intermediate state.
async def state2(transition_value):
    output_value = f'State 2 with transition value = {transition_value}\n'
    # Generate a new random number for the next decision.
    input_value = randint(0, 1)

    # Pause for 1 second.
    await asyncio.sleep(1)
    print('...evaluating...')

    # Decide the next state.
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)

    # Return the current state info plus the result of the next states.
    return output_value + f'State 2 calling {result}'


# Third intermediate state.
async def state3(transition_value):
    output_value = f'State 3 with transition value = {transition_value}\n'
    # Generate a new random number for the next decision.
    input_value = randint(0, 1)

    # Pause for 1 second.
    await asyncio.sleep(1)
    print('...evaluating...')

    # Decide the next state: This is the only state that can jump to the End State.
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)

    # Return the current state info plus the result of the next states.
    return output_value + f'State 3 calling {result}'


# The final destination state.
async def end_state(transition_value):
    output_value = f'End State with transition value = {transition_value}\n'
    print('...stop computation...')
    
    # Just return the final message, no more states are called after this.
    return output_value


# Check if the user is running this file directly.
if __name__ == '__main__':
    print('Finite State Machine simulation with Asyncio Coroutine')
    # Start the event loop manager and run the starting state.
    asyncio.run(start_state())