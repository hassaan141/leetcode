/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  let stack = []

  let arr = s.split('');

  for(let i = 0; i <s.length; i++){
      if (arr[i] == '(' || arr[i] == '{' || arr[i] == '['){
          stack.push(arr[i])
      }
      else{
          let char = stack.pop()
          if (
              arr[i]
          )
      }
  }
};