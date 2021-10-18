def area_of_a_triangle(length_1, length_2, length_3):
    """This function returns the area of a triangle when 
    all the length of the triangles are passed into it."""
    half_perimeter = (length_1 + length_2 + length_3) / 2
    area = (half_perimeter * (half_perimeter-length_1) * (half_perimeter-length_2) * (half_perimeter-length_3)) ** 0.5
    return area


print(area_of_a_triangle(3, 4, 5))


