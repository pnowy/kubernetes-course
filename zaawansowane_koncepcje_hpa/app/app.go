package main

import (
	"fmt"
	"net/http"
	"os"
	"runtime"
	"strconv"
	"time"
)

func generateLoad(duration time.Duration) {
	finish := time.Now().Add(duration)
	for time.Now().Before(finish) {
		for i := 0; i < 1000000; i++ {
		}
		runtime.Gosched() // Yield to allow other goroutines to run
	}
}

func loadHandler(w http.ResponseWriter, r *http.Request) {
	// Default load time of 1000 milliseconds (1 second) if not specified
	loadTime := 1000 // milliseconds
	if lt, ok := r.URL.Query()["time"]; ok && len(lt[0]) >= 1 {
		if ltInt, err := strconv.Atoi(lt[0]); err == nil {
			loadTime = ltInt
		}
	}

	go generateLoad(time.Duration(loadTime) * time.Millisecond)

	// Get current time
	currentTime := time.Now().Format(time.RFC3339)

	// Get Pod IP from environment variables
	podIP := os.Getenv("POD_IP")
	if podIP == "" {
		podIP = "Unknown" // Default value if POD_IP env var is not set
	}

	fmt.Fprintf(w, "Generating CPU load for %d milliseconds. Current Time: %s. Pod IP: %s\n", loadTime, currentTime, podIP)
}

func main() {
	http.HandleFunc("/load", loadHandler)
	fmt.Println("Server started on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Printf("Error starting server: %s\n", err)
	}
}
