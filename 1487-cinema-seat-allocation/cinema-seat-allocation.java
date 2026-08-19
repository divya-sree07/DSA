import java.util.*;

class Solution {
    public int maxNumberOfFamilies(int n, int[][] rseats) {

        List<int[]> seats = new ArrayList<>();

        for (int[] seat : rseats) {
            seats.add(seat);
        }

        seats.add(new int[]{0, 10});
        seats.add(new int[]{n + 1, 1});

        seats.sort((a, b) -> {
            if (a[0] != b[0]) {
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });

        int size = seats.size();
        int count = 0;
        int skipRows, skipCols;

        for (int i = 1; i < size; i++) {

            if (seats.get(i)[0] > seats.get(i - 1)[0]) {

                skipRows = seats.get(i)[0] - seats.get(i - 1)[0] - 1;
                count += 2 * skipRows;

                if (seats.get(i - 1)[1] == 1)
                    count += 2;
                else if (seats.get(i - 1)[1] < 6)
                    count += 1;

                if (seats.get(i)[1] == 10)
                    count += 2;
                else if (seats.get(i)[1] > 5)
                    count += 1;

            } else {

                if (seats.get(i - 1)[1] == 1 && seats.get(i)[1] == 10)
                    count += 2;
                else if (seats.get(i - 1)[1] < 4 && seats.get(i)[1] > 7)
                    count += 1;
                else if (seats.get(i - 1)[1] == 1 && seats.get(i)[1] > 5)
                    count += 1;
                else if (seats.get(i - 1)[1] < 6 && seats.get(i)[1] == 10)
                    count += 1;
            }
        }

        return count;
    }
}