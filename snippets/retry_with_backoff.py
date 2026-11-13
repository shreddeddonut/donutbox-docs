import time
import random


def retry_with_backoff(func, attempts=5, base_delay=1.0, max_delay=30.0):
    """Retry a callable with exponential backoff and jitter.

    Returns the result of the first successful call, or raises the last
    exception after all attempts are exhausted.
    """
    for attempt in range(1, attempts + 1):
        try:
            return func()
        except Exception as exc:
            if attempt == attempts:
                raise
            delay = min(base_delay * (2 ** (attempt - 1)), max_delay)
            delay *= random.uniform(0.5, 1.5)  # jitter
            print(f"Attempt {attempt} failed ({exc}); retrying in {delay:.1f}s")
            time.sleep(delay)


# Usage
def flaky_call():
    if random.random() < 0.6:
        raise ConnectionError("transient failure")
    return "ok"


print(retry_with_backoff(flaky_call, attempts=5))
