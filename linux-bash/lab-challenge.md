### Core Requirements:

1. **Batch Creation:** Create exactly **25** empty (0 KB) files per execution using the `touch` command.
    
2. **Dynamic Naming Convention:** File names must follow the pattern `<yourName><number>` (e.g., `user1`, `user2`, etc.).
    
3. **Automatic Number Detection (No Hardcoding):** The script must dynamically check the directory for existing files matching the naming pattern, find the highest existing number, and begin the next batch immediately following it. If no files exist, it should start at `1`.
    
4. **Validation:** Test the script and display a long directory listing (`ls -l`) to verify that the correct batch of 25 files was successfully created.