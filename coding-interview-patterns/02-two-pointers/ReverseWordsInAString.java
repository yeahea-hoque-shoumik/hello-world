public class ReverseWordsInPlace {

    public static String reverseWords(String s) {
        StringBuilder sb = new StringBuilder(s);

        // 1️⃣ Remove extra spaces
        removeExtraSpaces(sb);

        // 2️⃣ Reverse entire string
        reverse(sb, 0, sb.length() - 1);

        // 3️⃣ Reverse each word
        int start = 0;
        for (int i = 0; i <= sb.length(); i++) {
            if (i == sb.length() || sb.charAt(i) == ' ') {
                reverse(sb, start, i - 1);
                start = i + 1;
            }
        }

        return sb.toString();
    }

    // Reverse characters between left and right (inclusive)
    private static void reverse(StringBuilder sb, int left, int right) {
        while (left < right) {
            char temp = sb.charAt(left);
            sb.setCharAt(left++, sb.charAt(right));
            sb.setCharAt(right--, temp);
        }
    }

    // Remove leading, trailing, and multiple spaces
    private static void removeExtraSpaces(StringBuilder sb) {
        int i = 0; // write pointer
        int j = 0; // read pointer

        while (j < sb.length()) {
            // skip spaces
            while (j < sb.length() && sb.charAt(j) == ' ') j++;

            // copy word
            while (j < sb.length() && sb.charAt(j) != ' ') {
                sb.setCharAt(i++, sb.charAt(j++));
            }

            // add single space after word
            if (j < sb.length()) {
                sb.setCharAt(i++, ' ');
            }
        }

        // remove trailing space
        if (i > 0 && sb.charAt(i - 1) == ' ') i--;

        sb.setLength(i);
    }
}
