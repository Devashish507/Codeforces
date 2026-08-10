package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(x, y int) string {
	if (x-2*y)%3 != 0 {
		return "NO"
	}
	if x < y {
		return "NO"
	}
	return "YES"
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var t int
	fmt.Fscan(in, &t)

	for i := 0; i < t; i++ {
		var x, y int
		fmt.Fscan(in, &x, &y)

		fmt.Fprintln(out, solve(x, y))
	}
}