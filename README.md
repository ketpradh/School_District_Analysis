# School District Analysis by Ketaki
Analysis of School District Data for Data Science Class
## Overview of the School District Analysis
The purpose of this analysis is to find any evidence of academic dishonesty for Thomas High school ninth graders scores. This is done by replacing the values of reading and math scores of ninth graders of Thomas High school by NaNs and repeating the school district analysis on the datasets.

## Results 
We can find that the results of the altered dataset and the original dataset was the same.
### District summary changes:
The district summary is similar as before, with slight changes to the passing percentage that dropped by ~0.2%. 
**Before:**
Total Schools	Total Students	Total Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
15	          39,170	        $24,649,428.00	  79.0	             81.9	                 **75.0**	         **85.8**            **65.2**
**After:**
Total Schools	Total Students	Total Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
15	              39,170	    $24,649,428.00	    78.9	            81.9	               **74.8**	         **85.7**	            **64.9**

### School summary changes:
The school summary is similar after changing the data for Thomas High school. However, the overall passing percentage for Thomas High School dropped by ~0.3%.
Before:
      -     School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
- Thomas High School	Charter	1635	      $1,043,130.00	          $638.00	          83.418349	             **83.848930	        93.272171	      97.308869	        90.948012**
After:
      -     School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
- Thomas High School	Charter	1635	      $1,043,130.00	          $638.00	          83.350937	             **83.896082	        93.185690	      97.018739	        90.630324**

### Thomas High School’s performance
Thomas High School remained as the second highest in the top five of the overall ranking, even after replacing the grades. 
However, the overall passing percentage dropped by ~0.3% as below:
Before:
      -     School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
-Thomas High School	Charter	1635	      $1,043,130.00	          $638.00	          83.418349	             **83.848930	        93.272171	      97.308869	        90.948012**
After:
      -     School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
-Thomas High School	Charter	1635	      $1,043,130.00	          $638.00	          83.350937	             **83.896082	        93.185690	      97.018739	        90.630324**


### Math and reading scores by grade
- Math grades remain unchanged, except for Thomas High School 9th grade math scores which are now NaN.
- Reading grades remain unchanged, except for Thomas High School 9th grade reading scores which are now NaN.

### Scores by school spending
Scores by school spending remained same, except in the **$630-644** category where the overall passing percentage reduced than before by ~0.07%.

### Scores by school size
Scores by school size remained same,except for Medium schools where the averages and overall passing percentage dropped by ~0.06%.

### Scores by school type
Scores by school type remained same, except for Charter school overall percentage reduced by ~0.04%.

## Summary
Four major changes in the updated school district analysis after reading and math scores for the ninth grade at Thomas High School have been replaced with NaNs.
- The district summary is similar as before, with slight changes to the passing percentage that dropped by ~0.2%. 
- The school summary is similar after changing the data for Thomas High school. However, the overall passing percentage for Thomas High School dropped by ~0.3%.
- The changes in the other summary categories by grades, spending, size and type are less than 0.1.
- Since no major changes were seen, there seems to be less evidence of academic dishonesty from Thomas High School.
