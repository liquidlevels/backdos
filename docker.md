# Install gRPC and Protocol Buffer to work with golang inside a docker container

## Docker container

pull the ubuntu image
```
docker pull ubuntu
```

run it with:
```
docker run -it --name [name] ubuntu /bin/bash
```

inside the container run this:
```
apt update && apt upgrade
```

## Golang installation

download version 1.23.5 with:
```
wget https://go.dev/dl/go1.23.5.linux-amd64.tar.gz
```
remove old installations
```
rm -rf /usr/local/go
```

then
```
tar -C /usr/local -xzf go1.23.5.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
```

verify installation:
```
go version
```
should output:
```
go version go1.23.5 linux/amd64
```

### Set up Go workspace

open .bashrc
```
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$PATH
```
then
```
source ~/.bashrc
```

### Test the installation

*hello.go*
```
package main
import "fmt"
func main() {
    fmt.Println("Hello, Go!")
}
```

run with:
```
go run hello.go
```

should output:
```
Hello, Go!
```

source: https://go.dev/doc/install

## Protocol Buffer Compiler installation

```
PB_REL="https://github.com/protocolbuffers/protobuf/releases"
```
```
curl -LO $PB_REL/download/v25.1/protoc-25.1-linux-x86_64.zip
```
```
unzip protoc-25.1-linux-x86_64.zip -d $HOME/.local
```

open .bashrc
```
export PATH="$PATH:$HOME/.local/bin"
```

then
```
source .bashrc
```

verify installation:
```
protoc --version
```

### Testing the installation

*example.proto*
```
syntax = "proto3";

//Go package’s import path must be provided for every .proto file
option go_package = "./";

message SearchRequest {
  string query = 1;
  int32 page_number = 2;
  int32 results_per_page = 3;
}
```

run with:
```
protoc --go_out=. example.proto
```

source: 
- https://protobuf.dev/reference/go/go-generated/#package
- https://protobuf.dev/programming-guides/proto3/


## Following the Go Protocol Buffer Tutorial

source: https://tutorialedge.net/golang/go-protocol-buffer-tutorial/

initialize go module
```
go mod init [name]
```

install dependencies
```
go get google.golang.org/protobuf
```
```
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```

open .bashrc
```
export PATH=$PATH:$(go env GOPATH)/bin
```

then
```
source .bashrc
```

### First part

*person.proto*
```
syntax="proto3";

package main;
//added this
option go_package = "./proto";

message Person {
      string name = 1;
      int32 age = 2;
}
```

run with:
```
protoc --go_out=. person.proto
```

should output *person.pb.go* inside *proto* package

---
There are some changes, in the import section we added *person "your_package_name/proto"* this is because of better package and module structure of Go. *person* is the alias assigned to where the *Person* struct is, if you omit the use of *person* you'll get an *undefined* because Go doesn't know where *Person* is defined

*main.go*
```
package main

import (
    "fmt"
    "log"

    "github.com/golang/protobuf/proto"
    person "your_package_name/proto"
)

func main() {

    elliot := &person.Person{
        Name: "Elliot",
        Age:  24,
    }

    data, err := proto.Marshal(elliot)
    if err != nil {
        log.Fatal("marshaling error: ", err)
    }

  // printing out our raw protobuf object
    fmt.Println(data)

  // let's go the other way and unmarshal
  // our byte array into an object we can modify
  // and use
    newElliot := &person.Person{}
    err = proto.Unmarshal(data, newElliot)
    if err != nil {
        log.Fatal("unmarshaling error: ", err)
  }

  // print out our `newElliot` object
  // for good measure
  fmt.Println(newElliot.GetAge())
    fmt.Println(newElliot.GetName())

}
```

run with:
```
go run main.go
```

should output:
```
[10 6 69 108 108 105 111 116 16 24]
24
Elliot
```

### Second part

*person.proto*
```
syntax="proto3";

package main;
option go_package = "./proto";

message SocialFollowers {
  int32 youtube = 1;
  int32 twitter = 2;
}

message Person {
      string name = 1;
      int32 age = 2;
    SocialFollowers socialFollowers = 3;
}
```

run with:
```
protoc --go_out=. person.proto
```

should output *person.pb.proto*

*main.proto*
```
package main

import (
    "fmt"
    "log"

    //use this import because the other used in the tutorial is deprecated
    "google.golang.org/protobuf/proto"

    protogo "your_package_name/proto"
)

func main() {

    elliot := Person{
        Name: "Elliot",
        Age:  24,
        SocialFollowers: &protogo.SocialFollowers{
            Youtube: 2500,
            Twitter: 1400,
        },
    }
    
    data, err := proto.Marshal(elliot)
    if err != nil {
        log.Fatal("marshaling error: ", err)
    }

    // let's go the other way and unmarshal
    // our protocol buffer into an object we can modify
    // and use
    newElliot := &protogo.Person{}
    err = proto.Unmarshal(data, newElliot)
    if err != nil {
        log.Fatal("unmarshaling error: ", err)
    }

    // print out our `newElliot` object
    // for good measure
    fmt.Println(newElliot.GetName())
    fmt.Println(newElliot.GetAge())
    fmt.Println(newElliot.SocialFollowers.GetTwitter())
    fmt.Println(newElliot.SocialFollowers.GetYoutube())

}

```

run with:
```
go run main.go
```

should output:
```
Elliot
24
1400
2500
```

source:
- https://withcodeexample.com/go-mod-init-dependency-management-go/
- https://grpc.io/docs/languages/go/quickstart/
- https://tutorialedge.net/golang/go-protocol-buffer-tutorial/
- https://go.dev/doc/modules/layout
- some chatgpt help
