package cmd

import (
	"fmt"
	"net"

	"github.com/spf13/cobra"
)

var (
	Target string
	Port   int
)

// scanCmd represents the scan command
var scanCmd = &cobra.Command{
	Use:   "scan",
	Short: "A command that will scan a target for open ports.",
	Long:  ``,
	Run: func(cmd *cobra.Command, args []string) {
		Target, _ := cmd.Flags().GetString("target")
		Port, _ := cmd.Flags().GetInt("port")
		scan(Target, Port)
	},
}

func init() {
	rootCmd.AddCommand(scanCmd)
	scanCmd.Flags().StringVarP(&Target, "target", "t", "", "An IP address to scan for open ports.")
	scanCmd.MarkFlagRequired("target")
	scanCmd.Flags().IntVarP(&Port, "port", "p", 0, "A port to scan.")
	scanCmd.MarkFlagRequired("port")

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
