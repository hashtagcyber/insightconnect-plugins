package actions

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// ReadInput is the input for Read
type ReadInput struct {
	FilePathname string `json:"file_pathname"`
	LinesToRead  int    `json:"lines_to_read"`
}

// ReadOutput is the output for Read
type ReadOutput struct {
	LinesRead []string `json:"lines_read"`
}

// ReadAction is an action the plugin can take
type ReadAction struct{}