package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func login(c *gin.Context) {
	c.String(http.StatusOK, "sessiion:'login'")
}

func logout(c *gin.Context) {
	c.String(http.StatusOK, "sessiion:'logout'")
}

func main() {
	router := gin.Default()

	router.GET("/login", login)
	router.GET("/logout", logout)
	router.Run(":8000")
}
