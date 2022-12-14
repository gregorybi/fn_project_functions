package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"log"

	fdk "github.com/fnproject/fdk-go"
)

func main() {
	fdk.Handle(fdk.HandlerFunc(myHandler))
}

type Person struct {
	Name string `json:"name"`
}

func myHandler(ctx context.Context, in io.Reader, out io.Writer) {
	p := &Person{Name: "World"}
	json.NewDecoder(in).Decode(p)
	msg := struct {
		Msg string `json:"message"`
	}{
		Msg: fmt.Sprintf("Goodbye %s", p.Name),
	}
	log.Print("Inside Go Goodbye World function")
	json.NewEncoder(out).Encode(&msg)
}
