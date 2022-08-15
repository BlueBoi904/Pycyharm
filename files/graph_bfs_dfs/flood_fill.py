"""

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

"""


def floodFill(image, sr: int, sc: int, color: int):
    cur_color = image[sr][sc]

    if cur_color == color:
        return image
    height, width = len(image), len(image[0])

    def dfs(r, c):
        # Check that the square is inbounds "Within the height and width bounds."
        if 0 <= r < height and 0 <= c < width and image[r][c] == cur_color and image[r][c] != color:
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

    dfs(sr, sc)

    return image
