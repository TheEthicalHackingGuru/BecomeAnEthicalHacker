package main

import (
	"fmt"
	"net"
	"os"
	"sync"
	"time"
)

type scannerBot struct {
	responseChan chan string
	errorChan    chan string
	timeoutChan  chan bool
}

type Scanner interface {
	scanPorts(int, *sync.WaitGroup)
}

func NewScannerBot(rc chan string, ec chan string, toc chan bool) *scannerBot {
	return &scannerBot{responseChan: rc, errorChan: ec, timeoutChan: toc}
}

func (sb scannerBot) scanPorts(port int) {
	address := fmt.Sprintf("127.0.0.1:%s", port)
	_, err := net.Dial("tcp", address)

	if err != nil {

		sb.errorChan <- fmt.Sprintf("port not open for port %s", port)
	}
	if err == nil {

		sb.responseChan <- fmt.Sprintf("port open for port %s", port)
	}
	time.Sleep(2 * time.Second)
	select {
	case <-sb.errorChan:
		fmt.Println("Connection fail")
	case <-sb.responseChan:
		fmt.Println("Connection successful")
	case <-sb.timeoutChan:
		fmt.Println("timed out!")
		os.Exit(0)
	}

}

func main() {
	// timeout chan is true when timeout counter hits its time
	timeout := make(chan bool, 1)
	go func() {
		time.Sleep(6 * time.Second)
		timeout <- true
	}()
	// responses chan will contain all success conns
	responses := make(chan string, 10)
	// errors chan will contain all non-success conns
	errors := make(chan string, 10)
	// create new instance of scannerbot
	sb := NewScannerBot(responses, errors, timeout)

	// use WaitGroup to sync jobs
	var waitgroup sync.WaitGroup
	for i := 0; i <= 10; i++ {
		waitgroup.Add(1)
	}
	go func() {
		for i := 0; i <= 10; i++ {
			sb.scanPorts(i)
			waitgroup.Done()
		}
	}()

	waitgroup.Wait()

	fmt.Println("bye")

}
