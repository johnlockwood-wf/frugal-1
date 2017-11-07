// Adding this 'fake' file so that goverge can properly report code coverage stats.
// goverge runs 'go test' on each package, which throws a 'no buildable Go source files'
// error here since we require adding '-tags integrations' to run these tests
// We could instead add the short tag to each test in this package, but according to Wes that
// could cause other issues.

package util
