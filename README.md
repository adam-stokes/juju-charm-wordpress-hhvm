# Overview

Wordpress on HHVM

# Install

## Setup juju environment

Edit ```~/.juju/environments.yaml``` 

Than do

```
$ juju bootstrap
```


Folow  [this](https://jujucharms.com/juju-gui/) instructions to start JuJu GUI
Run 
```
juju deploy juju-gui --to 0
juju expose juju-gui
```
Use ```juju stat``` to find juju-gui address

## Building juju-charm-wordpress-hhvm 

Edit ```site.toml``` add your configuration options.
Go to folder conteining this charm and run.

```
$ juju charm build 
```
This will create a subfolder ```trusty``` conteining ready ```wordpress-hhvm``` charm

## Deploying wordpress-hhvm Charm

Open directory containing this charm and run

```
$ juju deploy --repository=$(pwd) local:trusty/wordpress-hhvm --to 0
```

> NOTICE: Add ```--to 0``` to deploy on same machine


Monitor the status of ```wordpress-hhvm/0``` unit

```
$ juju stat
```

To get access to pintostack context use

```
$ juju ssh wordpress-hhvm/0
```



# License

The MIT License (MIT)

Copyright (c) 2015 Adam Stokes <adam.stokes@ubuntu.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
