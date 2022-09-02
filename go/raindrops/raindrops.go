package raindrops

import "strconv"

// Convert -- returns a string "Pling" for factors
//of 3, "Plang" for factors of 5 and "Plong" for factors of 7,
//or the number n if not factor of either number.
func Convert(n int) string {
	var result string = ""
	if n%3 == 0 {
		result += "Pling"
	}
	if n%5 == 0 {
		result += "Plang"
	}
	if n%7 == 0 {
		result += "Plong"
	}
	if result == "" {
		result = strconv.Itoa(n)
	}
	return result
}
