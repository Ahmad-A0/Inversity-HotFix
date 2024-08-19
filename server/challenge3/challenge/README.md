# *Log4Jelly: Refactor the Logger*

Welcome to Challenge 3! In this challenge, you'll need to identify and fix an unsafe use of the `eval()` function in a logger implementation.

## Objective

Your task is to refactor the logger function in the Node.js application to remove the unsafe `eval()` call while maintaining the logging functionality.

## Instructions

1. Connect to the provided server using SSH.
2. Navigate to the `/app` directory.
3. Locate the `app.js` file and open it in your preferred text editor.
4. Find the `logger` function within the `app.js` file.
5. Identify the unsafe use of `eval()` in the logger implementation.
6. Refactor the logger to remove the `eval()` call while preserving the logging functionality.
7. Ensure that the logger still supports different log levels (info, warn, error) and formats the messages correctly.
8. Test your changes to make sure the logger works as expected without using `eval()`.

## Hints

- The `eval()` function in JavaScript can execute arbitrary code, which is a severe security risk.
- Consider using template literals or string concatenation instead of `eval()`.
- Make sure to preserve the log level functionality in your refactored solution.

## Submission

Once you've successfully refactored the logger:

1. Save your changes to the `app.js` file.
2. Exit the text editor.
3. The system will automatically detect your changes and evaluate them.

Good luck, and code securely!
