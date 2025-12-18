package main

import (
	"encoding/json"
	"fmt"
	"log"
)

type HctSignal struct {
	Signal      string             `json:"signal"`
	Performance PerformanceDetails `json:"performance"`
}

type PerformanceDetails struct {
	Tempo    string `json:"tempo"`
	Dynamics string `json:"dynamics"`
}

func main() {
	// Identify as Conductor
	conductorName := "GoOrchestrator"
	log.Printf("[%s] Starting sequence...", conductorName)

	// 1. Fermata (Hold)
	s1 := HctSignal{
		Signal: "fermata",
		Performance: PerformanceDetails{
			Tempo:    "largo",
			Dynamics: "pp",
		},
	}
	send(s1)

	// 2. Caesura (Stop)
	s2 := HctSignal{
		Signal: "caesura",
		Performance: PerformanceDetails{
			Tempo:    "presto", // Stop immediately!
			Dynamics: "mf",
		},
	}
	send(s2)
}

func send(s HctSignal) {
	b, _ := json.MarshalIndent(s, "", "  ")
	fmt.Printf("Dispatching:\n%s\n", string(b))
}
