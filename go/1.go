package main

import "fmt"

func isMod3Or5(num int) bool {
	return (num%3 == 0) || (num%5 == 0)
}

func main() {
	ceiling := 1000
	sum := 0
	nums := make([]int, ceiling)
	for i := range nums {
		if isMod3Or5(i) {
			sum = sum + i
		}
	}

	fmt.Println(sum)
}
