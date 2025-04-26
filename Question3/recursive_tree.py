import turtle

def draw_tree(t, branch_length, level, angle_left, angle_right, reduction_factor):
    """
    Recursively draws a tree pattern using turtle graphics.

    Args:
        t (Turtle): The turtle object.
        branch_length (float): The length of the current branch.
        level (int): The current recursion depth.
        angle_left (float): The angle to turn left for the left branch.
        angle_right (float): The angle to turn right for the right branch.
        reduction_factor (float): The factor by which the branch length is reduced
                                   at each level.
    """
    if level > 0:
        t.forward(branch_length)
        t.left(angle_left)
        draw_tree(t, branch_length * reduction_factor, level - 1, angle_left, angle_right, reduction_factor)
        t.right(angle_left + angle_right)
        draw_tree(t, branch_length * reduction_factor, level - 1, angle_left, angle_right, reduction_factor)
        t.left(angle_right)
        t.backward(branch_length)

if __name__ == "__main__":
    print("Let's draw a recursive tree!")
    angle_left = float(input("Enter the left branch angle (in degrees): "))
    angle_right = float(input("Enter the right branch angle (in degrees): "))
    start_length = float(input("Enter the starting branch length (in pixels): "))
    depth = int(input("Enter the recursion depth: "))
    reduction = float(input("Enter the branch length reduction factor (e.g., 0.7 for 70%): "))

    screen = turtle.Screen()
    turtle_pen = turtle.Turtle()
    turtle_pen.speed(0)  # Set speed to fastest
    turtle_pen.left(90)  # Make sure turtle faces straight up

    turtle_pen.penup()
    turtle_pen.goto(0, -screen.window_height() / 2 + 20)  # Start from bottom
    turtle_pen.pendown()

    draw_tree(turtle_pen, start_length, depth, angle_left, angle_right, reduction)

    screen.mainloop()