package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func root(c *gin.Context) {
	c.String(http.StatusOK, "Hello World!")
}

func login(c *gin.Context) {
	c.String(http.StatusOK, "sessiion:'adasdasdasd'")
}

func main() {
	router := gin.Default()
	router.GET("/", root)
	router.GET("/login", login)
	router.Run(":8000")
}
