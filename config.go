package main
import (
	"context"
	"fmt"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

// MongoDBConfig เก็บข้อมูลการเชื่อมต่อ MongoDB
type MongoDBConfig struct {
	ConnectionString string
	DatabaseName     string
}

// NewMongoDBClient สร้างและคืนค่า Client สำหรับการเชื่อมต่อ MongoDB
func NewMongoDBClient(config MongoDBConfig) (*mongo.Client, error) {
	clientOptions := options.Client().ApplyURI(config.ConnectionString)

	// ตั้งค่า Timeout สำหรับการเชื่อมต่อ
	clientOptions.SetConnectTimeout(10 * time.Second)

	// เชื่อมต่อ MongoDB
	client, err := mongo.Connect(context.Background(), clientOptions)
	if err != nil {
		return nil, fmt.Errorf("failed to connect to MongoDB: %v", err)
	}

	// ตรวจสอบการเชื่อมต่อ
	err = client.Ping(context.Background(), nil)
	if err != nil {
		return nil, fmt.Errorf("failed to ping MongoDB: %v", err)
	}

	log.Println("Connected to MongoDB!")

	return client, nil
}

// CloseMongoDBClient ปิดการเชื่อมต่อ MongoDB Client
func CloseMongoDBClient(client *mongo.Client) {
	if client != nil {
		err := client.Disconnect(context.Background())
		if err != nil {
			log.Printf("Error disconnecting MongoDB client: %v", err)
		} else {
			log.Println("Disconnected from MongoDB")
		}
	}
}

func main() {
	// กำหนดค่า Config
	config := MongoDBConfig{
		ConnectionString: "mongodb://localhost:27017",
		DatabaseName:     "your_database_name",
	}

	// สร้าง MongoDB Client
	client, err := NewMongoDBClient(config)
	if err != nil {
		log.Fatal(err)
	}

	// ทำงานกับ MongoDB Client ที่ได้รับ
	// ...

	// ปิดการเชื่อมต่อ MongoDB Client เมื่อไม่ใช้งาน
	defer CloseMongoDBClient(client)
}
