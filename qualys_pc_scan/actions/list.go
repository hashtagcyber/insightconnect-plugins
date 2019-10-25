package actions

// Code generated by the Komand Go SDK Generator. DO NOT EDIT
import (
	"time"

	"github.com/rapid7/komand-plugins/qualys_pc_scan/types"
)

// ListInput is the input for List
type ListInput struct {
	LaunchedAfter  time.Time `json:"launched_after"`
	LaunchedBefore time.Time `json:"launched_before"`
	Processed      int       `json:"processed"`
	Reference      string    `json:"reference"`
	State          string    `json:"state"`
	Target         string    `json:"target"`
	Type           string    `json:"type"`
	UserLogin      string    `json:"user_login"`
}

// ListOutput is the output for List
type ListOutput struct {
	Scans []types.Scan `json:"scans"`
}

// ListAction is an action the plugin can take
type ListAction struct{}