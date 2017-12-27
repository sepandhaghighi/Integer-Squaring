# Integer Squaring & Integer Multiplication (by product scanning) Algorithm #

### Sepand Haghighi & Mohammad Abassi

### Cryptographic Engineering Course Seminar At [Sharif University Of Technology](http://www.sharif.ir/ "Sharif University Of Technology") (Winter 2017)
### Instructor : [Dr.Siavash Bayat-Sarmadi](http://sharif.edu/~sbayat/ "http://sharif.edu/~sbayat/")
### Book : Cryptographic Engineering (Serdar S¨ uer Erdem, Tuˇ grul Yanık, and C ¸ etin Kaya Koc)	 
[![Build Status](https://travis-ci.org/sepandhaghighi/Integer-Squaring.svg?branch=master)](https://travis-ci.org/sepandhaghighi/Integer-Squaring)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0f5fc6d4f3e84a06b004a716dc1ece6e)](https://www.codacy.com/app/sepand-haghighi/Integer-Squaring?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/Integer-Squaring&amp;utm_campaign=Badge_Grade)

----------
# Integer Multiplication
							
### Chapter : 5					
				
### Page : 79				


<div align="center">

<img src="files/algorithm2.png">
<p>Algorithm-2 Pseudocode</p>
<img src="files/example3.png">
<p>Algorithm-2 Example</p>

</div> 

```
>>> IntegerMultiplication("1 1","1 1",Base=2)
>>> 1 0 0 1 
```




# Integer Squaring
### Book : Cryptographic Engineering (Serdar S¨ uer Erdem, Tuˇ grul Yanık, and C ¸ etin Kaya Koc)				
				
### Chapter : 5					
				
### Page : 80				


<div align="center">

<img src="files/algorithm3.png">
<p>Algorithm-3 Pseudocode</p>
<img src="files/example1.png">
<p>Algorithm-3 Example</p>
* It seems this algorithm is wrong and `(U,H,L)` should be set to zero after each iteration and add shifted `(U,H,L)` outside of the loop (modified in code)
<img src="files/example2.png">
<p>Algorithm-3(Modified) Example</p>


</div> 

```
>>> IntegerSquaring("1 1",Base=2)
>>> 1 0 0 1 
```