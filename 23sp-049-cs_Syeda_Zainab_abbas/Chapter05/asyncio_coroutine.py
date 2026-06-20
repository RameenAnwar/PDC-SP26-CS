# asyncio_coroutine.py  --  Chapter 5: Coroutines (Finite State Machine)
# Simulates a finite state machine. Each state is a coroutine that randomly
# transitions to another state until it reaches end_state. Shows how coroutines
# call each other with `yield from`.
# RUN COMMAND:  python asyncio_coroutine.py
#
# ----------------------- CODE (commented out) -----------------------
# import asyncio
# import time
# from random import randint
# @asyncio.coroutine
# def start_state():
#     print('Start State called\n')
#     input_value = randint(0, 1)            # random 0 or 1 decides next state
#     time.sleep(1)
#     if input_value == 0:
#         result = yield from state2(input_value)
#     else:
#         result = yield from state1(input_value)
#     print('Resume of the Transition : \nStart State calling ' + result)
# @asyncio.coroutine
# def state1(transition_value):
#     output_value = 'State 1 with transition value = %s\n' % transition_value
#     input_value = randint(0, 1)
#     time.sleep(1)
#     print('...evaluating...')
#     if input_value == 0:
#         result = yield from state3(input_value)
#     else:
#         result = yield from state2(input_value)
#     return output_value + 'State 1 calling %s' % result
# @asyncio.coroutine
# def state2(transition_value):
#     output_value = 'State 2 with transition value = %s\n' % transition_value
#     input_value = randint(0, 1)
#     time.sleep(1)
#     print('...evaluating...')
#     if input_value == 0:
#         result = yield from state1(input_value)
#     else:
#         result = yield from state3(input_value)
#     return output_value + 'State 2 calling %s' % result
# @asyncio.coroutine
# def state3(transition_value):
#     output_value = 'State 3 with transition value = %s\n' % transition_value
#     input_value = randint(0, 1)
#     time.sleep(1)
#     print('...evaluating...')
#     if input_value == 0:
#         result = yield from state1(input_value)
#     else:
#         result = yield from end_state(input_value)
#     return output_value + 'State 3 calling %s' % result
# @asyncio.coroutine
# def end_state(transition_value):
#     output_value = 'End State with transition value = %s\n' % transition_value
#     print('...stop computation...')
#     return output_value
# if __name__ == '__main__':
#     print('Finite State Machine simulation with Asyncio Coroutine')
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(start_state())
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# (random each run - one possible path)
# Finite State Machine simulation with Asyncio Coroutine
# Start State called
#
# ...evaluating...
# ...evaluating...
# ...evaluating...
# ...stop computation...
# Resume of the Transition :
# Start State calling State 1 with transition value = 1
# State 1 calling State 2 with transition value = 0
# State 2 calling State 3 with transition value = 1
# State 3 calling End State with transition value = 1
# --------------------------------------------------------------------
