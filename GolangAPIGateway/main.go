package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil)
}

func handler(w http.ResponseWriter, r *http.Request) {
	// Handle incoming requests from Raspberry Pi nodes
	fmt.Fprintf(w, "API Gateway is up and running!")
	// [Code to process and route data to Arduino Hub]
}