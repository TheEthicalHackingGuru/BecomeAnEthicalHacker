package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
)

func main() {
	listener, err := net.Listen("tcp", "localhost:8080")
	if err != nil {
		fmt.Println(err)
	}
	log.Printf("Now listening for connections.")

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println(err)
		}
		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	command, err := bufio.NewReader(conn).ReadString('\n')
	if err != nil {
		
		fmt.Fprintf(conn, fmt.Sprintf("%s", err))
	}

	fmt.Fprintf(conn, command)
}
