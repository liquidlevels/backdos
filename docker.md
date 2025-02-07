# Install gRPC and Protocol Buffer with golang inside a docker container

## Docker container

```
docker pull ubuntu
docker run -it --name [name] ubuntu /bin/bash
apt update -y
apt upgrade -y
```

## Install golang

```
wget https://go.dev/dl/go1.23.5.linux-amd64.tar.gz
rm -rf /usr/local/go
tar -C /usr/local -xzf go1.23.5.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
```

```
go version
```
should output something like:

go version go1.23.5 linux/amd64

set up go workspace

open .bashrc
```
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$PATH
source ~/.bashrc
```

now we can test the installation

open hello.go
```
package main
import "fmt"
func main() {
    fmt.Println("Hello, Go!")
}
```

now run it with:
```
go run hello.go
```

should output

Hello, Go!

source: https://go.dev/doc/install

## Protobuf compiler

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
source .bashrc

protoc --version
```


## Simple example 

```
go mod init [name]
```
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
```
source .bashrc
```
