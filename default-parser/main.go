package main

import (
	"errors"
	"fmt"
	"golang.org/x/net/html"
	"log"
	"net/http"
)

const url = "https://rbc.ru"

func main() {
	links, err := getLinks(url)

	if err != nil {
		log.Fatal(err)
	}

	for _, link := range links {
		fmt.Println(link)
	}
}

func getLinks(url string) ([]string, error) {
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}

	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, errors.New("some error")
	}
	doc, err := html.Parse(resp.Body)
	if err != nil {
		return nil, err
	}
	return parse(nil, doc), nil
}

func parse(links []string, node *html.Node) []string {
	if node.Type == html.ElementNode && node.Data == "a" {
		for _, a := range node.Attr {
			if a.Key == "href" {
				links = append(links, a.Val)
			}
		}
	}
	for c := node.FirstChild; c != nil; c = c.NextSibling {
		links = parse(links, c)
	}
	return links
}
