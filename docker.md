# Install gRPC and Protocol Buffer9 with golang inside a docker container

## Docker container

```
docker pull ubuntu
docker run -it --name [name] ubuntu /bin/bash
apt update -y
apt upgrade -y
```

## Install golang

```
apt install wget
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

open *.bashrc*
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
