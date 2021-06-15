  Fcomp - short for file/folder comparison
  
  Function receives the path and analyzes the directory it represents in order to find the files/directories of maximum and minimum sizes that the initial folder contains.
  Then returns information about those files.
  
  !!!
  Usage of '\' in paths should be avoided due to it causing the function to fail.
  Either '\\' or '/' should be used instead. Alternatively, the path can be initially inputted as raw, e.g. fcomp(r'C:\Users')
