/* Function declaration */

foo(); // "bar"

function foo() {
  console.log('bar');
}

/* Function expression */

baz(); // TypeError: baz is not a function

var baz = function() {
  console.log('bar2');
};