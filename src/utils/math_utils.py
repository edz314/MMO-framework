# src/utils/math_utils.py

import math
import random

def clamp(value, min_value, max_value):
    """
    Clamp a value between a minimum and maximum value.
    :param value: The value to clamp.
    :param min_value: The minimum value.
    :param max_value: The maximum value.
    :return: The clamped value.
    """
    return max(min_value, min(value, max_value))

def lerp(start, end, t):
    """
    Linearly interpolate between two values.
    :param start: The start value.
    :param end: The end value.
    :param t: The interpolation factor (0.0 to 1.0).
    :return: The interpolated value.
    """
    return start + t * (end - start)

def distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in 2D space.
    :param point1: A tuple representing the first point (x1, y1).
    :param point2: A tuple representing the second point (x2, y2).
    :return: The Euclidean distance between the two points.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def random_range(min_value, max_value):
    """
    Generate a random float within a given range.
    :param min_value: The minimum value of the range.
    :param max_value: The maximum value of the range.
    :return: A random float within the range [min_value, max_value].
    """
    return random.uniform(min_value, max_value)

def normalize(value, min_value, max_value):
    """
    Normalize a value to a range between 0 and 1 based on the given min and max values.
    :param value: The value to normalize.
    :param min_value: The minimum possible value.
    :param max_value: The maximum possible value.
    :return: The normalized value between 0 and 1.
    """
    return (value - min_value) / (max_value - min_value)

def dot_product(vec1, vec2):
    """
    Calculate the dot product of two vectors.
    :param vec1: The first vector as a tuple (x1, y1).
    :param vec2: The second vector as a tuple (x2, y2).
    :return: The dot product of the two vectors.
    """
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]

