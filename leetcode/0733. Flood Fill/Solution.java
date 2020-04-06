// https://leetcode.com/problems/flood-fill/

class Solution {
    public int[][] floodFillRec(int[][] image, int sr, int sc, int newColor, int targetColor) {
        if (image[sr][sc] == newColor)
            return image;

        if (image[sr][sc] != targetColor)
            return image;

        image[sr][sc] = newColor;

        if (sr + 1 < image.length)
            floodFillRec(image, sr + 1, sc, newColor, targetColor);
        if (sc + 1 < image[0].length)
            floodFillRec(image, sr, sc + 1, newColor, targetColor);
        if (sr - 1 >= 0)
            floodFillRec(image, sr - 1, sc, newColor, targetColor);
        if (sc - 1 >= 0)
            floodFillRec(image, sr, sc - 1, newColor, targetColor);

        return image;
    }

    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        return floodFillRec(image, sr, sc, newColor, image[sr][sc]);
    }
}
