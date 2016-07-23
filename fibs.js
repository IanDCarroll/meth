/* A study in recursive functions and their speeds
 * 
 * slowFibs is slow because with each increment of num, 
 * it has to do about twice as many sloFibs calls as num-1.
 *
 * If you call it, it will churn to a halt with numbers greater than 50, 
 * and be noticibly slow by 30.
 *
 * fastFibs doesn't have that problem. 
 * For each recursion, It is called a static number of times.
 * So even if you pass it 1000, there is no noticeable slow-down at all.
 */

function slowFibs(num) {
    if((num === 0) || (num === 1)) {
	return(num);
    } else {
	return(fibs(num - 1) + fibs(num - 2));
    }
}

function fastFibs(n, curr = 0, next = 1) {
  if(n < 1) return curr;
  else return fibs(n-1, next, curr + next);
}

function main(n) {
    for(i = 0; i < n; i++) {
	process.stdout.write(fastFibs(i) + " ");
	//process.stdout.write(slowFibs(i) + " ");
    }
    console.log("");
}

main(50);

