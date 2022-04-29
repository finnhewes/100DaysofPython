This is a bot that uses Selenium WebDriver to scrape LinkedIn for job postings, given certain parameters (hard-coded url, predetermined, not responsive to user input).
The program finds all jobs matching these parameters and applies to them, if the "EasyApply" option is valid for the given listing. 
The program skips over any applications that request extra input (sometimes desired salary, sometimes years of experience..) 
There are too many case-specific exceptions to catch. If I were to try to catch them all, I might as well apply to these jobs manually to begin with! So I just skip these!
A potential (simple) next evolution of this project would be to save any job listings that look promising, but cannot be "EasyApplied" to, for me to come around later and fill out manually.
Let me know if you use this program to make all the monies!
