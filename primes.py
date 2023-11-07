import math
import logging
import click


def verify_positive_integer(ctx, param, value):
    if value < 1:
        raise click.BadParameter('positive integer required')
    return value


@click.command()
@click.option(
    '--limit',
    type=click.INT,
    required=True,
    callback=verify_positive_integer,
    help='stop searching for primes when we reach this number')
def main(limit: int):
    """Print all primes up to <limit>"""
    logging.debug(f'looking for primes up to {limit}')

    def _is_prime(n: int):
        return math.factorial(n - 1) % n == n - 1

    for p in filter(_is_prime, range(2, limit + 1)):
        print(p)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()