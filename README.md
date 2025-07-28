# Simple-arithmetic-expression-evaluator
A simple python based math expression evaluator, takes human input and turns it into an appropriate arithmetic expression to be safely evaluated by eval() function in python <br><br>
## Usage

You may import the `Simple_evaluator.py` in your python code and use these functions. <br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;project_folder<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ├── main.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Simple_evaluator.py<br>
                 

`from Simple_evaluator import eval_exp`<br>
`from Simple_evaluator import valid_exp`

### `valid_exp(x)` - Returns the arithmatic expression in appropriate form<br>
where x is any string like `log(5)(95)20/3.142(27)(sin(0.14))=?`  <br>
  ex - <br>
  `>>log(5)(90)20/3.142(27)(sin(0.12))(cot(1))(log(2, 10))log(2)=?`  <br>
`  math.log(5)*(90)*20/3.142*(27)*(math.sin(0.12))*(1/math.tan(1))*(math.log(2, 10))*math.log(2)`<br><br>
### `eval_exp(x)` - Evaluates the arithmatic expression and returns the value <br>
ex - <br>
`>>log(5)(90)20/3.142(27)(sin(0.12))(cot(1))(log(2, 10))log(2)=?`  <br>
`  399.2782593179661`<br><br>
running this code -<br>
  `  enter a valid arithmatic expression` <br>
   `   Can contain only log(num,base) cos() sec() sin() cosec() tan() cot() () + - . , * ^ / ÷ = `<br>
`>>log(5)(90)20/3.142(27)(sin(0.12))(cot(1))(log(2, 10))log(2)=?`  <br>
`  math.log(5)*(90)*20/3.142*(27)*(math.sin(0.12))*(1/math.tan(1))*(math.log(2, 10))*math.log(2)`<br>
   `  399.2782593179661`
<br>
