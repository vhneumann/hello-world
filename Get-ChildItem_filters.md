query: powershell exclude files whose path contains string

To exclude files based on a substring within their path in PowerShell, you must use the `Where-Object` cmdlet with the `-notlike` operator, as the native `-Exclude` parameter only supports wildcards against **item names** (basenames) and not full directory paths.

For simple exclusions, pipe `Get-ChildItem` to `Where-Object` and check the `.FullName` or `.DirectoryName` property:

```powershell
Get-ChildItem -Path "C:\Source" -Recurse -File | 
    Where-Object { $_.FullName -notlike "*test*" }
```

For more complex scenarios involving multiple exclusion patterns or specific subdirectories, use an array with `-notmatch` and `Regex::Escape` to handle special characters safely:

```powershell
$excludedPaths = @("*\bin\*", "*\obj\*", "*\Test*")
$regexPattern = '(?<=^|\\)(' + ($excludedPaths.ForEach({ [regex]::Escape($_) }) -join '|') + ')(?=\\|$)'

Get-ChildItem -Path "C:\Source" -Recurse -File | 
    Where-Object { $_.FullName -notmatch $regexPattern }
```

Key considerations include:
*   **Performance**: Filtering with `Where-Object` retrieves all items first, which can be slower than native `-Exclude` for large directories.
*   **Wildcards**: The `-like` operator supports wildcards (`*` and `?`), while `-match` uses regular expressions.
*   **Property Choice**: Use `.FullName` to check the entire path or `.DirectoryName` to check only the parent folder path.